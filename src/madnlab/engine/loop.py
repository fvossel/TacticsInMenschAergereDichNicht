"""The game loop (GM-3), with the per-turn metric accumulation §6.2 needs.

D-43c requires AK-7 to measure with the per-turn ``leader(t)`` recomputation
inside the loop, so the loop computes it rather than deferring it.

Event recording is optional and off by default: pass ``record`` a list and the
loop appends the LG-1 event stream to it. That stream is what AK-3's replay
validator compares, so it has to capture every decision — including the full
offered legal-move set and the chosen index — not merely the resulting state.

Turn structure (GM-3.3, GM-3.10, D-10)
--------------------------------------
1. **Attempt phase.** With ``dreimal_wuerfeln`` on and the D-1 condition
   holding — no piece on the ring and no goal piece movable by any value 1..6
   — the player rolls up to three times looking for a 6. A 6 ends the sequence
   immediately, whether or not it produced a move.
2. **Extra rolls.** A 6 grants one ordinary follow-up, chaining on a further
   6. ``bonus_roll_forfeited`` withholds it when the 6 could not be moved;
   ``bonus_roll_after_quick_entry`` adds a second grant, stacking, when entry
   happened on attempt 1 or 2.

D-10's resulting per-turn roll budget is 1 / 4 / 5. ``RuleSet.entry_attempts``
is the *attempt* count, not that budget.
"""

from __future__ import annotations

import random
from collections.abc import Sequence
from typing import NamedTuple

from madnlab.agents.policies import Agent
from madnlab.engine.geometry import GOAL_FIELDS, PIECES_PER_SEAT, Board
from madnlab.engine.moves import Move, MoveKind, legal_moves_with_restriction
from madnlab.engine.rules import GameEndMode, RuleSet
from madnlab.engine.state import GameState
from madnlab.eventlog.events import (
    BarrierEvent,
    CaptureEvent,
    Event,
    FinishEvent,
    GameEndEvent,
    MoveEvent,
    PassEvent,
    RollEvent,
)

#: A turn's roll chain is geometric with p = 1/6, so reaching this needs ~64
#: consecutive 6s. Exceeding it *is* a defect and raises.
MAX_ROLLS_PER_TURN = 64

#: Turn bound after which a game is **abandoned** rather than played out
#: (D-70). Not a defect signal: some rule combinations produce games whose
#: expected length is astronomically long, and abandoning them with a recorded
#: flag makes that a measurable property of the arm instead of a hang. 20,000
#: is ~7x the longest legitimate mean measured (the 6-seat worst-case cell, at
#: 2,894 turns).
MAX_TURNS_PER_GAME = 20_000


class GameOutcome(NamedTuple):
    """Per-game results — the §6.2 fields that cost per turn."""

    ranks: tuple[int, ...]
    winner: int
    turns: int
    rounds: int
    dice_rolls: int
    turns_to_first_win: int
    rounds_to_first_win: int
    captures_total: int
    captures_by_seat: tuple[int, ...]
    #: Captures *suffered*. Not derivable from ``captures_by_seat``: that says
    #: who struck, this says who was struck, and RQ-1's dynamics ask both.
    captured_by_seat: tuple[int, ...]
    passes_by_seat: tuple[int, ...]
    #: Turns in which the D-1 condition held at turn start, counted whether or
    #: not ``dreimal_wuerfeln`` is on — under the baseline it measures how long
    #: a seat sat waiting to enter, which is the quantity §6.2 names. Overlaps
    #: ``passes_by_seat`` by construction; the two must never be summed.
    entry_waits_by_seat: tuple[int, ...]
    lead_changes: int
    turns_without_leader: int
    time_in_lead_by_seat: tuple[int, ...]
    extra_laps_by_seat: tuple[int, ...]
    barriers_formed: int
    barrier_turns: int
    #: Turns at whose start *this seat* had a barrier standing. Sums to more
    #: than ``barrier_turns`` when two seats hold one simultaneously, which is
    #: why §6.2 keeps both.
    barrier_turns_by_seat: tuple[int, ...]
    capture_forcing_offered: int
    capture_forcing_violations: int
    #: The ``mandatory_extended`` half of AK-5's invariant (§11). Offered
    #: counts decisions where every legal move carried an extra lap.
    forced_extra_lap_offered: int
    forced_extra_lap_violations: int
    #: §6.2 checkpoint ranks: the eventual winner's progress rank at
    #: ``ceil(k * turns_to_first_win)``, standard competition ranking. ``-1``
    #: when the game never produced a first win (stalemate or abandoned), so a
    #: missing checkpoint can never be read as rank 0.
    winner_rank_at_50: int
    winner_rank_at_75: int
    winner_rank_at_50_tied: bool
    #: Winner's checkpoint rank >= 2 (2-3 players) or >= 3 (4+). The threshold
    #: travels with the row so a comeback rate can never be compared across
    #: player counts without it (§6.2).
    comeback: bool
    comeback_rank_threshold: int
    comeback_depth: float
    #: Progress gap winner vs. runner-up at the first win; the normalized form
    #: is the one that survives a change of ``seats``.
    final_margin: int
    final_margin_norm: float
    #: True when the game ended because no seat could move on any die value
    #: (D-69). A measured outcome of the rule set, not an error.
    stalemate: bool
    #: True when the game hit :data:`MAX_TURNS_PER_GAME` with more than one
    #: seat still unfinished (D-70). Also a measured outcome; the analysis
    #: layer reports the rate per cell and no estimand may be published from a
    #: cell whose rate is non-negligible without saying so.
    abandoned: bool


class GameTerminationError(RuntimeError):
    """A game or turn exceeded its safety bound — a legality defect."""


def _is_deadlocked(
    board: Board,
    positions: list[int],
    seats: Sequence[int],
    finished: Sequence[int],
    rules: RuleSet,
) -> bool:
    """Whether no unfinished seat has a legal move on **any** die value.

    Expensive — 6 legality calls per unfinished seat — so it is only consulted
    after a full round has passed without a single move, which is cheap to
    detect and which a live game essentially never triggers.

    A round with no moves is not by itself a deadlock: under ``strict`` a round
    in which nobody rolls a 6 has no legal move anywhere and is perfectly
    ordinary. Only the all-values test distinguishes the two.
    """
    state = GameState(positions=tuple(positions))
    for seat in seats:
        if seat in finished:
            continue
        for roll in range(1, 7):
            if legal_moves_with_restriction(board, state, seat, roll, rules)[0]:
                return False
    return True


def _goal_piece_movable(board: Board, state: GameState, seat: int, rules: RuleSet) -> bool:
    """D-1's second conjunct, evaluated over the whole die before rolling."""
    ring_length = board.ring_length
    occupied = {
        pos - ring_length - 1 for pos in state.seat_positions(seat) if pos > ring_length
    }
    for index in occupied:
        for roll in range(1, 7):
            target = index + roll
            if target >= GOAL_FIELDS or target in occupied:
                continue
            if rules.goal_no_jump and any(j in occupied for j in range(index + 1, target)):
                continue
            return True
    return False


def _three_attempts_apply(board: Board, state: GameState, seat: int, rules: RuleSet) -> bool:
    """The D-1 condition. Only consulted when ``dreimal_wuerfeln`` is on."""
    if any(1 <= pos <= board.ring_length for pos in state.seat_positions(seat)):
        return False
    return not _goal_piece_movable(board, state, seat, rules)


def _own_on_field(board: Board, positions: list[int], seat: int, pos: int) -> int:
    """How many of ``seat``'s pieces stand on the ring field of ``pos``."""
    if not 1 <= pos <= board.ring_length:
        return 0
    field = board.ring_field(seat, pos)
    base = seat * PIECES_PER_SEAT
    return sum(
        1
        for offset in range(PIECES_PER_SEAT)
        if 1 <= positions[base + offset] <= board.ring_length
        and board.ring_field(seat, positions[base + offset]) == field
    )


def _legal_wire(moves: Sequence[Move]) -> tuple[tuple[int, int, int, str, int | None], ...]:
    return tuple(
        (m.piece, m.from_pos, m.to_pos, str(m.kind), m.captures) for m in moves
    )


def play_game(
    board: Board,
    seats_in_play: Sequence[int],
    rules: RuleSet,
    agents: dict[int, Agent],
    initial: GameState,
    dice: random.Random,
    agent_rngs: dict[int, random.Random],
    start_seat: int,
    record: list[Event] | None = None,
    max_turns: int = MAX_TURNS_PER_GAME,
) -> GameOutcome:
    """Play one complete game under ``play_out`` (GM-3.11)."""
    if rules.game_end_mode is not GameEndMode.PLAY_OUT:
        raise NotImplementedError(
            f"game_end_mode={rules.game_end_mode} is a config value the v1 "
            f"campaigns do not use (GM-3.11)"
        )

    seats = list(seats_in_play)
    positions = list(initial.positions)
    ring_length = board.ring_length

    finished: list[int] = []
    captures_by_seat = [0] * board.seats
    captured_by_seat = [0] * board.seats
    passes_by_seat = [0] * board.seats
    entry_waits = [0] * board.seats
    time_in_lead = [0] * board.seats
    extra_laps = [0] * board.seats
    barrier_turns_seat = [0] * board.seats

    #: Per-seat progress after each turn of the first-win segment, so §6.2's
    #: checkpoints can be read off once ``turns_to_first_win`` is known — it is
    #: not known until the win happens, and the checkpoint is defined as a
    #: fraction of it. Dropped when the row is built.
    progress_trace: list[tuple[int, ...]] = []
    final_margin = 0

    turns = dice_rolls = captures_total = lead_changes = turns_without_leader = 0
    forcing_offered = forcing_violations = 0
    extra_lap_offered = extra_lap_violations = 0
    barriers_formed = barrier_turns = 0
    turns_to_first_win = slots_to_first_win = 0
    leader: int | None = None
    turn_slots = 0
    slots_without_move = 0
    stalemate = False
    abandoned = False

    order = seats[seats.index(start_seat) :] + seats[: seats.index(start_seat)]
    cursor = 0

    while len(finished) < len(seats) - 1:
        if turns >= max_turns:
            abandoned = True
            break

        seat = order[cursor % len(order)]
        cursor += 1
        turn_slots += 1
        if seat in finished:
            continue
        turns += 1

        if rules.barriers:
            holders = {
                s
                for s in seats
                for p in range(PIECES_PER_SEAT)
                if _own_on_field(board, positions, s, positions[s * PIECES_PER_SEAT + p]) >= 2
            }
            if holders:
                barrier_turns += 1
            for holder in holders:
                barrier_turns_seat[holder] += 1

        state = GameState(positions=tuple(positions))
        agent = agents[seat]
        rng = agent_rngs[seat]

        # The D-1 condition is evaluated every turn, not only when the variant
        # that acts on it is enabled: under the baseline it is the "waiting to
        # enter" measurement §6.2 asks for, and a counter that only exists in
        # one arm cannot be compared across arms.
        waiting = _three_attempts_apply(board, state, seat, rules)
        if waiting:
            entry_waits[seat] += 1

        attempts = rules.entry_attempts if rules.dreimal_wuerfeln and waiting else 1
        pending_extra = 0
        moved_this_turn = False
        roll_index = 0

        def _take(
            roll: int,
            attempt: int,
            seat: int = seat,
            agent: Agent = agent,
            rng: random.Random = rng,
        ) -> tuple[bool, Move | None]:
            """Roll, choose and apply. Returns ``(moved, move)``.

            ``seat``, ``agent`` and ``rng`` are bound as defaults rather
            than captured: a closure over the loop variables would read
            whatever the *last* iteration left behind if it ever outlived
            its turn, and the counters it mutates are exactly the ones
            AK-5 is checked against.
            """
            nonlocal state, captures_total, forcing_offered, barriers_formed
            nonlocal extra_lap_offered
            if record is not None:
                record.append(RollEvent(seat, roll, attempt))
            legal, restriction = legal_moves_with_restriction(
                board, state, seat, roll, rules
            )
            if restriction.value == "capture":
                forcing_offered += 1
                # The extended-capture obligation is *offered* when the
                # narrowed set leaves the seat no way to satisfy it without
                # taking another lap — that is the clause AK-5's second half
                # is about, and it is a property of the set, not of the pick.
                if legal and all(m.extra_lap for m in legal):
                    extra_lap_offered += 1
            if not legal:
                if record is not None:
                    record.append(PassEvent(seat))
                return False, None

            move = agent(board, state, seat, roll, legal, rng)
            chosen = legal.index(move)
            if record is not None:
                record.append(
                    MoveEvent(
                        seat,
                        move.piece,
                        move.from_pos,
                        move.to_pos,
                        str(move.kind),
                        _legal_wire(legal),
                        chosen,
                        restriction.value,
                    )
                )

            origin_pair = _own_on_field(board, positions, seat, move.from_pos) >= 2
            positions[move.piece] = move.to_pos
            if move.captures is not None:
                victim = move.captures
                if record is not None:
                    record.append(
                        CaptureEvent(
                            seat,
                            move.piece % PIECES_PER_SEAT,
                            victim // PIECES_PER_SEAT,
                            victim % PIECES_PER_SEAT,
                            board.ring_field(seat, move.to_pos),
                        )
                    )
                positions[victim] = 0
                captures_total += 1
                captures_by_seat[seat] += 1
                captured_by_seat[victim // PIECES_PER_SEAT] += 1
            if move.extra_lap:
                extra_laps[seat] += 1

            if rules.barriers:
                if _own_on_field(board, positions, seat, move.to_pos) >= 2:
                    barriers_formed += 1
                    if record is not None:
                        record.append(
                            BarrierEvent(seat, board.ring_field(seat, move.to_pos), True)
                        )
                if origin_pair and record is not None:
                    record.append(
                        BarrierEvent(seat, board.ring_field(seat, move.from_pos), False)
                    )

            state = GameState(positions=tuple(positions))
            return True, move

        for attempt in range(1, attempts + 1):
            roll = dice.randint(1, 6)
            dice_rolls += 1
            roll_index += 1
            moved, move = _take(roll, roll_index)
            if moved:
                moved_this_turn = True
                if roll == 6:
                    pending_extra += 1
                    if (
                        rules.bonus_roll_after_quick_entry
                        and attempt <= 2
                        and move is not None
                        and move.kind is MoveKind.ENTER
                    ):
                        pending_extra += 1
                break
            if roll == 6:
                # A 6 ends the attempt sequence whether or not it moved (D-10).
                if not rules.bonus_roll_forfeited:
                    pending_extra += 1
                break

        while pending_extra > 0:
            pending_extra -= 1
            roll_index += 1
            if roll_index > MAX_ROLLS_PER_TURN:
                raise GameTerminationError(
                    f"turn exceeded {MAX_ROLLS_PER_TURN} rolls — rule defect"
                )
            roll = dice.randint(1, 6)
            dice_rolls += 1
            moved, _move = _take(roll, roll_index)
            if moved:
                moved_this_turn = True
                if roll == 6:
                    pending_extra += 1
            elif roll == 6 and not rules.bonus_roll_forfeited:
                pending_extra += 1

        if not moved_this_turn:
            passes_by_seat[seat] += 1
            slots_without_move += 1
            # A full round with no move anywhere is the cheap trigger; the
            # all-die-values test below is what actually decides (D-69).
            if slots_without_move >= len(seats) and _is_deadlocked(
                board, positions, seats, finished, rules
            ):
                stalemate = True
                break
        else:
            slots_without_move = 0

        base = seat * PIECES_PER_SEAT
        first_win_this_turn = False
        if seat not in finished and all(
            positions[base + p] > ring_length for p in range(PIECES_PER_SEAT)
        ):
            finished.append(seat)
            if record is not None:
                record.append(FinishEvent(seat, len(finished)))
            if len(finished) == 1:
                turns_to_first_win = turns
                slots_to_first_win = turn_slots
                first_win_this_turn = True

        totals = {
            s: sum(positions[s * PIECES_PER_SEAT + p] for p in range(PIECES_PER_SEAT))
            for s in seats
        }
        if not finished or first_win_this_turn:
            progress_trace.append(tuple(totals[s] for s in seats))
        if first_win_this_turn:
            others = sorted((totals[s] for s in seats if s != seat), reverse=True)
            final_margin = totals[seat] - others[0] if others else 0

        if not finished:
            best = max(totals.values())
            tied = [s for s in seats if totals[s] == best]
            if len(tied) == 1:
                new_leader: int | None = tied[0]
            elif leader is not None and leader in tied:
                new_leader = leader
            elif leader is not None:
                new_leader = min(tied)
            else:
                new_leader = None
            if new_leader is None:
                turns_without_leader += 1
            else:
                if leader is not None and new_leader != leader:
                    lead_changes += 1
                time_in_lead[new_leader] += 1
            leader = new_leader

    unfinished = [s for s in seats if s not in finished]
    if stalemate or abandoned:
        # Ranks for a game that did not play out fall back to total
        # progress, the rule §6.1 gives ``first_winner``; ties keep ascending
        # seat order.
        unfinished.sort(
            key=lambda s: (
                -sum(positions[s * PIECES_PER_SEAT + p] for p in range(PIECES_PER_SEAT)),
                s,
            )
        )
    ranks = tuple(finished) + tuple(unfinished)
    if record is not None:
        record.append(GameEndEvent(ranks))
    players = len(seats)
    #: Every piece home: the four goal fields are ``ring_length+1 .. +4``.
    max_progress = 4 * ring_length + 10

    def _checkpoint(num: int, den: int) -> tuple[int, bool]:
        """The winner's competition rank at ``ceil(num/den * turns_to_first_win)``.

        Integer arithmetic throughout: the checkpoint is a turn index, and
        ``int(0.75 * 4)`` is 2 on some floats and 3 on others. Returns ``-1``
        when there was no first win, so a caller cannot mistake "no checkpoint"
        for "the winner led".
        """
        if turns_to_first_win <= 0 or not progress_trace:
            return -1, False
        turn = -(-turns_to_first_win * num // den)
        snapshot = progress_trace[max(1, min(turn, len(progress_trace))) - 1]
        winner_index = seats.index(ranks[0])
        mine = snapshot[winner_index]
        # Standard competition ranking (1, 2, 2, 4): one plus the number
        # strictly ahead, so a tied winner takes the best rank of its group.
        rank = 1 + sum(1 for value in snapshot if value > mine)
        tied = any(
            value == mine for index, value in enumerate(snapshot) if index != winner_index
        )
        return rank, tied

    rank_50, tied_50 = _checkpoint(1, 2)
    rank_75, _ = _checkpoint(3, 4)
    threshold = 2 if players <= 3 else 3

    return GameOutcome(
        ranks=ranks,
        winner=ranks[0],
        turns=turns,
        rounds=-(-turn_slots // players),
        dice_rolls=dice_rolls,
        turns_to_first_win=turns_to_first_win,
        rounds_to_first_win=-(-slots_to_first_win // players),
        captures_total=captures_total,
        captures_by_seat=tuple(captures_by_seat),
        captured_by_seat=tuple(captured_by_seat),
        passes_by_seat=tuple(passes_by_seat),
        entry_waits_by_seat=tuple(entry_waits),
        lead_changes=lead_changes,
        turns_without_leader=turns_without_leader,
        time_in_lead_by_seat=tuple(time_in_lead),
        extra_laps_by_seat=tuple(extra_laps),
        barriers_formed=barriers_formed,
        barrier_turns=barrier_turns,
        barrier_turns_by_seat=tuple(barrier_turns_seat),
        capture_forcing_offered=forcing_offered,
        capture_forcing_violations=forcing_violations,
        forced_extra_lap_offered=extra_lap_offered,
        forced_extra_lap_violations=extra_lap_violations,
        winner_rank_at_50=rank_50,
        winner_rank_at_75=rank_75,
        winner_rank_at_50_tied=tied_50,
        comeback=rank_50 >= threshold if rank_50 > 0 else False,
        comeback_rank_threshold=threshold,
        comeback_depth=(rank_50 - 1) / (players - 1) if rank_50 > 0 and players > 1 else 0.0,
        final_margin=final_margin,
        final_margin_norm=final_margin / max_progress if max_progress else 0.0,
        stalemate=stalemate,
        abandoned=abandoned,
    )

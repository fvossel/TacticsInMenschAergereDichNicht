"""The game loop (GM-3), with the per-turn metric accumulation §6.2 needs.

This is the minimum that makes AK-7 an honest measurement: D-43c requires the
benchmark to run with the per-turn ``leader(t)`` recomputation *inside* the
measured loop, so the loop has to compute it, not skip it. The event-log
writer and the full summary row are not here yet; what is here is every cost
that scales with turns.

Turn structure (GM-3.3, GM-3.10, D-10)
--------------------------------------
1. **Attempt phase.** When ``dreimal_wuerfeln`` is on and the D-1 condition
   holds — no piece on the ring track and no goal piece movable by any value
   1..6 — the player rolls up to three times looking for a 6. A 6 terminates
   the sequence immediately, whether or not it produced a move.
2. **Extra rolls.** A 6 grants one ordinary follow-up roll, which chains on a
   further 6. ``bonus_roll_forfeited`` withholds that grant when the 6 could
   not be moved; ``bonus_roll_after_quick_entry`` adds a second grant, stacking
   with the first, when entry happened on attempt 1 or 2.

D-10's resulting per-turn roll budget is 1 / 4 / 5 for attempt limits of
1 / 3 / 3-with-bonus. ``RuleSet.entry_attempts`` is the *attempt* count, not
that budget.
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

#: Safety valve. A turn's roll chain is geometric with p = 1/6, so reaching
#: this needs ~64 consecutive 6s; it exists so a rule bug surfaces as a loud
#: failure instead of a hung benchmark.
MAX_ROLLS_PER_TURN = 64

#: Same purpose at game scope. Play-out games are long but bounded; a game
#: that passes this has a legality or termination defect.
MAX_TURNS_PER_GAME = 100_000


class GameOutcome(NamedTuple):
    """Per-game results — the subset of §6.2 that costs per turn.

    The remaining battery fields (checkpoints, comeback, entropy, barrier and
    AK-5 counters) are derived in the summary-row layer, which is not written
    yet; nothing here would change their cost.
    """

    ranks: tuple[int, ...]
    winner: int
    turns: int
    rounds: int
    dice_rolls: int
    turns_to_first_win: int
    rounds_to_first_win: int
    captures_total: int
    captures_by_seat: tuple[int, ...]
    passes_by_seat: tuple[int, ...]
    lead_changes: int
    turns_without_leader: int
    time_in_lead_by_seat: tuple[int, ...]
    extra_laps_by_seat: tuple[int, ...]
    capture_forcing_offered: int
    capture_forcing_violations: int


class GameTerminationError(RuntimeError):
    """A game or turn exceeded its safety bound — a legality defect."""


def _goal_piece_movable(board: Board, state: GameState, seat: int, rules: RuleSet) -> bool:
    """Whether any goal piece of ``seat`` could move on *some* value 1..6.

    D-1's second conjunct, evaluated over the whole die **before** rolling.
    Written directly rather than by calling ``legal_moves`` six times: this
    runs once per turn whenever ``dreimal_wuerfeln`` is on.
    """
    ring_length = board.ring_length
    occupied = {
        pos - ring_length - 1
        for pos in state.seat_positions(seat)
        if pos > ring_length
    }
    for index in occupied:
        for roll in range(1, 7):
            target = index + roll
            if target >= GOAL_FIELDS or target in occupied:
                continue
            if rules.goal_no_jump and any(
                j in occupied for j in range(index + 1, target)
            ):
                continue
            return True
    return False


def _three_attempts_apply(board: Board, state: GameState, seat: int, rules: RuleSet) -> bool:
    """The D-1 condition. Only consulted when ``dreimal_wuerfeln`` is on."""
    ring_length = board.ring_length
    if any(1 <= pos <= ring_length for pos in state.seat_positions(seat)):
        return False
    return not _goal_piece_movable(board, state, seat, rules)


def _apply(positions: list[int], move: Move) -> int | None:
    """Apply ``move`` in place. Returns the captured piece index, if any."""
    positions[move.piece] = move.to_pos
    if move.captures is not None:
        positions[move.captures] = 0
    return move.captures


def play_game(
    board: Board,
    seats_in_play: Sequence[int],
    rules: RuleSet,
    agents: dict[int, Agent],
    initial: GameState,
    dice: random.Random,
    agent_rngs: dict[int, random.Random],
    start_seat: int,
) -> GameOutcome:
    """Play one complete game and return its per-turn metrics.

    ``play_out`` (GM-3.11) is the only mode implemented: the game runs until
    all but one seat have finished, and finished seats are skipped in the turn
    order.
    """
    if rules.game_end_mode is not GameEndMode.PLAY_OUT:
        raise NotImplementedError(
            f"game_end_mode={rules.game_end_mode} is a config value the v1 "
            f"campaigns do not use (GM-3.11)"
        )

    seats = list(seats_in_play)
    n_seats = board.seats
    positions = list(initial.positions)
    ring_length = board.ring_length

    finished: list[int] = []
    captures_by_seat = [0] * n_seats
    passes_by_seat = [0] * n_seats
    time_in_lead = [0] * n_seats
    extra_laps = [0] * n_seats

    turns = dice_rolls = captures_total = lead_changes = turns_without_leader = 0
    forcing_offered = forcing_violations = 0
    turns_to_first_win = 0
    leader: int | None = None
    turn_slots = 0
    slots_to_first_win = 0

    order = seats[seats.index(start_seat) :] + seats[: seats.index(start_seat)]
    cursor = 0

    while len(finished) < len(seats) - 1:
        if turns > MAX_TURNS_PER_GAME:
            raise GameTerminationError(
                f"game exceeded {MAX_TURNS_PER_GAME} turns — legality or "
                f"termination defect (rules={rules})"
            )

        seat = order[cursor % len(order)]
        cursor += 1
        turn_slots += 1
        if seat in finished:
            continue
        turns += 1

        state = GameState(positions=tuple(positions))
        agent = agents[seat]
        rng = agent_rngs[seat]

        attempts = (
            rules.entry_attempts
            if rules.dreimal_wuerfeln and _three_attempts_apply(board, state, seat, rules)
            else 1
        )

        pending_extra = 0
        moved_this_turn = False
        rolls_this_turn = 0

        for attempt in range(1, attempts + 1):
            roll = dice.randint(1, 6)
            dice_rolls += 1
            rolls_this_turn += 1
            legal, restriction = legal_moves_with_restriction(
                board, state, seat, roll, rules
            )
            if restriction.value == "capture":
                forcing_offered += 1
            if legal:
                move = agent(board, state, seat, roll, legal, rng)
                if move.captures is not None:
                    captures_total += 1
                    captures_by_seat[seat] += 1
                if move.extra_lap:
                    extra_laps[seat] += 1
                _apply(positions, move)
                state = GameState(positions=tuple(positions))
                moved_this_turn = True
                if roll == 6:
                    pending_extra += 1
                    if (
                        rules.bonus_roll_after_quick_entry
                        and attempt <= 2
                        and move.kind is MoveKind.ENTER
                    ):
                        pending_extra += 1
                break
            if roll == 6:
                # A 6 ends the attempt sequence whether or not it moved (D-10).
                if not rules.bonus_roll_forfeited:
                    pending_extra += 1
                break

        if not moved_this_turn:
            passes_by_seat[seat] += 1

        while pending_extra > 0:
            pending_extra -= 1
            rolls_this_turn += 1
            if rolls_this_turn > MAX_ROLLS_PER_TURN:
                raise GameTerminationError(
                    f"turn exceeded {MAX_ROLLS_PER_TURN} rolls — rule defect"
                )
            roll = dice.randint(1, 6)
            dice_rolls += 1
            legal, restriction = legal_moves_with_restriction(
                board, state, seat, roll, rules
            )
            if restriction.value == "capture":
                forcing_offered += 1
            if legal:
                move = agent(board, state, seat, roll, legal, rng)
                if move.captures is not None:
                    captures_total += 1
                    captures_by_seat[seat] += 1
                if move.extra_lap:
                    extra_laps[seat] += 1
                _apply(positions, move)
                state = GameState(positions=tuple(positions))
                if roll == 6:
                    pending_extra += 1
            else:
                if roll == 6 and not rules.bonus_roll_forfeited:
                    pending_extra += 1

        # -- finishing ------------------------------------------------------
        base = seat * PIECES_PER_SEAT
        if seat not in finished and all(
            positions[base + p] > ring_length for p in range(PIECES_PER_SEAT)
        ):
            finished.append(seat)
            if len(finished) == 1:
                turns_to_first_win = turns
                slots_to_first_win = turn_slots

        # -- leader(t), over the first-win segment (§6.1, §6.2) -------------
        if not finished:
            best = -1
            best_seat = -1
            tie = False
            for s in seats:
                b = s * PIECES_PER_SEAT
                total = (
                    positions[b] + positions[b + 1] + positions[b + 2] + positions[b + 3]
                )
                if total > best:
                    best, best_seat, tie = total, s, False
                elif total == best:
                    tie = True
            if tie:
                # On ties the previous leader persists iff it is itself among
                # the tied maxima; otherwise the lowest tied seat index (D-18).
                if leader is not None:
                    b = leader * PIECES_PER_SEAT
                    if (
                        positions[b]
                        + positions[b + 1]
                        + positions[b + 2]
                        + positions[b + 3]
                    ) != best:
                        leader = min(
                            s
                            for s in seats
                            if sum(
                                positions[s * PIECES_PER_SEAT + p]
                                for p in range(PIECES_PER_SEAT)
                            )
                            == best
                        )
                new_leader = leader
            else:
                new_leader = best_seat
            if new_leader is None:
                turns_without_leader += 1
            else:
                if leader is not None and new_leader != leader:
                    lead_changes += 1
                time_in_lead[new_leader] += 1
            leader = new_leader

    unfinished = [s for s in seats if s not in finished]
    ranks = tuple(finished) + tuple(unfinished)
    players = len(seats)
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
        passes_by_seat=tuple(passes_by_seat),
        lead_changes=lead_changes,
        turns_without_leader=turns_without_leader,
        time_in_lead_by_seat=tuple(time_in_lead),
        extra_laps_by_seat=tuple(extra_laps),
        capture_forcing_offered=forcing_offered,
        capture_forcing_violations=forcing_violations,
    )

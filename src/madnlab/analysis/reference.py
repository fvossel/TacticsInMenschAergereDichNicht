"""AK-9 — an independent re-derivation of the summary row from the event log.

§4.1 forbids analyses from re-deriving a number the summary row already carries. AK-9 is the
one place that rule is violated on purpose: without a second route, a wrong ``lead_changes`` or
``winner_rank_at_50`` passes AK-1 through AK-7 unchanged and reaches ``docs/results.md``.

The route is deliberately unlike the engine's. The game loop accumulates counters as it plays;
this module walks the finished event stream, reconstructs the board from the moves, and
recomputes every field from positions. Two implementations agreeing is evidence; one
implementation called twice is not.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

from madnlab.engine.geometry import PIECES_PER_SEAT, board_for
from madnlab.engine.rules import ColdStart
from madnlab.eventlog.events import (
    CaptureEvent,
    Event,
    FinishEvent,
    GameEndEvent,
    LogHeader,
    MoveEvent,
    PassEvent,
    RollEvent,
)
from madnlab.eventlog.replay import rules_from_header


def derive_from_events(header: LogHeader, events: Sequence[Event]) -> dict[str, Any]:
    """Recompute the §6.2 fields by walking ``events``.

    Returns a mapping keyed the way :class:`~madnlab.eventlog.writer.SummaryRow` is, restricted
    to the fields an event stream can support. Fields the log cannot see — the seeds, the config
    echo — are omitted rather than guessed, so a caller comparing dictionaries compares only
    what was re-derived.
    """
    board = board_for(header.seats)
    rules = rules_from_header(header)
    seats = list(header.occupied_seats)
    ring_length = board.ring_length

    positions = [0] * (board.seats * PIECES_PER_SEAT)
    if rules.cold_start is ColdStart.ONE_PIECE_OUT:
        for seat in seats:
            positions[seat * PIECES_PER_SEAT] = 1

    captures_by_seat = [0] * board.seats
    captured_by_seat = [0] * board.seats
    passes_by_seat = [0] * board.seats
    entry_waits = [0] * board.seats
    time_in_lead = [0] * board.seats
    extra_laps = [0] * board.seats
    barrier_turns_seat = [0] * board.seats

    dice_rolls = captures_total = lead_changes = turns_without_leader = 0
    barriers_formed = 0
    extra_lap_offered = 0
    turns = 0
    turns_to_first_win = 0
    final_margin = 0
    progress_trace: list[tuple[int, ...]] = []
    trace_open = True
    finished: list[int] = []
    ranks: tuple[int, ...] = ()
    leader: int | None = None

    def _seat_total(seat: int) -> int:
        base = seat * PIECES_PER_SEAT
        return sum(positions[base + offset] for offset in range(PIECES_PER_SEAT))

    def _holds_barrier(seat: int) -> bool:
        """Two of ``seat``'s pieces on one ring field, read off positions."""
        base = seat * PIECES_PER_SEAT
        fields = [
            board.ring_field(seat, positions[base + offset])
            for offset in range(PIECES_PER_SEAT)
            if 1 <= positions[base + offset] <= ring_length
        ]
        return len(fields) != len(set(fields))

    def _entry_waiting(seat: int) -> bool:
        """D-1: no piece on the ring, and no goal piece movable by any value.

        Reimplemented here rather than imported: calling the engine's predicate would reduce
        AK-9 to one implementation invoked twice.
        """
        base = seat * PIECES_PER_SEAT
        pieces = [positions[base + offset] for offset in range(PIECES_PER_SEAT)]
        if any(1 <= pos <= ring_length for pos in pieces):
            return False
        occupied = {pos - ring_length - 1 for pos in pieces if pos > ring_length}
        for index in occupied:
            for roll in range(1, 7):
                target = index + roll
                if target >= 4 or target in occupied:
                    continue
                if rules.goal_no_jump and any(
                    step in occupied for step in range(index + 1, target)
                ):
                    continue
                return False
        return True

    def _close_turn() -> None:
        """Recompute leader(t) exactly as §6.1 defines it, over positions."""
        nonlocal leader, lead_changes, turns_without_leader
        if finished:
            return
        totals = {seat: _seat_total(seat) for seat in seats}
        best = max(totals.values())
        tied = [seat for seat in seats if totals[seat] == best]
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

    #: A turn boundary in the stream is a ``roll`` with attempt number 1.
    open_turn = False
    turn_seat = -1
    turn_moved = False

    def _end_turn() -> None:
        """Close the open turn, counting it as a pass if nothing moved.

        ``passes_by_seat`` counts turns with no legal move (§6.2), while the log emits one
        ``pass`` event per unusable roll (§4.1): a turn of three attempts that never moves is
        one pass and three events (D-71).
        """
        nonlocal turn_moved, trace_open, final_margin
        if not turn_moved and turn_seat >= 0:
            passes_by_seat[turn_seat] += 1
        # The first-win segment's progress trace, closed by the turn in which the first seat
        # finished — that turn belongs to the segment.
        if trace_open:
            progress_trace.append(tuple(_seat_total(seat) for seat in seats))
            if finished:
                trace_open = False
                winner_total = _seat_total(finished[0])
                others = sorted(
                    (_seat_total(seat) for seat in seats if seat != finished[0]),
                    reverse=True,
                )
                final_margin = winner_total - others[0] if others else 0
        _close_turn()
        turn_moved = False

    for event in events:
        if isinstance(event, RollEvent):
            if event.attempt == 1:
                if open_turn:
                    _end_turn()
                turns += 1
                open_turn = True
                turn_seat = event.seat
                # Turn-start quantities, evaluated before this turn's moves land, which is
                # where §6.2 defines them.
                if rules.barriers:
                    for seat in seats:
                        if _holds_barrier(seat):
                            barrier_turns_seat[seat] += 1
                if _entry_waiting(event.seat):
                    entry_waits[event.seat] += 1
            dice_rolls += 1
        elif isinstance(event, MoveEvent):
            turn_moved = True
            # The offered set is on the event, so the extended-capture obligation is visible
            # without replaying legality: it applied when a capture was forced and every
            # option cost a lap.
            if (
                event.restriction == "capture"
                and event.legal
                and all(
                    kind == "ring" and to_pos < from_pos and from_pos + 6 > ring_length
                    for _piece, from_pos, to_pos, kind, _captures in event.legal
                )
            ):
                extra_lap_offered += 1
            positions[event.piece] = event.to_pos
            # An extra lap is the one move kind whose target lies behind its origin on the
            # ring, which is visible in the stream without any engine state.
            if (
                event.kind == "ring"
                and event.to_pos < event.from_pos
                and event.from_pos + 6 > ring_length
            ):
                extra_laps[event.seat] += 1
        elif isinstance(event, CaptureEvent):
            positions[event.victim_seat * PIECES_PER_SEAT + event.victim_piece] = 0
            captures_total += 1
            captures_by_seat[event.captor_seat] += 1
            captured_by_seat[event.victim_seat] += 1
        elif isinstance(event, PassEvent):
            # Counted at turn scope in _end_turn, not here — see D-71.
            pass
        elif isinstance(event, FinishEvent):
            finished.append(event.seat)
            if len(finished) == 1:
                turns_to_first_win = turns
        elif isinstance(event, GameEndEvent):
            if open_turn:
                _end_turn()
                open_turn = False
            ranks = event.ranks
        else:  # BarrierEvent
            if getattr(event, "formed", False):
                barriers_formed += 1
    if open_turn:
        _end_turn()

    players = len(seats)
    max_progress = 4 * ring_length + 10

    def _checkpoint(num: int, den: int) -> tuple[int, bool]:
        if turns_to_first_win <= 0 or not progress_trace or not ranks:
            return -1, False
        turn = -(-turns_to_first_win * num // den)
        snapshot = progress_trace[max(1, min(turn, len(progress_trace))) - 1]
        winner_index = seats.index(ranks[0])
        mine = snapshot[winner_index]
        rank = 1 + sum(1 for value in snapshot if value > mine)
        tied = any(
            value == mine for index, value in enumerate(snapshot) if index != winner_index
        )
        return rank, tied

    rank_50, tied_50 = _checkpoint(1, 2)
    rank_75, _ = _checkpoint(3, 4)
    threshold = 2 if players <= 3 else 3

    return {
        "turns": turns,
        "dice_rolls": dice_rolls,
        "turns_to_first_win": turns_to_first_win,
        "captures_total": captures_total,
        "captures_by_seat": tuple(captures_by_seat),
        "captured_by_seat": tuple(captured_by_seat),
        "passes_by_seat": tuple(passes_by_seat),
        "entry_waits_by_seat": tuple(entry_waits),
        "lead_changes": lead_changes,
        "turns_without_leader": turns_without_leader,
        "time_in_lead_by_seat": tuple(time_in_lead),
        "extra_laps_by_seat": tuple(extra_laps),
        "barriers_formed": barriers_formed,
        "barrier_turns_by_seat": tuple(barrier_turns_seat),
        "forced_extra_lap_offered": extra_lap_offered,
        "winner_rank_at_50": rank_50,
        "winner_rank_at_75": rank_75,
        "winner_rank_at_50_tied": tied_50,
        "comeback": rank_50 >= threshold if rank_50 > 0 else False,
        "comeback_rank_threshold": threshold,
        "comeback_depth": (
            (rank_50 - 1) / (players - 1) if rank_50 > 0 and players > 1 else 0.0
        ),
        "final_margin": final_margin,
        "final_margin_norm": final_margin / max_progress if max_progress else 0.0,
        "ranks": ranks,
        "winner": ranks[0] if ranks else -1,
        "final_positions": tuple(positions),
    }

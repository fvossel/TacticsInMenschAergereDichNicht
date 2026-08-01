"""AK-9 — an independent re-derivation of the summary row from the event log.

§4.1 forbids analyses from re-deriving a number the summary row already
carries, and that rule removes the only redundant path: a wrong
``lead_changes`` or ``winner_rank_at_50`` would pass AK-1 through AK-7
unchanged and go straight into ``docs/results.md``. AK-9 is the one place the
rule is violated **on purpose**, so the absent cross-check stops being
load-bearing.

The point is that this is a *different* route, not the same code twice. The
game loop accumulates counters as it plays. This walks the finished event
stream, reconstructs the board from the moves, and recomputes everything from
positions. Two implementations agreeing is evidence; one implementation called
twice is not.
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

    Returns a mapping keyed the way :class:`~madnlab.eventlog.writer.SummaryRow`
    is, restricted to the fields an event stream can support. Fields the log
    cannot see — the seeds, the config echo — are not returned rather than
    guessed, so a caller comparing dictionaries compares only what was actually
    re-derived.
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
    passes_by_seat = [0] * board.seats
    time_in_lead = [0] * board.seats
    extra_laps = [0] * board.seats

    dice_rolls = captures_total = lead_changes = turns_without_leader = 0
    barriers_formed = 0
    turns = 0
    turns_to_first_win = 0
    finished: list[int] = []
    ranks: tuple[int, ...] = ()
    leader: int | None = None

    def _seat_total(seat: int) -> int:
        base = seat * PIECES_PER_SEAT
        return sum(positions[base + offset] for offset in range(PIECES_PER_SEAT))

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

        ``passes_by_seat`` counts **turns** with no legal move (§6.2), while
        the log emits one ``pass`` event per unusable **roll** (§4.1) — a turn
        of three attempts that never moves is one pass and three events. AK-9
        found the two being conflated here; counting pass events would have
        over-reported passes by the number of extra rolls (D-71).
        """
        nonlocal turn_moved
        if not turn_moved and turn_seat >= 0:
            passes_by_seat[turn_seat] += 1
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
            dice_rolls += 1
        elif isinstance(event, MoveEvent):
            turn_moved = True
            positions[event.piece] = event.to_pos
            # An extra lap is the one move kind whose target is *behind* its
            # origin on the ring, which is visible in the stream without any
            # engine state.
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

    return {
        "turns": turns,
        "dice_rolls": dice_rolls,
        "turns_to_first_win": turns_to_first_win,
        "captures_total": captures_total,
        "captures_by_seat": tuple(captures_by_seat),
        "passes_by_seat": tuple(passes_by_seat),
        "lead_changes": lead_changes,
        "turns_without_leader": turns_without_leader,
        "time_in_lead_by_seat": tuple(time_in_lead),
        "extra_laps_by_seat": tuple(extra_laps),
        "barriers_formed": barriers_formed,
        "ranks": ranks,
        "winner": ranks[0] if ranks else -1,
        "final_positions": tuple(positions),
    }

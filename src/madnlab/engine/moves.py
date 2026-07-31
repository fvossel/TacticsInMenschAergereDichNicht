"""Legality — the single source of truth (GM-7).

:func:`legal_moves` implements *all* of requirements §2.3–§2.6, parameterized
by the rule flags. The game loop, every agent, the replay validator and the UI
consume this one function; nothing re-implements any part of it.

The returned list is ordered canonically (D-3), so agent tie-breaking is
reproducible and the ``chosen index`` recorded in the event log means the same
thing on replay.

Structure of the implementation
-------------------------------
1. :func:`_candidate_moves` generates every move that is legal on its own
   terms — geometry, occupancy, barriers, exact fit, goal jumping.
2. :func:`legal_moves_with_restriction` applies the GM-5.1 priority lattice,
   which can only ever *narrow* that set:

   ``entry-clearing > forced entry > mandatory capture``

3. The survivors are sorted canonically.

Keeping generation and forcing apart is what makes the lattice auditable:
every restriction is one filter over one list, and the restriction that fired
is reported so the event log can record it (§4.1) and AK-5 can count it.
"""

from __future__ import annotations

import enum
from typing import NamedTuple

from madnlab.engine.geometry import (
    GOAL_FIELDS,
    PIECES_PER_SEAT,
    POS_YARD,
    Board,
    PieceLocation,
)
from madnlab.engine.rules import CaptureMode, RuleSet
from madnlab.engine.state import GameState, piece_index, seat_of


class MoveKind(enum.StrEnum):
    """Move kinds as recorded in the event log (§4.1)."""

    ENTER = "enter"
    RING = "ring"
    GOAL_ENTER = "goal_enter"
    GOAL = "goal"


class Restriction(enum.StrEnum):
    """Which clause of the GM-5.1 lattice narrowed the legal set.

    Recorded on every ``move`` event (§4.1). AK-5 counts a capture obligation
    as *offered* only when this is :attr:`CAPTURE`, which is what makes the
    gate independent of the lattice's direction (D-32).
    """

    NONE = "none"
    CLEARING = "clearing"
    FORCED_ENTRY = "forced_entry"
    CAPTURE = "capture"


class Move(NamedTuple):
    """One legal move.

    ``piece`` is the global piece index (``seat * 4 + p``), stable for the
    whole game. ``captures`` is the global index of the captured piece or
    ``None`` — the event log writes it per offered move so AK-5 can be checked
    from a sampled log without re-simulating (§4.1).
    """

    piece: int
    from_pos: int
    to_pos: int
    kind: MoveKind
    captures: int | None = None
    #: True for a ``mandatory_extended`` move forced past the own goal entry
    #: onto another lap (GM-5). Feeds ``extra_laps_by_seat`` (§6.2).
    extra_lap: bool = False


# -- occupancy --------------------------------------------------------------


def _ring_occupancy(board: Board, state: GameState) -> dict[int, tuple[int, ...]]:
    """Map absolute ring field -> global indices of the pieces standing there.

    Only ring pieces appear. A field with two entries is a barrier, which is
    reachable only under ``barriers = True``; goal columns are strictly one
    piece per field (D-34) and are not represented here.
    """
    occupancy: dict[int, tuple[int, ...]] = {}
    ring_length = board.ring_length
    for index, pos in enumerate(state.positions):
        if pos == POS_YARD or pos > ring_length:
            continue
        field = board.ring_field(index // PIECES_PER_SEAT, pos)
        occupancy[field] = occupancy.get(field, ()) + (index,)
    return occupancy


def _is_barrier(occupancy: dict[int, tuple[int, ...]], field: int) -> bool:
    """Two pieces on one field. Blocks passage and landing for everyone."""
    return len(occupancy.get(field, ())) >= 2


def _landing(
    occupancy: dict[int, tuple[int, ...]],
    field: int,
    seat: int,
    rules: RuleSet,
) -> tuple[bool, int | None]:
    """Whether ``seat`` may land on ``field``, and whom it captures.

    Returns ``(allowed, captured_index)``.

    * empty -> allowed, no capture
    * one own piece -> allowed only with ``barriers`` (forms a barrier,
      GM-6.1); otherwise the no-stacking clause GM-3.6 forbids it
    * one opponent piece -> allowed, captures it (GM-3.6)
    * two pieces -> a barrier; not landable and not capturable (GM-6.2/6.3)
    """
    occupants = occupancy.get(field, ())
    if not occupants:
        return True, None
    if len(occupants) >= 2:
        return False, None
    occupant = occupants[0]
    if seat_of(occupant) == seat:
        return rules.barriers, None
    return True, occupant


def _ring_path_clear(
    board: Board,
    occupancy: dict[int, tuple[int, ...]],
    seat: int,
    from_pos: int,
    steps: int,
    rules: RuleSet,
) -> bool:
    """Whether the ring fields strictly between origin and target are passable.

    Only barriers block passage (GM-6.2); single pieces are passed over
    freely. Without ``barriers`` no field can hold two pieces, so the scan is
    skipped entirely.

    ``steps`` counts the intermediate fields, i.e. the target itself is *not*
    checked here — :func:`_landing` does that.
    """
    if not rules.barriers or steps <= 0:
        return True
    for offset in range(1, steps + 1):
        if _is_barrier(occupancy, board.ring_field(seat, from_pos + offset)):
            return False
    return True


def _goal_path_clear(
    board: Board,
    state: GameState,
    seat: int,
    first_index: int,
    target_index: int,
    rules: RuleSet,
) -> bool:
    """Whether the goal column allows the move to ``target_index``.

    The target field must always be free — goal columns are one piece per
    field (D-34, GM-3.7). With ``goal_no_jump`` every goal field strictly
    before the target must be free as well; the official variant's second
    sentence, that the last piece coming home can only enter on the first goal
    field, follows from this and needs no separate rule.
    """
    occupied = {
        board.goal_index(pos)
        for pos in state.seat_positions(seat)
        if board.location(pos) is PieceLocation.GOAL
    }
    if target_index in occupied:
        return False
    if not rules.goal_no_jump:
        return True
    return all(index not in occupied for index in range(first_index, target_index))


# -- candidate generation ---------------------------------------------------


def _candidate_moves(
    board: Board,
    state: GameState,
    seat: int,
    roll: int,
    rules: RuleSet,
    occupancy: dict[int, tuple[int, ...]],
) -> list[Move]:
    """Every move legal on its own terms, before the GM-5.1 lattice."""
    moves: list[Move] = []
    ring_length = board.ring_length
    entry_emitted = False

    for piece in range(PIECES_PER_SEAT):
        index = piece_index(seat, piece)
        pos = state.positions[index]
        location = board.location(pos)

        # -- from the yard: entry (GM-3.2 / GM-3.5 / cold_start) ------------
        if location is PieceLocation.YARD:
            # Exactly one entry move is generated, for the lowest-index yard
            # piece (D-60). Yard pieces are indistinguishable, so emitting one
            # move per yard piece would put duplicates in the legal set — and
            # since RANDOM chooses uniformly over that set, entering would be
            # oversampled by the number of pieces still in the yard. The
            # duplicates are not a cosmetic issue; they would bias every
            # campaign that contains a RANDOM field.
            if entry_emitted:
                continue
            if rules.cold_start.requires_six_to_enter and roll != 6:
                continue
            field = board.entry_field(seat)
            allowed, captured = _landing(occupancy, field, seat, rules)
            if allowed:
                moves.append(Move(index, pos, 1, MoveKind.ENTER, captured))
                entry_emitted = True
            continue

        # -- from the goal column: advance inside it -----------------------
        if location is PieceLocation.GOAL:
            current = board.goal_index(pos)
            target = current + roll
            # D-54: a roll that would carry the piece past the last goal field
            # generates no move. The rulebook is silent; this is the project
            # choice, and it is deliberately not a bounce-back.
            if target >= GOAL_FIELDS:
                continue
            if _goal_path_clear(board, state, seat, current + 1, target, rules):
                moves.append(Move(index, pos, board.goal_pos(target), MoveKind.GOAL))
            continue

        # -- from the ring --------------------------------------------------
        destination = pos + roll

        if destination <= ring_length:
            # Stays on the ring.
            if not _ring_path_clear(board, occupancy, seat, pos, roll - 1, rules):
                continue
            field = board.ring_field(seat, destination)
            allowed, captured = _landing(occupancy, field, seat, rules)
            if allowed:
                moves.append(Move(index, pos, destination, MoveKind.RING, captured))
            continue

        # Would pass the own goal entry, so it enters the goal column
        # (GM-3.8). ``ring_steps`` is how much of the roll is spent on the
        # ring before the column starts.
        ring_steps = ring_length - pos
        goal_target = destination - ring_length - 1

        # Exact fit on entry (GM-3.8, verified): a roll that overshoots the
        # column does not produce a move for this piece.
        if goal_target < GOAL_FIELDS and _ring_path_clear(
            board, occupancy, seat, pos, ring_steps, rules
        ):
            if _goal_path_clear(board, state, seat, 0, goal_target, rules):
                moves.append(
                    Move(index, pos, board.goal_pos(goal_target), MoveKind.GOAL_ENTER)
                )

        # mandatory_extended (GM-5): continuing on the ring past the own goal
        # entry is otherwise impossible, and becomes legal exactly when it
        # captures. The lattice then forces it, because it lands in the
        # capturing set.
        if rules.capture_mode is CaptureMode.MANDATORY_EXTENDED:
            lap_pos = destination - ring_length
            if not _ring_path_clear(board, occupancy, seat, pos, roll - 1, rules):
                continue
            field = board.ring_field(seat, lap_pos)
            allowed, captured = _landing(occupancy, field, seat, rules)
            if allowed and captured is not None:
                moves.append(
                    Move(index, pos, lap_pos, MoveKind.RING, captured, extra_lap=True)
                )

    return moves


# -- the GM-5.1 priority lattice -------------------------------------------


def _has_yard_piece(state: GameState, seat: int) -> bool:
    return any(pos == POS_YARD for pos in state.seat_positions(seat))


def _entry_field_occupants(state: GameState, seat: int) -> tuple[int, ...]:
    """Own pieces standing on the own entry field (position 1)."""
    base = seat * PIECES_PER_SEAT
    return tuple(
        base + piece
        for piece, pos in enumerate(state.seat_positions(seat))
        if pos == 1
    )


def _canonical(moves: list[Move]) -> tuple[Move, ...]:
    """Canonical move ordering (D-3).

    Goal moves before ring moves, then by piece index ascending, then by
    target position ascending. The third key is a safety net: a piece
    contributes at most one move per group, so ``(group, piece)`` is already
    unique except under ``mandatory_extended``, where the two moves of one
    piece fall into different groups anyway.

    "Target field" is read as the target *position* in the piece's own frame,
    which is monotone in distance travelled; the absolute ring field wraps and
    would make the order depend on the seat.
    """
    return tuple(
        sorted(
            moves,
            key=lambda m: (
                0 if m.kind in (MoveKind.GOAL, MoveKind.GOAL_ENTER) else 1,
                m.piece,
                m.to_pos,
            ),
        )
    )


def legal_moves_with_restriction(
    board: Board,
    state: GameState,
    seat: int,
    roll: int,
    rules: RuleSet,
) -> tuple[tuple[Move, ...], Restriction]:
    """Legal moves plus the lattice clause that produced them.

    The game loop uses this so the ``move`` event can record ``restriction``
    (§4.1) and the AK-5 counters can be maintained. Agents use
    :func:`legal_moves`, which drops the second element.
    """
    occupancy = _ring_occupancy(board, state)
    candidates = _candidate_moves(board, state, seat, roll, rules, occupancy)
    if not candidates:
        return (), Restriction.NONE

    # 1. Entry-field clearing (GM-3.4). Verified official, and stated by the
    #    rulebook as an express exception *inside* the 6-rule, so the priority
    #    is textual rather than an artefact of clause ordering (D-2).
    if _has_yard_piece(state, seat):
        occupants = _entry_field_occupants(state, seat)
        if occupants:
            clearing = [m for m in candidates if m.piece in occupants]
            if clearing:
                return _canonical(clearing), Restriction.CLEARING

    # 2. Forced entry on a 6 (GM-3.5). Never fires under ``free_entry``, where
    #    entering is an ordinary legal move (D-7). Reaching this point means
    #    clearing was either not in force or not legal — which is exactly
    #    D-52's second clause: an entry-field occupant that cannot move gives
    #    way to the ordinary forced entry.
    if (
        rules.cold_start.requires_six_to_enter
        and roll == 6
        and _has_yard_piece(state, seat)
    ):
        entries = [m for m in candidates if m.kind is MoveKind.ENTER]
        if entries:
            return _canonical(entries), Restriction.FORCED_ENTRY

    # 3. Mandatory capture (GM-5). Subordinate to both clauses above, by the
    #    project owner's decision recorded in D-9.
    if rules.capture_mode.is_forcing:
        capturing = [m for m in candidates if m.captures is not None]
        if capturing:
            return _canonical(capturing), Restriction.CAPTURE

    return _canonical(candidates), Restriction.NONE


def legal_moves(
    board: Board,
    state: GameState,
    seat: int,
    roll: int,
    rules: RuleSet,
) -> tuple[Move, ...]:
    """The ordered legal-move set for ``seat`` given ``roll`` (GM-7).

    Total: returns an empty tuple when the seat has no legal move, in which
    case the turn passes (GM-3.9).
    """
    return legal_moves_with_restriction(board, state, seat, roll, rules)[0]

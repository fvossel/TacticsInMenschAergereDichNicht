"""Game state, held as a flat tuple of ints (NF-2).

There is no per-piece object. A state is ``positions``, a tuple of
``seats * 4`` integers using the encoding documented in
:mod:`madnlab.engine.geometry`, plus the small amount of bookkeeping the game
loop needs. Applying a move produces a new tuple; nothing is mutated.

The global index of seat ``s``'s piece ``p`` is ``s * 4 + p``. Piece indices
are stable for the whole game, which is what lets the canonical move order
(D-3) and the event log refer to pieces by number.
"""

from __future__ import annotations

from typing import NamedTuple

from madnlab.engine.geometry import (
    GOAL_FIELDS,
    PIECES_PER_SEAT,
    POS_YARD,
    Board,
    PieceLocation,
)
from madnlab.engine.rules import ColdStart, RuleSet


class GameState(NamedTuple):
    """An immutable game state.

    ``positions`` is indexed by global piece index. ``finished`` is the
    realized finishing order, which is what GM-3.11's ``play_out`` ranks are
    read from; a seat appears in it once all four of its pieces are home.
    """

    positions: tuple[int, ...]
    finished: tuple[int, ...] = ()

    # -- accessors ----------------------------------------------------------

    def pos(self, seat: int, piece: int) -> int:
        return self.positions[seat * PIECES_PER_SEAT + piece]

    def seat_positions(self, seat: int) -> tuple[int, ...]:
        base = seat * PIECES_PER_SEAT
        return self.positions[base : base + PIECES_PER_SEAT]

    def is_finished(self, seat: int) -> bool:
        return seat in self.finished


def piece_index(seat: int, piece: int) -> int:
    return seat * PIECES_PER_SEAT + piece


def seat_of(index: int) -> int:
    return index // PIECES_PER_SEAT


def initial_state(board: Board, seats_in_play: tuple[int, ...], rules: RuleSet) -> GameState:
    """Build the opening position for ``seats_in_play`` (GM-3.2).

    Under the baseline ``one_piece_out`` each occupied seat starts with piece 0
    on its own entry field and pieces 1..3 in the yard — the official setup,
    verified against all three editions (D-55). ``strict`` and ``free_entry``
    start with all four pieces in the yard.

    Unoccupied seats keep their pieces in the yard and never move; the game
    loop skips them.
    """
    positions = [POS_YARD] * (board.seats * PIECES_PER_SEAT)
    if rules.cold_start is ColdStart.ONE_PIECE_OUT:
        for seat in seats_in_play:
            positions[piece_index(seat, 0)] = 1  # pos 1 == the own entry field
    return GameState(positions=tuple(positions))


# -- progress (§6.1) --------------------------------------------------------


def progress_of_piece(pos: int) -> int:
    """Progress of a single piece.

    The position encoding *is* the progress value, so this is the identity —
    it exists so call sites read as the specification does and so the one
    definition has one name. See :mod:`madnlab.engine.geometry` for why a
    lapped piece under ``mandatory_extended`` drops back rather than
    overtaking goal pieces (D-8).
    """
    return pos


def progress_of_seat(state: GameState, seat: int) -> int:
    """Sum of a seat's four piece progress values (§6.1)."""
    base = seat * PIECES_PER_SEAT
    return sum(state.positions[base : base + PIECES_PER_SEAT])


def normalized_progress(board: Board, state: GameState, seat: int) -> float:
    """Seat progress divided by the lap-0 seat maximum (§6.1, D-8)."""
    return progress_of_seat(state, seat) / board.max_progress_per_seat


def track_progress(board: Board, pos: int) -> int | None:
    """Ranking key for the movement agents (D-43a).

    ``progress`` restricted to pieces **on the ring**; pieces in the yard and
    in the goal column are excluded from the ranking entirely and yield
    ``None``. Defined here rather than in the agents so that all of them
    consume one definition, the way every consumer consumes one
    ``legal_moves``.
    """
    return pos if board.location(pos) is PieceLocation.RING else None


def seat_has_finished(board: Board, state: GameState, seat: int) -> bool:
    """Whether all four of ``seat``'s pieces stand in its goal column.

    The goal column has exactly :data:`GOAL_FIELDS` fields and a seat has
    exactly :data:`PIECES_PER_SEAT` pieces, both 4, and the column holds at
    most one piece per field (D-34) — so "all four are in the column" is the
    win condition and needs no per-field check.
    """
    assert GOAL_FIELDS == PIECES_PER_SEAT  # the equality the argument rests on
    return all(pos > board.ring_length for pos in state.seat_positions(seat))

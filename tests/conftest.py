"""Shared fixtures and builders for the acceptance suite."""

from __future__ import annotations

from collections.abc import Iterable

import pytest

from madnlab.engine.geometry import PIECES_PER_SEAT, Board, board_for
from madnlab.engine.rules import ColdStart, RuleSet
from madnlab.engine.state import GameState


@pytest.fixture(scope="session")
def b4() -> Board:
    return board_for(4)


@pytest.fixture(scope="session")
def b6() -> Board:
    return board_for(6)


def state_for(board: Board, **seat_positions: Iterable[int]) -> GameState:
    """Build a state from ``s0=(...), s1=(...)`` keyword arguments.

    Seats not named keep all four pieces in the yard. Positions use the
    encoding in :mod:`madnlab.engine.geometry`: 0 yard, ``1..R`` ring,
    ``R+1..R+4`` goal.
    """
    positions = [0] * (board.seats * PIECES_PER_SEAT)
    for key, values in seat_positions.items():
        seat = int(key[1:])
        for piece, pos in enumerate(values):
            positions[seat * PIECES_PER_SEAT + piece] = pos
    return GameState(positions=tuple(positions))


def pos_on_field(board: Board, seat: int, field: int) -> int:
    """The position at which ``seat``'s piece stands on absolute ``field``.

    The inverse of :meth:`Board.ring_field` over ``1..ring_length``. Scenarios
    must go through this rather than solving the modulo by hand: an
    out-of-range position happens to land on the right field because
    ``ring_field`` reduces modulo the ring (D-64), so a hand-rolled offset can
    place a piece at a position no game state can reach and still make the
    assertion pass.
    """
    pos = (field - seat * board.spacing) % board.ring_length + 1
    assert board.ring_field(seat, pos) == field
    return pos


#: ``strict`` puts all four pieces in the yard, which keeps most scenarios free
#: of the entry-clearing rule that the baseline triggers from turn one. Where
#: clearing is the thing under test the baseline is used instead.
STRICT = RuleSet(cold_start=ColdStart.STRICT)
FREE = RuleSet(cold_start=ColdStart.FREE_ENTRY)


def targets(moves: Iterable[object], piece: int | None = None) -> list[int]:
    """Target positions of ``moves``, optionally filtered to one piece."""
    return [
        m.to_pos  # type: ignore[attr-defined]
        for m in moves
        if piece is None or m.piece == piece  # type: ignore[attr-defined]
    ]

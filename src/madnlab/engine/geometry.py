"""Board geometry (GM-1) and the piece-position encoding.

Every position is a pure function of ``(seats, seat_index)``. The only
board-specific constants are the ring length and the start-field spacing in
:data:`_RING_LENGTH` and :data:`_SPACING`; everything else is derived.

Position encoding
-----------------
A piece's position is stored as a single integer that **is** its progress
value as defined in requirements §6.1, so no conversion is needed between the
engine and the metric layer:

===================  ==========================================
``pos``              meaning
===================  ==========================================
``0``                in the yard ("B" fields)
``1 .. R``           on the ring, ``pos - 1`` steps past own entry
``R+1 .. R+4``       in the goal column, index ``pos - R - 1``
===================  ==========================================

with ``R`` the ring length. ``pos == R`` is the seat's own goal-entry field,
the last ring field before its goal column.

Under ``capture_mode = mandatory_extended`` a piece can be forced past its own
goal entry onto another lap (GM-5). Per D-8 the ring component is stored
modulo the ring length, so such a piece drops back to a low ``pos`` rather
than colliding with the goal encoding, progress is not monotone in time in
that arm, and GM-3.8 re-applies on the next pass without any lap-count state
being carried on the piece.
"""

from __future__ import annotations

import enum
from typing import Final, NamedTuple

#: Ring track length per board (GM-1).
_RING_LENGTH: Final[dict[int, int]] = {4: 40, 6: 48}

#: Distance between two seats' entry fields on the ring (GM-1).
_SPACING: Final[dict[int, int]] = {4: 10, 6: 8}

#: Pieces per seat, and goal fields per seat. Both are 4 on every board, and
#: the equality is load-bearing: D-1's three-attempts condition omits a
#: yard-occupancy guard because 0 pieces on the ring and 0 in the yard implies
#: all four are home, which is the win condition.
PIECES_PER_SEAT: Final[int] = 4
GOAL_FIELDS: Final[int] = 4

#: Sentinel position for a piece in the yard.
POS_YARD: Final[int] = 0


class PieceLocation(enum.IntEnum):
    """Coarse classification of a position, for readable branching."""

    YARD = 0
    RING = 1
    GOAL = 2


class Board(NamedTuple):
    """Immutable geometry for one board size.

    Construct with :func:`board_for`, which validates ``seats`` and caches.
    """

    seats: int
    ring_length: int
    spacing: int

    # -- position classification -------------------------------------------

    def location(self, pos: int) -> PieceLocation:
        if pos == POS_YARD:
            return PieceLocation.YARD
        if pos <= self.ring_length:
            return PieceLocation.RING
        return PieceLocation.GOAL

    # -- ring geometry ------------------------------------------------------

    def entry_field(self, seat: int) -> int:
        """Absolute ring field of ``seat``'s entry field ("A")."""
        return (seat * self.spacing) % self.ring_length

    def goal_entry_field(self, seat: int) -> int:
        """Absolute ring field directly before ``seat``'s goal column.

        A piece reaches it after ``ring_length - 1`` steps, i.e. at
        ``pos == ring_length``; the next step enters the goal column. Expressed
        through :meth:`ring_field` so the seat offset has exactly one
        definition (D-3).
        """
        return self.ring_field(seat, self.ring_length)

    def ring_field(self, seat: int, pos: int) -> int:
        """Absolute ring field of ``seat``'s piece standing at ``pos``.

        ``pos`` is normally a ring position (``1 <= pos <= ring_length``), but
        the domain is wider: ``pos`` may exceed the ring length and is reduced
        modulo it (D-64). The wrap is load-bearing. ``mandatory_extended``'s
        extra-lap path scan walks positions up to ``ring_length + 5``, and the
        barrier checks along that path read the wrapped fields of the next lap,
        so an NF-2 optimization pass has to reproduce the wrap rather than
        bound the index at ``ring_length``.
        """
        return (seat * self.spacing + pos - 1) % self.ring_length

    # -- goal geometry ------------------------------------------------------

    def goal_index(self, pos: int) -> int:
        """Goal-column index (0 = outermost) of a goal position."""
        return pos - self.ring_length - 1

    def goal_pos(self, index: int) -> int:
        """Position value for goal-column index ``index``."""
        return self.ring_length + 1 + index

    # -- progress -----------------------------------------------------------

    @property
    def max_progress_per_piece(self) -> int:
        """Progress of a piece on the innermost goal field."""
        return self.ring_length + GOAL_FIELDS

    @property
    def max_progress_per_seat(self) -> int:
        """Sum of all four pieces' progress when a seat has finished.

        170 on the 4-seat board, 202 on the 6-seat board (requirements §2.1).
        Used as the normalization denominator in §6.1; per D-8 it is the lap-0
        maximum and is not raised by ``mandatory_extended``'s extra laps.
        """
        top = self.max_progress_per_piece
        return sum(range(top - GOAL_FIELDS + 1, top + 1))


_BOARD_CACHE: dict[int, Board] = {}


def board_for(seats: int) -> Board:
    """Return the :class:`Board` for ``seats``, which must be 4 or 6."""
    try:
        return _BOARD_CACHE[seats]
    except KeyError:
        pass
    if seats not in _RING_LENGTH:
        raise ValueError(
            f"unsupported seat count {seats!r}: the specification defines the "
            f"4-seat and 6-seat boards only (requirements §2.1, §12)"
        )
    board = Board(seats=seats, ring_length=_RING_LENGTH[seats], spacing=_SPACING[seats])
    _BOARD_CACHE[seats] = board
    return board


# -- seat patterns (GM-2) ---------------------------------------------------


class SeatPattern(enum.StrEnum):
    """Named player-to-seat assignments (requirements §2.2)."""

    ADJACENT = "adjacent"
    SPREAD = "spread"
    OPPOSITE = "opposite"


def occupied_seats(seats: int, players: int, pattern: SeatPattern) -> tuple[int, ...]:
    """Seat indices occupied by ``players`` players under ``pattern``.

    ``adjacent`` fills seats ``0..players-1``. ``spread`` means maximally even
    spacing, ``step = seats // players``, which requires ``players`` to divide
    ``seats`` (D-65); even spacing rather than a literal "every second seat" is
    the property EX-5 tests, and it is the reading §8's spread cells use.
    ``opposite`` is defined for two players only.

    The ``players >= 2`` floor is §2.4's measured-axis range, and the three
    patterns are degenerate at one player. AK-8b's single-player calibration
    configuration does not go through here: it passes a seat tuple to
    ``initial_state`` directly (D-66).
    """
    if players > seats:
        raise ValueError(
            f"{players} players do not fit on a {seats}-seat board "
            f"(requirements §2.4 constrains players <= seats)"
        )
    if players < 2:
        raise ValueError(
            f"{players} players is below the measured range: requirements §2.4 "
            f"defines the players axis as 2-6, and the seat patterns are "
            f"degenerate at one player. AK-8b's 1-player calibration cell builds "
            f"its seat tuple directly instead (D-66)"
        )

    if pattern is SeatPattern.ADJACENT:
        return tuple(range(players))

    if pattern is SeatPattern.SPREAD:
        if seats % players:
            raise ValueError(
                f"seat_pattern 'spread' needs players to divide seats evenly; "
                f"{players} players do not divide {seats} seats"
            )
        step = seats // players
        return tuple(i * step for i in range(players))

    if pattern is SeatPattern.OPPOSITE:
        if players != 2:
            raise ValueError("seat_pattern 'opposite' is defined for 2 players only")
        return (0, seats // 2)

    raise AssertionError(f"unhandled seat pattern {pattern!r}")

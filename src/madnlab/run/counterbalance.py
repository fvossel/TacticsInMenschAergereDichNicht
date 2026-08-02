"""Seat and starting-player counterbalancing (§7.3, D-39).

A cell's games are spread evenly over the strategy→seat arrangements and the starting seats, so
a seat effect cannot be mistaken for a strategy effect. §7.3 also forbids averaging a seat
effect away silently, which is why every row records the arrangement and starting seat it ran
under rather than only the aggregate.

Balance block
-------------
``B = (#arrangements) × (#starting seats)``. Game ``i`` takes arrangement
``(i mod B) // #starting_seats`` and starting seat ``i mod #starting_seats``, so every complete
block covers every combination exactly once. A cell's ``n_effective`` is ``n_requested`` rounded
up to a whole number of blocks (D-39), so every arrangement-by-starting-seat combination runs
the same number of games.

Which arrangements
------------------
Full permutations exactly when a cell contains two or more distinct non-field strategies;
cyclic rotations otherwise (D-39). For a homogeneous cell every rotation is the same
assignment, so there is one arrangement and only the starting seat is balanced (D-25).
"""

from __future__ import annotations

from collections.abc import Sequence
from itertools import permutations
from typing import NamedTuple

from madnlab.engine.geometry import SeatPattern


class Balance(NamedTuple):
    """The counterbalancing plan for one cell."""

    arrangements: tuple[tuple[str, ...], ...]
    starting_seats: tuple[int, ...]
    mode: str

    @property
    def block(self) -> int:
        """``B`` — games per complete block."""
        return len(self.arrangements) * len(self.starting_seats)

    def effective_games(self, requested: int) -> int:
        """``n_requested`` rounded up to a whole number of blocks (D-39)."""
        if requested < 0:
            raise ValueError(f"requested must be non-negative, got {requested}")
        block = self.block
        return -(-requested // block) * block

    def assign(self, game_index: int) -> tuple[tuple[str, ...], int, int, int]:
        """``(agent_ids, starting_seat, arrangement_index, start_index)``."""
        within = game_index % self.block
        arrangement_index = within // len(self.starting_seats)
        start_index = within % len(self.starting_seats)
        return (
            self.arrangements[arrangement_index],
            self.starting_seats[start_index],
            arrangement_index,
            start_index,
        )


def _rotations(agent_ids: Sequence[str]) -> list[tuple[str, ...]]:
    length = len(agent_ids)
    seen: list[tuple[str, ...]] = []
    for offset in range(length):
        rotated = tuple(agent_ids[offset:]) + tuple(agent_ids[:offset])
        if rotated not in seen:
            seen.append(rotated)
    return seen


def _permutations(agent_ids: Sequence[str]) -> list[tuple[str, ...]]:
    seen: list[tuple[str, ...]] = []
    for candidate in permutations(agent_ids):
        if candidate not in seen:
            seen.append(candidate)
    return seen


def needs_full_permutations(agent_ids: Sequence[str]) -> bool:
    """D-39's trigger: two or more distinct non-field strategies.

    The *field* is the most common agent. A homogeneous cell has none besides the field; a
    1-deviant cell has exactly one, so rotations suffice and cover every seat for the deviant.
    Two or more deviants need the full permutation set, because rotations keep them in a fixed
    relative order and their adjacency is itself a seat effect.
    """
    if not agent_ids:
        return False
    counts: dict[str, int] = {}
    for agent in agent_ids:
        counts[agent] = counts.get(agent, 0) + 1
    field = max(counts, key=lambda name: (counts[name], name))
    return sum(1 for name in counts if name != field) >= 2


def plan(
    agent_ids: Sequence[str], occupied_seats: Sequence[int], *, force_full: bool | None = None
) -> Balance:
    """Build the counterbalancing plan for one cell.

    ``force_full`` overrides D-39's trigger; the campaign config exposes it so an unusual cell
    can be balanced more strongly on purpose, and the choice is recorded in the summary row.
    """
    if len(agent_ids) != len(occupied_seats):
        raise ValueError(
            f"{len(agent_ids)} agents for {len(occupied_seats)} occupied seats"
        )
    full = needs_full_permutations(agent_ids) if force_full is None else force_full
    arrangements = _permutations(agent_ids) if full else _rotations(agent_ids)
    return Balance(
        arrangements=tuple(arrangements),
        starting_seats=tuple(occupied_seats),
        mode="permutations" if full else "rotations",
    )


def describe(balance: Balance) -> str:
    """One line for the campaign manifest and the run log."""
    return (
        f"{len(balance.arrangements)} {balance.mode} x "
        f"{len(balance.starting_seats)} starting seats = block {balance.block}"
    )


#: Patterns whose occupied-seat tuple is rotation-symmetric, so rotating the agents through the
#: seats visits every structural position. ``adjacent`` on a partly filled board is not: seat 1
#: of a 3-on-4-board block is the middle seat, and rotating within the block keeps it middle,
#: which is what EX-5 measures.
ROTATION_SYMMETRIC = (SeatPattern.SPREAD, SeatPattern.OPPOSITE)

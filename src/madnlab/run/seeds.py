"""Seed derivation (NF-1, D-38).

One master seed determines everything. A game's seed is

    SHA-256(master_seed ‖ cell_key ‖ game_index)

so it depends on the configuration and the game's index within its cell, and
on nothing else — not the worker that runs it, not the node, not the shard
boundary, not ``PYTHONHASHSEED``. Arms are therefore **independent** rather
than common-random-number paired, which is what makes §6.3's unpaired
procedures valid as written.

Each game splits into independent **named streams**: the dice, the starting
player draw, and one per seat for its agent. Naming them rather than
sequencing them off one generator is what lets a seat's agent consume a
different number of draws without moving anybody else's stream.
"""

from __future__ import annotations

import hashlib
import random
from collections.abc import Iterable
from typing import NamedTuple

#: Bytes of the digest used per seed. 8 gives a 64-bit seed, comfortably more
#: entropy than ``random.Random`` consumes to initialise.
_SEED_BYTES = 8


def _digest(*parts: object) -> int:
    payload = "\x1f".join(str(part) for part in parts).encode("utf-8")
    return int.from_bytes(hashlib.sha256(payload).digest()[:_SEED_BYTES], "big")


def game_seed(master_seed: int, cell_key: str, game_index: int) -> int:
    """The per-game seed. Depends on the config and the index, nothing else."""
    return _digest(master_seed, cell_key, game_index)


def stream_seed(seed: int, name: str) -> int:
    """Seed of the named stream ``name`` within a game."""
    return _digest(seed, name)


class Streams(NamedTuple):
    """The named random streams of one game (NF-1)."""

    dice: random.Random
    start: random.Random
    agents: dict[int, random.Random]

    @property
    def seed_record(self) -> dict[str, int]:
        """Placeholder for the header's seed block; filled by :func:`derive`."""
        return {}


def derive(seed: int, seats: Iterable[int]) -> Streams:
    """Split a game seed into its named streams."""
    return Streams(
        dice=random.Random(stream_seed(seed, "dice")),
        start=random.Random(stream_seed(seed, "start")),
        agents={
            seat: random.Random(stream_seed(seed, f"agent:{seat}")) for seat in seats
        },
    )


def draw_start_seat(streams: Streams, seats: Iterable[int]) -> int:
    """The starting seat, drawn from its own stream (§9 D-6).

    Campaign cells override this with the counterbalanced assignment (§7.3);
    the resolved value is recorded in the header either way, because §4.3
    requires re-simulation from the header alone.
    """
    ordered = list(seats)
    return ordered[streams.start.randrange(len(ordered))]

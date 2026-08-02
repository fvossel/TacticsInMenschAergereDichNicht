"""Seed derivation (NF-1, D-38).

One master seed determines everything. A game's seed is

    SHA-256(master_seed ‖ cell_key ‖ game_index)

so it depends on the configuration and on the game's index within its cell, and on nothing
else — not the worker that runs it, not the node, not the shard boundary, not
``PYTHONHASHSEED``. Arms are therefore **independent** rather than common-random-number
paired, which is what makes §6.3's unpaired procedures valid as written.

Each game splits into independent **named streams**: the dice, the starting player draw,
and one per seat for its agent. Naming the streams rather than sequencing them off a single
generator lets a seat's agent consume a different number of draws without moving anybody
else's stream.
"""

from __future__ import annotations

import hashlib
import random
from collections.abc import Iterable
from typing import NamedTuple

#: Digest bytes taken per seed. 8 makes every seed a plain 64-bit integer, wide enough that
#: the seeds of a campaign's games stay apart in practice.
_SEED_BYTES = 8


def _digest(*parts: object) -> int:
    """Hash the parts into a seed, unit-separated so adjacent parts cannot run together."""
    payload = "\x1f".join(str(part) for part in parts).encode("utf-8")
    return int.from_bytes(hashlib.sha256(payload).digest()[:_SEED_BYTES], "big")


def game_seed(master_seed: int, cell_key: str, game_index: int) -> int:
    """The per-game seed. Determined by these three inputs and by nothing else."""
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
        """The header's seed block, deliberately empty.

        The header carries ``master_seed``, ``cell_key`` and ``game_index``; every stream
        seed follows from those through :func:`game_seed` and :func:`stream_seed`, so
        recording them again would only add a second source of truth.
        """
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

    Campaign cells override this with the counterbalanced assignment (§7.3). Either way the
    resolved value is recorded in the header, because §4.3 requires re-simulation from the
    header alone.
    """
    ordered = list(seats)
    return ordered[streams.start.randrange(len(ordered))]

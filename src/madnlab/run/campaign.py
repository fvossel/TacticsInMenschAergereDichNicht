"""Running a cell across workers, and sealing its output (NF-3, D-33).

The determinism invariant is the binding constraint, not the worker count:
output is a deterministic function of the config alone, never of the worker
layout, node count or scheduling order (NF-3, D-48).

Two things make that true, and both are here rather than in the engine:

* **Sharding is by game index.** A shard is a contiguous range, so which games
  a worker gets depends on the shard count, but what each game *is* does not —
  its seed comes from ``(master_seed, cell_key, game_index)`` and nothing else
  (D-38).
* **Sealing is by ascending global game index**, independent of the order
  shards complete in. AK-2 compares bytes, so "same rows in some order" is not
  enough — that is precisely the weaker claim the original AK-2 made.
"""

from __future__ import annotations

import os
from collections.abc import Iterator, Sequence
from concurrent.futures import ProcessPoolExecutor
from typing import NamedTuple

from madnlab.eventlog.writer import SummaryRow, summary_line
from madnlab.run.game import GameSpec, play_indexed_game


class Shard(NamedTuple):
    number: int
    start: int
    stop: int


def plan_shards(games: int, workers: int) -> list[Shard]:
    """Contiguous, gap-free ranges covering ``0..games``.

    Deliberately not round-robin: contiguous ranges make a shard's identity a
    pure function of ``(games, workers, index)``, so a rerun with a different
    worker count still covers exactly the same game indices.
    """
    if games < 0:
        raise ValueError(f"games must be non-negative, got {games}")
    if workers < 1:
        raise ValueError(f"workers must be at least 1, got {workers}")
    workers = min(workers, max(games, 1))
    size, remainder = divmod(games, workers)
    shards: list[Shard] = []
    cursor = 0
    for index in range(workers):
        length = size + (1 if index < remainder else 0)
        shards.append(Shard(number=index, start=cursor, stop=cursor + length))
        cursor += length
    assert cursor == games
    return shards


def run_shard(spec: GameSpec, shard: Shard) -> list[SummaryRow]:
    """Play one shard. Module-level so it survives ``spawn`` on Windows."""
    return [
        play_indexed_game(spec, index, record_events=False).summary
        for index in range(shard.start, shard.stop)
    ]


def run_cell(spec: GameSpec, games: int, workers: int = 1) -> list[SummaryRow]:
    """Run ``games`` games of ``spec`` and return the sealed rows.

    Sealed means ascending global game index, whatever order the shards
    finished in.
    """
    shards = plan_shards(games, workers)
    if workers == 1 or len(shards) == 1:
        results = [run_shard(spec, shard) for shard in shards]
    else:
        with ProcessPoolExecutor(max_workers=min(workers, os.cpu_count() or 1)) as pool:
            results = list(pool.map(run_shard, [spec] * len(shards), shards))
    rows = [row for shard_rows in results for row in shard_rows]
    rows.sort(key=lambda row: row.game_index)
    return rows


def summary_bytes(rows: Sequence[SummaryRow]) -> bytes:
    """``summary.jsonl`` as bytes — the artifact AK-2 compares."""
    return "".join(summary_line(row) + "\n" for row in rows).encode("utf-8")


def iter_games(spec: GameSpec, games: int) -> Iterator[int]:
    return iter(range(games))

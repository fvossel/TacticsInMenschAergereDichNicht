"""AK-7 — the NF-2 throughput benchmark.

Two cells, both defined in requirements §11 and pinned by D-43c:

* **baseline**  — 4 players, 4-seat board, all-``RANDOM``, baseline rules
* **worst case** — 6 players, 6-seat board, ``barriers`` +
  ``mandatory_extended``, all-``SPREAD``

D-43c also fixes *how* they are measured: with the per-turn ``leader(t))``
recomputation inside the measured loop, and with logging at the campaign
default. The first is satisfied — the loop computes it. The second is **not
yet**: the event-log writer does not exist, so this run omits the sampled
event logs (``sample:100`` per cell, i.e. ~0.1% of games) and the summary-row
serialization. Both omissions make the number optimistic, and by how much is
not knowable until they exist. The result is reported as such rather than as a
final AK-7 verdict.

Run::

    .venv/Scripts/python.exe benchmarks/ak7.py
    .venv/Scripts/python.exe benchmarks/ak7.py --games 2000
"""

from __future__ import annotations

import argparse
import hashlib
import random
import statistics
import time
from typing import NamedTuple

from madnlab.agents.policies import REGISTRY, Agent
from madnlab.engine.geometry import Board, SeatPattern, board_for, occupied_seats
from madnlab.engine.loop import play_game
from madnlab.engine.rules import BASELINE, CaptureMode, RuleSet
from madnlab.engine.state import initial_state

#: NF-2's target, for the pass/fail line.
TARGET_GAMES_PER_SECOND = 1000


class Cell(NamedTuple):
    name: str
    board: Board
    players: int
    rules: RuleSet
    agent_id: str


CELLS = [
    Cell("baseline", board_for(4), 4, BASELINE, "RANDOM"),
    Cell(
        "worst_case",
        board_for(6),
        6,
        RuleSet(barriers=True, capture_mode=CaptureMode.MANDATORY_EXTENDED),
        "SPREAD",
    ),
]


def _seed(master: int, *parts: object) -> int:
    """Per-stream seed, derived the way NF-1 derives per-game seeds."""
    payload = "|".join(str(p) for p in (master, *parts)).encode()
    return int.from_bytes(hashlib.sha256(payload).digest()[:8], "big")


def run_cell(cell: Cell, games: int, master_seed: int) -> dict[str, float]:
    seats = occupied_seats(cell.board.seats, cell.players, SeatPattern.ADJACENT)
    agent: Agent = REGISTRY[cell.agent_id]
    agents = dict.fromkeys(seats, agent)
    start = initial_state(cell.board, seats, cell.rules)

    turns_seen: list[int] = []
    rolls_seen: list[int] = []
    elapsed = 0.0

    for index in range(games):
        dice = random.Random(_seed(master_seed, cell.name, index, "dice"))
        agent_rngs = {
            seat: random.Random(_seed(master_seed, cell.name, index, "agent", seat))
            for seat in seats
        }
        start_seat = seats[
            random.Random(_seed(master_seed, cell.name, index, "start")).randrange(
                len(seats)
            )
        ]
        t0 = time.perf_counter()
        outcome = play_game(
            cell.board, seats, cell.rules, agents, start, dice, agent_rngs, start_seat
        )
        elapsed += time.perf_counter() - t0
        turns_seen.append(outcome.turns)
        rolls_seen.append(outcome.dice_rolls)

    per_second = games / elapsed
    return {
        "games": games,
        "seconds": elapsed,
        "games_per_second": per_second,
        "mean_turns": statistics.fmean(turns_seen),
        "mean_rolls": statistics.fmean(rolls_seen),
        "us_per_game": elapsed / games * 1e6,
        "ratio_to_target": per_second / TARGET_GAMES_PER_SECOND,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="AK-7 throughput benchmark (NF-2)")
    parser.add_argument("--games", type=int, default=1000)
    parser.add_argument("--seed", type=int, default=20260801)
    args = parser.parse_args()

    print(f"AK-7 — NF-2 target: >= {TARGET_GAMES_PER_SECOND} games/s single-core\n")
    header = f"{'cell':<12}{'games/s':>10}{'us/game':>10}{'turns':>9}{'rolls':>9}{'vs target':>11}"
    print(header)
    print("-" * len(header))

    results = {}
    for cell in CELLS:
        stats = run_cell(cell, args.games, args.seed)
        results[cell.name] = stats
        print(
            f"{cell.name:<12}{stats['games_per_second']:>10.1f}"
            f"{stats['us_per_game']:>10.0f}{stats['mean_turns']:>9.1f}"
            f"{stats['mean_rolls']:>9.1f}{stats['ratio_to_target']:>10.2f}x"
        )

    worst = min(r["games_per_second"] for r in results.values())
    print()
    print(
        "AK-7 verdict: "
        + ("MET" if worst >= TARGET_GAMES_PER_SECOND else "MISSED")
        + f" (slowest cell {worst:.0f} games/s)"
    )
    print(
        "\nIncomplete: the event-log writer and summary-row serialization do not\n"
        "exist yet, so logging at the campaign default is not in the measured\n"
        "loop. Both omissions make these numbers optimistic."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

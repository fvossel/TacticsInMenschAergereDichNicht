"""AK-2 — determinism.

Same master seed twice gives byte-identical logs and summaries; 1 worker
against 8 against the maximum gives byte-identical ``summary.jsonl``.

The worker clause is deliberately stated on **bytes**, not on row sets. The
original criterion said "identical row sets", which passes while row order —
and therefore byte identity, and any position-dependent bootstrap — varies
with scheduling (D-33).
"""

from __future__ import annotations

import os
import subprocess
import sys

import pytest

from madnlab.engine.geometry import SeatPattern
from madnlab.engine.rules import BASELINE, CaptureMode, ColdStart, RuleSet
from madnlab.eventlog.writer import log_bytes
from madnlab.run.campaign import plan_shards, run_cell, summary_bytes
from madnlab.run.game import GameSpec, play_indexed_game

SPEC = GameSpec(
    cell_key="ak2/4s4p/random",
    seats=4,
    players=4,
    seat_pattern=SeatPattern.ADJACENT,
    rules=BASELINE,
    agent_ids=("RANDOM",) * 4,
    master_seed=20260801,
)

MIXED = GameSpec(
    cell_key="ak2/6s6p/mixed",
    seats=6,
    players=6,
    seat_pattern=SeatPattern.ADJACENT,
    rules=RuleSet(
        cold_start=ColdStart.STRICT,
        capture_mode=CaptureMode.MANDATORY_EXTENDED,
        barriers=True,
        goal_no_jump=True,
    ),
    agent_ids=("RANDOM", "SPREAD", "FOCUS_FRONT", "FOCUS_REAR", "GREEDY_CAPTURE", "RANDOM"),
    master_seed=99,
)


@pytest.mark.parametrize("spec", [SPEC, MIXED], ids=["baseline", "mixed"])
def test_same_seed_twice_gives_byte_identical_logs(spec):
    for index in range(6):
        first = play_indexed_game(spec, index)
        second = play_indexed_game(spec, index)
        assert log_bytes(first.header, first.events) == log_bytes(
            second.header, second.events
        )
        assert first.summary == second.summary


@pytest.mark.parametrize("spec", [SPEC, MIXED], ids=["baseline", "mixed"])
def test_summary_is_byte_identical_across_worker_counts(spec):
    reference = summary_bytes(run_cell(spec, games=24, workers=1))
    for workers in (2, 3, 8, 24):
        assert summary_bytes(run_cell(spec, games=24, workers=workers)) == reference


def test_shard_plan_covers_every_index_exactly_once():
    for games in (0, 1, 7, 24, 100):
        for workers in (1, 2, 3, 8, 64):
            shards = plan_shards(games, workers)
            covered = [i for s in shards for i in range(s.start, s.stop)]
            assert covered == list(range(games))
            assert [s.number for s in shards] == list(range(len(shards)))


def test_game_identity_does_not_depend_on_the_shard_layout():
    """The invariant the sharding rests on: index determines the game."""
    solo = {index: play_indexed_game(SPEC, index).summary for index in range(12)}
    for workers in (1, 5, 12):
        for row in run_cell(SPEC, games=12, workers=workers):
            assert row == solo[row.game_index]


def test_output_is_independent_of_pythonhashseed():
    """NF-1: results must not depend on ``PYTHONHASHSEED``.

    Run in subprocesses because the interpreter fixes the hash seed at start;
    setting the variable in-process would prove nothing.
    """
    script = (
        "from madnlab.engine.geometry import SeatPattern;"
        "from madnlab.engine.rules import BASELINE;"
        "from madnlab.run.campaign import run_cell, summary_bytes;"
        "from madnlab.run.game import GameSpec;"
        "import hashlib,sys;"
        "spec=GameSpec('ak2/4s4p/random',4,4,SeatPattern.ADJACENT,BASELINE,('RANDOM',)*4,20260801);"
        "sys.stdout.write(hashlib.sha256(summary_bytes(run_cell(spec,8,1))).hexdigest())"
    )
    digests = set()
    for hash_seed in ("0", "1", "12345"):
        env = dict(os.environ, PYTHONHASHSEED=hash_seed)
        result = subprocess.run(
            [sys.executable, "-c", script], capture_output=True, text=True, env=env, check=True
        )
        digests.add(result.stdout.strip())
    assert len(digests) == 1, f"output varied with PYTHONHASHSEED: {digests}"

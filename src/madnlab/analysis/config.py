"""Analysis-run configuration and its manifest (NF-7).

NF-1 makes the simulation reproducible from a master seed. NF-7 extends that
to the half that actually gets published: §6.4's decision rules are threshold
rules — "CI excludes 1", "CI excludes zero" — so a bootstrap without a
recorded seed and resample count means a borderline verdict can flip between
two runs on byte-identical input. That would leave the simulation
byte-reproducible and the results not.

The manifest records the environment as well as the seed, because BLAS
reduction order differs across CPU architectures and library builds. Simulation
may fan out across HPC nodes; analysis runs single-node under a pinned
environment, and re-running it elsewhere is a *new* analysis rather than a
reproduction.
"""

from __future__ import annotations

import hashlib
import json
import platform
import sys
from collections.abc import Sequence
from pathlib import Path
from typing import Any, NamedTuple

from madnlab import ENGINE_VERSION

#: Resamples for every headline interval (NF-7).
DEFAULT_BOOTSTRAP_B = 10_000


class AnalysisConfig(NamedTuple):
    """Everything an analysis run decides before it looks at data."""

    campaign_dir: str
    estimands: tuple[str, ...]
    analysis_seed: int
    bootstrap_b: int = DEFAULT_BOOTSTRAP_B
    alpha: float = 0.05
    confidence_level: float = 0.95

    def seed_for(self, *parts: object) -> int:
        """A distinct, derived seed per estimand.

        One seed per run and a shared generator would make an estimand's
        interval depend on how many estimands ran before it, so adding a
        descriptive statistic would move a published confirmatory bound.
        """
        payload = "\x1f".join(str(part) for part in (self.analysis_seed, *parts))
        return int.from_bytes(
            hashlib.sha256(payload.encode("utf-8")).digest()[:8], "big"
        )


def environment() -> dict[str, str]:
    """The pinned environment, as recorded in the manifest."""
    return {
        "python": sys.version.split()[0],
        "implementation": platform.python_implementation(),
        "platform": platform.platform(),
        "machine": platform.machine(),
        "engine_version": ENGINE_VERSION,
    }


def input_digest(paths: Sequence[Path]) -> str:
    """SHA-256 over the input files, in the order given."""
    digest = hashlib.sha256()
    for path in paths:
        digest.update(path.name.encode("utf-8"))
        digest.update(path.read_bytes())
    return digest.hexdigest()


def manifest(
    config: AnalysisConfig,
    inputs: Sequence[Path],
    results: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """The ``analysis.json`` payload."""
    return {
        "config": dict(config._asdict()),
        "environment": environment(),
        "input_digest": input_digest(inputs),
        "input_files": [path.name for path in inputs],
        "results": results if results is not None else {},
    }


def write_manifest(path: Path, payload: dict[str, Any]) -> None:
    """Write ``analysis.json`` with the same canonical rules as the logs.

    AK-2 asserts that the same analysis config twice produces byte-identical
    output, which needs the encoding pinned here exactly as D-33 pins it for
    the event log.
    """
    text = json.dumps(payload, ensure_ascii=True, separators=(",", ":"), sort_keys=True)
    path.write_text(text + "\n", encoding="utf-8", newline="")

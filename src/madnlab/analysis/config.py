"""Analysis-run configuration and its manifest (NF-7).

NF-1 makes the simulation reproducible from a master seed. NF-7 extends that to the half
that actually gets published: §6.4's decision rules are threshold rules — "CI excludes 1",
"CI excludes zero" — so recording the bootstrap seed and the resample count is what fixes a
borderline verdict to one value across every run on byte-identical input.

The manifest records the environment alongside the seed, because floating-point summation
order and library builds differ across interpreters and architectures. Simulation may fan
out across any number of processes or machines; analysis runs in one process under a pinned
environment, and re-running it elsewhere is a new analysis rather than a reproduction.
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

        Hashing the analysis seed together with the estimand's own parts makes each
        interval depend on that estimand alone, so the number and the order of the other
        estimands in the run leave a published confirmatory bound untouched.
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

    The encoding is pinned here exactly as D-33 pins it for the event log, so that the
    same analysis config run twice produces the byte-identical output AK-2 asserts.
    """
    text = json.dumps(payload, ensure_ascii=True, separators=(",", ":"), sort_keys=True)
    path.write_text(text + "\n", encoding="utf-8", newline="")

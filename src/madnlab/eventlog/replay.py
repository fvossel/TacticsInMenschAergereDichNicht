"""The replay validator (LG-3, AK-3).

``header + engine version`` must reproduce a game byte-identically. The
validator re-simulates from the header alone and asserts event-stream
equality, so the check passes only if the header carries everything the run
depended on — the completeness §4.3 claims.

Version skew is refused rather than reported as a mismatch (D-33): a log
written by a different engine differs for a legitimate reason.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import NamedTuple

from madnlab import ENGINE_VERSION
from madnlab.engine.geometry import SeatPattern
from madnlab.engine.rules import (
    CaptureEnforcement,
    CaptureMode,
    ColdStart,
    GameEndMode,
    RuleSet,
)
from madnlab.eventlog.events import SCHEMA_VERSION, Event, LogHeader
from madnlab.eventlog.writer import canonical_dumps, event_payload
from madnlab.run.game import GameSpec, play_indexed_game

_ENUM_FIELDS = {
    "cold_start": ColdStart,
    "capture_mode": CaptureMode,
    "game_end_mode": GameEndMode,
    "capture_enforcement": CaptureEnforcement,
}


class VersionSkewError(RuntimeError):
    """The log was written by a different engine or log schema."""


class ReplayMismatch(NamedTuple):
    """Where two event streams first diverge."""

    at: int
    recorded: str
    replayed: str

    def describe(self) -> str:
        return (
            f"event {self.at} differs\n"
            f"  recorded: {self.recorded}\n"
            f"  replayed: {self.replayed}"
        )


def rules_from_header(header: LogHeader) -> RuleSet:
    """Rebuild the rule set from the header's ``(name, value)`` pairs."""
    values: dict[str, object] = {}
    for name, raw in header.rules:
        if name in _ENUM_FIELDS:
            values[name] = _ENUM_FIELDS[name](raw)
        else:
            values[name] = raw == "True"
    return RuleSet(**values)  # type: ignore[arg-type]


def spec_from_header(header: LogHeader, agent_ids: Sequence[str] | None = None) -> GameSpec:
    """Rebuild the cell spec from the header.

    ``agent_ids`` overrides the policies the header recorded; the default
    replays the recorded ones, which is what AK-3 does.

    ``counterbalanced=False`` is load-bearing. The header records the
    **resolved** assignment and starting seat, so re-deriving them from the
    game index would apply §7.3's rotation a second time on top of an already
    rotated tuple and replay a different game.
    """
    recorded = tuple(name for _seat, name in header.agents)
    return GameSpec(
        cell_key=header.cell_key,
        seats=header.seats,
        players=len(header.occupied_seats),
        seat_pattern=SeatPattern(header.seat_pattern),
        rules=rules_from_header(header),
        agent_ids=tuple(agent_ids) if agent_ids is not None else recorded,
        master_seed=header.master_seed,
        counterbalanced=False,
    )


def replay(header: LogHeader) -> list[Event]:
    """Re-simulate the game the header describes, from the header alone."""
    if header.engine_version != ENGINE_VERSION:
        raise VersionSkewError(
            f"log was written by engine {header.engine_version!r}, this is "
            f"{ENGINE_VERSION!r}. Regenerate the log or check it out at that "
            f"version; a replay across versions is not a mismatch (D-33)."
        )
    if header.schema_version != SCHEMA_VERSION:
        raise VersionSkewError(
            f"log schema {header.schema_version!r} != {SCHEMA_VERSION!r}"
        )
    run = play_indexed_game(
        spec_from_header(header),
        header.game_index,
        record_events=True,
        starting_seat=header.starting_seat,
    )
    return run.events


def compare(recorded: Sequence[Event], replayed: Sequence[Event]) -> ReplayMismatch | None:
    """First divergence between two event streams, or ``None`` if identical.

    Compared on the canonical serialization rather than on the objects, so the
    check is the byte-identity LG-3 claims and not the weaker structural
    equality of the objects.
    """
    for at in range(max(len(recorded), len(replayed))):
        left = (
            canonical_dumps(event_payload(recorded[at])) if at < len(recorded) else "<end>"
        )
        right = (
            canonical_dumps(event_payload(replayed[at])) if at < len(replayed) else "<end>"
        )
        if left != right:
            return ReplayMismatch(at=at, recorded=left, replayed=right)
    return None


def validate(header: LogHeader, recorded: Sequence[Event]) -> ReplayMismatch | None:
    """Replay ``header`` and compare against ``recorded``."""
    return compare(recorded, replay(header))

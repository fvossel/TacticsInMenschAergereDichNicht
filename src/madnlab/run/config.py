"""Campaign configuration as data (§7.1).

A campaign is one declarative JSON file. Nothing statistical is decided in code
at run time: the arms, the sample sizes, the agent assignment and the master
seed all come from the file, and the resolved form is written back out beside
the results so a published number can be traced to the configuration that
produced it.

The resolver is deliberately strict. An unknown key is an error rather than a
silently ignored typo — a misspelled ``capture_mode`` that falls back to the
default would run the baseline arm under a name claiming otherwise, and
nothing downstream would notice.
"""

from __future__ import annotations

import json
from collections.abc import Iterator, Sequence
from pathlib import Path
from typing import Any, NamedTuple

from madnlab.agents.policies import REGISTRY
from madnlab.engine.geometry import SeatPattern
from madnlab.engine.rules import (
    CaptureMode,
    ColdStart,
    GameEndMode,
    RuleSet,
)
from madnlab.run.game import GameSpec

_RULE_ENUMS: dict[str, type[ColdStart] | type[CaptureMode] | type[GameEndMode]] = {
    "cold_start": ColdStart,
    "capture_mode": CaptureMode,
    "game_end_mode": GameEndMode,
}
_RULE_BOOLS = (
    "dreimal_wuerfeln",
    "bonus_roll_after_quick_entry",
    "bonus_roll_forfeited",
    "goal_no_jump",
    "barriers",
)


class CellConfig(NamedTuple):
    """One cell of a campaign, as written in the file."""

    key: str
    seats: int
    players: int
    seat_pattern: str
    agents: tuple[str, ...]
    games: int
    rules: dict[str, Any]
    force_full_permutations: bool | None = None

    def to_spec(self, master_seed: int, prereg_version: str = "prereg-v1") -> GameSpec:
        return GameSpec(
            cell_key=self.key,
            seats=self.seats,
            players=self.players,
            seat_pattern=SeatPattern(self.seat_pattern),
            rules=build_rules(self.rules),
            agent_ids=self.agents,
            master_seed=master_seed,
            prereg_version=prereg_version,
            counterbalanced=True,
            force_full_permutations=self.force_full_permutations,
        )


class CampaignConfig(NamedTuple):
    """A whole campaign."""

    name: str
    description: str
    master_seed: int
    cells: tuple[CellConfig, ...]
    log_events: dict[str, Any]
    #: Which pre-registration this campaign runs under (§14). Per campaign
    #: rather than global: a later study gets its own freeze, and stamping its
    #: tag on rows produced under the earlier one would misdate them (D-78).
    prereg_version: str = "prereg-v1"

    def specs(self) -> Iterator[tuple[GameSpec, int]]:
        """Each cell's spec with its **effective** game count (D-39)."""
        for cell in self.cells:
            spec = cell.to_spec(self.master_seed, self.prereg_version)
            yield spec, spec.balance().effective_games(cell.games)


class ConfigError(ValueError):
    """The configuration is malformed or names something that does not exist."""


def build_rules(values: dict[str, Any]) -> RuleSet:
    """Resolve a rules mapping, rejecting anything not an axis."""
    known = set(RuleSet._fields)
    unknown = set(values) - known
    if unknown:
        raise ConfigError(
            f"unknown rule flags {sorted(unknown)}; the axes are "
            f"{sorted(known)} (§2.4)"
        )
    resolved: dict[str, Any] = {}
    for name, value in values.items():
        if name in _RULE_ENUMS:
            try:
                resolved[name] = _RULE_ENUMS[name](value)
            except ValueError as error:
                raise ConfigError(f"{name}={value!r} is not a valid value") from error
        elif name in _RULE_BOOLS:
            if not isinstance(value, bool):
                raise ConfigError(f"{name} must be a boolean, got {value!r}")
            resolved[name] = value
        else:
            resolved[name] = value
    rules = RuleSet(**resolved)
    rules.validate()
    return rules


def _require(payload: dict[str, Any], key: str, where: str) -> Any:
    if key not in payload:
        raise ConfigError(f"{where} is missing required key {key!r}")
    return payload[key]


def parse(payload: dict[str, Any]) -> CampaignConfig:
    """Validate and resolve a campaign payload."""
    allowed = {"name", "description", "master_seed", "cells", "log_events",
               "prereg_version"}
    unknown = set(payload) - allowed
    if unknown:
        raise ConfigError(f"unknown campaign keys {sorted(unknown)}")

    cells: list[CellConfig] = []
    seen_keys: set[str] = set()
    for raw in _require(payload, "cells", "campaign"):
        cell_allowed = {
            "key", "seats", "players", "seat_pattern", "agents", "games", "rules",
            "force_full_permutations",
        }
        unknown_cell = set(raw) - cell_allowed
        if unknown_cell:
            raise ConfigError(f"cell {raw.get('key')!r}: unknown keys {sorted(unknown_cell)}")

        key = _require(raw, "key", "cell")
        if key in seen_keys:
            raise ConfigError(
                f"duplicate cell key {key!r}: cell keys seed the per-game RNG "
                f"(D-38), so two cells sharing one would run identical games"
            )
        seen_keys.add(key)

        agents = tuple(_require(raw, "agents", f"cell {key!r}"))
        unknown_agents = [name for name in agents if name not in REGISTRY]
        if unknown_agents:
            raise ConfigError(
                f"cell {key!r}: unknown agents {unknown_agents}; "
                f"registered: {sorted(REGISTRY)}"
            )
        players = _require(raw, "players", f"cell {key!r}")
        if len(agents) != players:
            raise ConfigError(
                f"cell {key!r}: {len(agents)} agents for {players} players"
            )
        cells.append(
            CellConfig(
                key=key,
                seats=_require(raw, "seats", f"cell {key!r}"),
                players=players,
                seat_pattern=raw.get("seat_pattern", "adjacent"),
                agents=agents,
                games=_require(raw, "games", f"cell {key!r}"),
                rules=raw.get("rules", {}),
                force_full_permutations=raw.get("force_full_permutations"),
            )
        )
    if not cells:
        raise ConfigError("campaign has no cells")

    return CampaignConfig(
        name=_require(payload, "name", "campaign"),
        description=payload.get("description", ""),
        master_seed=_require(payload, "master_seed", "campaign"),
        cells=tuple(cells),
        log_events=payload.get("log_events", {"mode": "sample", "k": 100}),
        prereg_version=str(payload.get("prereg_version", "prereg-v1")),
    )


def load(path: Path) -> CampaignConfig:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise ConfigError(f"{path}: {error}") from error
    return parse(payload)


def resolved_payload(config: CampaignConfig) -> dict[str, Any]:
    """The fully resolved configuration, for ``campaign.json`` (§7.2)."""
    cells = []
    for cell in config.cells:
        spec = cell.to_spec(config.master_seed, config.prereg_version)
        balance = spec.balance()
        cells.append(
            {
                "key": cell.key,
                "seats": cell.seats,
                "players": cell.players,
                "seat_pattern": cell.seat_pattern,
                "occupied_seats": list(spec.occupied()),
                "agents": list(cell.agents),
                "games_requested": cell.games,
                "games_effective": balance.effective_games(cell.games),
                "balance_block": balance.block,
                "balance_mode": balance.mode,
                "arrangements": len(balance.arrangements),
                "rules": {
                    field: str(getattr(spec.rules, field)) for field in spec.rules._fields
                },
            }
        )
    return {
        "name": config.name,
        "description": config.description,
        "master_seed": config.master_seed,
        "log_events": config.log_events,
        "prereg_version": config.prereg_version,
        "cells": cells,
    }


def total_games(config: CampaignConfig) -> int:
    return sum(games for _spec, games in config.specs())


def cell_specs(config: CampaignConfig) -> Sequence[tuple[GameSpec, int]]:
    return list(config.specs())

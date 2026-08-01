"""Generate the §8 campaign configurations from the D-59 plan.

The plan is data, not prose: 385 cells across seven campaigns, with the
confirmatory cells at their derived sample sizes and everything else at the
descriptive n = 20,000. Generating them rather than hand-writing them is the
only way the counts in D-59 and the files on disk can be checked against each
other — and this script asserts them.

Run from the repository root::

    .venv/Scripts/python.exe campaigns/generate.py
"""

from __future__ import annotations

import itertools
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from madnlab.engine.rules import RuleSet  # noqa: E402

OUT = ROOT / "campaigns"

#: D-59's two tiers.
DESCRIPTIVE = 20_000
CONFIRMATORY = {"ex2": 250_000, "ex3": 200_000, "ex5": 250_000, "ex6": 400_000,
                "ex7": 200_000}

AGENTS = ("RANDOM", "SPREAD", "FOCUS_FRONT", "FOCUS_REAR", "GREEDY_CAPTURE")
#: RQ-3's four agents. GREEDY_CAPTURE is a control for RQ-1/RQ-2, not a
#: strategy under study, so it stays out of EX-3 (D-44, D-45).
RQ3_AGENTS = ("RANDOM", "SPREAD", "FOCUS_FRONT", "FOCUS_REAR")
CAPTURE_MODES = ("optional", "mandatory", "mandatory_extended")


def board_for_players(players: int) -> int:
    """D-11: seats 4 for players <= 4, seats 6 for 5 and 6."""
    return 4 if players <= 4 else 6


def cell(
    key: str,
    seats: int,
    players: int,
    agents: tuple[str, ...],
    games: int,
    rules: dict[str, Any] | None = None,
    pattern: str = "adjacent",
) -> dict[str, Any]:
    return {
        "key": key,
        "seats": seats,
        "players": players,
        "seat_pattern": pattern,
        "agents": list(agents),
        "games": games,
        "rules": rules or {},
    }


def ex2() -> list[dict[str, Any]]:
    """RQ-1 Schlagzwang. 3 capture modes x 4 player counts x 3 fields."""
    cells = []
    for mode, players, field in itertools.product(
        CAPTURE_MODES, (2, 3, 4, 6), ("RANDOM", "SPREAD", "GREEDY_CAPTURE")
    ):
        seats = board_for_players(players)
        # The RQ-1 confirmatory family lives in one headline cell set: 4
        # players, seats 4, all-RANDOM (§6.4).
        confirmatory = players == 4 and field == "RANDOM"
        cells.append(
            cell(
                f"ex2/{seats}s{players}p/{field.lower()}/{mode}",
                seats,
                players,
                (field,) * players,
                CONFIRMATORY["ex2"] if confirmatory else DESCRIPTIVE,
                {"capture_mode": mode} if mode != "optional" else {},
            )
        )
    return cells


def ex3() -> list[dict[str, Any]]:
    """RQ-3 strategies: homogeneous fields plus every 1-deviant combination."""
    cells = []
    for agent, players in itertools.product(RQ3_AGENTS, (2, 3, 4, 6)):
        seats = board_for_players(players)
        cells.append(
            cell(
                f"ex3/homogeneous/{seats}s{players}p/{agent.lower()}",
                seats,
                players,
                (agent,) * players,
                DESCRIPTIVE,
            )
        )
    for deviant, field, players in itertools.product(RQ3_AGENTS, RQ3_AGENTS, (2, 3, 4, 6)):
        if deviant == field:
            continue
        seats = board_for_players(players)
        # RQ-3's confirmatory contrasts are the three non-RANDOM deviants
        # against a RANDOM field at 4 players (§6.4).
        confirmatory = field == "RANDOM" and players == 4 and deviant != "RANDOM"
        cells.append(
            cell(
                f"ex3/deviant/{seats}s{players}p/{deviant.lower()}-vs-{field.lower()}",
                seats,
                players,
                (deviant,) + (field,) * (players - 1),
                CONFIRMATORY["ex3"] if confirmatory else DESCRIPTIVE,
            )
        )
    return cells


def ex4() -> list[dict[str, Any]]:
    """RQ-2: the complete admissible factorial over the seven axes (D-13)."""
    cells = []
    for cold, dreimal, bonus, forfeited, no_jump, mode, barriers in itertools.product(
        ("one_piece_out", "strict", "free_entry"),
        (False, True),
        (False, True),
        (False, True),
        (False, True),
        CAPTURE_MODES,
        (False, True),
    ):
        # Nested axis: the quick-entry bonus needs the three-attempts variant.
        if bonus and not dreimal:
            continue
        # Under free_entry both entry axes are provably inert, so the 72
        # admissible cells there collapse to 24 distinct behaviours. Pinning
        # them to their defaults is what makes the collapse explicit rather
        # than a counting argument (D-13).
        if cold == "free_entry" and (dreimal or bonus):
            continue
        rules: dict[str, Any] = {}
        if cold != "one_piece_out":
            rules["cold_start"] = cold
        if dreimal:
            rules["dreimal_wuerfeln"] = True
        if bonus:
            rules["bonus_roll_after_quick_entry"] = True
        if forfeited:
            rules["bonus_roll_forfeited"] = True
        if no_jump:
            rules["goal_no_jump"] = True
        if mode != "optional":
            rules["capture_mode"] = mode
        if barriers:
            rules["barriers"] = True
        flags = "-".join(f"{k}={v}" for k, v in sorted(rules.items())) or "baseline"
        cells.append(cell(f"ex4/4s4p/random/{flags}", 4, 4, ("RANDOM",) * 4, DESCRIPTIVE, rules))
    return cells


def ex5() -> list[dict[str, Any]]:
    """Seating geometry, with the D-27 control that separates the two effects."""
    cells = []
    arms = [
        ("4s-adjacent", 4, "adjacent"),
        ("6s-spread", 6, "spread"),
        ("6s-adjacent", 6, "adjacent"),  # the D-27 control
    ]
    for (name, seats, pattern), field in itertools.product(arms, ("RANDOM", "SPREAD")):
        cells.append(
            cell(
                f"ex5/3p/{name}/{field.lower()}",
                seats,
                3,
                (field,) * 3,
                CONFIRMATORY["ex5"],
                pattern=pattern,
            )
        )
    for pattern, field in itertools.product(("adjacent", "opposite"), ("RANDOM", "SPREAD")):
        cells.append(
            cell(
                f"ex5/2p/{pattern}/{field.lower()}",
                4,
                2,
                (field,) * 2,
                DESCRIPTIVE,
                pattern=pattern,
            )
        )
    return cells


def ex6() -> list[dict[str, Any]]:
    """RQ-4 interactions, six explicitly typed rows (D-28, D-46)."""
    cells = []
    deviants = ("SPREAD", "FOCUS_FRONT", "FOCUS_REAR", "GREEDY_CAPTURE")
    #: The cells carrying the RQ-4 confirmatory contrasts (§6.4).
    confirmatory_deviants = ("SPREAD", "FOCUS_FRONT")

    for mode, field in itertools.product(CAPTURE_MODES, AGENTS):  # 6a
        cells.append(
            cell(
                f"ex6a/4s4p/{field.lower()}/{mode}",
                4, 4, (field,) * 4, DESCRIPTIVE,
                {"capture_mode": mode} if mode != "optional" else {},
            )
        )
    for mode, deviant in itertools.product(CAPTURE_MODES, deviants):  # 6b
        games = (
            CONFIRMATORY["ex6"] if deviant in confirmatory_deviants else DESCRIPTIVE
        )
        cells.append(
            cell(
                f"ex6b/4s4p/{deviant.lower()}-vs-random/{mode}",
                4, 4, (deviant, "RANDOM", "RANDOM", "RANDOM"), games,
                {"capture_mode": mode} if mode != "optional" else {},
            )
        )
    for barriers, field in itertools.product((False, True), AGENTS):  # 6c
        cells.append(
            cell(
                f"ex6c/4s4p/{field.lower()}/barriers={barriers}",
                4, 4, (field,) * 4, DESCRIPTIVE,
                {"barriers": True} if barriers else {},
            )
        )
    for barriers, deviant in itertools.product((False, True), deviants):  # 6d
        games = (
            CONFIRMATORY["ex6"] if deviant in confirmatory_deviants else DESCRIPTIVE
        )
        cells.append(
            cell(
                f"ex6d/4s4p/{deviant.lower()}-vs-random/barriers={barriers}",
                4, 4, (deviant, "RANDOM", "RANDOM", "RANDOM"), games,
                {"barriers": True} if barriers else {},
            )
        )
    for mode, players in itertools.product(CAPTURE_MODES, (2, 3, 4, 6)):  # 6e
        # D-12: every player-count contrast is estimated at a fixed seats
        # level, so this whole row runs on the 6-seat board.
        games = (
            CONFIRMATORY["ex6"]
            if mode in ("optional", "mandatory") and players in (2, 6)
            else DESCRIPTIVE
        )
        cells.append(
            cell(
                f"ex6e/6s{players}p/random/{mode}",
                6, players, ("RANDOM",) * players, games,
                {"capture_mode": mode} if mode != "optional" else {},
            )
        )
    for mode, deviant, players in itertools.product(CAPTURE_MODES, deviants, (2, 3, 4, 6)):  # 6f
        cells.append(
            cell(
                f"ex6f/6s{players}p/{deviant.lower()}-vs-random/{mode}",
                6, players, (deviant,) + ("RANDOM",) * (players - 1), DESCRIPTIVE,
                {"capture_mode": mode} if mode != "optional" else {},
            )
        )
    return cells


def ex7() -> list[dict[str, Any]]:
    """RQ-5, seat exposure (§15).

    Two players on the 4-seat board sit either `adjacent` (cyclic entry-field
    gaps of 10 and 30) or `opposite` (20 and 20). A piece is exposed to an
    opponent over the stretch it occupies downstream of that opponent's entry,
    so `adjacent` should be lopsided and `opposite` should not.
    """
    cells = []
    for pattern, field in itertools.product(("adjacent", "opposite"), AGENTS):
        cells.append(
            cell(
                f"ex7/2p/4s-{pattern}/{field.lower()}",
                4, 2, (field,) * 2, CONFIRMATORY["ex7"], pattern=pattern,
            )
        )
    for pattern, field in itertools.product(("adjacent", "spread"), ("RANDOM", "SPREAD")):
        cells.append(
            cell(
                f"ex7/3p/6s-{pattern}/{field.lower()}",
                6, 3, (field,) * 3, CONFIRMATORY["ex7"], pattern=pattern,
            )
        )
    return cells


CAMPAIGNS = {
    "ex2": ("RQ-1 Schlagzwang", 20261010, ex2),
    "ex3": ("RQ-3 movement strategies", 20261011, ex3),
    "ex4": ("RQ-2 rule main effects", 20261012, ex4),
    "ex5": ("Seating geometry", 20261013, ex5),
    "ex6": ("RQ-4 interactions", 20261014, ex6),
    # A fresh seed, and its own pre-registration (§15, D-78).
    "ex7": ("RQ-5 seat exposure", 20261015, ex7),
}

#: D-59's cell counts. Asserted, so the plan and the files cannot drift.
EXPECTED_CELLS = {"ex2": 36, "ex3": 64, "ex4": 168, "ex5": 10, "ex6": 105,
                  "ex7": 14}


def main() -> int:
    total_cells = total_games = 0
    for name, (description, seed, builder) in CAMPAIGNS.items():
        cells = builder()
        expected = EXPECTED_CELLS[name]
        if len(cells) != expected:
            print(f"{name}: {len(cells)} cells but D-59 says {expected}", file=sys.stderr)
            return 1
        keys = [c["key"] for c in cells]
        if len(set(keys)) != len(keys):
            duplicates = [k for k in keys if keys.count(k) > 1]
            print(f"{name}: duplicate cell keys {sorted(set(duplicates))[:5]}", file=sys.stderr)
            return 1
        for c in cells:
            RuleSet(**{
                k: v for k, v in c["rules"].items()
            }).validate()

        payload = {
            "name": name.upper(),
            "description": description,
            "master_seed": seed,
            "log_events": {"mode": "sample", "k": 100},
            "prereg_version": "prereg-v1",
            "cells": cells,
        }
        path = OUT / f"{name}.json"
        path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8", newline="")
        games = sum(c["games"] for c in cells)
        total_cells += len(cells)
        total_games += games
        print(f"{name}: {len(cells):>4} cells  {games:>12,} games  -> {path.name}")

    # EX-1 and EX-1b are already written by hand and already run.
    print(f"\n{total_cells + 2:>4} cells total (with EX-1 and EX-1b)")
    print(f"{total_games + 800_002:>12,} games total")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

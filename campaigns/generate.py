"""Generate the §8 campaign configurations from the D-59 plan.

The plan is data, not prose: 529 cells across eleven campaigns. Each cell's sample size comes
from its tier: confirmatory cells at their derived n (D-59), interaction cells at the §17 n,
EX-4's factorial at 40,000, and everything else at the descriptive n = 20,000. Generating the
files keeps the cell counts checkable against D-59, and main() asserts them.

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

#: Games per cell in D-59's descriptive tier.
DESCRIPTIVE = 20_000
#: EX-4 alone: its 168 cells are the pooled arms of RQ-7's 21 rule-pair interactions,
#: 42 cells per arm (§17).
EX4_N = 40_000
CONFIRMATORY = {"ex2": 250_000, "ex3": 200_000, "ex5": 250_000, "ex6": 400_000,
                "ex7": 200_000, "ex8": 250_000}

AGENTS = ("RANDOM", "SPREAD", "FOCUS_FRONT", "FOCUS_REAR", "GREEDY_CAPTURE")
#: RQ-3's four agents. GREEDY_CAPTURE is a control for RQ-1/RQ-2, not a strategy under
#: study, so it stays out of EX-3 (D-44, D-45).
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
    """Build one campaign cell in the on-disk JSON shape."""
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
        # The RQ-1 confirmatory family lives in one cell set: 4 players, seats 4,
        # all-RANDOM (§6.4).
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
        # RQ-3's confirmatory contrasts are the three non-RANDOM deviants against a
        # RANDOM field at 4 players (§6.4).
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
        # Under free_entry both entry axes are provably inert, so the 72 admissible cells there
        # collapse to 24 distinct behaviours. Skipping the non-default levels makes the
        # collapse explicit in the generated files rather than only in a counting
        # argument (D-13).
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
        cells.append(cell(f"ex4/4s4p/random/{flags}", 4, 4, ("RANDOM",) * 4, EX4_N, rules))
    return cells


def ex5() -> list[dict[str, Any]]:
    """Seating geometry. The D-27 control separates seat count from seat pattern."""
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
    #: Deviants whose cells carry the RQ-4 confirmatory contrasts (§6.4).
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
        # D-12: every player-count contrast is estimated at a fixed seats level, so this
        # whole row runs on the 6-seat board.
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

    Two players on the 4-seat board sit either `adjacent` (cyclic entry-field gaps of 10 and
    30) or `opposite` (20 and 20). A piece is exposed to an opponent over the stretch it
    occupies downstream of that opponent's entry, which makes the exposure asymmetric under
    `adjacent` and symmetric under `opposite`.
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


def ex8() -> list[dict[str, Any]]:
    """RQ-6 (§16): starting-player advantage, and GREEDY_CAPTURE against a RANDOM field.

    Both contrasts are sized to resolve 0.5 pp, which the descriptive n does not reach. Reading
    the starting-player advantage against player count requires the board held fixed (D-12), so
    all four counts run on the 6-seat board.
    """
    cells = []
    for players in (2, 3, 4, 6):
        cells.append(
            cell(
                f"ex8/6s{players}p/random/baseline",
                6, players, ("RANDOM",) * players, CONFIRMATORY["ex8"],
            )
        )
    for mode in ("optional", "mandatory"):
        cells.append(
            cell(
                f"ex8/4s4p/greedy_capture-vs-random/{mode}",
                4, 4, ("GREEDY_CAPTURE", "RANDOM", "RANDOM", "RANDOM"),
                CONFIRMATORY["ex8"],
                {"capture_mode": mode} if mode != "optional" else {},
            )
        )
    return cells


#: The ten rule configurations the interaction campaigns cross against everything else:
#: the baseline plus each §2.4 axis moved one level. Defined once because four campaigns
#: and five families index into them. ``bonus_quick`` carries ``dreimal_wuerfeln`` with it,
#: since the flag is nested (§2.4); its contrast is against ``dreimal``, not the baseline.
RULE_CONFIGS: tuple[tuple[str, dict[str, Any]], ...] = (
    ("baseline", {}),
    ("cold_start=strict", {"cold_start": "strict"}),
    ("cold_start=free_entry", {"cold_start": "free_entry"}),
    ("capture=mandatory", {"capture_mode": "mandatory"}),
    ("capture=mandatory_extended", {"capture_mode": "mandatory_extended"}),
    ("dreimal", {"dreimal_wuerfeln": True}),
    ("bonus_quick", {"dreimal_wuerfeln": True, "bonus_roll_after_quick_entry": True}),
    ("goal_no_jump", {"goal_no_jump": True}),
    ("barriers", {"barriers": True}),
    ("bonus_forfeited", {"bonus_roll_forfeited": True}),
)

#: Games per interaction cell. A 0.5 pp interaction in a family of 180 needs 601,249 games
#: per arm (§17), and here every arm is a single cell.
INTERACTION_N = 600_000


def ex9() -> list[dict[str, Any]]:
    """RQ-8: does a rule change what a strategy is worth? (§17)"""
    fields: tuple[tuple[str, str | None], ...] = (
        ("random", None),
        ("spread", "SPREAD"),
        ("focus_front", "FOCUS_FRONT"),
        ("focus_rear", "FOCUS_REAR"),
        ("greedy_capture", "GREEDY_CAPTURE"),
    )
    cells = []
    for (rule_name, rules), (field_name, deviant) in itertools.product(
        RULE_CONFIGS, fields
    ):
        agents = ("RANDOM",) * 4 if deviant is None else (deviant,) + ("RANDOM",) * 3
        cells.append(
            cell(f"ex9/4s4p/{field_name}/{rule_name}", 4, 4, agents, INTERACTION_N, rules)
        )
    return cells


def ex10() -> list[dict[str, Any]]:
    """RQ-9: does a rule's effect depend on how many people are playing?

    All on the 6-seat board (D-12): a player-count contrast at mixed board sizes measures the
    board as much as the count.
    """
    return [
        cell(
            f"ex10/6s{players}p/random/{rule_name}",
            6, players, ("RANDOM",) * players, INTERACTION_N, rules,
        )
        for (rule_name, rules), players in itertools.product(RULE_CONFIGS, (2, 3, 4, 6))
    ]


def ex11() -> list[dict[str, Any]]:
    """RQ-10: does a strategy's worth depend on the number of opponents?

    The RANDOM arm of every contrast is EX-10's baseline cell at the same player count, so it
    is not duplicated here.
    """
    return [
        cell(
            f"ex11/6s{players}p/{deviant.lower()}-vs-random/baseline",
            6, players, (deviant,) + ("RANDOM",) * (players - 1), INTERACTION_N,
        )
        for deviant, players in itertools.product(
            ("SPREAD", "FOCUS_FRONT", "FOCUS_REAR", "GREEDY_CAPTURE"), (2, 3, 4, 6)
        )
    ]


def ex12() -> list[dict[str, Any]]:
    """RQ-11: does a rule land differently depending on where people sit?"""
    return [
        cell(
            f"ex12/2p/4s-{pattern}/random/{rule_name}",
            4, 2, ("RANDOM",) * 2, INTERACTION_N, rules, pattern=pattern,
        )
        for (rule_name, rules), pattern in itertools.product(
            RULE_CONFIGS, ("adjacent", "opposite")
        )
    ]


CAMPAIGNS = {
    "ex2": ("RQ-1 Schlagzwang", 20261010, ex2),
    "ex3": ("RQ-3 movement strategies", 20261011, ex3),
    "ex4": ("RQ-2 rule main effects", 20261012, ex4),
    "ex5": ("Seating geometry", 20261013, ex5),
    "ex6": ("RQ-4 interactions", 20261014, ex6),
    # Own seed and own pre-registration (§15, D-78).
    "ex7": ("RQ-5 seat exposure", 20261015, ex7),
    "ex8": ("RQ-6 turn order, capture play, middle seat", 20261016, ex8),
    "ex9": ("RQ-8 rule x strategy", 20261020, ex9),
    "ex10": ("RQ-9 rule x player count", 20261021, ex10),
    "ex11": ("RQ-10 strategy x player count", 20261022, ex11),
    "ex12": ("RQ-11 rule x seating", 20261023, ex12),
}

#: D-59's cell counts. main() checks every builder against them, so the plan and the files
#: on disk state the same thing.
EXPECTED_CELLS = {"ex2": 36, "ex3": 64, "ex4": 168, "ex5": 10, "ex6": 105,
                  "ex7": 14, "ex8": 6, "ex9": 50, "ex10": 40, "ex11": 16,
                  "ex12": 20}


def main() -> int:
    """Write one JSON file per campaign.

    Returns 1 if a builder's cell count disagrees with D-59 or a campaign repeats a cell key.
    """
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

    # EX-1 and EX-1b are hand-written rather than generated here. Their two cells complete the
    # plan's 531, and their 800,000 games plus the AK-5 smoke cell's two complete its
    # 99,650,002.
    print(f"\n{total_cells + 2:>4} cells total (with EX-1 and EX-1b)")
    print(f"{total_games + 800_002:>12,} games total")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

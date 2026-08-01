"""Resolving §6.4's four confirmatory families against the campaign data.

§6.4 fixes the hypotheses; :mod:`multiplicity` carries them as data; this
module is where each one is bound to the cells that answer it and turned into
an :class:`~madnlab.analysis.estimands.Estimate`. Holm then runs **within**
each family, over metrics x contrasts jointly, exactly as §6.4 specifies.

The binding is the part that has to be explicit. A contrast named
"capture_mode:mandatory-optional" means nothing until someone says which cells
are the mandatory arm and which are the optional one, and for RQ-2 the answer
is "all 84 EX-4 cells at that level, pooled" while for RQ-1 it is one named
headline cell. Both live here, in code, rather than in a reader's head.
"""

from __future__ import annotations

import json
from collections.abc import Sequence
from pathlib import Path
from typing import NamedTuple

from madnlab.analysis import estimands
from madnlab.analysis.aggregate import CellSummary, load_cells
from madnlab.analysis.estimands import Estimate
from madnlab.analysis.multiplicity import FAMILIES, HolmResult, Hypothesis, holm


class Dataset(NamedTuple):
    """Every campaign's cells, with the configuration that produced them."""

    cells: dict[str, CellSummary]
    rules: dict[str, dict[str, str]]
    agents: dict[str, tuple[str, ...]]

    def matching(self, prefix: str) -> list[str]:
        return sorted(key for key in self.cells if key.startswith(prefix))


def load_dataset(run_dirs: Sequence[Path]) -> Dataset:
    """Load every campaign in ``run_dirs`` into one addressable dataset."""
    cells: dict[str, CellSummary] = {}
    rules: dict[str, dict[str, str]] = {}
    agents: dict[str, tuple[str, ...]] = {}
    for directory in run_dirs:
        summary = directory / "summary.jsonl.gz"
        if not summary.exists():
            summary = directory / "summary.jsonl"
        if not summary.exists():
            continue
        cells.update(load_cells(summary))
        config = directory / "campaign.json"
        if config.exists():
            payload = json.loads(config.read_text(encoding="utf-8"))
            for entry in payload.get("cells", []):
                key = str(entry["key"])
                rules[key] = {str(k): str(v) for k, v in entry.get("rules", {}).items()}
                agents[key] = tuple(str(a) for a in entry.get("agents", []))
    return Dataset(cells=cells, rules=rules, agents=agents)


class FamilyResult(NamedTuple):
    family: str
    estimates: list[Estimate]
    holm: list[HolmResult]
    #: Contrasts §6.4 declares that no cell in the dataset could answer. Named
    #: rather than dropped: a family reported as "3 of 4 rejected" when the
    #: fourth never ran is a different claim from "3 of 4 rejected".
    unavailable: list[str]


def _win_rate_by_starting_seat(cells: Sequence[CellSummary]) -> tuple[int, int]:
    """P(win | seat is the starter), pooled. Returns (wins, games).

    §6.3's symmetry identity makes this the win-rate estimand for RQ-2: in a
    homogeneous field every seat wins exactly 1/k whatever the rules, so a
    per-seat rate carries no rule information at all. The starter's rate does.
    """
    wins = sum(cell.wins_by_turn_offset.get(0, 0) for cell in cells)
    games = sum(cell.games for cell in cells)
    return wins, games


def _pooled_lengths(cells: Sequence[CellSummary]) -> list[float]:
    pooled: list[float] = []
    for cell in cells:
        pooled.extend(float(value) for value in cell.rounds_to_first_win)
    return pooled


def rq1(data: Dataset, *, seed: int, resamples: int) -> FamilyResult:
    """Dispersion and dynamics in the headline cell (4 players, seats 4, RANDOM)."""
    arms = {
        mode: f"ex2/4s4p/random/{mode}"
        for mode in ("optional", "mandatory", "mandatory_extended")
    }
    estimates: list[Estimate] = []
    hypotheses: list[Hypothesis] = []
    unavailable: list[str] = []

    baseline_key = arms["optional"]
    for index, mode in enumerate(("mandatory", "mandatory_extended")):
        key = arms[mode]
        contrast = f"{mode}-optional"
        if key not in data.cells or baseline_key not in data.cells:
            unavailable.extend(
                f"{metric} @ {contrast}" for metric in FAMILIES["RQ-1"][0]
            )
            continue
        arm, base = data.cells[key], data.cells[baseline_key]

        estimates.append(
            estimands.cv_ratio(
                [float(v) for v in arm.rounds_to_first_win],
                [float(v) for v in base.rounds_to_first_win],
                label=f"CV ratio rounds_to_first_win :: {contrast}",
                seed=seed + index,
                resamples=resamples,
            )
        )
        hypotheses.append(
            Hypothesis("RQ-1", "cv_ratio_rounds_to_first_win", contrast)
        )

        estimates.append(
            estimands.mean_difference(
                arm.lead_changes_per_turn,
                base.lead_changes_per_turn,
                label=f"lead changes per turn :: {contrast}",
                seed=seed + 100 + index,
                resamples=resamples,
            )
        )
        hypotheses.append(Hypothesis("RQ-1", "lead_changes_per_turn", contrast))

        estimates.append(
            estimands.proportion_difference(
                arm.comebacks, arm.checkpointed,
                base.comebacks, base.checkpointed,
                label=f"comeback rate :: {contrast}",
            )
        )
        hypotheses.append(Hypothesis("RQ-1", "comeback_rate", contrast))

        # Predictability enters the family as the *leader-wins* proportion.
        # The skill score is a monotone affine rescaling of it at fixed k, so
        # the test is identical and the proportion keeps an exact variance.
        estimates.append(
            estimands.proportion_difference(
                arm.leader_at_50_won, arm.checkpointed,
                base.leader_at_50_won, base.checkpointed,
                label=f"leader-at-50%% wins :: {contrast}",
            )
        )
        hypotheses.append(Hypothesis("RQ-1", "predictability_skill", contrast))

    results = holm([e.p_value for e in estimates], hypotheses) if estimates else []
    return FamilyResult("RQ-1", estimates, results, unavailable)


#: RQ-2's nine axis contrasts, as (contrast name, rule key, level a, level b).
#: The defaults matter: a cell that does not carry a flag is at its baseline
#: level, which is how §8's configs are written.
RQ2_AXES = (
    ("cold_start:strict-one_piece_out", "cold_start", "strict", "one_piece_out"),
    ("cold_start:free_entry-one_piece_out", "cold_start", "free_entry", "one_piece_out"),
    ("capture_mode:mandatory-optional", "capture_mode", "mandatory", "optional"),
    (
        "capture_mode:mandatory_extended-optional",
        "capture_mode",
        "mandatory_extended",
        "optional",
    ),
    ("dreimal_wuerfeln:on-off", "dreimal_wuerfeln", "True", "False"),
    (
        "bonus_roll_after_quick_entry:true-false",
        "bonus_roll_after_quick_entry",
        "True",
        "False",
    ),
    ("goal_no_jump:true-false", "goal_no_jump", "True", "False"),
    ("barriers:true-false", "barriers", "True", "False"),
    ("bonus_roll_forfeited:true-false", "bonus_roll_forfeited", "True", "False"),
)


def rq2(data: Dataset, *, seed: int, resamples: int) -> FamilyResult:
    """Main effects, pooled over the EX-4 factorial.

    Pooling is what makes n = 20,000 per cell enough: a two-level axis is
    estimated from all 84 cells at each level, so the contrast rests on 1.68M
    games and resolves to 0.18 pp. Nothing here is a per-cell claim.
    """
    keys = data.matching("ex4/")
    estimates: list[Estimate] = []
    hypotheses: list[Hypothesis] = []
    unavailable: list[str] = []

    for index, (name, rule_key, level_a, level_b) in enumerate(RQ2_AXES):
        def level_of(key: str, _rule: str = rule_key) -> str:
            return data.rules.get(key, {}).get(_rule, "")

        arm_a = [data.cells[k] for k in keys if level_of(k) == level_a]
        arm_b = [data.cells[k] for k in keys if level_of(k) == level_b]
        if not arm_a or not arm_b:
            unavailable.extend(
                f"{metric} @ {name} ({len(arm_a)} vs {len(arm_b)} cells)"
                for metric in FAMILIES["RQ-2"][0]
            )
            continue

        wins_a, games_a = _win_rate_by_starting_seat(arm_a)
        wins_b, games_b = _win_rate_by_starting_seat(arm_b)
        estimates.append(
            estimands.proportion_difference(
                wins_a, games_a, wins_b, games_b,
                label=f"win rate by starting seat :: {name}",
            )
        )
        hypotheses.append(Hypothesis("RQ-2", "win_rate_by_starting_seat", name))

        estimates.append(
            estimands.mean_difference(
                _pooled_lengths(arm_a),
                _pooled_lengths(arm_b),
                label=f"rounds to first win :: {name}",
                seed=seed + 200 + index,
                resamples=resamples,
            )
        )
        hypotheses.append(Hypothesis("RQ-2", "rounds_to_first_win", name))

    results = holm([e.p_value for e in estimates], hypotheses) if estimates else []
    return FamilyResult("RQ-2", estimates, results, unavailable)


def rq3(data: Dataset, *, seed: int, resamples: int) -> FamilyResult:
    """Deviant win rate against a RANDOM field at 4 players.

    The deviant occupies seat 0 of the 1-deviant cells, so its win rate is
    tested against the 1/k reference directly. §6.3 forbids reading this off a
    homogeneous field, where the symmetry identity fixes every seat at 1/k
    whatever the policy does.
    """
    del seed, resamples
    estimates: list[Estimate] = []
    hypotheses: list[Hypothesis] = []
    unavailable: list[str] = []

    deviant_cells: dict[str, CellSummary] = {}
    for agent in ("SPREAD", "FOCUS_FRONT", "FOCUS_REAR"):
        key = f"ex3/deviant/4s4p/{agent.lower()}-vs-random"
        if key in data.cells:
            deviant_cells[agent] = data.cells[key]
        else:
            unavailable.append(f"deviant_win_rate @ {agent}-reference")

    for agent, cell in deviant_cells.items():
        wins = cell.wins_by_seat.get(0, 0)
        reference = cell.games / cell.players
        # Against a *fixed* reference, so a one-sample proportion test.
        estimates.append(
            estimands.proportion_difference(
                wins, cell.games,
                round(reference), cell.games,
                label=f"deviant win rate vs 1/k :: {agent}",
            )
        )
        hypotheses.append(Hypothesis("RQ-3", "deviant_win_rate", f"{agent}-reference"))

    if "FOCUS_FRONT" in deviant_cells and "FOCUS_REAR" in deviant_cells:
        front, rear = deviant_cells["FOCUS_FRONT"], deviant_cells["FOCUS_REAR"]
        estimates.append(
            estimands.proportion_difference(
                front.wins_by_seat.get(0, 0), front.games,
                rear.wins_by_seat.get(0, 0), rear.games,
                label="deviant win rate :: FOCUS_FRONT - FOCUS_REAR",
            )
        )
        hypotheses.append(
            Hypothesis("RQ-3", "deviant_win_rate", "FOCUS_FRONT-FOCUS_REAR")
        )
    else:
        unavailable.append("deviant_win_rate @ FOCUS_FRONT-FOCUS_REAR")

    results = holm([e.p_value for e in estimates], hypotheses) if estimates else []
    return FamilyResult("RQ-3", estimates, results, unavailable)


#: RQ-4's named interaction contrasts. Each is a difference of differences:
#: how much the deviant's edge changes when the rule changes. A 2x2
#: interaction does **not** pool, which is why these cells run at 400k.
RQ4_INTERACTIONS = (
    (
        "capture_mode:mandatory x strategy",
        "ex6b/4s4p/spread-vs-random/mandatory",
        "ex6b/4s4p/spread-vs-random/optional",
    ),
    (
        "capture_mode:mandatory_extended x strategy",
        "ex6b/4s4p/spread-vs-random/mandatory_extended",
        "ex6b/4s4p/spread-vs-random/optional",
    ),
    (
        "barriers x strategy",
        "ex6d/4s4p/spread-vs-random/barriers=True",
        "ex6d/4s4p/spread-vs-random/barriers=False",
    ),
    (
        "capture_mode:mandatory x strategy x players",
        "ex6b/4s4p/focus_front-vs-random/mandatory",
        "ex6b/4s4p/focus_front-vs-random/optional",
    ),
    (
        "capture_mode:mandatory_extended x strategy x players",
        "ex6b/4s4p/focus_front-vs-random/mandatory_extended",
        "ex6b/4s4p/focus_front-vs-random/optional",
    ),
    (
        "barriers x strategy x players",
        "ex6d/4s4p/focus_front-vs-random/barriers=True",
        "ex6d/4s4p/focus_front-vs-random/barriers=False",
    ),
)

#: The player-count and geometry rows, which contrast whole cells rather than
#: a deviant's edge.
RQ4_CELL_CONTRASTS = (
    ("capture_mode x players", "ex6e/6s2p/random/mandatory", "ex6e/6s6p/random/mandatory"),
    ("capture_mode x players x board", "ex6e/6s2p/random/optional", "ex6e/6s6p/random/optional"),
    ("EX-5 pattern effect", "ex5/3p/6s-adjacent/random", "ex5/3p/6s-spread/random"),
    ("EX-5 geometry effect", "ex5/3p/4s-adjacent/random", "ex5/3p/6s-adjacent/random"),
)


def rq4(data: Dataset, *, seed: int, resamples: int) -> FamilyResult:
    """Named interaction contrasts (§6.4, D-28, D-46)."""
    del seed, resamples
    estimates: list[Estimate] = []
    hypotheses: list[Hypothesis] = []
    unavailable: list[str] = []

    for name, key_a, key_b in RQ4_INTERACTIONS:
        if key_a not in data.cells or key_b not in data.cells:
            unavailable.append(f"primary_per_row @ {name}")
            continue
        arm, base = data.cells[key_a], data.cells[key_b]
        # The deviant sits at seat 0; the interaction is how much its edge
        # over 1/k moves when the rule flips.
        estimates.append(
            estimands.proportion_difference(
                arm.wins_by_seat.get(0, 0), arm.games,
                base.wins_by_seat.get(0, 0), base.games,
                label=f"deviant edge shift :: {name}",
            )
        )
        hypotheses.append(Hypothesis("RQ-4", "primary_per_row", name))

    for name, key_a, key_b in RQ4_CELL_CONTRASTS:
        if key_a not in data.cells or key_b not in data.cells:
            unavailable.append(f"primary_per_row @ {name}")
            continue
        arm, base = data.cells[key_a], data.cells[key_b]
        # Starter's win rate: the one win-rate estimand that carries
        # information in a homogeneous field (§6.3).
        wins_a, games_a = _win_rate_by_starting_seat([arm])
        wins_b, games_b = _win_rate_by_starting_seat([base])
        estimates.append(
            estimands.proportion_difference(
                wins_a, games_a, wins_b, games_b,
                label=f"starter win rate :: {name}",
            )
        )
        hypotheses.append(Hypothesis("RQ-4", "primary_per_row", name))

    results = holm([e.p_value for e in estimates], hypotheses) if estimates else []
    return FamilyResult("RQ-4", estimates, results, unavailable)


class RQ1Verdict(NamedTuple):
    """§6.4's decidable biconditional, evaluated rather than argued."""

    supported: bool
    cv_lower_bound: float
    cv_exceeds_one: bool
    dynamism_conjuncts: int
    detail: list[str]


def rq1_verdict(result: FamilyResult) -> RQ1Verdict:
    """RQ-1 is supported iff the CV lower bound exceeds 1 **and** 2 of 3.

    The three dynamism conjuncts are ``lead_changes_per_turn``, the comeback
    rate and ``1 - predictability``, each Holm-adjusted and each required to
    exclude zero *in the dynamism direction* — a significant move the wrong
    way is not support, which a bare "CI excludes zero" test would count.
    """
    by_key = {
        (r.hypothesis.metric, r.hypothesis.contrast): r for r in result.holm
    }
    estimates = {e.label.split(" :: ")[0].strip(): e for e in result.estimates}
    detail: list[str] = []

    contrast = "mandatory-optional"
    cv_result = by_key.get(("cv_ratio_rounds_to_first_win", contrast))
    cv_estimate = next(
        (
            e
            for e in result.estimates
            if e.label.startswith("CV ratio") and e.label.endswith(contrast)
        ),
        None,
    )
    if cv_estimate is None or cv_result is None:
        return RQ1Verdict(False, float("nan"), False, 0, ["CV ratio contrast missing"])

    cv_lower = cv_estimate.interval.low
    cv_ok = cv_lower > 1.0
    detail.append(
        f"(i) CV ratio {cv_estimate.estimate:.4f}, 95% CI lower bound "
        f"{cv_lower:.4f} {'>' if cv_ok else '<='} 1"
    )

    conjuncts = 0
    # Direction is fixed per conjunct: more lead changes, more comebacks and
    # *less* predictability all mean more dynamic.
    directions = (
        ("lead_changes_per_turn", "lead changes per turn", +1),
        ("comeback_rate", "comeback rate", +1),
        ("predictability_skill", "leader-at-50%% wins", -1),
    )
    for metric, prefix, direction in directions:
        holm_result = by_key.get((metric, contrast))
        estimate = next(
            (
                e
                for e in result.estimates
                if e.label.startswith(prefix) and e.label.endswith(contrast)
            ),
            None,
        )
        if holm_result is None or estimate is None:
            detail.append(f"(ii) {metric}: missing")
            continue
        signed = estimate.estimate * direction
        counts = holm_result.rejected and signed > 0
        conjuncts += counts
        detail.append(
            f"(ii) {metric}: {estimate.estimate:+.6f} "
            f"(dynamism direction {'yes' if signed > 0 else 'no'}), "
            f"Holm {'rejected' if holm_result.rejected else 'not rejected'} "
            f"at alpha={holm_result.adjusted_alpha:.5f} -> "
            f"{'counts' if counts else 'does not count'}"
        )
    del estimates
    return RQ1Verdict(cv_ok and conjuncts >= 2, cv_lower, cv_ok, conjuncts, detail)


def run_all(data: Dataset, *, seed: int, resamples: int) -> list[FamilyResult]:
    return [
        rq1(data, seed=seed, resamples=resamples),
        rq2(data, seed=seed, resamples=resamples),
        rq3(data, seed=seed, resamples=resamples),
        rq4(data, seed=seed, resamples=resamples),
    ]

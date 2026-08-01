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
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from typing import NamedTuple

from madnlab.analysis import estimands, intervals
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
                label=f"leader-at-50% wins :: {contrast}",
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


def _mean_difference_job(
    payload: tuple[list[float], list[float], str, int, int],
) -> Estimate:
    """One pooled mean difference, at module scope so it can be pickled."""
    sample_a, sample_b, label, seed, resamples = payload
    return estimands.mean_difference(
        sample_a, sample_b, label=label, seed=seed, resamples=resamples
    )


def rq2(
    data: Dataset, *, seed: int, resamples: int, workers: int = 1
) -> FamilyResult:
    """Main effects, pooled over the EX-4 factorial.

    Pooling is what makes n = 20,000 per cell enough: a two-level axis is
    estimated from all 84 cells at each level, so the contrast rests on 1.68M
    games and resolves to 0.18 pp. Nothing here is a per-cell claim.

    The nine bootstrap contrasts are independent of each other, so ``workers``
    runs them in parallel. That is a scheduling decision and nothing else — the
    seed of each contrast is fixed by its index, so the numbers do not depend
    on how many workers ran them, which is the property AK-2 asserts for the
    engine and which an analysis has no more right to give up than a run does.
    """
    keys = data.matching("ex4/")
    estimates: list[Estimate | None] = []
    hypotheses: list[Hypothesis] = []
    unavailable: list[str] = []
    jobs: list[tuple[list[float], list[float], str, int, int]] = []
    slots: list[int] = []

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

        slots.append(len(estimates))
        estimates.append(None)
        jobs.append(
            (
                _pooled_lengths(arm_a),
                _pooled_lengths(arm_b),
                f"rounds to first win :: {name}",
                seed + 200 + index,
                resamples,
            )
        )
        hypotheses.append(Hypothesis("RQ-2", "rounds_to_first_win", name))

    if jobs and workers > 1:
        with ProcessPoolExecutor(max_workers=min(workers, len(jobs))) as pool:
            for slot, estimate in zip(
                slots, pool.map(_mean_difference_job, jobs), strict=True
            ):
                estimates[slot] = estimate
    else:
        for slot, job in zip(slots, jobs, strict=True):
            estimates[slot] = _mean_difference_job(job)

    resolved = [e for e in estimates if e is not None]
    results = holm([e.p_value for e in resolved], hypotheses) if resolved else []
    return FamilyResult("RQ-2", resolved, results, unavailable)


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
        # Against a *fixed* reference: 1/k is arithmetic, not an estimate, so
        # it carries no sampling variance and the test is one-sample (SQ-1).
        estimates.append(
            estimands.proportion_vs_reference(
                cell.wins_by_seat.get(0, 0), cell.games, 1.0 / cell.players,
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

#: The player-count and geometry rows. §8.1 gives EX-6e's primary metric as
#: "battery metrics" — the homogeneous field makes win rate uninformative —
#: and each is a genuine 2x2 interaction, given as four cells: (a1, a0, b1, b0)
#: for (a1 - a0) - (b1 - b0).
RQ4_BATTERY_INTERACTIONS = (
    (
        "capture_mode x players",
        "ex6e/6s2p/random/mandatory", "ex6e/6s2p/random/optional",
        "ex6e/6s6p/random/mandatory", "ex6e/6s6p/random/optional",
    ),
    (
        "capture_mode x players x board",
        "ex6e/6s4p/random/mandatory", "ex6e/6s4p/random/optional",
        "ex2/4s4p/random/mandatory", "ex2/4s4p/random/optional",
    ),
)

#: EX-5's pre-registered decomposition (§8). Two-arm battery contrasts, not
#: interactions: the naive comparison is their *sum* and §8 forbids publishing
#: it as a pattern effect.
RQ4_EX5_ROWS = (
    ("EX-5 pattern effect", "ex5/3p/6s-adjacent/random", "ex5/3p/6s-spread/random"),
    ("EX-5 geometry effect", "ex5/3p/4s-adjacent/random", "ex5/3p/6s-adjacent/random"),
)


def rq4(data: Dataset, *, seed: int, resamples: int) -> FamilyResult:
    """Named interaction contrasts (§6.4, D-28, D-46, D-77)."""
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

    for name, key_a1, key_a0, key_b1, key_b0 in RQ4_BATTERY_INTERACTIONS:
        keys = (key_a1, key_a0, key_b1, key_b0)
        if any(k not in data.cells for k in keys):
            unavailable.append(f"primary_per_row @ {name}")
            continue
        arms = [
            [float(v) for v in data.cells[k].rounds_to_first_win] for k in keys
        ]
        estimates.append(
            estimands.mean_difference_in_differences(
                *arms, label=f"rounds to first win, interaction :: {name}"
            )
        )
        hypotheses.append(Hypothesis("RQ-4", "primary_per_row", name))

    for name, key_a, key_b in RQ4_EX5_ROWS:
        if key_a not in data.cells or key_b not in data.cells:
            unavailable.append(f"primary_per_row @ {name}")
            continue
        arm, base = data.cells[key_a], data.cells[key_b]
        estimates.append(
            estimands.mean_difference(
                [float(v) for v in arm.rounds_to_first_win],
                [float(v) for v in base.rounds_to_first_win],
                label=f"rounds to first win :: {name}",
                seed=seed + 900 + len(estimates),
                resamples=resamples,
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
        ("predictability_skill", "leader-at-50% wins", -1),
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


def run_all(
    data: Dataset, *, seed: int, resamples: int, workers: int = 1
) -> list[FamilyResult]:
    return [
        rq1(data, seed=seed, resamples=resamples),
        rq2(data, seed=seed, resamples=resamples, workers=workers),
        rq3(data, seed=seed, resamples=resamples),
        rq4(data, seed=seed, resamples=resamples),
        rq5(data),
        rq6(data),
    ]


# -- §15: seat exposure ------------------------------------------------------

#: Cells RQ-5 reads, by short name.
RQ5_CELLS = {
    "adjacent-spread": "ex7/2p/4s-adjacent/spread",
    "adjacent-random": "ex7/2p/4s-adjacent/random",
    "opposite-spread": "ex7/2p/4s-opposite/spread",
    "opposite-random": "ex7/2p/4s-opposite/random",
    "3p-adjacent-spread": "ex7/3p/6s-adjacent/spread",
    "3p-spread-spread": "ex7/3p/6s-spread/spread",
    "3p-adjacent-random": "ex7/3p/6s-adjacent/random",
    "3p-spread-random": "ex7/3p/6s-spread/random",
}

#: §15.2's equivalence margin for the negative controls, and the magnitude
#: threshold hypothesis 1 has to clear.
RQ5_EQUIVALENCE_PP = 1.0
RQ5_MAGNITUDE_PP = 5.0


def _seat_asymmetry(cell: CellSummary, label: str) -> Estimate:
    """p(second occupied seat) − p(first), multinomial (§15.2).

    The seats are named by position, not by which one happened to win more.
    Selecting the extreme pair out of the data and then testing it is a
    selection the interval knows nothing about.
    """
    first, second = cell.occupied[0], cell.occupied[1]
    return estimands.seat_difference(
        cell.wins_by_seat.get(second, 0),
        cell.wins_by_seat.get(first, 0),
        cell.games,
        label=label,
    )


def _asymmetry_difference(
    arm: CellSummary, base: CellSummary, label: str
) -> Estimate:
    """Difference of two cells' seat asymmetries — separate games, so the
    variances add."""
    left = _seat_asymmetry(arm, "left")
    right = _seat_asymmetry(base, "right")
    estimate = left.estimate - right.estimate
    z_crit = intervals.z_for(0.95)
    se_left = (left.interval.high - left.interval.low) / (2 * z_crit)
    se_right = (right.interval.high - right.interval.low) / (2 * z_crit)
    se = (se_left**2 + se_right**2) ** 0.5
    interval = intervals.Interval(
        estimate, estimate - z_crit * se, estimate + z_crit * se, 0.95
    )
    p_value = estimands.two_sided_p(estimate / se) if se > 0 else 1.0
    return Estimate(label, estimate, interval, p_value, arm.games, base.games)


def rq5(data: Dataset, *, seed: int = 0, resamples: int = 0) -> FamilyResult:
    """§15's family: does seating position decide the game? Eight hypotheses.

    ``seed`` and ``resamples`` are accepted and unused — every contrast here is
    a proportion with a closed-form variance, so nothing is bootstrapped. They
    keep the signature uniform with the other families.
    """
    del seed, resamples
    estimates: list[Estimate] = []
    hypotheses: list[Hypothesis] = []
    unavailable: list[str] = []
    contrasts = FAMILIES["RQ-5"][1]

    plan: tuple[tuple[str, str, tuple[str, ...]], ...] = (
        (contrasts[0], "single", ("adjacent-spread",)),
        (contrasts[1], "single", ("adjacent-random",)),
        (contrasts[2], "single", ("opposite-spread",)),
        (contrasts[3], "single", ("opposite-random",)),
        (contrasts[4], "diff", ("adjacent-spread", "adjacent-random")),
        (contrasts[5], "diff", ("adjacent-spread", "opposite-spread")),
        (contrasts[6], "diff", ("3p-adjacent-spread", "3p-spread-spread")),
        (contrasts[7], "diff", ("3p-adjacent-random", "3p-spread-random")),
    )

    for name, kind, arms in plan:
        cells = [data.cells.get(RQ5_CELLS[arm]) for arm in arms]
        first = cells[0]
        if first is None or any(c is None for c in cells):
            unavailable.append(f"seat_asymmetry @ {name}")
            continue
        if kind == "single":
            estimates.append(_seat_asymmetry(first, f"seat asymmetry :: {name}"))
        else:
            second = cells[1]
            assert second is not None
            estimates.append(
                _asymmetry_difference(first, second, f"asymmetry shift :: {name}")
            )
        hypotheses.append(Hypothesis("RQ-5", "seat_asymmetry", name))

    results = holm([e.p_value for e in estimates], hypotheses) if estimates else []
    return FamilyResult("RQ-5", estimates, results, unavailable)


class RQ5Verdict(NamedTuple):
    """§15.2's biconditional, evaluated rather than argued."""

    supported: bool
    detail: list[str]


def rq5_verdict(result: FamilyResult) -> RQ5Verdict:
    """Supported iff 1, 5 and 6 reject in direction **and** 3 is equivalent.

    The conjunction is what makes it an explanation rather than an
    observation: (6) attributes the effect to the seating geometry, (5) shows
    the strategy matters, and (3) is the negative control — `opposite` seating
    has equal gaps and must show nothing.
    """
    contrasts = FAMILIES["RQ-5"][1]
    by_contrast = {
        holm_result.hypothesis.contrast: (holm_result, estimate)
        for holm_result, estimate in zip(result.holm, result.estimates, strict=True)
    }
    detail: list[str] = []
    conditions: list[bool] = []

    for index, requirement in ((0, "> 0 and > 5 pp"), (4, "> 0"), (5, "> 0")):
        name = contrasts[index]
        pair = by_contrast.get(name)
        if pair is None:
            detail.append(f"H{index + 1} ({name}): missing")
            conditions.append(False)
            continue
        holm_result, estimate = pair
        big_enough = estimate.estimate * 100 > RQ5_MAGNITUDE_PP if index == 0 else True
        ok = holm_result.rejected and estimate.estimate > 0 and big_enough
        conditions.append(ok)
        detail.append(
            f"H{index + 1} ({name}): {estimate.estimate * 100:+.3f} pp, "
            f"Holm {'rejected' if holm_result.rejected else 'not rejected'}, "
            f"needs {requirement} -> {'holds' if ok else 'fails'}"
        )

    name = contrasts[2]
    pair = by_contrast.get(name)
    if pair is None:
        detail.append(f"H3 ({name}): missing")
        conditions.append(False)
    else:
        estimate = pair[1]
        margin = RQ5_EQUIVALENCE_PP / 100.0
        equivalent = estimate.interval.low > -margin and estimate.interval.high < margin
        conditions.append(equivalent)
        detail.append(
            f"H3 ({name}): {estimate.estimate * 100:+.3f} pp, CI "
            f"[{estimate.interval.low * 100:+.3f}, "
            f"{estimate.interval.high * 100:+.3f}] vs margin "
            f"+/-{RQ5_EQUIVALENCE_PP} pp -> "
            f"{'equivalent' if equivalent else 'not equivalent'}"
        )

    return RQ5Verdict(all(conditions), detail)


# -- §16: turn order, capture play, and the middle seat ----------------------


def _starter_advantage(cell: CellSummary, label: str) -> Estimate:
    """P(win | seat is the starter) against the fixed 1/k reference.

    Measured since M3 and reported in every campaign, but never tested: it had
    a ledger row, a function and a report section, and no hypothesis (§16).
    """
    return estimands.proportion_vs_reference(
        cell.wins_by_turn_offset.get(0, 0),
        cell.games,
        1.0 / cell.players,
        label=label,
    )


def _deviant_edge(cell: CellSummary, label: str) -> Estimate:
    """The seat-0 deviant's win rate against 1/k."""
    return estimands.proportion_vs_reference(
        cell.wins_by_seat.get(0, 0), cell.games, 1.0 / cell.players, label=label
    )


def _middle_seat(cell: CellSummary, label: str) -> Estimate:
    """Seat 1 against the mean of its two neighbours, three players on four seats.

    §1's own question — "is the middle seat measurably disadvantaged" — with
    §2.2's stated reason: an opponent directly behind and the other's start
    area directly ahead. Weights (-1/2, +1, -1/2), which is not a difference
    of two seats and needs the multinomial contrast.
    """
    counts = [cell.wins_by_seat.get(seat, 0) for seat in cell.occupied]
    return estimands.multinomial_contrast(
        counts, [-0.5, 1.0, -0.5], cell.games, label=label
    )


def rq6(data: Dataset, *, seed: int = 0, resamples: int = 0) -> FamilyResult:
    """§16's family. Nine hypotheses; every contrast has a closed-form variance."""
    del seed, resamples
    estimates: list[Estimate] = []
    hypotheses: list[Hypothesis] = []
    unavailable: list[str] = []
    contrasts = FAMILIES["RQ-6"][1]

    def add(name: str, estimate: Estimate | None) -> None:
        if estimate is None:
            unavailable.append(f"turn_order_and_play @ {name}")
            return
        estimates.append(estimate)
        hypotheses.append(Hypothesis("RQ-6", "turn_order_and_play", name))

    # 1-2: does going first help, on each board?
    four = data.cells.get("ex1/4s4p/random/baseline")
    six = data.cells.get("ex1b/6s6p/random/baseline")
    add(contrasts[0], _starter_advantage(four, f"starter advantage :: {contrasts[0]}")
        if four else None)
    add(contrasts[1], _starter_advantage(six, f"starter advantage :: {contrasts[1]}")
        if six else None)

    # 3: and does it shrink as the table grows? Board held fixed (D-12).
    two_p = data.cells.get("ex8/6s2p/random/baseline")
    six_p = data.cells.get("ex8/6s6p/random/baseline")
    if two_p and six_p:
        add(
            contrasts[2],
            estimands.independent_difference(
                _starter_advantage(two_p, "2p"),
                _starter_advantage(six_p, "6p"),
                label=f"starter advantage :: {contrasts[2]}",
            ),
        )
    else:
        add(contrasts[2], None)

    # 4-6: the one agent that plays toward a rule. Under mandatory capture the
    # rule applies to everyone, so its edge should go away.
    greedy = {
        mode: data.cells.get(f"ex8/4s4p/greedy_capture-vs-random/{mode}")
        for mode in ("optional", "mandatory")
    }
    add(
        contrasts[3],
        _deviant_edge(greedy["optional"], f"GREEDY edge :: {contrasts[3]}")
        if greedy["optional"] else None,
    )
    add(
        contrasts[4],
        _deviant_edge(greedy["mandatory"], f"GREEDY edge :: {contrasts[4]}")
        if greedy["mandatory"] else None,
    )
    if greedy["optional"] and greedy["mandatory"]:
        add(
            contrasts[5],
            estimands.independent_difference(
                _deviant_edge(greedy["optional"], "optional"),
                _deviant_edge(greedy["mandatory"], "mandatory"),
                label=f"GREEDY edge shift :: {contrasts[5]}",
            ),
        )
    else:
        add(contrasts[5], None)

    # 7-8: §1's middle-seat question, finally asked.
    for index, field in ((6, "random"), (7, "spread")):
        middle = data.cells.get(f"ex5/3p/4s-adjacent/{field}")
        add(
            contrasts[index],
            _middle_seat(middle, f"middle seat :: {contrasts[index]}")
            if middle else None,
        )

    # 9: the manipulation check §6.4 names and no code ran. Mandatory capture
    # must raise the capture count, or the arm did not do anything.
    optional = data.cells.get("ex2/4s4p/random/optional")
    mandatory = data.cells.get("ex2/4s4p/random/mandatory")
    if optional and mandatory:
        add(
            contrasts[8],
            estimands.mean_difference_from_moments(
                mandatory.metric_means["captures_total"],
                mandatory.metric_vars["captures_total"],
                mandatory.games,
                optional.metric_means["captures_total"],
                optional.metric_vars["captures_total"],
                optional.games,
                label=f"captures per game :: {contrasts[8]}",
            ),
        )
    else:
        add(contrasts[8], None)

    results = holm([e.p_value for e in estimates], hypotheses) if estimates else []
    return FamilyResult("RQ-6", estimates, results, unavailable)

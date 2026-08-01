"""Holm correction and the §6.4 confirmatory families.

Holm runs **within each research question's family, over metrics × contrasts
jointly** (D-14). The family sizes are not a runtime detail: they are the
pre-registration, so they live here as data and a test asserts they still add
up to the 40 hypotheses §6.4 declares.

The whole point of D-59 was that these numbers are small. An earlier draft
treated every pairwise cell contrast as confirmatory, which put EX-4's family
at 334 tests and drove n to 325k per cell for an estimand nobody had asked
for. Keeping the families here, next to the correction that consumes them,
makes the cost of widening one visible.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import NamedTuple


class Hypothesis(NamedTuple):
    """One pre-registered confirmatory test."""

    family: str
    metric: str
    contrast: str


class HolmResult(NamedTuple):
    """A hypothesis with its adjusted level and verdict."""

    hypothesis: Hypothesis
    p_value: float
    adjusted_alpha: float
    rejected: bool
    #: Position in the ascending-p ordering, 1-based. Recorded because the
    #: step-down structure is what makes Holm's thresholds non-constant, and a
    #: reader checking a published number needs to see which step it took.
    step: int


#: The §6.4 table, as data. Family -> (metrics, contrasts).
FAMILIES: dict[str, tuple[tuple[str, ...], tuple[str, ...]]] = {
    "RQ-1": (
        (
            "cv_ratio_rounds_to_first_win",
            "lead_changes_per_turn",
            "comeback_rate",
            "predictability_skill",
        ),
        ("mandatory-optional", "mandatory_extended-optional"),
    ),
    "RQ-2": (
        ("win_rate_by_starting_seat", "rounds_to_first_win"),
        (
            "cold_start:strict-one_piece_out",
            "cold_start:free_entry-one_piece_out",
            "capture_mode:mandatory-optional",
            "capture_mode:mandatory_extended-optional",
            "dreimal_wuerfeln:on-off",
            "bonus_roll_after_quick_entry:true-false",
            "goal_no_jump:true-false",
            "barriers:true-false",
            "bonus_roll_forfeited:true-false",
        ),
    ),
    "RQ-3": (
        ("deviant_win_rate",),
        (
            "SPREAD-reference",
            "FOCUS_FRONT-reference",
            "FOCUS_REAR-reference",
            "FOCUS_FRONT-FOCUS_REAR",
        ),
    ),
    "RQ-4": (
        ("primary_per_row",),
        (
            "capture_mode:mandatory x strategy",
            "capture_mode:mandatory_extended x strategy",
            "barriers x strategy",
            "capture_mode x players",
            "EX-5 pattern effect",
            "EX-5 geometry effect",
            "capture_mode:mandatory x strategy x players",
            "capture_mode:mandatory_extended x strategy x players",
            "barriers x strategy x players",
            "capture_mode x players x board",
        ),
    ),
    "RQ-5": (
        ("seat_asymmetry",),
        (
            "4s2p-adjacent-spread",
            "4s2p-adjacent-random",
            "4s2p-opposite-spread",
            "4s2p-opposite-random",
            "spread-minus-random x adjacent",
            "adjacent-minus-opposite x spread",
            "6s3p adjacent-minus-spread x spread",
            "6s3p adjacent-minus-spread x random",
        ),
    ),
    "RQ-6": (
        ("turn_order_and_play",),
        (
            "starter advantage, 4 players",
            "starter advantage, 6 players",
            "starter advantage, 2p minus 6p",
            "GREEDY_CAPTURE vs 1/k, optional",
            "GREEDY_CAPTURE vs 1/k, mandatory",
            "GREEDY_CAPTURE edge, optional minus mandatory",
            "middle seat, 3p on 4 seats, RANDOM",
            "middle seat, 3p on 4 seats, SPREAD",
            "manipulation check: captures under mandatory",
        ),
    ),
}

#: §17's interaction matrix. Sizes rather than contrast lists: the contrasts
#: are the product of an axis list and a variant list and enumerating them
#: twice is how the two copies drift apart.
INTERACTION_FAMILIES: dict[str, int] = {
    "RQ-7": 21 * 5,   # 7 EX-4 axes, pairwise, x 5 metrics
    "RQ-8": 9 * 4 * 5,
    "RQ-9": 9 * 3 * 5,
    "RQ-10": 4 * 3 * 5,
    "RQ-11": 9 * 1 * 5,
}

#: The total §6.4, §15, §16 and §17 declare together.
CONFIRMATORY_TOTAL = 57 + sum(INTERACTION_FAMILIES.values())



def family_hypotheses(family: str) -> tuple[Hypothesis, ...]:
    """Every hypothesis in ``family``, metrics × contrasts."""
    metrics, contrasts = FAMILIES[family]
    return tuple(
        Hypothesis(family=family, metric=metric, contrast=contrast)
        for metric in metrics
        for contrast in contrasts
    )


def family_size(family: str) -> int:
    metrics, contrasts = FAMILIES[family]
    return len(metrics) * len(contrasts)


def holm(
    p_values: Sequence[float],
    hypotheses: Sequence[Hypothesis],
    alpha: float = 0.05,
) -> list[HolmResult]:
    """Holm-Bonferroni step-down over one family.

    Sorted ascending by p; hypothesis at step ``i`` (1-based) is compared
    against ``alpha / (m - i + 1)``; the first failure stops rejection for it
    and everything after it, whatever their own thresholds would allow. That
    monotonicity is the part a naive per-test comparison gets wrong.
    """
    if len(p_values) != len(hypotheses):
        raise ValueError(
            f"{len(p_values)} p-values for {len(hypotheses)} hypotheses"
        )
    if not 0 < alpha < 1:
        raise ValueError(f"alpha must be in (0, 1), got {alpha}")
    m = len(p_values)
    order = sorted(range(m), key=lambda i: p_values[i])
    results: list[HolmResult | None] = [None] * m
    still_rejecting = True
    for step, index in enumerate(order, start=1):
        adjusted = alpha / (m - step + 1)
        if still_rejecting and p_values[index] > adjusted:
            still_rejecting = False
        results[index] = HolmResult(
            hypothesis=hypotheses[index],
            p_value=p_values[index],
            adjusted_alpha=adjusted,
            rejected=still_rejecting,
            step=step,
        )
    return [result for result in results if result is not None]


def first_threshold(family: str, alpha: float = 0.05) -> float:
    """Holm's first-step threshold for a family — its most stringent one."""
    return alpha / family_size(family)

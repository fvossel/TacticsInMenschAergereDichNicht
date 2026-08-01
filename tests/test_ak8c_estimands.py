"""The §6.4 contrast estimators, against the numbers §6.3 works out by hand.

§6.3 states three quantities explicitly — the multinomial SE at p = 0.25 and
n = 100k, the independent SE for the same counts, and the variance ratio a
pure location shift produces. A specification that carries its own worked
values is a specification that can be tested against, and these are the cases
where using the wrong estimator is invisible in the output but wrong by
about 15%.
"""

from __future__ import annotations

import random

import pytest

from madnlab.analysis.estimands import (
    Estimate,
    cv,
    cv_ratio,
    mean_difference,
    mean_ratio,
    predictability_skill,
    proportion_difference,
    seat_difference,
    variance_ratio,
)
from madnlab.analysis.intervals import z_for


def half_width_pp(estimate: Estimate, level: float = 0.95) -> float:
    width: float = estimate.interval.high - estimate.interval.low
    return width / (2 * z_for(level)) * 100


def test_multinomial_se_matches_the_specification() -> None:
    """§6.3: 0.224 pp at p = 0.25, n = 100k."""
    estimate = seat_difference(25_000, 25_000, 100_000, label="seat 0 - seat 1")
    assert half_width_pp(estimate) == pytest.approx(0.224, abs=0.001)


def test_independent_se_is_the_smaller_wrong_one() -> None:
    """§6.3: 0.194 pp — what two independent Wilson intervals would imply.

    Kept as a test because the failure mode is silent: the wrong estimator
    produces a plausible number about 15% too narrow, and every interval
    built on it is overconfident in the same direction.
    """
    estimate = proportion_difference(25_000, 100_000, 25_000, 100_000, label="x")
    assert half_width_pp(estimate) == pytest.approx(0.194, abs=0.001)


def test_the_multinomial_se_is_wider_than_the_independent_one() -> None:
    """The direction of the error, stated so a refactor cannot flip it."""
    within = seat_difference(25_000, 25_000, 100_000, label="within")
    between = proportion_difference(25_000, 100_000, 25_000, 100_000, label="between")
    assert half_width_pp(within) > half_width_pp(between)


def test_pure_location_shift_moves_variance_but_not_cv() -> None:
    """§6.3's worked case for why the CV ratio is the primary estimand.

    A +10% location shift at constant CV gives a variance ratio of 1.21 —
    which would read as a dispersion effect. The CV ratio stays at 1.
    """
    rng = random.Random(7)
    base = [rng.gauss(100, 20) for _ in range(4_000)]
    shifted = [value * 1.1 for value in base]

    assert variance_ratio(shifted, base) == pytest.approx(1.21, abs=0.001)
    assert mean_ratio(shifted, base) == pytest.approx(1.1, abs=0.001)
    assert cv(shifted) == pytest.approx(cv(base), rel=1e-9)
    ratio = cv_ratio(shifted, base, label="cv", seed=1, resamples=300)
    assert ratio.estimate == pytest.approx(1.0, abs=1e-9)


def test_cv_ratio_detects_a_real_dispersion_change() -> None:
    """The complement: widen the spread at constant mean and it must show."""
    rng = random.Random(11)
    base = [rng.gauss(100, 10) for _ in range(4_000)]
    wide = [100 + (value - 100) * 1.5 for value in base]
    ratio = cv_ratio(wide, base, label="cv", seed=2, resamples=400)
    assert ratio.estimate == pytest.approx(1.5, rel=0.02)
    assert ratio.excludes_one


def test_skill_score_is_zero_at_chance_and_one_at_perfect() -> None:
    """SQ-4: scaled so the chance level is k-invariant."""
    for players in (2, 3, 4, 6):
        chance_hits = 1_000 // players
        assert predictability_skill(chance_hits, 1_000, players) == pytest.approx(
            0.0, abs=0.01
        )
        assert predictability_skill(1_000, 1_000, players) == pytest.approx(1.0)


def test_raw_accuracy_would_not_be_comparable_across_k() -> None:
    """Why the skill score exists: 50% is chance at k=2 and excellent at k=6."""
    at_two = predictability_skill(500, 1_000, 2)
    at_six = predictability_skill(500, 1_000, 6)
    assert at_two == pytest.approx(0.0, abs=0.01)
    assert at_six > 0.39


def test_identical_arms_produce_a_null_result() -> None:
    """No difference in, no significance out — for every estimator."""
    rng = random.Random(3)
    sample = [rng.gauss(50, 5) for _ in range(1_500)]
    other = [rng.gauss(50, 5) for _ in range(1_500)]

    difference = mean_difference(sample, other, label="m", seed=5, resamples=300)
    assert not difference.excludes_zero
    assert difference.p_value > 0.05

    seats = seat_difference(2_500, 2_500, 10_000, label="s")
    assert seats.estimate == 0.0
    assert seats.p_value == pytest.approx(1.0)


def test_empty_arms_are_reported_not_guessed() -> None:
    """An estimator that cannot run says so rather than returning zero."""
    assert proportion_difference(0, 0, 5, 10, label="x").note
    assert mean_difference([], [1.0, 2.0], label="m", seed=1).note
    assert cv_ratio([1.0], [1.0, 2.0], label="c", seed=1).note


@pytest.mark.parametrize("shift", [0.0, 2.0, -3.5])
def test_the_estimate_lies_inside_its_own_interval(shift: float) -> None:
    """The invariant that catches a one-sample bootstrap used on two samples.

    Concatenating the arms and resampling the result mixes them in every
    draw, so the replicates trace the permutation null instead of the
    sampling distribution. The point estimate then sits *outside* its own
    interval — a mean difference of 2.0 with a CI of [-0.21, 0.22] — while
    every individual number still looks plausible.
    """
    rng = random.Random(23)
    base = [rng.gauss(20, 3) for _ in range(1_500)]
    other = [value + shift for value in base]
    estimate = mean_difference(other, base, label="m", seed=13, resamples=300)
    assert estimate.interval.low <= estimate.estimate <= estimate.interval.high

    ratio = cv_ratio(other, base, label="c", seed=13, resamples=300)
    assert ratio.interval.low <= ratio.estimate <= ratio.interval.high


def test_mean_difference_recovers_a_known_shift() -> None:
    rng = random.Random(17)
    base = [rng.gauss(20, 3) for _ in range(2_000)]
    shifted = [value + 2.0 for value in base]
    estimate = mean_difference(shifted, base, label="m", seed=9, resamples=400)
    assert estimate.estimate == pytest.approx(2.0, abs=0.01)
    assert estimate.excludes_zero

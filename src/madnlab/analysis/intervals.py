"""Interval estimators (SQ-1, SQ-2, SQ-3, SQ-6).

Stdlib only. The engine has no dependencies and the analysis layer keeps that
property: NF-7 pins the environment because BLAS reduction order differs across
architectures, and the cheapest way to honour that is not to link BLAS at all.

Two rules from §6.3 are enforced by the shapes here rather than by discipline:

* **Wilson is for a single proportion against a fixed reference.** A
  seat-to-seat or strategy-to-strategy difference inside one cell is
  multinomial — exactly one seat wins each game — so two independent Wilson
  intervals understate the SE of their difference (0.194 pp against the correct
  0.224 pp at p = 0.25, n = 100k). :func:`multinomial_difference_ci` is the one
  to use there.
* **The game is the independent unit.** Every bootstrap resamples whole rows,
  never seat records, so the resampler takes a sequence of per-game values and
  there is no way to hand it seat-level data by accident.
"""

from __future__ import annotations

import math
import random
from collections.abc import Callable, Sequence
from statistics import NormalDist
from typing import NamedTuple

_NORMAL = NormalDist()


class Interval(NamedTuple):
    """A point estimate with a two-sided confidence interval."""

    estimate: float
    low: float
    high: float
    level: float

    def excludes(self, value: float) -> bool:
        """Whether ``value`` lies outside the interval.

        The §6.4 decision rules are threshold rules — "CI excludes 1", "CI
        excludes zero" — so the test they turn on lives here rather than being
        rewritten at each call site.
        """
        return value < self.low or value > self.high

    @property
    def half_width(self) -> float:
        return (self.high - self.low) / 2


def z_for(level: float) -> float:
    """Two-sided normal critical value for a confidence ``level``."""
    if not 0 < level < 1:
        raise ValueError(f"level must be in (0, 1), got {level}")
    return _NORMAL.inv_cdf(1 - (1 - level) / 2)


def wilson(successes: int, trials: int, level: float = 0.95) -> Interval:
    """Wilson score interval for a single proportion (SQ-1).

    Used for a proportion against a **fixed reference** — AK-4's 1/k identity,
    a deviant's win rate against 1/k — and not for the difference of two
    proportions observed in the same games.
    """
    if trials <= 0:
        raise ValueError(f"trials must be positive, got {trials}")
    if not 0 <= successes <= trials:
        raise ValueError(f"successes {successes} outside 0..{trials}")
    z = z_for(level)
    p = successes / trials
    denominator = 1 + z * z / trials
    centre = (p + z * z / (2 * trials)) / denominator
    spread = z * math.sqrt(p * (1 - p) / trials + z * z / (4 * trials * trials)) / denominator
    return Interval(estimate=p, low=centre - spread, high=centre + spread, level=level)


def multinomial_difference_ci(
    wins_a: int, wins_b: int, games: int, level: float = 0.95
) -> Interval:
    """CI for ``p_a - p_b`` when both are observed in the same games (SQ-6).

    The per-game win indicators are multinomial: exactly one seat wins, so the
    two proportions are negatively correlated and

        Var(p_a - p_b) = (p_a(1-p_a) + p_b(1-p_b) + 2 p_a p_b) / n

    The final term is the covariance that two independent Wilson intervals
    would drop, and dropping it makes the interval too narrow — the direction
    that produces false positives.
    """
    if games <= 0:
        raise ValueError(f"games must be positive, got {games}")
    p_a = wins_a / games
    p_b = wins_b / games
    variance = (p_a * (1 - p_a) + p_b * (1 - p_b) + 2 * p_a * p_b) / games
    z = z_for(level)
    spread = z * math.sqrt(variance)
    difference = p_a - p_b
    return Interval(
        estimate=difference, low=difference - spread, high=difference + spread, level=level
    )


def _percentile(sorted_values: Sequence[float], fraction: float) -> float:
    """Linear-interpolated percentile of an already sorted sequence."""
    if not sorted_values:
        raise ValueError("empty sample")
    if fraction <= 0:
        return sorted_values[0]
    if fraction >= 1:
        return sorted_values[-1]
    position = fraction * (len(sorted_values) - 1)
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return sorted_values[lower]
    weight = position - lower
    return sorted_values[lower] * (1 - weight) + sorted_values[upper] * weight


def bca_bootstrap(
    sample: Sequence[float],
    statistic: Callable[[Sequence[float]], float],
    *,
    resamples: int = 10_000,
    level: float = 0.95,
    seed: int,
) -> Interval:
    """Bias-corrected and accelerated bootstrap CI (SQ-2, SQ-3).

    ``seed`` is required, not optional. NF-7 makes every published interval
    reproducible from ``analysis_seed`` and ``bootstrap_B``, and a default seed
    is how that quietly stops being true.

    The acceleration comes from the jackknife, which is O(n) statistic
    evaluations; for the per-game samples this is applied to that is the
    cheaper half of the computation.
    """
    values = list(sample)
    n = len(values)
    if n < 2:
        raise ValueError(f"BCa needs at least 2 observations, got {n}")
    if resamples < 100:
        raise ValueError(f"resamples must be at least 100, got {resamples}")

    observed = statistic(values)
    rng = random.Random(seed)
    replicates: list[float] = []
    for _ in range(resamples):
        draw = [values[rng.randrange(n)] for _ in range(n)]
        replicates.append(statistic(draw))
    replicates.sort()

    # Bias correction: how far the replicate median sits from the observed
    # value, on the normal scale.
    below = sum(1 for value in replicates if value < observed)
    if below == 0 or below == resamples:
        # Degenerate: the statistic is constant across replicates. Fall back to
        # the percentile interval rather than dividing by zero.
        alpha = (1 - level) / 2
        return Interval(
            estimate=observed,
            low=_percentile(replicates, alpha),
            high=_percentile(replicates, 1 - alpha),
            level=level,
        )
    z0 = _NORMAL.inv_cdf(below / resamples)

    # Acceleration from the jackknife skewness.
    jackknife = [statistic(values[:i] + values[i + 1 :]) for i in range(n)]
    mean_jack = sum(jackknife) / n
    deviations = [mean_jack - value for value in jackknife]
    numerator = sum(d**3 for d in deviations)
    denominator = 6 * (sum(d * d for d in deviations) ** 1.5)
    acceleration = numerator / denominator if denominator else 0.0

    z_alpha = z_for(level)
    lower_fraction = _NORMAL.cdf(
        z0 + (z0 - z_alpha) / (1 - acceleration * (z0 - z_alpha))
    )
    upper_fraction = _NORMAL.cdf(
        z0 + (z0 + z_alpha) / (1 - acceleration * (z0 + z_alpha))
    )
    return Interval(
        estimate=observed,
        low=_percentile(replicates, lower_fraction),
        high=_percentile(replicates, upper_fraction),
        level=level,
    )


def bca_two_sample(
    sample_a: Sequence[float],
    sample_b: Sequence[float],
    statistic: Callable[[Sequence[float], Sequence[float]], float],
    *,
    resamples: int = 1_000,
    level: float = 0.95,
    seed: int,
    jackknife_groups: int = 100,
) -> Interval:
    """BCa for a two-sample contrast — a difference or a ratio between arms.

    Not expressible through :func:`bca_bootstrap`. Concatenating the arms and
    resampling the result mixes them in every draw, which produces the
    *permutation null* rather than a confidence interval: the point estimate
    lands outside its own interval, which is how this was caught. Each arm has
    to be resampled independently, because each arm is its own population.

    **Grouped jackknife.** Textbook BCa jackknifes one observation at a time —
    O(n) statistic evaluations, each O(n). At the confirmatory sample sizes
    (250k games per arm) that is 10^11 operations and simply cannot be run.
    The acceleration is therefore estimated by deleting *groups* of
    consecutive observations, the standard delete-d construction. With
    ``jackknife_groups`` at 100 the cost drops to 100 evaluations while the
    skewness it measures is unchanged — the grouping is a variance-reduction
    device, not an approximation of a different quantity.
    """
    values_a, values_b = list(sample_a), list(sample_b)
    n_a, n_b = len(values_a), len(values_b)
    if n_a < 2 or n_b < 2:
        raise ValueError(f"BCa needs at least 2 observations per arm, got {n_a}/{n_b}")
    if resamples < 100:
        raise ValueError(f"resamples must be at least 100, got {resamples}")

    observed = statistic(values_a, values_b)
    rng = random.Random(seed)
    replicates = sorted(
        statistic(
            rng.choices(values_a, k=n_a),
            rng.choices(values_b, k=n_b),
        )
        for _ in range(resamples)
    )

    below = sum(1 for value in replicates if value < observed)
    if below == 0 or below == resamples:
        alpha = (1 - level) / 2
        return Interval(
            estimate=observed,
            low=_percentile(replicates, alpha),
            high=_percentile(replicates, 1 - alpha),
            level=level,
        )
    z0 = _NORMAL.inv_cdf(below / resamples)

    jackknife: list[float] = []
    for arm, (values, other, first) in enumerate(
        ((values_a, values_b, True), (values_b, values_a, False))
    ):
        groups = min(jackknife_groups, len(values))
        size = len(values) // groups
        for index in range(groups):
            start = index * size
            stop = len(values) if index == groups - 1 else start + size
            reduced = values[:start] + values[stop:]
            if len(reduced) < 2:
                continue
            jackknife.append(
                statistic(reduced, other) if first else statistic(other, reduced)
            )
        del arm

    if len(jackknife) < 2:
        acceleration = 0.0
    else:
        mean_jack = sum(jackknife) / len(jackknife)
        deviations = [mean_jack - value for value in jackknife]
        numerator = sum(d**3 for d in deviations)
        denominator = 6 * (sum(d * d for d in deviations) ** 1.5)
        acceleration = numerator / denominator if denominator else 0.0

    z_alpha = z_for(level)
    lower_fraction = _NORMAL.cdf(
        z0 + (z0 - z_alpha) / (1 - acceleration * (z0 - z_alpha))
    )
    upper_fraction = _NORMAL.cdf(
        z0 + (z0 + z_alpha) / (1 - acceleration * (z0 + z_alpha))
    )
    return Interval(
        estimate=observed,
        low=_percentile(replicates, lower_fraction),
        high=_percentile(replicates, upper_fraction),
        level=level,
    )


def coefficient_of_variation(values: Sequence[float]) -> float:
    """SD over mean. The scale-free dispersion measure SQ-3 makes primary."""
    n = len(values)
    if n < 2:
        raise ValueError("need at least 2 values")
    mean = sum(values) / n
    if mean == 0:
        raise ValueError("coefficient of variation is undefined at mean zero")
    variance = sum((value - mean) ** 2 for value in values) / (n - 1)
    return math.sqrt(variance) / mean


def cv_ratio(treatment: Sequence[float], control: Sequence[float]) -> float:
    """The RQ-1 primary estimand (SQ-3, D-16).

    Deliberately not the raw variance ratio: a pure +10% location shift at
    constant CV produces a raw variance ratio of 1.21, whose CI excludes 1 with
    near-certainty at the pre-registered n — a length effect published as a
    dynamics effect.
    """
    return coefficient_of_variation(treatment) / coefficient_of_variation(control)

"""The §6.4 contrasts — the estimators the confirmatory families are made of.

§6.3 fixes the method per estimand class, and this module is where those
choices become code:

- proportions against a fixed reference use Wilson (SQ-1);
- two proportions from **different** cells are independent, so their
  difference uses the pooled two-proportion normal test;
- two proportions from the **same** cell are not — per-seat win indicators of
  one game are multinomial — so their difference uses the multinomial
  difference variance SQ-6 requires;
- means and the CV ratio use the BCa bootstrap over whole games (SQ-6's unit).

Every function returns an :class:`Estimate`, which carries the p-value Holm
needs alongside the interval a reader needs. Reporting one without the other
is how a threshold verdict loses its provenance.
"""

from __future__ import annotations

import math
from collections.abc import Sequence
from typing import NamedTuple

from madnlab.analysis.intervals import Interval, bca_two_sample, wilson, z_for

#: §6.4's minimum substantively interesting win-rate difference.
MIN_RELEVANT_PP = 0.5
#: §6.3's minimum practically relevant dispersion effect.
MIN_RELEVANT_CV_RATIO = 1.05


class Estimate(NamedTuple):
    """One contrast: point estimate, interval, and the p-value Holm reads."""

    label: str
    estimate: float
    interval: Interval
    p_value: float
    #: What the estimate counts, so a reader can see the sample behind it.
    n_a: int
    n_b: int
    #: Set when the estimator could not run — an empty arm, a cell with no
    #: checkpointed game. Never silently returned as zero.
    note: str = ""

    @property
    def excludes_zero(self) -> bool:
        return self.interval.excludes(0.0)

    @property
    def excludes_one(self) -> bool:
        return self.interval.excludes(1.0)


def _phi(z: float) -> float:
    """Standard normal CDF, via the error function."""
    return 0.5 * (1.0 + math.erf(z / math.sqrt(2.0)))


def _two_sided_p(z: float) -> float:
    return 2.0 * (1.0 - _phi(abs(z)))


def mean(values: Sequence[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def _variance(values: Sequence[float]) -> float:
    if len(values) < 2:
        return 0.0
    mu = mean(values)
    return sum((value - mu) ** 2 for value in values) / (len(values) - 1)


def cv(values: Sequence[float]) -> float:
    """Coefficient of variation — the scale-free dispersion measure of SQ-3."""
    mu = mean(values)
    return math.sqrt(_variance(values)) / mu if mu else 0.0


def proportion(successes: int, trials: int, *, level: float = 0.95) -> Interval:
    """A single proportion against a fixed reference (SQ-1)."""
    return wilson(successes, trials, level=level)


def proportion_difference(
    successes_a: int,
    trials_a: int,
    successes_b: int,
    trials_b: int,
    *,
    label: str,
    level: float = 0.95,
) -> Estimate:
    """Difference of two proportions from **independent** cells.

    Independent is the load-bearing word. Two arms of a factorial are separate
    games and this is correct for them; two seats of one cell are not, and
    :func:`seat_difference` is the estimator for that case (SQ-6).
    """
    if trials_a == 0 or trials_b == 0:
        return Estimate(label, 0.0, Interval(0.0, 0.0, 0.0, level), 1.0, trials_a, trials_b,
                        note="empty arm")
    p_a = successes_a / trials_a
    p_b = successes_b / trials_b
    difference = p_a - p_b
    # Unpooled SE for the interval, pooled for the test — the standard pairing:
    # the interval should not assume the null it is testing.
    se = math.sqrt(p_a * (1 - p_a) / trials_a + p_b * (1 - p_b) / trials_b)
    pooled = (successes_a + successes_b) / (trials_a + trials_b)
    se_null = math.sqrt(pooled * (1 - pooled) * (1 / trials_a + 1 / trials_b))
    z_crit = z_for(level)
    interval = Interval(difference, difference - z_crit * se, difference + z_crit * se, level)
    p_value = _two_sided_p(difference / se_null) if se_null > 0 else 1.0
    return Estimate(label, difference, interval, p_value, trials_a, trials_b)


def seat_difference(
    wins_a: int,
    wins_b: int,
    games: int,
    *,
    label: str,
    level: float = 0.95,
) -> Estimate:
    """Difference of two seats' win rates **within one cell** (SQ-6).

    The per-seat win indicators of a single game are multinomial: exactly one
    seat wins, so the two counts are negatively correlated. Two independent
    Wilson intervals understate the SE of their difference — 0.194 pp against
    the correct 0.224 pp at p = 0.25, n = 100k — and §6.3 fixes the
    multinomial form as the one to use.

        Var(p_a - p_b) = [p_a(1-p_a) + p_b(1-p_b) + 2 p_a p_b] / n
    """
    if games == 0:
        return Estimate(label, 0.0, Interval(0.0, 0.0, 0.0, level), 1.0, 0, 0, note="empty cell")
    p_a = wins_a / games
    p_b = wins_b / games
    difference = p_a - p_b
    variance = (p_a * (1 - p_a) + p_b * (1 - p_b) + 2 * p_a * p_b) / games
    se = math.sqrt(variance)
    z_crit = z_for(level)
    interval = Interval(difference, difference - z_crit * se, difference + z_crit * se, level)
    p_value = _two_sided_p(difference / se) if se > 0 else 1.0
    return Estimate(label, difference, interval, p_value, games, games)


def mean_difference(
    sample_a: Sequence[float],
    sample_b: Sequence[float],
    *,
    label: str,
    seed: int,
    resamples: int = 1_000,
    level: float = 0.95,
) -> Estimate:
    """Difference of means with a BCa interval (SQ-2).

    The bootstrap resamples whole games, which is SQ-6's unit of analysis. The
    p-value is Welch's rather than a bootstrap inversion: the interval and the
    test then answer the same question at the same n without needing 10x the
    resamples to resolve a tail.
    """
    if len(sample_a) < 2 or len(sample_b) < 2:
        return Estimate(label, 0.0, Interval(0.0, 0.0, 0.0, level), 1.0,
                        len(sample_a), len(sample_b), note="arm too small")
    difference = mean(sample_a) - mean(sample_b)

    def statistic(left: Sequence[float], right: Sequence[float]) -> float:
        return mean(left) - mean(right)

    try:
        interval = bca_two_sample(
            sample_a, sample_b, statistic, resamples=resamples, level=level, seed=seed
        )
    except (ValueError, ZeroDivisionError):
        interval = Interval(difference, difference, difference, level)
    se = math.sqrt(
        _variance(sample_a) / len(sample_a) + _variance(sample_b) / len(sample_b)
    )
    p_value = _two_sided_p(difference / se) if se > 0 else 1.0
    return Estimate(label, difference, interval, p_value, len(sample_a), len(sample_b))


def cv_ratio(
    sample_a: Sequence[float],
    sample_b: Sequence[float],
    *,
    label: str,
    seed: int,
    resamples: int = 1_000,
    level: float = 0.95,
) -> Estimate:
    """CV ratio with a BCa interval — the RQ-1 primary estimand (SQ-3).

    The ratio, not the raw variance ratio: a pure +10% location shift at
    constant CV produces a variance ratio of 1.21, which would read as a
    dynamics effect when nothing about the dispersion changed. The caller
    reports the mean ratio and variance ratio alongside so the two are
    visibly separated.

    The null here is 1, not 0. The p-value is computed on log scale, where the
    ratio's sampling distribution is far closer to normal than on the raw
    scale — a ratio bounded below by zero is skewed by construction.
    """
    if len(sample_a) < 2 or len(sample_b) < 2:
        return Estimate(label, 1.0, Interval(1.0, 1.0, 1.0, level), 1.0,
                        len(sample_a), len(sample_b), note="arm too small")
    cv_a, cv_b = cv(sample_a), cv(sample_b)
    if cv_b == 0:
        return Estimate(label, 1.0, Interval(1.0, 1.0, 1.0, level), 1.0,
                        len(sample_a), len(sample_b), note="reference CV is zero")
    ratio = cv_a / cv_b

    def statistic(left: Sequence[float], right: Sequence[float]) -> float:
        denominator = cv(right)
        return cv(left) / denominator if denominator else 1.0

    try:
        interval = bca_two_sample(
            sample_a, sample_b, statistic, resamples=resamples, level=level, seed=seed
        )
    except (ValueError, ZeroDivisionError):
        interval = Interval(ratio, ratio, ratio, level)
    # Log-scale SE implied by the BCa interval, so the p-value and the
    # interval cannot disagree about where the null sits.
    if interval.low > 0 and interval.high > 0 and interval.high > interval.low:
        z_crit = z_for(level)
        se_log = (math.log(interval.high) - math.log(interval.low)) / (2 * z_crit)
        p_value = _two_sided_p(math.log(ratio) / se_log) if se_log > 0 else 1.0
    else:
        p_value = 1.0
    return Estimate(label, ratio, interval, p_value, len(sample_a), len(sample_b))


def variance_ratio(sample_a: Sequence[float], sample_b: Sequence[float]) -> float:
    """Reported beside the CV ratio so location and scale stay separated."""
    var_b = _variance(sample_b)
    return _variance(sample_a) / var_b if var_b else 0.0


def mean_ratio(sample_a: Sequence[float], sample_b: Sequence[float]) -> float:
    mean_b = mean(sample_b)
    return mean(sample_a) / mean_b if mean_b else 0.0


def predictability_skill(leader_wins: int, checkpointed: int, players: int) -> float:
    """``(accuracy - 1/k) / (1 - 1/k)`` — SQ-4's reportable accuracy form.

    Scaled so 0 is chance and 1 is perfect prediction whatever ``k`` is. Raw
    accuracy is not comparable across player counts: 1/2 is chance at two
    players and excellent at six.
    """
    if checkpointed == 0 or players < 2:
        return 0.0
    accuracy = leader_wins / checkpointed
    chance = 1.0 / players
    return (accuracy - chance) / (1.0 - chance)


def proportion_vs_reference(
    successes: int,
    trials: int,
    reference: float,
    *,
    label: str,
    level: float = 0.95,
) -> Estimate:
    """A single proportion against a **fixed** reference (SQ-1).

    The reference is a constant — 1/k is arithmetic, not an estimate — so it
    contributes no sampling variance. Routing this through
    :func:`proportion_difference` by passing the reference as a second sample
    of the same size treats it as if it did, and inflates the interval by a
    factor of sqrt(2). §6.3 names Wilson for exactly this case, and the
    interval is reported on the difference scale by shifting Wilson's.
    """
    if trials == 0:
        return Estimate(label, 0.0, Interval(0.0, 0.0, 0.0, level), 1.0, 0, 0,
                        note="empty cell")
    observed = successes / trials
    difference = observed - reference
    bounds = wilson(successes, trials, level=level)
    interval = Interval(
        difference, bounds.low - reference, bounds.high - reference, level
    )
    # The test is one-sample: the SE is evaluated under the null, where the
    # proportion is the reference itself.
    se_null = math.sqrt(reference * (1 - reference) / trials)
    p_value = _two_sided_p(difference / se_null) if se_null > 0 else 1.0
    return Estimate(label, difference, interval, p_value, trials, 0)


def difference_in_differences(
    a1: tuple[int, int],
    a0: tuple[int, int],
    b1: tuple[int, int],
    b0: tuple[int, int],
    *,
    label: str,
    level: float = 0.95,
) -> Estimate:
    """A 2x2 interaction on proportions: (a1 - a0) - (b1 - b0).

    Each argument is ``(successes, trials)``. The four cells are separate
    games, so the variances add.

    This is what an interaction contrast means, and getting it wrong is not
    subtle in its consequences but is invisible in its output: comparing two
    player counts at one rule level answers "does k change the win rate",
    whose answer is 1/2 against 1/6 and is arithmetic rather than a finding
    (D-77).
    """
    counts = (a1, a0, b1, b0)
    if any(trials == 0 for _, trials in counts):
        return Estimate(label, 0.0, Interval(0.0, 0.0, 0.0, level), 1.0, 0, 0,
                        note="empty arm")
    rates = [successes / trials for successes, trials in counts]
    estimate = (rates[0] - rates[1]) - (rates[2] - rates[3])
    variance = sum(
        rate * (1 - rate) / trials
        for rate, (_, trials) in zip(rates, counts, strict=True)
    )
    se = math.sqrt(variance)
    z_crit = z_for(level)
    interval = Interval(estimate, estimate - z_crit * se, estimate + z_crit * se, level)
    p_value = _two_sided_p(estimate / se) if se > 0 else 1.0
    total = sum(trials for _, trials in counts)
    return Estimate(label, estimate, interval, p_value, total, total)


def mean_difference_in_differences(
    a1: Sequence[float],
    a0: Sequence[float],
    b1: Sequence[float],
    b0: Sequence[float],
    *,
    label: str,
    level: float = 0.95,
) -> Estimate:
    """The same interaction on a battery metric, from four independent samples.

    Analytic rather than bootstrapped, unlike the two-arm contrasts. A
    difference of differences is a linear combination of four independent
    sample means; at §8's cell sizes its sampling distribution is normal well
    past the precision published here, and a four-arm BCa would cost four
    resample passes per replicate to reproduce the same interval. §6.3's SQ-2
    names BCa for a "difference between arms"; this is a difference between
    differences, and the deviation is recorded rather than assumed (D-77).
    """
    arms = (a1, a0, b1, b0)
    if any(len(arm) < 2 for arm in arms):
        return Estimate(label, 0.0, Interval(0.0, 0.0, 0.0, level), 1.0, 0, 0,
                        note="arm too small")
    means = [mean(arm) for arm in arms]
    estimate = (means[0] - means[1]) - (means[2] - means[3])
    se = math.sqrt(sum(_variance(arm) / len(arm) for arm in arms))
    z_crit = z_for(level)
    interval = Interval(estimate, estimate - z_crit * se, estimate + z_crit * se, level)
    p_value = _two_sided_p(estimate / se) if se > 0 else 1.0
    total = sum(len(arm) for arm in arms)
    return Estimate(label, estimate, interval, p_value, total, total)

"""Chi-square goodness of fit, for the AK-8b analytic calibration gate.

Implemented from the regularized upper incomplete gamma rather than pulled in
from SciPy, for the reason NF-7 gives: the analysis layer avoids BLAS-backed
dependencies so a published threshold verdict cannot flip between machines.
The implementation is verified against tabulated critical values in the test
suite rather than trusted.
"""

from __future__ import annotations

import math
from collections.abc import Sequence
from typing import NamedTuple

_MAX_ITERATIONS = 300
_EPSILON = 3e-14
_TINY = 1e-300


def _gamma_series(a: float, x: float) -> float:
    """Regularized lower incomplete gamma P(a, x) by series expansion."""
    term = 1.0 / a
    total = term
    for n in range(1, _MAX_ITERATIONS):
        term *= x / (a + n)
        total += term
        if abs(term) < abs(total) * _EPSILON:
            break
    return total * math.exp(-x + a * math.log(x) - math.lgamma(a))


def _gamma_continued_fraction(a: float, x: float) -> float:
    """Regularized upper incomplete gamma Q(a, x) by continued fraction."""
    b = x + 1.0 - a
    c = 1.0 / _TINY
    d = 1.0 / b
    h = d
    for i in range(1, _MAX_ITERATIONS):
        an = -i * (i - a)
        b += 2.0
        d = an * d + b
        if abs(d) < _TINY:
            d = _TINY
        c = b + an / c
        if abs(c) < _TINY:
            c = _TINY
        d = 1.0 / d
        delta = d * c
        h *= delta
        if abs(delta - 1.0) < _EPSILON:
            break
    return h * math.exp(-x + a * math.log(x) - math.lgamma(a))


def gamma_upper(a: float, x: float) -> float:
    """Regularized upper incomplete gamma Q(a, x) = 1 - P(a, x)."""
    if x < 0 or a <= 0:
        raise ValueError(f"invalid arguments a={a}, x={x}")
    if x == 0:
        return 1.0
    if x < a + 1.0:
        return 1.0 - _gamma_series(a, x)
    return _gamma_continued_fraction(a, x)


def chi2_sf(statistic: float, df: int) -> float:
    """Upper-tail probability of the chi-square distribution."""
    if df < 1:
        raise ValueError(f"df must be at least 1, got {df}")
    if statistic <= 0:
        return 1.0
    return gamma_upper(df / 2.0, statistic / 2.0)


class GoodnessOfFit(NamedTuple):
    statistic: float
    df: int
    p_value: float
    #: Bins whose standardized residual exceeds 3, so a failure names where it
    #: failed instead of only that it did.
    outlier_bins: tuple[int, ...]


def chi_square_test(
    observed: Sequence[int], expected: Sequence[float], estimated_parameters: int = 0
) -> GoodnessOfFit:
    """Pearson chi-square against a fully specified expected distribution.

    ``estimated_parameters`` is 0 for AK-8b: the geometric distribution's ``p``
    comes from the rule set, not from the data, so no degree of freedom is
    spent on it. Getting that wrong would make the test conservative and hide
    exactly the dice or entry-logic bias the gate exists to catch.
    """
    if len(observed) != len(expected):
        raise ValueError(f"{len(observed)} bins against {len(expected)} expectations")
    if len(observed) < 2:
        raise ValueError("need at least 2 bins")
    if any(value <= 0 for value in expected):
        raise ValueError("every expected count must be positive")

    statistic = 0.0
    outliers: list[int] = []
    for index, (o, e) in enumerate(zip(observed, expected, strict=True)):
        residual = (o - e) / math.sqrt(e)
        statistic += residual * residual
        if abs(residual) > 3:
            outliers.append(index)
    df = len(observed) - 1 - estimated_parameters
    return GoodnessOfFit(
        statistic=statistic,
        df=df,
        p_value=chi2_sf(statistic, df),
        outlier_bins=tuple(outliers),
    )


def geometric_pmf(p: float, k: int) -> float:
    """P(X = k) for the number of trials until the first success, k >= 1."""
    if not 0 < p <= 1:
        raise ValueError(f"p must be in (0, 1], got {p}")
    if k < 1:
        raise ValueError(f"k must be at least 1, got {k}")
    return (1 - p) ** (k - 1) * p


def geometric_expectations(p: float, bins: int, trials: int) -> list[float]:
    """Expected counts for turn counts ``1..bins``, with the tail folded in.

    The last bin absorbs ``P(X > bins)`` so the expectations sum to ``trials``
    exactly; leaving the tail out would make the statistic depend on where the
    binning stopped.
    """
    head = [geometric_pmf(p, k) * trials for k in range(1, bins)]
    return [*head, trials - sum(head)]

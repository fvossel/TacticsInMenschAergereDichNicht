"""AK-8 — estimator calibration.

Wilson and BCa must achieve nominal coverage on synthetic data with known
truth, and Holm must reproduce a hand-worked example.

This is the gate §11 originally lacked entirely: every AK-1..AK-7 criterion
tested the simulated games, and §1 says the games are the by-product. A
mis-implemented interval would have passed all of them and gone straight into
``docs/results.md``.
"""

from __future__ import annotations

import math
import random

import pytest

from madnlab.analysis.config import AnalysisConfig, environment, manifest
from madnlab.analysis.gof import chi2_sf, chi_square_test, geometric_expectations
from madnlab.analysis.intervals import (
    bca_bootstrap,
    coefficient_of_variation,
    cv_ratio,
    multinomial_difference_ci,
    wilson,
    z_for,
)
from madnlab.analysis.multiplicity import (
    CONFIRMATORY_TOTAL,
    FAMILIES,
    INTERACTION_FAMILIES,
    Hypothesis,
    family_hypotheses,
    family_size,
    first_threshold,
    holm,
)

# -- Wilson -------------------------------------------------------------------


def test_wilson_matches_a_hand_worked_value():
    """A textbook case, so the formula is pinned and not merely self-consistent."""
    interval = wilson(successes=25, trials=100, level=0.95)
    assert interval.estimate == 0.25
    # z = 1.959964, denominator = 1 + z²/n = 1.038415,
    # centre = (0.25 + z²/200) / denominator = 0.259250,
    # half-width = z·sqrt(0.1875/100 + z²/40000) / denominator = 0.083796.
    # The published Wilson interval for 25/100 is (0.1755, 0.3430).
    assert interval.low == pytest.approx(0.175452, abs=1e-5)
    assert interval.high == pytest.approx(0.343047, abs=1e-5)
    assert interval.estimate < (interval.low + interval.high) / 2, (
        "Wilson's centre is pulled toward 1/2, which is what distinguishes it "
        "from the Wald interval"
    )


def test_wilson_achieves_nominal_coverage():
    """The property the gate is actually about."""
    rng = random.Random(20260801)
    for true_p, trials in ((0.25, 200), (0.05, 400), (0.5, 100)):
        covered = 0
        replications = 4000
        for _ in range(replications):
            successes = sum(1 for _ in range(trials) if rng.random() < true_p)
            if not wilson(successes, trials, level=0.95).excludes(true_p):
                covered += 1
        rate = covered / replications
        # Monte-Carlo error at 4000 replications is ~0.35 pp; Wilson is known
        # to be slightly conservative, so the band is asymmetric on purpose.
        assert 0.93 <= rate <= 0.98, f"p={true_p} n={trials} coverage {rate:.3f}"


def test_z_for_matches_tabulated_critical_values():
    assert z_for(0.95) == pytest.approx(1.959964, abs=1e-5)
    assert z_for(0.99) == pytest.approx(2.575829, abs=1e-5)
    assert z_for(0.999) == pytest.approx(3.290527, abs=1e-5)
    with pytest.raises(ValueError):
        z_for(1.0)


# -- the multinomial difference (SQ-6) ---------------------------------------


def test_multinomial_difference_is_wider_than_two_independent_wilsons():
    """§6.3's stated arithmetic: 0.224 pp against 0.194 pp at p=0.25, n=100k.

    Two independent Wilson intervals drop the covariance term, which makes the
    difference interval too narrow — the direction that manufactures false
    positives.
    """
    games = 100_000
    wins = games // 4
    correct_se = math.sqrt(
        (0.25 * 0.75 + 0.25 * 0.75 + 2 * 0.25 * 0.25) / games
    )
    naive_se = math.sqrt(2 * 0.25 * 0.75 / games)
    assert correct_se * 100 == pytest.approx(0.2236, abs=1e-3)
    assert naive_se * 100 == pytest.approx(0.1936, abs=1e-3)
    assert correct_se > naive_se

    interval = multinomial_difference_ci(wins, wins, games, level=0.95)
    assert interval.estimate == 0.0
    assert interval.half_width == pytest.approx(z_for(0.95) * correct_se, rel=1e-9)


# -- BCa ----------------------------------------------------------------------


def test_bca_achieves_nominal_coverage_on_a_known_mean():
    rng = random.Random(4242)
    true_mean = 3.0
    covered = 0
    replications = 300
    for replication in range(replications):
        sample = [rng.expovariate(1 / true_mean) for _ in range(120)]
        interval = bca_bootstrap(
            sample,
            lambda values: sum(values) / len(values),
            resamples=400,
            level=0.95,
            seed=replication,
        )
        if not interval.excludes(true_mean):
            covered += 1
    rate = covered / replications
    assert 0.88 <= rate <= 1.0, f"BCa coverage {rate:.3f}"


def test_bca_is_reproducible_from_its_seed_and_only_from_it():
    """NF-7: a published interval is reproducible, and its seed is required."""
    sample = [float(value) for value in range(1, 60)]
    mean = lambda values: sum(values) / len(values)  # noqa: E731
    first = bca_bootstrap(sample, mean, resamples=200, seed=7)
    assert first == bca_bootstrap(sample, mean, resamples=200, seed=7)
    assert first != bca_bootstrap(sample, mean, resamples=200, seed=8)
    with pytest.raises(TypeError):
        bca_bootstrap(sample, mean, resamples=200)  # type: ignore[call-arg]


def test_bca_rejects_a_sample_it_cannot_accelerate():
    with pytest.raises(ValueError, match="at least 2"):
        bca_bootstrap([1.0], lambda v: v[0], seed=1)
    with pytest.raises(ValueError, match="resamples"):
        bca_bootstrap([1.0, 2.0], lambda v: v[0], resamples=10, seed=1)


# -- dispersion (SQ-3, D-16) --------------------------------------------------


def test_cv_ratio_is_blind_to_a_pure_location_shift():
    """The reason D-16 made it primary over the raw variance ratio.

    A +10% shift at constant relative dispersion leaves the CV ratio at 1 while
    the raw variance ratio reads 1.21 — which at the pre-registered n would
    publish a length effect as a dynamics effect.
    """
    rng = random.Random(11)
    control = [rng.gauss(100, 20) for _ in range(4000)]
    shifted = [value * 1.1 for value in control]
    assert cv_ratio(shifted, control) == pytest.approx(1.0, abs=1e-9)

    var_control = sum((v - sum(control) / len(control)) ** 2 for v in control)
    var_shifted = sum((v - sum(shifted) / len(shifted)) ** 2 for v in shifted)
    assert var_shifted / var_control == pytest.approx(1.21, abs=1e-6)


def test_cv_ratio_detects_a_real_dispersion_change():
    rng = random.Random(12)
    control = [rng.gauss(100, 20) for _ in range(4000)]
    spread = [100 + (value - 100) * 1.5 for value in control]
    assert cv_ratio(spread, control) == pytest.approx(1.5, abs=0.02)
    assert coefficient_of_variation(control) == pytest.approx(0.2, abs=0.01)


# -- Holm ---------------------------------------------------------------------


def test_holm_reproduces_a_hand_worked_example():
    """m = 4, alpha = 0.05, p = (0.003, 0.013, 0.020, 0.700).

    ====  =======  =========================  =======
    step  p        threshold alpha/(m-i+1)    verdict
    ====  =======  =========================  =======
    1     0.003    0.05/4 = 0.01250           reject
    2     0.013    0.05/3 = 0.01667           reject
    3     0.020    0.05/2 = 0.02500           reject
    4     0.700    0.05/1 = 0.05000           stop
    ====  =======  =========================  =======

    Note that 0.013 and 0.020 would both fail a plain Bonferroni comparison
    against 0.0125; Holm's widening thresholds are what admits them, and that
    is the behaviour worth pinning.
    """
    hypotheses = [Hypothesis("RQ-X", "m", f"c{i}") for i in range(4)]
    results = holm([0.003, 0.013, 0.020, 0.700], hypotheses, alpha=0.05)
    assert [r.adjusted_alpha for r in results] == pytest.approx(
        [0.0125, 0.05 / 3, 0.025, 0.05]
    )
    assert [r.rejected for r in results] == [True, True, True, False]
    assert [r.step for r in results] == [1, 2, 3, 4]


def test_holm_is_monotone_a_failure_stops_everything_after_it():
    """The part a naive per-test comparison gets wrong."""
    hypotheses = [Hypothesis("RQ-X", "m", f"c{i}") for i in range(3)]
    # 0.030 fails at step 1 (0.05/3 = 0.0167), so 0.040 must not be rejected
    # even though it is below its own step-3 threshold of 0.05.
    results = holm([0.030, 0.040, 0.045], hypotheses, alpha=0.05)
    assert [r.rejected for r in results] == [False, False, False]


def test_the_confirmatory_families_still_add_up():
    """The declared total is the pre-registration; drift here is drift in the claim.

    The core families are enumerated contrast by contrast; the interaction
    families of §17 are declared as sizes, because their contrasts are the
    product of an axis list and a variant list and writing that product out
    twice is how two copies of it drift apart.
    """
    core = sum(family_size(name) for name in FAMILIES)
    assert core + sum(INTERACTION_FAMILIES.values()) == CONFIRMATORY_TOTAL, {
        n: family_size(n) for n in FAMILIES
    }
    assert family_size("RQ-1") == 8
    assert family_size("RQ-2") == 18
    assert family_size("RQ-3") == 4
    assert family_size("RQ-4") == 10
    assert family_size("RQ-5") == 8
    assert family_size("RQ-6") == 9
    assert INTERACTION_FAMILIES["RQ-7"] == 21 * 5
    for name in FAMILIES:
        assert len(family_hypotheses(name)) == family_size(name)
        assert len({h.contrast + h.metric for h in family_hypotheses(name)}) == family_size(name)


def test_first_thresholds_match_the_ledger():
    """D-59's table, which is what the sample sizes were derived from."""
    assert first_threshold("RQ-1") == pytest.approx(0.00625)
    assert first_threshold("RQ-2") == pytest.approx(0.05 / 18)
    assert first_threshold("RQ-3") == pytest.approx(0.0125)
    assert first_threshold("RQ-4") == pytest.approx(0.005)


# -- chi-square, which AK-8b depends on ---------------------------------------


def test_chi2_sf_matches_tabulated_critical_values():
    """The implementation is verified, not trusted (no SciPy by design)."""
    assert chi2_sf(3.841459, 1) == pytest.approx(0.05, abs=1e-6)
    assert chi2_sf(16.918978, 9) == pytest.approx(0.05, abs=1e-6)
    assert chi2_sf(27.877165, 9) == pytest.approx(0.001, abs=1e-6)
    assert chi2_sf(11.070498, 5) == pytest.approx(0.05, abs=1e-6)
    assert chi2_sf(0.0, 4) == 1.0


def test_chi_square_test_flags_the_bin_that_deviates():
    expected = [100.0] * 5
    observed = [100, 100, 160, 90, 50]
    result = chi_square_test(observed, expected)
    assert result.df == 4
    assert result.p_value < 0.001
    assert set(result.outlier_bins) == {2, 4}


def test_geometric_expectations_fold_the_tail_and_sum_exactly():
    expectations = geometric_expectations(p=1 - (5 / 6) ** 3, bins=10, trials=100_000)
    assert len(expectations) == 10
    assert sum(expectations) == pytest.approx(100_000, abs=1e-6)
    assert all(value > 0 for value in expectations)


# -- NF-7 manifest ------------------------------------------------------------


def test_analysis_seeds_are_derived_per_estimand(tmp_path):
    config = AnalysisConfig(
        campaign_dir=str(tmp_path), estimands=("a", "b"), analysis_seed=99
    )
    assert config.seed_for("a") != config.seed_for("b")
    assert config.seed_for("a") == config.seed_for("a")
    assert config.bootstrap_b == 10_000


def test_manifest_records_the_input_digest_and_environment(tmp_path):
    first = tmp_path / "summary.jsonl"
    first.write_text('{"a":1}\n', encoding="utf-8", newline="")
    config = AnalysisConfig(campaign_dir=str(tmp_path), estimands=("x",), analysis_seed=1)
    payload = manifest(config, [first])
    assert payload["input_digest"]
    assert payload["environment"]["engine_version"] == environment()["engine_version"]

    first.write_text('{"a":2}\n', encoding="utf-8", newline="")
    assert manifest(config, [first])["input_digest"] != payload["input_digest"]

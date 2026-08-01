"""AK-8b — analytic calibration against ground truth outside the engine.

Every other gate is a self-consistency check: rules against scenarios written
by the engine's own author, replay against the same engine, symmetry against
an identity that holds by construction. A uniform bias in the dice stream or
an off-by-one in the entry logic would pass all of them — AK-4 is structurally
blind to it because a uniform bias hits every seat equally.

This gate compares against a distribution the rules imply and the engine has
no say in: the number of turns until a seat brings out its first piece is
geometric with ``p = 1 - (5/6)^attempts``.
"""

from __future__ import annotations

from collections import Counter

import pytest

from madnlab.analysis.gof import chi_square_test, geometric_expectations
from madnlab.engine.geometry import SeatPattern
from madnlab.engine.rules import ColdStart, RuleSet
from madnlab.eventlog.events import MoveEvent, RollEvent
from madnlab.run.game import GameSpec, play_indexed_game

#: Enough for the chi-square to have power against a bias of a few tenths of a
#: percent without making the suite slow.
GAMES = 3000


def _turns_to_first_entry(events, seat: int) -> int | None:
    """Turns the seat took before its first ``enter`` move.

    A turn boundary is a roll with attempt number 1, so this reads the same
    turn structure D-10 defines without re-implementing it.
    """
    turns = 0
    for event in events:
        if isinstance(event, RollEvent) and event.seat == seat and event.attempt == 1:
            turns += 1
        elif isinstance(event, MoveEvent) and event.seat == seat and event.kind == "enter":
            return turns
    return None


@pytest.mark.parametrize(
    ("dreimal", "attempts"), [(False, 1), (True, 3)], ids=["one_attempt", "three_attempts"]
)
def test_turns_to_first_entry_matches_the_geometric_distribution(dreimal, attempts):
    """The distribution the rules imply, with no free parameter.

    ``p`` comes from the rule set, not from the data, so the chi-square spends
    no degree of freedom estimating it — getting that wrong would make the test
    conservative and hide the bias it exists to catch.

    Two players rather than one: ``occupied_seats`` keeps §2.4's floor of two
    (D-66), and a seat's first entry cannot be blocked by an opponent anyway —
    each seat has its own entry field, and an opponent standing on it is
    captured rather than blocking.
    """
    spec = GameSpec(
        cell_key=f"ak8b/entry/{attempts}",
        seats=4,
        players=2,
        seat_pattern=SeatPattern.OPPOSITE,
        rules=RuleSet(cold_start=ColdStart.STRICT, dreimal_wuerfeln=dreimal),
        agent_ids=("RANDOM", "RANDOM"),
        master_seed=20260801 + attempts,
    )
    observed_turns = []
    for index in range(GAMES):
        run = play_indexed_game(spec, index)
        turns = _turns_to_first_entry(run.events, seat=0)
        if turns is not None:
            observed_turns.append(turns)

    assert len(observed_turns) > GAMES * 0.99, "almost every game must reach an entry"

    p = 1 - (5 / 6) ** attempts
    bins = 10
    counts = Counter(min(value, bins) for value in observed_turns)
    observed = [counts.get(k, 0) for k in range(1, bins + 1)]
    expected = geometric_expectations(p, bins=bins, trials=len(observed_turns))

    result = chi_square_test(observed, expected)
    assert result.df == bins - 1
    assert result.p_value > 0.001, (
        f"turns-to-first-entry deviates from Geometric(p={p:.4f}): "
        f"chi2={result.statistic:.1f} df={result.df} p={result.p_value:.2e} "
        f"outlier bins {result.outlier_bins}\n"
        f"observed {observed}\nexpected {[round(v, 1) for v in expected]}"
    )

    mean = sum(observed_turns) / len(observed_turns)
    assert mean == pytest.approx(1 / p, rel=0.06), f"mean {mean:.3f} against {1 / p:.3f}"


def test_the_die_is_uniform():
    """A biased die would shift every metric and no other gate would notice."""
    spec = GameSpec(
        cell_key="ak8b/die",
        seats=4,
        players=4,
        seat_pattern=SeatPattern.ADJACENT,
        rules=RuleSet(),
        agent_ids=("RANDOM",) * 4,
        master_seed=555,
    )
    faces: Counter[int] = Counter()
    for index in range(400):
        for event in play_indexed_game(spec, index).events:
            if isinstance(event, RollEvent):
                faces[event.value] += 1

    total = sum(faces.values())
    assert total > 100_000, f"only {total} rolls, too few to have power"
    assert set(faces) == {1, 2, 3, 4, 5, 6}

    observed = [faces[face] for face in range(1, 7)]
    result = chi_square_test(observed, [total / 6] * 6)
    assert result.df == 5
    assert result.p_value > 0.001, (
        f"die-face distribution is not uniform: chi2={result.statistic:.1f} "
        f"p={result.p_value:.2e} counts={observed}"
    )


def test_the_gate_would_catch_a_biased_die():
    """A calibration gate that cannot fail is not a gate.

    Perturbs the observed counts by 1% on one face and asserts the test
    rejects, so the assertion above is known to have power at the sample size
    it actually runs at.
    """
    total = 120_000
    fair = [total // 6] * 6
    assert chi_square_test(fair, [total / 6] * 6).p_value > 0.5

    biased = list(fair)
    shift = int(total * 0.01)
    biased[5] += shift
    biased[0] -= shift
    assert chi_square_test(biased, [total / 6] * 6).p_value < 0.001

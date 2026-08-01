"""AK-4's trichotomy and the scope of the gate (D-29, D-72, D-74).

AK-4 had no tests. Both defects D-74 records survived a full campaign because
of it: the report line printed ``FAIL`` under an ``INCONCLUSIVE`` verdict, and
the gate applied to every cell rather than to the calibration cells §11 scopes
it to. Neither is visible to ruff or mypy, and neither changes any interval —
they only change what a reader and an exit code are told.
"""

from __future__ import annotations

import pytest

from madnlab.analysis.aggregate import (
    AK4_DELTA_PP,
    CellSummary,
    ak4,
    seats_exchangeable,
)


def cell(
    *,
    games: int,
    players: int,
    wins: dict[int, int],
    seats: int = 4,
    occupied: tuple[int, ...] | None = None,
    key: str = "test/cell",
) -> CellSummary:
    """A CellSummary carrying only what AK-4 reads."""
    return CellSummary(
        cell_key=key,
        games=games,
        seats=seats,
        players=players,
        occupied=occupied if occupied is not None else tuple(range(players)),
        wins_by_seat=wins,
        wins_by_turn_offset={},
        abandoned=0,
        stalemated=0,
        capture_forcing_offered=0,
        capture_forcing_violations=0,
        forced_extra_lap_offered=0,
        forced_extra_lap_violations=0,
        forced_extra_laps=0,
        mean_rounds_to_first_win=0.0,
        rounds_to_first_win=(),
        lead_changes_per_turn=(),
        checkpointed=0,
        comebacks=0,
        leader_at_50_won=0,
        metric_means={},
    )


def even_wins(games: int, players: int) -> dict[int, int]:
    return {seat: games // players for seat in range(players)}


# -- the trichotomy ---------------------------------------------------------


def test_underpowered_cell_is_inconclusive_not_failed() -> None:
    """n = 20,000 cannot resolve delta = 0.5 pp, whatever the data.

    This is the D-29 error pointed the other way: reporting it as FAIL would
    say "the seats are asymmetric" when the data says "n is too small".
    """
    result = ak4(cell(games=20_000, players=4, wins=even_wins(20_000, 4)))
    assert not result.conclusive
    assert result.verdict == "INCONCLUSIVE"
    assert not result.passed


def test_report_last_line_agrees_with_the_verdict() -> None:
    """The regression D-74 records.

    The report explained the cell was underpowered and that this is not
    evidence of asymmetry, then printed FAIL three lines below it. A reader
    trusts the last line.
    """
    result = ak4(cell(games=20_000, players=4, wins=even_wins(20_000, 4)))
    report = result.report()
    assert "UNDERPOWERED" in report
    assert report.splitlines()[-1].strip() == "INCONCLUSIVE"
    assert result.verdict in report


def test_symmetric_cell_at_adequate_n_passes() -> None:
    result = ak4(cell(games=400_000, players=4, wins=even_wins(400_000, 4)))
    assert result.conclusive
    assert result.verdict == "PASS"
    assert result.report().splitlines()[-1].strip() == "PASS"


def test_asymmetric_cell_at_adequate_n_fails() -> None:
    """One seat pushed well outside the margin must still be caught."""
    wins = {0: 104_000, 1: 100_000, 2: 98_000, 3: 98_000}
    result = ak4(cell(games=400_000, players=4, wins=wins))
    assert result.conclusive
    assert result.verdict == "FAIL"
    assert result.report().splitlines()[-1].strip() == "FAIL"


def test_conclusiveness_is_about_n_not_about_the_wins() -> None:
    """A wildly skewed small cell is still inconclusive, not failed."""
    wins = {0: 12_000, 1: 4_000, 2: 2_000, 3: 2_000}
    result = ak4(cell(games=20_000, players=4, wins=wins))
    assert not result.conclusive
    assert result.verdict == "INCONCLUSIVE"


def test_half_width_shrinks_below_delta_between_the_two_n() -> None:
    """The boundary the trichotomy turns on, stated as a fact about n."""
    small = ak4(cell(games=20_000, players=4, wins=even_wins(20_000, 4)))
    large = ak4(cell(games=400_000, players=4, wins=even_wins(400_000, 4)))
    assert small.half_width_pp > AK4_DELTA_PP > large.half_width_pp


# -- the scope of the gate (D-74) -------------------------------------------


@pytest.mark.parametrize(
    ("occupied", "seats", "agents", "expected"),
    [
        # Every seat occupied: rotationally symmetric by construction.
        ((0, 1, 2, 3), 4, ("RANDOM",) * 4, True),
        ((0, 1, 2, 3, 4, 5), 6, ("RANDOM",) * 6, True),
        # EX-5's spread arm: three players evenly spaced on the six-ring.
        ((0, 2, 4), 6, ("RANDOM",) * 3, True),
        # EX-5's adjacent arms: the gap breaks the symmetry, and that is the
        # research question rather than an engine fault (D-27).
        ((0, 1, 2), 4, ("RANDOM",) * 3, False),
        ((0, 1, 2), 6, ("RANDOM",) * 3, False),
        # Two players facing each other vs. sitting side by side.
        ((0, 2), 4, ("RANDOM",) * 2, True),
        ((0, 1), 4, ("RANDOM",) * 2, False),
        # A deviant policy: 1/k is the wrong reference, not a broken engine.
        ((0, 1, 2, 3), 4, ("SPREAD", "RANDOM", "RANDOM", "RANDOM"), False),
        # Both defects at once.
        ((0, 1, 2), 6, ("SPREAD", "RANDOM", "RANDOM"), False),
    ],
)
def test_seats_exchangeable(
    occupied: tuple[int, ...], seats: int, agents: tuple[str, ...], expected: bool
) -> None:
    assert seats_exchangeable(occupied, seats, agents) is expected


def test_the_calibration_cells_are_exchangeable() -> None:
    """EX-1 and EX-1b, the two cells §11 names, must be inside the gate."""
    assert seats_exchangeable((0, 1, 2, 3), 4, ("RANDOM",) * 4)
    assert seats_exchangeable((0, 1, 2, 3, 4, 5), 6, ("RANDOM",) * 6)


def test_missing_agents_does_not_silently_widen_the_gate() -> None:
    """An empty agent list means the config was unreadable.

    It has to resolve one way or the other; it resolves to "exchangeable" so
    a cell is never dropped from the gate by a missing file. A dropped cell
    is the failure mode that matters — it turns a real asymmetry into silence.
    """
    assert seats_exchangeable((0, 1, 2, 3), 4, ())

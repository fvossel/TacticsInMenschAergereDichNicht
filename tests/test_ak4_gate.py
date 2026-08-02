"""AK-4's trichotomy and the scope of the gate (D-29, D-72, D-74).

AK-4 resolves to ``PASS``, ``FAIL`` or ``INCONCLUSIVE``, and gates the run only
on the calibration cells §11 scopes it to; every other cell is still reported in
full but sets no exit code. Neither property changes an interval; they decide
what the report's reader and the exit code are told.
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
        metric_vars={},
    )


def even_wins(games: int, players: int) -> dict[int, int]:
    return {seat: games // players for seat in range(players)}


# -- the trichotomy ---------------------------------------------------------


def test_underpowered_cell_is_inconclusive_not_failed() -> None:
    """n = 20,000 cannot resolve delta = 0.5 pp, the equivalence margin (D-29).

    FAIL asserts that the seats are asymmetric; at this n the data supports only
    the weaker claim that n is too small, so the verdict is INCONCLUSIVE (D-72).
    """
    result = ak4(cell(games=20_000, players=4, wins=even_wins(20_000, 4)))
    assert not result.conclusive
    assert result.verdict == "INCONCLUSIVE"
    assert not result.passed


def test_report_last_line_agrees_with_the_verdict() -> None:
    """The last line of the report is the verdict a reader acts on."""
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
    """One seat well outside the margin resolves to FAIL at adequate n."""
    wins = {0: 104_000, 1: 100_000, 2: 98_000, 3: 98_000}
    result = ak4(cell(games=400_000, players=4, wins=wins))
    assert result.conclusive
    assert result.verdict == "FAIL"
    assert result.report().splitlines()[-1].strip() == "FAIL"


def test_conclusiveness_is_about_n_not_about_the_wins() -> None:
    """Skew in an underpowered cell yields INCONCLUSIVE, not FAIL."""
    wins = {0: 12_000, 1: 4_000, 2: 2_000, 3: 2_000}
    result = ak4(cell(games=20_000, players=4, wins=wins))
    assert not result.conclusive
    assert result.verdict == "INCONCLUSIVE"


def test_half_width_shrinks_below_delta_between_the_two_n() -> None:
    """The half-width crosses AK4_DELTA_PP between the two n; that is the boundary."""
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
        # EX-5's adjacent arms: the gap breaks the symmetry, which is the
        # research question rather than an engine fault (D-27).
        ((0, 1, 2), 4, ("RANDOM",) * 3, False),
        ((0, 1, 2), 6, ("RANDOM",) * 3, False),
        # Two players facing each other vs. sitting side by side.
        ((0, 2), 4, ("RANDOM",) * 2, True),
        ((0, 1), 4, ("RANDOM",) * 2, False),
        # A deviant policy: 1/k is the wrong reference, not a broken engine.
        ((0, 1, 2, 3), 4, ("SPREAD", "RANDOM", "RANDOM", "RANDOM"), False),
        # Both symmetry breakers at once.
        ((0, 1, 2), 6, ("SPREAD", "RANDOM", "RANDOM"), False),
    ],
)
def test_seats_exchangeable(
    occupied: tuple[int, ...], seats: int, agents: tuple[str, ...], expected: bool
) -> None:
    assert seats_exchangeable(occupied, seats, agents) is expected


def test_the_calibration_cells_are_exchangeable() -> None:
    """EX-1 and EX-1b, the two cells §11 names, lie inside the gate."""
    assert seats_exchangeable((0, 1, 2, 3), 4, ("RANDOM",) * 4)
    assert seats_exchangeable((0, 1, 2, 3, 4, 5), 6, ("RANDOM",) * 6)


def test_missing_agents_does_not_silently_widen_the_gate() -> None:
    """An empty agent list means the config was unreadable.

    The predicate resolves it to "exchangeable" so that an unreadable file never
    drops a cell from the gate: a dropped cell turns a real asymmetry into
    silence.
    """
    assert seats_exchangeable((0, 1, 2, 3), 4, ())

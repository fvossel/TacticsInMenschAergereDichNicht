"""Reading a campaign back, and the two gates that run over whole cells.

AK-4 is a seat-symmetry **equivalence** test, not a failure to reject. AK-5 is
a counter invariant summed over every row of every mandatory cell, which is
what makes it independent of the GM-5.1 priority direction and of how many
event logs were sampled (D-32).

Both are here rather than in the runner because they are analyses of a
finished campaign, and NF-7 puts analyses under their own reproducibility
contract.
"""

from __future__ import annotations

import gzip
import json
from collections.abc import Iterator, Sequence
from pathlib import Path
from typing import Any, NamedTuple

from madnlab.analysis.intervals import Interval, wilson
from madnlab.engine.geometry import SeatPattern, occupied_seats

#: AK-4's equivalence margin and level (D-29).
AK4_DELTA_PP = 0.5
AK4_LEVEL = 0.99


def read_rows(path: Path) -> Iterator[dict[str, Any]]:
    """Stream summary rows from ``summary.jsonl`` or ``summary.jsonl.gz``."""
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                yield json.loads(line)


class CellSummary(NamedTuple):
    """Aggregates for one cell, from its rows alone."""

    cell_key: str
    games: int
    seats: int
    players: int
    occupied: tuple[int, ...]
    wins_by_seat: dict[int, int]
    wins_by_turn_offset: dict[int, int]
    abandoned: int
    stalemated: int
    capture_forcing_offered: int
    capture_forcing_violations: int
    forced_extra_laps: int
    mean_rounds_to_first_win: float
    rounds_to_first_win: tuple[int, ...]


def summarize_cell(rows: Sequence[dict[str, Any]]) -> CellSummary:
    """Aggregate one cell's rows."""
    if not rows:
        raise ValueError("no rows")
    first = rows[0]
    seats = first["seats"]
    players = first["players"]

    # The occupied seats are a function of the configuration, not of the
    # results. Deriving them from the seats that happened to win would silently
    # drop a seat that won nothing — which is exactly the case AK-4 exists to
    # catch, and it would drop it from the test rather than failing it.
    seat_list = occupied_seats(seats, players, SeatPattern(first["seat_pattern"]))

    wins_by_seat: dict[int, int] = dict.fromkeys(seat_list, 0)
    wins_by_offset: dict[int, int] = dict.fromkeys(range(len(seat_list)), 0)
    lengths: list[int] = []
    abandoned = stalemated = offered = violations = laps = 0

    for row in rows:
        winner = row["winner"]
        wins_by_seat[winner] = wins_by_seat.get(winner, 0) + 1
        # Turn-order offset of the winner from the drawn starting seat (D-25),
        # counted over the occupied seats in play order rather than over raw
        # seat indices, so a partly filled board produces no phantom offsets.
        offset = (
            seat_list.index(winner) - seat_list.index(row["starting_seat"])
        ) % len(seat_list)
        wins_by_offset[offset] = wins_by_offset.get(offset, 0) + 1
        lengths.append(row["rounds_to_first_win"])
        abandoned += bool(row["abandoned"])
        stalemated += bool(row["stalemate"])
        offered += row["capture_forcing_offered"]
        violations += row["capture_forcing_violations"]
        laps += sum(row["extra_laps_by_seat"])

    return CellSummary(
        cell_key=first["cell_key"],
        games=len(rows),
        seats=seats,
        players=players,
        occupied=tuple(seat_list),
        wins_by_seat=wins_by_seat,
        wins_by_turn_offset=wins_by_offset,
        abandoned=abandoned,
        stalemated=stalemated,
        capture_forcing_offered=offered,
        capture_forcing_violations=violations,
        forced_extra_laps=laps,
        mean_rounds_to_first_win=sum(lengths) / len(lengths),
        rounds_to_first_win=tuple(lengths),
    )


class SeatVerdict(NamedTuple):
    seat: int
    wins: int
    rate: float
    interval: Interval
    deviation_pp: float
    within_margin: bool


class AK4Result(NamedTuple):
    cell_key: str
    games: int
    players: int
    delta_pp: float
    level: float
    seats: tuple[SeatVerdict, ...]
    passed: bool
    half_width_pp: float
    #: False when the CI half-width is not smaller than the margin, in
    #: which case the test cannot pass on any data and its verdict says
    #: nothing about symmetry (D-72).
    conclusive: bool

    @property
    def verdict(self) -> str:
        if not self.conclusive:
            return "INCONCLUSIVE"
        return "PASS" if self.passed else "FAIL"

    def report(self) -> str:
        slack = self.delta_pp - self.half_width_pp
        lines = [
            f"AK-4  {self.cell_key}  n={self.games:,}  k={self.players}  "
            f"delta={self.delta_pp} pp  level={self.level}",
            f"      {self.level:.0%} half-width {self.half_width_pp:.4f} pp, "
            f"margin leaves {slack:+.4f} pp of slack",
        ]
        if not self.conclusive:
            needed = self.games * (self.half_width_pp / (self.delta_pp * 0.6)) ** 2
            lines.append(
                f"      UNDERPOWERED: the half-width exceeds the margin, so the "
                f"equivalence test cannot pass on any data. This is not evidence "
                f"of asymmetry. Comfortable power needs about n = {needed:,.0f}."
            )
        for verdict in self.seats:
            # Under an inconclusive test a per-seat "FAIL" would be the same
            # confusion at seat scope: the interval is wider than the margin
            # for every seat, whatever the data (D-72).
            flag = (
                "wide"
                if not self.conclusive
                else ("ok  " if verdict.within_margin else "FAIL")
            )
            lines.append(
                f"      seat {verdict.seat}: {verdict.rate * 100:8.4f}%  "
                f"[{verdict.interval.low * 100:8.4f}, {verdict.interval.high * 100:8.4f}]  "
                f"dev {verdict.deviation_pp:+.4f} pp  {flag}"
            )
        # Through ``verdict``, not ``passed``: an inconclusive cell printing
        # "FAIL" here contradicts the UNDERPOWERED line three rows above it,
        # and this is the line a reader trusts (D-74).
        lines.append(f"      {self.verdict}")
        return "\n".join(lines)


def seats_exchangeable(
    occupied: Sequence[int], seats: int, agents: Sequence[str]
) -> bool:
    """Whether AK-4's null — every seat wins exactly 1/k — holds by construction.

    §11 scopes AK-4 to the *calibration* cells, and this is the property that
    makes a cell one. Two things must hold.

    The agents must be identical. In a deviant cell one seat plays a different
    policy on purpose, so 1/k is not the reference its win rate should be
    compared against — that comparison is RQ-3's estimand, not a gate.

    The occupied seats must be evenly spaced around the ring. Three players
    sitting adjacent on a six-seat board leave one of them a 24-field run
    containing no opponent entry field, and the resulting asymmetry is EX-5's
    research question rather than an engine fault (D-27, D-74).
    """
    if len(set(agents)) > 1:
        return False
    ordered = sorted(occupied)
    if len(ordered) < 2:
        return True
    gaps = {
        (ordered[(i + 1) % len(ordered)] - ordered[i]) % seats
        for i in range(len(ordered))
    }
    return len(gaps) == 1


def ak4(
    cell: CellSummary, delta_pp: float = AK4_DELTA_PP, level: float = AK4_LEVEL
) -> AK4Result:
    """Seat symmetry as an equivalence test (D-29).

    Passes when, for **every** seat, the two-sided CI for ``p_seat - 1/k`` lies
    entirely inside ``+/- delta``. That is the opposite of the original
    criterion, which passed on a failure to reject and therefore also passed on
    a cell too small to reject anything.

    The mirror error is just as easy to make, and this guards against it: when
    the half-width is not smaller than the margin the test cannot pass on *any*
    data, so its result is **inconclusive** rather than a failure. Reporting
    that as FAIL would confuse "n is too small" with "the seats are asymmetric"
    — which is the same conflation, pointed the other way (D-72).
    """
    reference = 1 / cell.players
    verdicts = []
    for seat in cell.occupied:
        wins = cell.wins_by_seat.get(seat, 0)
        interval = wilson(wins, cell.games, level=level)
        low_pp = (interval.low - reference) * 100
        high_pp = (interval.high - reference) * 100
        verdicts.append(
            SeatVerdict(
                seat=seat,
                wins=wins,
                rate=wins / cell.games,
                interval=interval,
                deviation_pp=(wins / cell.games - reference) * 100,
                within_margin=low_pp >= -delta_pp and high_pp <= delta_pp,
            )
        )
    half_width = (
        verdicts[0].interval.half_width * 100 if verdicts else float("nan")
    )
    conclusive = half_width < delta_pp
    return AK4Result(
        cell_key=cell.cell_key,
        games=cell.games,
        players=cell.players,
        delta_pp=delta_pp,
        level=level,
        seats=tuple(verdicts),
        passed=conclusive and all(verdict.within_margin for verdict in verdicts),
        half_width_pp=half_width,
        conclusive=conclusive,
    )


class AK5Result(NamedTuple):
    cell_key: str
    games: int
    offered: int
    violations: int
    passed: bool

    def report(self) -> str:
        return (
            f"AK-5  {self.cell_key}  n={self.games:,}  "
            f"capture obligations offered {self.offered:,}  "
            f"violations {self.violations}  "
            f"{'PASS' if self.passed else 'FAIL'}"
        )


def ak5(cell: CellSummary) -> AK5Result:
    """The capture-forcing invariant, summed over the whole cell (D-32).

    ``offered`` counts only decisions where the restriction actually applied —
    neither GM-5.1 exception in force — so the gate does not depend on which
    way D-9's lattice was decided. A cell that offers nothing is reported as
    such rather than passing quietly: a mandatory arm with zero obligations
    would mean the restriction never fired, which is a defect wearing a green
    badge.
    """
    return AK5Result(
        cell_key=cell.cell_key,
        games=cell.games,
        offered=cell.capture_forcing_offered,
        violations=cell.capture_forcing_violations,
        passed=cell.capture_forcing_violations == 0 and cell.capture_forcing_offered > 0,
    )


def starting_player_advantage(cell: CellSummary, level: float = 0.95) -> dict[int, Interval]:
    """Win rate by turn-order offset from the starting seat (D-25).

    EX-1's headline deliverable, which §6.2 originally had no field for. The
    marginal per-seat rate is 1/k by construction under balancing, so this is
    the estimand that is not fixed by symmetry.
    """
    return {
        offset: wilson(wins, cell.games, level=level)
        for offset, wins in sorted(cell.wins_by_turn_offset.items())
    }


def load_cells(path: Path) -> dict[str, CellSummary]:
    """Group a campaign's rows by cell and aggregate each."""
    grouped: dict[str, list[dict[str, Any]]] = {}
    for row in read_rows(path):
        grouped.setdefault(row["cell_key"], []).append(row)
    return {key: summarize_cell(rows) for key, rows in grouped.items()}

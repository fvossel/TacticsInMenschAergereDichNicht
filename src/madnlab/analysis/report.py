"""Rendering ``docs/results.md`` — the §8 consolidated report.

§14.4 is the constraint that shapes this file: *every* §6.2 metric for *every*
campaign cell is reported, significant or not, with its confirmatory or
descriptive label attached. That, together with the `prereg-v1` freeze, is what
prevents cherry-picking — not the size of the multiplicity correction. So the
battery table here is deliberately exhaustive and deliberately boring.

The confirmatory sections come first because they are the pre-registered
claims; everything after them is labelled as not error-controlled, in the
document rather than in a footnote a reader can miss.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

from madnlab.analysis.aggregate import (
    CellSummary,
    ak4,
    ak5,
    seats_exchangeable,
    starting_player_advantage,
)
from madnlab.analysis.estimands import Estimate
from madnlab.analysis.families import Dataset, FamilyResult, RQ1Verdict

#: The §6.2 battery, in report order. Keys are ``CellSummary.metric_means``.
BATTERY = (
    ("turns", "turns"),
    ("rounds", "rounds"),
    ("dice_rolls", "rolls"),
    ("rounds_to_first_win", "rounds→win"),
    ("captures_total", "captures"),
    ("captured_by_seat", "captured"),
    ("passes_by_seat", "passes"),
    ("entry_waits_by_seat", "entry waits"),
    ("lead_changes", "lead chg"),
    ("turns_without_leader", "no leader"),
    ("barriers_formed", "barriers"),
    ("barrier_turns", "barrier turns"),
    ("extra_laps_by_seat", "extra laps"),
    ("winner_rank_at_50", "rank@50"),
    ("winner_rank_at_75", "rank@75"),
    ("comeback_depth", "cb depth"),
    ("final_margin", "margin"),
    ("final_margin_norm", "margin norm"),
)


def _fmt(value: float) -> str:
    if value != value:  # NaN
        return "—"
    if abs(value) >= 1000:
        return f"{value:,.0f}"
    if abs(value) >= 10:
        return f"{value:.1f}"
    # Four decimals below 10: a CV ratio of 1.1450 and one of 1.1499 are
    # different findings, and two decimals hides the difference.
    return f"{value:.4f}"


def _p(value: float) -> str:
    """A p-value that underflowed to zero is not zero, and must not print as it.

    Double precision bottoms out around 1e-308 and the normal tail reaches it
    easily at these sample sizes. Printing "0.000e+00" would claim an exact
    zero, which no finite sample can produce.
    """
    if value <= 0.0:
        return "&lt;1e-300"
    if value < 1e-4:
        return f"{value:.2e}"
    return f"{value:.4f}"


def _estimate_row(estimate: Estimate, rejected: bool | None, alpha: float | None) -> str:
    verdict = "—" if rejected is None else ("**rejected**" if rejected else "not rejected")
    alpha_text = "—" if alpha is None else f"{alpha:.5f}"
    note = f" _{estimate.note}_" if estimate.note else ""
    return (
        f"| {estimate.label}{note} | {_fmt(estimate.estimate)} | "
        f"[{_fmt(estimate.interval.low)}, {_fmt(estimate.interval.high)}] | "
        f"{_p(estimate.p_value)} | {alpha_text} | {verdict} |"
    )


def family_section(result: FamilyResult) -> list[str]:
    """One family, with its Holm step-down shown rather than summarized."""
    # holm() writes its verdicts back into the original order, so index i of
    # result.holm is the verdict for estimate i. The step-down reordering is
    # internal to it and is reported per row as the adjusted alpha.
    lines = [
        f"### {result.family}",
        "",
        f"{len(result.estimates)} tests, Holm-corrected within the family at "
        "alpha = 0.05.",
        "",
        "| Contrast | Estimate | 95% CI | p | Holm alpha | Verdict |",
        "|---|---:|---|---:|---:|---|",
    ]
    for index, estimate in enumerate(result.estimates):
        holm_result = result.holm[index] if index < len(result.holm) else None
        lines.append(
            _estimate_row(
                estimate,
                holm_result.rejected if holm_result else None,
                holm_result.adjusted_alpha if holm_result else None,
            )
        )
    lines.append("")
    if result.unavailable:
        lines.extend(
            [
                "**Not evaluated.** These contrasts are declared in §6.4 and no "
                "cell in the dataset answers them. Listed rather than dropped, "
                "because a family reported as complete when it is not is a "
                "different claim:",
                "",
            ]
        )
        lines.extend(f"- `{item}`" for item in result.unavailable)
        lines.append("")
    rejected = sum(1 for r in result.holm if r.rejected)
    lines.append(
        f"**{rejected} of {len(result.holm)} rejected** after Holm correction."
    )
    lines.append("")
    return lines


def rq1_section(verdict: RQ1Verdict) -> list[str]:
    """§6.4's biconditional, with both conjuncts shown."""
    lines = [
        "### RQ-1 support criterion",
        "",
        "§6.4 states the criterion as a decidable biconditional: RQ-1 is "
        "supported **iff** (i) the lower bound of the 95% BCa CI on the CV "
        "ratio of `rounds_to_first_win` (mandatory ÷ optional) exceeds 1, "
        "**and** (ii) at least 2 of 3 dynamism conjuncts have Holm-adjusted "
        "CIs excluding zero in the dynamism direction.",
        "",
    ]
    lines.extend(f"- {item}" for item in verdict.detail)
    lines.extend(
        [
            "",
            f"Conjuncts satisfied: **{verdict.dynamism_conjuncts} of 3** "
            f"(2 required).",
            "",
            f"## RQ-1 is {'**SUPPORTED**' if verdict.supported else '**NOT SUPPORTED**'}",
            "",
        ]
    )
    if not verdict.supported:
        lines.extend(
            [
                "Reported as not supported, with every metric value published "
                "either way (§6.4). A failure to meet a pre-registered "
                "criterion is a result, not a reason to look for another "
                "criterion.",
                "",
            ]
        )
    return lines


def battery_table(cells: dict[str, CellSummary], confirmatory: set[str]) -> list[str]:
    """§14.4's all-results table: every metric, every cell, no selection."""
    header = "| Cell | label | n | " + " | ".join(name for _, name in BATTERY) + " |"
    divider = "|---|---|---:|" + "---:|" * len(BATTERY)
    lines = [header, divider]
    for key in sorted(cells):
        cell = cells[key]
        label = "conf" if key in confirmatory else "desc"
        values = " | ".join(
            _fmt(cell.metric_means.get(field, float("nan"))) for field, _ in BATTERY
        )
        lines.append(f"| `{key}` | {label} | {cell.games:,} | {values} |")
    return lines


def gates_table(cells: dict[str, CellSummary], agents: dict[str, tuple[str, ...]]) -> list[str]:
    """AK-4 and AK-5 per cell, with AK-4's scope stated per row."""
    lines = [
        "| Cell | AK-4 | gates | half-width pp | AK-5 capture | AK-5 extra-lap |",
        "|---|---|---|---:|---|---|",
    ]
    for key in sorted(cells):
        cell = cells[key]
        result = ak4(cell)
        exchangeable = seats_exchangeable(cell.occupied, cell.seats, agents.get(key, ()))
        capture = extra = "—"
        if cell.capture_forcing_offered:
            five = ak5(cell)
            capture = f"{five.offered:,} / {five.violations}"
            extra = f"{five.lap_offered:,} / {five.lap_violations}"
        lines.append(
            f"| `{key}` | {result.verdict} | {'yes' if exchangeable else 'no'} | "
            f"{result.half_width_pp:.4f} | {capture} | {extra} |"
        )
    return lines


def seat_advantage_table(cells: dict[str, CellSummary], keys: Sequence[str]) -> list[str]:
    lines = ["| Cell | offset | win rate | 95% CI |", "|---|---:|---:|---|"]
    for key in keys:
        if key not in cells:
            continue
        for offset, interval in starting_player_advantage(cells[key]).items():
            label = "starter" if offset == 0 else f"+{offset}"
            lines.append(
                f"| `{key}` | {label} | {interval.estimate * 100:.3f}% | "
                f"[{interval.low * 100:.3f}, {interval.high * 100:.3f}] |"
            )
    return lines


def render(
    data: Dataset,
    families: Sequence[FamilyResult],
    verdict: RQ1Verdict,
    *,
    confirmatory: set[str],
    provenance: dict[str, Any],
) -> str:
    """The whole document."""
    total_games = sum(cell.games for cell in data.cells.values())
    abandoned = sum(cell.abandoned for cell in data.cells.values())
    stalemated = sum(cell.stalemated for cell in data.cells.values())

    lines = [
        "# MadnLab results",
        "",
        "Measured effects of the optional rules and movement strategies of "
        "*Mensch ärgere Dich nicht*, against the pre-registration frozen at "
        f"`{provenance.get('prereg_version', 'prereg-v1')}`.",
        "",
        "| | |",
        "|---|---|",
        f"| Pre-registration | `{provenance.get('prereg_version', 'prereg-v1')}` |",
        f"| Engine | `{provenance.get('engine_version', '?')}` |",
        f"| Campaigns | {provenance.get('campaigns', '?')} |",
        f"| Cells | {len(data.cells):,} |",
        f"| Games | {total_games:,} |",
        f"| Analysis seed | `{provenance.get('analysis_seed', '?')}` |",
        f"| Bootstrap resamples | {provenance.get('resamples', '?'):,} |",
        "",
        "## 1. Reading this document",
        "",
        "Sections 2 and 3 are **confirmatory**: 40 hypotheses fixed in §6.4 "
        "before any campaign ran, Holm-corrected within each family. Section 5 "
        "is **descriptive** — computed, published, and explicitly not "
        "error-controlled. §14.4 requires every §6.2 metric of every cell to "
        "appear whether or not anything depends on it, which is why section 5 "
        "is long and unselective.",
        "",
        f"Game outcomes: **{abandoned:,} abandoned**, **{stalemated:,} "
        f"stalemated** out of {total_games:,}. Both are measured outcomes of "
        "the rule set (D-69, D-70), not errors; no estimand is published from "
        "a cell with a non-negligible rate without saying so.",
        "",
        "## 2. Confirmatory results",
        "",
    ]
    for result in families:
        lines.extend(family_section(result))
    lines.extend(rq1_section(verdict))

    lines.extend(
        [
            "## 3. Calibration and invariants",
            "",
            "AK-4 is a harness and geometry gate scoped to the calibration "
            "cells (§11, D-74). It is reported for every cell — a large "
            "non-calibration cell showing asymmetry beyond δ is something the "
            "project wants to hear about — but only cells whose seats are "
            "exchangeable by construction gate the run. `INCONCLUSIVE` means "
            "the interval is wider than the margin, so the test could not pass "
            "on any data; it is not evidence of asymmetry (D-72).",
            "",
        ]
    )
    lines.extend(gates_table(data.cells, data.agents))
    lines.extend(
        [
            "",
            "## 4. Starting-player advantage",
            "",
            "D-25's estimand, on the two calibration cells.",
            "",
        ]
    )
    lines.extend(
        seat_advantage_table(
            data.cells, ["ex1/4s4p/random/baseline", "ex1b/6s6p/random/baseline"]
        )
    )
    lines.extend(
        [
            "",
            "## 5. Full metric battery (descriptive)",
            "",
            "Every §6.2 metric for every cell, per §14.4. Per-seat fields are "
            "summed to a game total, which is the k-comparable form; the "
            "per-seat profiles are what the gates in section 3 read. "
            "`conf` marks a cell carrying a confirmatory contrast; `desc` "
            "marks everything else. **Nominal 95% intervals apply to this "
            "section and it is not error-controlled** — no claim in it has "
            "survived a multiplicity correction.",
            "",
        ]
    )
    lines.extend(battery_table(data.cells, confirmatory))
    lines.extend(
        [
            "",
            "---",
            "",
            "Generated by `madnlab report`. Every number is reproducible from "
            "the master seeds in `campaigns/*.json` and the analysis seed "
            "above (NF-6, NF-7).",
            "",
        ]
    )
    return "\n".join(lines)

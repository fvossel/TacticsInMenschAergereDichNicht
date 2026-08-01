"""The campaign runner CLI (§7.1, §7.2).

``madnlab run <config.json>`` plays every cell and writes the §7.2 outputs:
``summary.jsonl.gz`` per NF-6, and ``campaign.json`` with the resolved
configuration. Sealing is by ascending game index, never by shard completion
order, so the bytes are a function of the configuration alone (D-33).
"""

from __future__ import annotations

import argparse
import gzip
import json
import sys
import time
from pathlib import Path

from madnlab import ENGINE_VERSION
from madnlab.analysis import aggregate
from madnlab.analysis.config import AnalysisConfig, manifest, write_manifest
from madnlab.run.campaign import run_cell, summary_bytes
from madnlab.run.config import ConfigError, load, resolved_payload, total_games
from madnlab.run.counterbalance import describe
from madnlab.run.game import PREREG_VERSION


def _write_gzip(path: Path, payload: bytes) -> None:
    """Write gzip deterministically.

    ``mtime=0`` and a fixed compression level: the default embeds the current
    time in the header, which would make two runs of the same configuration
    differ in bytes and break AK-2 for no reason at all.
    """
    with gzip.GzipFile(filename="", mode="wb", fileobj=path.open("wb"), mtime=0) as handle:
        handle.write(payload)


def run_campaign(config_path: Path, output_dir: Path, workers: int) -> int:
    config = load(config_path)
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"campaign: {config.name}")
    print(f"engine:   {ENGINE_VERSION}")
    print(f"seed:     {config.master_seed}")
    print(f"cells:    {len(config.cells)}  games: {total_games(config):,}")
    print(f"workers:  {workers}\n")

    all_rows = []
    started = time.perf_counter()
    for spec, games in config.specs():
        cell_started = time.perf_counter()
        rows = run_cell(spec, games=games, workers=workers)
        elapsed = time.perf_counter() - cell_started
        abandoned = sum(1 for row in rows if row.abandoned)
        stalemated = sum(1 for row in rows if row.stalemate)
        print(
            f"  {spec.cell_key:<34} {games:>9,} games  "
            f"{elapsed:>7.1f}s  {games / elapsed:>7.1f}/s  "
            f"{describe(spec.balance())}"
            + (f"  ABANDONED {abandoned}" if abandoned else "")
            + (f"  STALEMATE {stalemated}" if stalemated else "")
        )
        all_rows.extend(rows)

    summary_path = output_dir / "summary.jsonl.gz"
    _write_gzip(summary_path, summary_bytes(all_rows))

    payload = resolved_payload(config)
    payload["engine_version"] = ENGINE_VERSION
    payload["rows"] = len(all_rows)
    (output_dir / "campaign.json").write_text(
        json.dumps(payload, ensure_ascii=True, separators=(",", ":"), sort_keys=True) + "\n",
        encoding="utf-8",
        newline="",
    )

    total_elapsed = time.perf_counter() - started
    print(
        f"\n{len(all_rows):,} rows in {total_elapsed:.1f}s "
        f"-> {summary_path.name} ({summary_path.stat().st_size:,} bytes)"
    )
    return 0


def analyse(campaign_dir: Path, analysis_seed: int) -> int:
    """Report the gates that run over whole cells: AK-4 and AK-5.

    Writes ``analysis.json`` beside the campaign (NF-7) so the verdict carries
    its seed, its resample count and the digest of the rows it was computed
    from — §6.4's rules are threshold rules, and a threshold verdict without a
    reproducible provenance is an opinion.
    """
    summary_path = campaign_dir / "summary.jsonl.gz"
    if not summary_path.exists():
        summary_path = campaign_dir / "summary.jsonl"
    cells = aggregate.load_cells(summary_path)

    # The agent assignment is not in the summary rows (D-22 fixes their key
    # set), so the gate's scope comes from the campaign config beside them.
    agents_by_cell: dict[str, list[str]] = {}
    config_path = campaign_dir / "campaign.json"
    if config_path.exists():
        written = json.loads(config_path.read_text(encoding="utf-8"))
        for entry in written.get("cells", []):
            agents_by_cell[str(entry["key"])] = [str(a) for a in entry.get("agents", [])]

    results: dict[str, object] = {}
    failed = False
    for key, cell in sorted(cells.items()):
        print(
            f"\n{key}: {cell.games:,} games, mean rounds to first win "
            f"{cell.mean_rounds_to_first_win:.1f}"
        )
        if cell.abandoned or cell.stalemated:
            print(f"  abandoned {cell.abandoned}  stalemated {cell.stalemated}")

        ak4 = aggregate.ak4(cell)
        print(ak4.report())
        # Two things keep a cell out of the gate, and neither suppresses its
        # numbers -- the report above is printed either way (D-72's descriptive
        # value stands).
        #
        # An inconclusive cell is not a failure: a cell too small to resolve
        # the margin says nothing about symmetry either way (D-72).
        #
        # A cell whose seats are not exchangeable by construction is not a
        # failure either: §11 scopes AK-4 to the calibration cells, and a
        # deviant policy or an uneven seating gap makes 1/k the wrong
        # reference rather than the engine wrong (D-74).
        exchangeable = aggregate.seats_exchangeable(
            cell.occupied, cell.seats, agents_by_cell.get(key, [])
        )
        gated = exchangeable and ak4.conclusive
        if not exchangeable:
            print("      not a calibration cell: descriptive only, does not gate")
        failed |= gated and not ak4.passed
        results[f"{key}/ak4"] = {
            "verdict": ak4.verdict,
            "gates": gated,
            "exchangeable": exchangeable,
            "conclusive": ak4.conclusive,
            "passed": ak4.passed,
            "half_width_pp": ak4.half_width_pp,
            "seats": [
                {"seat": v.seat, "rate": v.rate, "deviation_pp": v.deviation_pp,
                 "within_margin": v.within_margin}
                for v in ak4.seats
            ],
        }

        if cell.capture_forcing_offered or "mandatory" in key:
            ak5 = aggregate.ak5(cell)
            print(ak5.report())
            failed |= not ak5.passed
            results[f"{key}/ak5"] = {
                "passed": ak5.passed,
                "offered": ak5.offered,
                "violations": ak5.violations,
                # Both halves of §11's invariant are persisted, not just the
                # one that existed first: a manifest recording half a verdict
                # is what let AK-5 pass on half a check for four milestones
                # (D-75).
                "lap_offered": ak5.lap_offered,
                "lap_violations": ak5.lap_violations,
            }

        offsets = aggregate.starting_player_advantage(cell)
        print("      starting-player advantage, win rate by turn-order offset:")
        for offset, interval in offsets.items():
            label = "starter" if offset == 0 else f"+{offset}"
            print(
                f"        {label:>8}: {interval.estimate * 100:7.3f}%  "
                f"[{interval.low * 100:7.3f}, {interval.high * 100:7.3f}]"
            )
        results[f"{key}/starting_player_advantage"] = {
            str(offset): [i.estimate, i.low, i.high] for offset, i in offsets.items()
        }

    config = AnalysisConfig(
        campaign_dir=str(campaign_dir),
        estimands=("ak4", "ak5", "starting_player_advantage"),
        analysis_seed=analysis_seed,
    )
    write_manifest(
        campaign_dir / "analysis.json", manifest(config, [summary_path], results)
    )
    print(f"\n-> {(campaign_dir / 'analysis.json').name}")
    print("VERDICT:", "FAIL" if failed else "PASS")
    return 1 if failed else 0


def build_report(
    run_dirs: list[Path], out: Path, analysis_seed: int,
    resamples: int, workers: int = 1,
) -> int:
    """Run §6.4's four families over every campaign and write the §8 report."""
    from madnlab.analysis import families, report

    data = families.load_dataset(run_dirs)
    if not data.cells:
        print(f"no campaign data in {[str(d) for d in run_dirs]}", file=sys.stderr)
        return 2
    print(f"{len(data.cells)} cells, {sum(c.games for c in data.cells.values()):,} games")

    started = time.perf_counter()
    results = []
    for name, function in (
        ("RQ-1", families.rq1),
        ("RQ-2", families.rq2),
        ("RQ-3", families.rq3),
        ("RQ-4", families.rq4),
    ):
        family_started = time.perf_counter()
        kwargs = {"workers": workers} if name == "RQ-2" else {}
        result = function(data, seed=analysis_seed, resamples=resamples, **kwargs)
        rejected = sum(1 for r in result.holm if r.rejected)
        print(
            f"  {name}: {len(result.estimates)} tests, {rejected} rejected, "
            f"{len(result.unavailable)} unavailable "
            f"({time.perf_counter() - family_started:.1f}s)"
        )
        results.append(result)

    verdict = families.rq1_verdict(results[0])
    print(f"\nRQ-1: {'SUPPORTED' if verdict.supported else 'NOT SUPPORTED'}")
    for line in verdict.detail:
        print(f"  {line}")

    # A cell is confirmatory when a §6.4 contrast reads it. Derived from the
    # sample sizes §8 assigned rather than re-listed here, so the label cannot
    # drift from the plan that produced it.
    confirmatory = {
        key for key, cell in data.cells.items() if cell.games > 20_100
    }
    document = report.render(
        data,
        results,
        verdict,
        confirmatory=confirmatory,
        provenance={
            "prereg_version": PREREG_VERSION,
            "engine_version": ENGINE_VERSION,
            "campaigns": ", ".join(sorted(d.name for d in run_dirs)),
            "analysis_seed": analysis_seed,
            "resamples": resamples,
        },
    )
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(document, encoding="utf-8", newline="\n")
    print(
        f"\n-> {out} ({len(document):,} bytes, "
        f"{time.perf_counter() - started:.1f}s total)"
    )
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="madnlab", description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    run = sub.add_parser("run", help="run a campaign configuration")
    run.add_argument("config", type=Path)
    run.add_argument("--out", type=Path, required=True)
    run.add_argument("--workers", type=int, default=1)

    check = sub.add_parser("check", help="resolve a configuration without running it")
    check.add_argument("config", type=Path)

    analyse_cmd = sub.add_parser("analyse", help="run AK-4 and AK-5 over a campaign")
    analyse_cmd.add_argument("campaign_dir", type=Path)
    analyse_cmd.add_argument("--analysis-seed", type=int, default=20260801)

    report_cmd = sub.add_parser(
        "report", help="run the §6.4 families over every campaign and write results.md"
    )
    report_cmd.add_argument("run_dirs", type=Path, nargs="+")
    report_cmd.add_argument("--out", type=Path, required=True)
    report_cmd.add_argument("--analysis-seed", type=int, default=20260801)
    report_cmd.add_argument("--resamples", type=int, default=1_000)
    report_cmd.add_argument("--workers", type=int, default=1)

    args = parser.parse_args(argv)
    try:
        if args.command == "check":
            config = load(args.config)
            print(
                json.dumps(resolved_payload(config), indent=2, ensure_ascii=False)
            )
            print(f"\ntotal games: {total_games(config):,}", file=sys.stderr)
            return 0
        if args.command == "analyse":
            return analyse(args.campaign_dir, args.analysis_seed)
        if args.command == "report":
            return build_report(
                args.run_dirs, args.out, args.analysis_seed,
                args.resamples, args.workers,
            )
        return run_campaign(args.config, args.out, args.workers)
    except ConfigError as error:
        print(f"configuration error: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

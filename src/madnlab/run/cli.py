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
        # An inconclusive cell is not a failure: AK-4 is a calibration gate
        # (D-29) and a cell too small to resolve the margin says nothing about
        # symmetry either way (D-72).
        failed |= ak4.conclusive and not ak4.passed
        results[f"{key}/ak4"] = {
            "verdict": ak4.verdict,
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
        return run_campaign(args.config, args.out, args.workers)
    except ConfigError as error:
        print(f"configuration error: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

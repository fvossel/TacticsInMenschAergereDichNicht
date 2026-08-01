"""Build the AK-6 harness page.

AK-6 requires the UI to render a golden reference game — fixed seed, checked-in
log — correctly end to end from the built artifact opened off disk, with every
event steppable and the final state matching the summary row.

A `fetch` cannot be used to load the log: over `file://` the origin is opaque
and the request is blocked, which is the same constraint that makes D-43
require a single self-contained file. So the harness embeds the log the same
way the build embeds the script, and asserts inside the page.

Run from the repository root, after `npm run build`::

    .venv/Scripts/python.exe ui/build-ak6.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from madnlab.eventlog.replay import validate  # noqa: E402
from madnlab.eventlog.writer import write_log  # noqa: E402
from madnlab.engine.geometry import SeatPattern  # noqa: E402
from madnlab.engine.rules import CaptureMode, RuleSet  # noqa: E402
from madnlab.run.game import GameSpec, play_indexed_game  # noqa: E402

GOLDEN = {
    "golden-4seat": GameSpec(
        "golden/4s4p/mixed", 4, 4, SeatPattern.ADJACENT, RuleSet(barriers=True),
        ("RANDOM", "SPREAD", "FOCUS_FRONT", "GREEDY_CAPTURE"), 20260806,
    ),
    "golden-6seat": GameSpec(
        "golden/6s6p/extended", 6, 6, SeatPattern.ADJACENT,
        RuleSet(capture_mode=CaptureMode.MANDATORY_EXTENDED, barriers=True),
        ("SPREAD", "RANDOM", "FOCUS_FRONT", "FOCUS_REAR", "GREEDY_CAPTURE", "RANDOM"),
        20260807,
    ),
}

#: ``type="module"`` is required, not cosmetic. The built app script is a
#: module and therefore deferred, so a classic checker runs *before* it and
#: finds ``window.madnlabLoad`` undefined. Modules execute in document order,
#: which puts this after the app.
CHECKER = """
<script type="module">
(function () {
  const results = [];
  function check(name, actual, expected) {
    const ok = JSON.stringify(actual) === JSON.stringify(expected);
    results.push({ name, ok, actual, expected });
    return ok;
  }
  for (const golden of window.__GOLDEN__) {
    const label = golden.name;
    window.madnlabLoad(golden.log, label);

    const state0 = window.madnlabState();
    check(label + ": frame count == events + 1", state0.frames, golden.events + 1);
    check(label + ": opens at the first frame", state0.cursor, 0);

    // Every event must be steppable: walk the whole stream one frame at a
    // time through the same control the user clicks, not through an internal
    // shortcut.
    const next = document.getElementById("next");
    let steps = 0;
    while (window.madnlabState().cursor < golden.events) {
      next.click();
      steps += 1;
      if (steps > golden.events + 5) break;
    }
    check(label + ": stepped through every event", steps, golden.events);

    const final = window.madnlabState();
    check(label + ": final frame index", final.cursor, golden.events);
    check(label + ": final positions match the summary row", final.positions, golden.positions);
    check(label + ": finishing order matches ranks", final.finished, golden.finished);
    check(label + ": turn count matches", final.turns, golden.turns);
    check(label + ": capture count matches", final.captures, golden.captures);

    // Stepping back to the start must restore the opening position exactly.
    document.getElementById("first").click();
    check(label + ": rewinds to the opening position", window.madnlabState().positions, golden.opening);

    // The board renders as SVG for this geometry.
    document.getElementById("last").click();
    const svg = document.querySelector("#board-host svg");
    check(label + ": board rendered", svg !== null, true);
    check(
      label + ": every piece drawn",
      document.querySelectorAll("#board-host .piece").length,
      golden.seats * 4,
    );
  }
  window.__ak6 = { passed: results.every((r) => r.ok), results };
})();
</script>
"""


def main() -> int:
    dist = ROOT / "ui" / "dist" / "index.html"
    if not dist.exists():
        print("run `npm run build` in ui/ first", file=sys.stderr)
        return 2

    payload = []
    out_dir = ROOT / "ui" / "public" / "golden"
    out_dir.mkdir(parents=True, exist_ok=True)

    for name, spec in GOLDEN.items():
        run = min(
            (play_indexed_game(spec, index) for index in range(8)),
            key=lambda r: len(r.events),
        )
        if validate(run.header, run.events) is not None:
            print(f"{name}: replay mismatch, refusing to build a golden", file=sys.stderr)
            return 1

        path = out_dir / f"{name}.jsonl"
        with path.open("w", encoding="utf-8", newline="") as handle:
            write_log(handle, run.header, run.events)

        # The opening position, reconstructed the way the viewer does.
        opening = [0] * (spec.seats * 4)
        if str(spec.rules.cold_start) == "one_piece_out":
            for seat in spec.occupied():
                opening[seat * 4] = 1

        # The final positions the viewer must arrive at, taken from the engine
        # rather than from the viewer's own fold — otherwise the check would
        # compare the viewer against itself.
        final = list(opening)
        for event in run.events:
            kind = type(event).__name__
            if kind == "MoveEvent":
                final[event.piece] = event.to_pos
            elif kind == "CaptureEvent":
                final[event.victim_seat * 4 + event.victim_piece] = 0

        payload.append(
            {
                "name": name,
                "log": path.read_text(encoding="utf-8"),
                "events": len(run.events),
                "seats": spec.seats,
                "positions": final,
                "opening": opening,
                "finished": list(run.outcome.ranks[: len(run.outcome.ranks) - 1]),
                "turns": run.outcome.turns,
                "captures": run.outcome.captures_total,
            }
        )
        print(f"{name}: {len(run.events)} events, {run.outcome.turns} turns")

    html = dist.read_text(encoding="utf-8")
    embed = (
        "<script>window.__GOLDEN__ = "
        + json.dumps(payload, ensure_ascii=True)
        + ";</script>"
    )
    harness = html.replace("</body>", embed + CHECKER + "</body>")
    target = ROOT / "ui" / "dist" / "ak6.html"
    target.write_text(harness, encoding="utf-8", newline="")
    print(f"-> {target.relative_to(ROOT)} ({target.stat().st_size:,} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

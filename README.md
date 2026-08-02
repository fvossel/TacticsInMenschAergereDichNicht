# MadnLab

**A measurement engine for the optional rules and movement strategies of
*Mensch ärgere Dich nicht*** — the German Ludo variant.

[![Python](https://img.shields.io/badge/python-3.11%2B-blue)](pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Dependencies](https://img.shields.io/badge/runtime%20deps-none-lightgrey)](pyproject.toml)
[![Games](https://img.shields.io/badge/games%20played-99.7M-orange)](docs/results.md)

Everyone has a house rule and a theory about it. *Schlagzwang* makes the game
more exciting. Spreading your pieces beats charging ahead. The player who
starts wins more often. This repository answers those questions the boring way:
pre-register the hypotheses, play a hundred million games, and report every
number whether or not it came out interesting.

The product is measurement series with uncertainty estimates. The simulated
games are a by-product.

---

## Contents

- [Results](#results) · [Quickstart](#quickstart) · [How it works](#how-it-works)
- [Experiment plan](#experiment-plan) · [Repository layout](#repository-layout)
- [Reproducing](#reproducing) · [Development](#development)
- [Rule baseline](#rule-baseline) · [Scope](#scope) · [Notation](#notation)

---

## Results

| | |
|---|---|
| **Games** | 99,690,710 |
| **Cells** | 533 |
| **Hypotheses** | 582 pre-registered, 577 evaluable |
| **Rejected** | 316, after Holm correction within eleven families |
| **Abandoned / stalemated games** | 0 / 0 |

Full report: **[docs/results.md](docs/results.md)** — all 582 hypotheses with
estimate, confidence interval, p-value and Holm threshold, the per-cell
calibration gates, the seat profiles, and every pre-registered metric of all 533
cells, significant or not.

| | Question | Tests | Rejected |
|---|---|---:|---:|
| **RQ-1** | Does mandatory capture make games more dynamic? | 8 | 7 |
| **RQ-2** | Do the optional rules move win rate or game length? | 18 | 10 |
| **RQ-3** | Does any movement strategy beat random? | 4 | **0** |
| **RQ-4** | Do rules and strategies interact as specified? | 10 | 4 |
| **RQ-5** | Does where you sit change what you win? | 8 | 7 |
| **RQ-6** | Turn order, capture play, the middle seat | 9 | 6 |
| **RQ-7** | rule × rule | 100 | 41 |
| **RQ-8** | rule × strategy | 180 | 92 |
| **RQ-9** | rule × player count | 135 | 83 |
| **RQ-10** | strategy × player count | 60 | 46 |
| **RQ-11** | rule × seating | 45 | 20 |

"Rejected" means the null was rejected — the effect is there. It does **not**
mean the research question was answered yes: RQ-1 and RQ-5 are stated as
conjunctions, and both fail their support criterion despite rejecting 7 of 8.

### The largest measured effect was not a hypothesis: where you sit

Two adjacent players, both playing SPREAD, win **35.40 % against 64.60 %**. On
a symmetric board, with a fair die, that is a **29.20 pp** seat advantage. Seat
the same two opposite each other and it collapses to 0.62 pp.

The mechanism is the geometry. Entry fields sit ten apart on the 40-field
track, so two adjacent seats leave cyclic gaps of 10 and 30, and the player with
the 30-gap spends three quarters of the lap inside the stretch where the other
one's fresh pieces enter. The seating alone does not do it, though: under
RANDOM play the same arrangement gives 4.01 pp. SPREAD is what keeps pieces
distributed along the exposed stretch, so the geometry needs a strategy to
convert it.

### Mandatory capture does not make the game more dynamic

It does raise the dispersion of game length — CV ratio 1.1641, 95 % CI lower
bound 1.1595. But of the three conjuncts the pre-registration requires, only
one holds. Lead changes per turn move *significantly in the opposite
direction*: under *Schlagzwang* the lead changes **less** often. Games get
longer and more variable in length, not more eventful.

### No movement strategy beats random

SPREAD, FOCUS_FRONT and FOCUS_REAR all sit within ±0.3 pp of 1/k at 200,000
games per cell, against a design resolution of 0.19 pp. That is a result, not a
power failure: the study can see a fifth of a percentage point, and there is
nothing above it to find. GREEDY_CAPTURE, tested separately under both capture
modes, joins them.

### The rules move length, almost never win rate

`free_entry` — all four pieces start in the yard, but any roll may bring one
out — lengthens the game by **207.6 rounds**, by far the largest rule effect
measured. Mandatory capture adds 64.3, *dreimal würfeln* takes off 69.9. Of
nine win-rate contrasts, exactly one survives correction: `free_entry`, at
−0.25 pp. The rules decide how long you sit at the table, not who wins.

### Most of the signal is in the interactions

282 of the 316 rejections are interaction terms. Rules that look inert on their
own change what a strategy is worth, what the player count does, and how much
the seating matters. Single-factor testing would have missed nearly all of it.

<details>
<summary><b>Two results that contradicted the pre-registration</b></summary>

**The middle seat is an advantage.** Three players on a four-player board: the
pre-registration predicted the middle seat would be squeezed. It gains
**+0.82 pp** under RANDOM and **+5.73 pp** under SPREAD.

**RQ-5's negative control missed its margin by 0.056 pp.** The support criterion
requires the `opposite` seating to be equivalent to zero within ±1 pp. It came
back at +0.62 pp, CI [+0.18, +1.06] — outside the margin by less than a
twentieth of a percentage point of interval, so the family is scored NOT
SUPPORTED. Re-running that one cell at a fresh seed with three times the games
gave −0.11 pp, CI [−0.36, +0.14], p = 0.39: the opposite sign, and entirely
consistent with zero. The replication is reported beside the pre-registered
verdict and is not used to overturn it.

</details>

---

## Quickstart

Python 3.11 or newer. No runtime dependencies.

```bash
pip install -e ".[dev]"
```

Play a small campaign — 40,000 games, about a minute at eight workers:

```bash
madnlab run campaigns/ak5-smoke.json --out runs/smoke --workers 8
```

Check it against the calibration gates. This prints the per-seat win rates with
their intervals, the capture-forcing counters, and a PASS / FAIL / INCONCLUSIVE
verdict:

```bash
madnlab analyse runs/smoke
```

Resolve any campaign configuration without running it, to see the cells and the
game counts it would produce:

```bash
madnlab check campaigns/ex2.json
```

Building the hypothesis report needs the campaigns that back the families —
see [Reproducing](#reproducing).

Watch a game back in the browser:

```bash
cd ui && npm install && npm run build
```

That produces `ui/dist/index.html`: one self-contained file that opens from
`file://` with no server and no network.

---

## How it works

**Pre-registration.** The hypotheses, metrics, family structure and decision
rules were fixed before the campaigns ran, and frozen at the git tag
`prereg-v1`. Every campaign config and every summary row carries the
`prereg_version` it ran under. Every pre-registered metric is reported for every
cell regardless of outcome — which is why the report is long and unselective.

**Multiplicity.** Holm step-down within each research question's family, over
metrics × contrasts jointly. Holm's cost is nearly flat in family size, which is
what made exhaustive interaction testing affordable: going from 10 to 200 tests
in a family raises the required n per arm from 199,688 to 304,271.

**Estimators.** Stdlib only, no SciPy. Wilson intervals for a single proportion
against a fixed reference; a multinomial contrast variance for seat-to-seat
differences, because exactly one seat wins each game and two independent Wilson
intervals would understate the standard error; BCa bootstrap for everything
else, two-sample with a grouped jackknife where the contrast spans two arms.
The **game** is the independent unit — every bootstrap resamples whole games,
never seat records.

**Trichotomy.** A family's verdict is PASS, FAIL or INCONCLUSIVE. Failing to
reject is not evidence of equivalence, so where the claim is "no effect" the
criterion is an equivalence margin, not a non-significant p-value.

**Determinism.** A game's seed derives from `(master_seed, cell_key,
game_index)` and from nothing else — not the worker, not the shard, not the
machine. Worker count changes wall-clock and nothing else.

**Counterbalancing.** Each cell's requested game count is rounded up to a whole
balance block, so every arrangement × starting-seat combination runs equally
often. That rounding is why the plan requests 99,690,000 games and the runner
plays 99,690,710.

---

## Experiment plan

The plan lives in `campaigns/` as data, generated by `campaigns/generate.py`,
which asserts every builder's cell count before writing.

| Campaign | Purpose | Cells | Games |
|---|---|---:|---:|
| `ex1` | Calibration and seat symmetry, 4 seats | 1 | 400,000 |
| `ex1b` | Calibration, 6 seats | 1 | 400,002 |
| `ex2` | RQ-1 *Schlagzwang* | 36 | 1,410,045 |
| `ex3` | RQ-3 movement strategies | 64 | 1,820,296 |
| `ex4` | RQ-2 rule main effects, full admissible factorial | 168 | 6,720,000 |
| `ex5` | Seating geometry | 10 | 1,580,012 |
| `ex6` | RQ-4 interactions | 105 | 7,420,287 |
| `ex7` | RQ-5 seat exposure | 14 | 2,800,004 |
| `ex8` | RQ-6 turn order, capture play, middle seat | 6 | 1,500,004 |
| `ex9` | RQ-8 rule × strategy | 50 | 30,000,000 |
| `ex10` | RQ-9 rule × player count | 40 | 24,000,000 |
| `ex11` | RQ-10 strategy × player count | 16 | 9,600,060 |
| `ex12` | RQ-11 rule × seating | 20 | 12,000,000 |
| `ak5-smoke` | Capture-forcing counters over a whole cell | 2 | 40,000 |
| | | **533** | **99,690,710** |

`ex4`'s factorial does double duty: its seven axes crossed pairwise answer all
21 rule-pair interactions of RQ-7 without a single additional game.

Regenerate the configs:

```bash
python campaigns/generate.py
```

---

## Repository layout

```
src/madnlab/
  engine/     Board geometry, rules, legal moves, the game loop
  agents/     The five policies
  eventlog/   Canonical JSON event log, summary rows, replay validator
  analysis/   Intervals, multiplicity, estimators, family bindings, report
  run/        Campaign runner, counterbalancing, seeds, CLI
campaigns/    The experiment plan as data, plus its generator
ui/           TypeScript replay viewer
tests/        137 tests
docs/         The generated report
```

| Path | Notes |
|---|---|
| `src/madnlab/engine/` | A single `legal_moves` owns legality; nothing else decides what a player may do. |
| `src/madnlab/agents/` | Each policy consumes exactly one RNG draw per decision, deterministic ones included, so the die stream does not depend on which policy is seated. |
| `src/madnlab/analysis/` | Stdlib only. Pinning an environment is cheaper when no BLAS is linked. |
| `src/madnlab/run/` | Streaming writes: a summary row costs ~16.7 KB live, so cells are written and dropped rather than accumulated. `--shard i/n` splits a campaign across machines without touching the numbers. |
| `ui/` | Builds to one self-contained HTML file that works from `file://`. |
| `tests/` | Rule conformance, determinism, replay equivalence, gate scope, estimator checks, metric cross-validation. |

---

## Reproducing

Run a campaign:

```bash
madnlab run campaigns/ex2.json --out runs/ex2 --workers 48
```

Split it across machines — each shard writes its own summary, and the analysis
reads them all:

```bash
madnlab run campaigns/ex9.json --out runs/ex9-a --shard 0 --shards 4 --workers 48
```

Build the full report:

```bash
madnlab report runs/ex1 runs/ex2 runs/ex3 --out docs/results.md --workers 16
```

Run the calibration gates over a finished campaign — seat symmetry against the
1/k identity, and the capture-forcing counters:

```bash
madnlab analyse runs/ex1
```

This writes an `analysis.json` manifest into the campaign directory recording
the seeds, the resample count, the interpreter and platform, and a SHA-256 over
the inputs, then prints a PASS / FAIL / INCONCLUSIVE verdict.

Every number is a function of the master seeds in `campaigns/*.json` and the
analysis seed. Worker and shard count change wall-clock and nothing else: in the
runner because output seals by ascending game index rather than by completion
order, and in the analysis because each contrast's bootstrap seed derives from
its own identity rather than from execution order.

---

## Development

```bash
pytest              # 137 tests
ruff check .
mypy
```

All artifacts — code, comments, identifiers, commit messages, documentation, UI
text — are English.

---

## Rule baseline

The baseline is the official Schmidt Spiele rule set, pinned to a named pair of
editions: **Art. 49020/49021 (2006)** for structure — 2 to 6 players, board
geometry — and **Art. 51204 (2023)** for mechanical clauses absent from it.
Rule claims in the code carry the German source text and the edition they were
verified against.

Optional rules covered: capture mode (optional / mandatory / mandatory extended
to the home stretch), cold start (strict / one piece out / free entry), *dreimal
würfeln*, bonus roll after a quick entry, bonus-roll forfeiture, barriers, and
the no-jump rule inside the goal.

---

## Scope

Results are statements about the defined agent policies, not about human play.
Where a rule's effect is mediated by an agent's choice, the measured effect is a
bound set by that policy — and the direction of the bound is part of the
pre-registered estimand, not an afterthought.

The findings in `docs/results.md` marked descriptive carry no multiplicity
control and are published because the pre-registration requires every computed
number to appear. Anything there worth believing needs its own pre-registered
replication.

---

## Notation

Docstrings and the report reference the specification the study was built
against: `§n` for a spec section, `D-n` for a decision-ledger row, `AK-n` for an
acceptance criterion, `GM-n` for a game-model rule, `NF-n` for a non-functional
requirement, `RQ-n` for a research question. The specification and the decision
ledger are internal working documents and are not part of this repository. What
they constrain is visible here instead: the frozen `prereg-v1` tag, the
`prereg_version` field on every config and summary row, and the acceptance tests
in `tests/`.

---

## License

MIT — see [LICENSE](LICENSE).

# TacticsInMenschÄrgereDichNicht

**MadnLab** — a measurement engine for the question: do optional rules and
piece-movement strategies in *Mensch ärgere Dich nicht* (the German Ludo
variant) have statistically measurable effects, and how large are they?

The product is measurement series with uncertainty estimates. Simulated games
are a by-product.

## Status

Pre-implementation. The specification is written and pre-registered; no engine
code exists yet.

## Documents

| File | What it is |
|---|---|
| [docs/requirements.md](docs/requirements.md) | The specification and pre-registration (version 2). Board and rule model, agents, logging, metric battery, the 40 confirmatory hypotheses, the experiment plan, acceptance criteria. |
| [docs/decisions.md](docs/decisions.md) | The decision ledger — 59 rows. Every rule-ambiguity resolution and every measurement-relevant choice, each with its status: verified against the official rulebook, explicit project choice where the rulebook is silent, or implementation decision. |
| [docs/spec-review.md](docs/spec-review.md) | The clause-by-clause review that version 2 answers. Kept because the pre-registration claim rests on what was found and fixed before any data existed. |

## Rule baseline

The baseline is the official Schmidt Spiele rule set, pinned to a named pair of
editions: **Art. 49020/49021 (2006)** for structure (2–6 players, board
geometry) and **Art. 51204 (2023)** for mechanical clauses absent from it. Each
cross-edition adoption is recorded individually in the ledger. Rule claims
carry the German source text and the edition they were verified against.

## Pre-registration

The specification is frozen at the git tag `prereg-v1` before the first
campaign runs. Every campaign config and summary row records the
`prereg_version` it ran under; any later change to the metrics or the
experiment plan is an amendment with its own ledger row. All pre-registered
metrics are reported for every cell regardless of outcome.

## Scope note

Results are statements about the defined agent policies, not about human play.
For the flags whose effect is mediated by agent choice, the measured effect is
a bound set by the policy, and the direction of that bound is part of the
pre-registered estimand.

## Language

All artifacts — code, comments, identifiers, commits, documentation, UI text —
are English.

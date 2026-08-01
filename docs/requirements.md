# MadnLab — Requirements (version 2)

A measurement engine for the question: **do optional rules and piece-movement
strategies in *Mensch ärgere Dich nicht* (the German Ludo variant, "MADN"
below) have statistically measurable effects — and how large are they?**

The product is **measurement series with uncertainty estimates**; simulated
games are a by-product. Everything below serves that: the simulator makes the
games cheap, the logger makes them auditable, the web UI makes them
inspectable, and the statistics layer turns them into answers. This document
doubles as the pre-registration of the metrics and hypotheses: the metric
battery of §6 and the confirmatory hypothesis set of §6.4 are fixed *before*
any campaign runs, under the freeze and amendment rules of §14.

Conventions: all artifacts (code, comments, identifiers, commits, docs, UI
text) are English; determinism is a first-class requirement, not an
afterthought; every measurement-relevant shortcut gets a ledger row.

> **Version 2 changes.** Version 1 was reviewed clause by clause
> ([spec-review.md](spec-review.md)) and its rule claims were checked against
> the official Schmidt Spiele rulebook. Two baseline misidentifications were
> found and corrected (§2.3, §2.4). The statistical plan gained a confirmatory
> hypothesis set (§6.4) and §8's sample sizes were derived from it. Every
> decision, with its rationale and its source citation, is in
> [decisions.md](decisions.md), which is the authoritative ledger; this
> document states the decisions, the ledger explains them.

---

## 1. Research questions

Each question is stated with its operationalization — the concrete numbers
that will answer it. "Measurable" always means: effect size with a confidence
interval, not just a p-value. The confirmatory hypotheses that answer each
question are enumerated in §6.4.

- **RQ-1 — Mandatory capture and game dynamics.** Does the optional
  mandatory-capture rule ("Schlagzwang") increase the variance/dynamics of
  games? Operationalized as the metric battery of §6 compared between the
  `capture_mode = optional` and `capture_mode = mandatory` arms (and the
  `mandatory_extended` arm), primarily: dispersion of game length, capture
  events per game, lead changes per game, comeback rate, and mid-game winner
  predictability. The support criterion is stated as a decidable
  biconditional in §6.4.
- **RQ-2 — Optional rules from the variant list.** For each rule flag in
  §2.4: what is its **main effect** on the metric battery, including win
  rates? Each flag is measured against the baseline rule set of §2.3 with
  every other flag at its default, in the field of all-`RANDOM` agents.
- **RQ-3 — Movement strategies.** Does it matter whether a player advances
  all pieces evenly ("spread") or focuses on a single piece ("focus") — and
  within focus, whether the protagonist is the front-most or the rear-most
  piece? Operationalized as win rates in mixed fields against the
  random-agent control, seat-counterbalanced (§7.3).
- **RQ-4 — Interaction effects.** Which pairs (rule × rule, rule × strategy,
  strategy × player count, anything × board geometry) interact beyond their
  main effects? Includes the specific seating question: with 3 players on the
  4-seat board, is the middle seat measurably disadvantaged, and does moving 3
  players to every second seat of the 6-seat board remove the disadvantage?
  §8's EX-5 separates the seat-pattern effect from the board-geometry effect,
  which are confounded in the naive comparison.

### 1.1 Scope: results are bounded by the agent policies

Results are statements about the **defined agent policies of §3**, not about
human play. Human players mix heuristics, threaten, and make errors; the
simulator measures the pure policies. This is a feature — clean attribution —
but the attribution is clean *for the policy*, and for the choice-mediated
flags the policy sets the magnitude. The bound direction is therefore part of
the pre-registered estimand, not a post-hoc caveat, and is repeated beside
every affected number in `docs/results.md`:

- `capture_mode`: with capture-blind agents the baseline capture rate is the
  *incidental* rate, the lowest attainable, so `optional → mandatory` is an
  **upper bound** on the Schlagzwang effect. The `GREEDY_CAPTURE` control
  (§3.2) supplies the other end, turning the bound into a measured interval.
- `barriers`: with no barrier-aware policy, barriers form incidentally and
  dissolve at random, so the barrier main effect is a **lower bound**
  measuring mechanical blocking only.
- `goal_no_jump`: reachable only through canonical move order (§2.7), not
  through any policy that values it.

§2.4's flag table marks each flag choice-mediated or mechanical.

---

## 2. Board and game model

### 2.1 Geometry (GM-1)

Parameterized board with `seats ∈ {4, 6}`:

| | 4-seat board | 6-seat board |
|---|---|---|
| Ring track length | 40 | 48 |
| Start-field spacing | 10 | 8 |
| Yard ("B") fields per seat | 4 | 4 |
| Goal fields per seat | 4 | 4 |

Per seat: an entry field ("A", on the ring), a goal entry position (the ring
field directly before the seat's goal column), 4 goal fields ordered
innermost-last. Positions are pure functions of (seats, seat index) — no
hardcoded per-board tables beyond the two constants above.

Maximum progress per seat (§6.1 normalization): **170** on the 4-seat board,
**202** on the 6-seat board.

### 2.2 Seats vs. players (GM-2)

Player→seat assignment is explicit configuration; empty seats are allowed.
Named seat patterns:

- `adjacent` — players occupy seats 0..k-1 (the naive 3-on-4-board setup;
  seat 1 is the "middle seat": an opponent directly behind and the other
  opponent's frequently-occupied start area directly ahead).
- `spread` — players occupy every second seat (3 players on the 6-seat
  board: seats 0, 2, 4).
- `opposite` — 2 players on maximally distant seats.

**Defaults (D-11).** `seats = 4` for players ≤ 4, `seats = 6` for
players ∈ {5, 6}; `seat_pattern = adjacent` unless an §8 row states otherwise.
`(seats, seat_pattern, occupied_seats)` is part of every cell key and is
written into every summary row.

**Player-count effects are estimated within a fixed `seats` level (D-12).**
Because `players ≤ seats`, any 6-player cell must run on the 48-ring board, so
a naive player-count contrast mixes player count with board geometry. Any
published player-count statement replicates players ∈ {2, 3, 4} at
`seats = 6`, and the 6-player cell is reported only against 6-seat companions.

### 2.3 Base rules (GM-3)

**The baseline is a named pair of official Schmidt Spiele editions (D-50).**
"The Schmidt rulebook" is not one document; three official redactions differ
on mechanics that matter to an engine. The baseline is:

- **Art. 49020/49021, Standardausgabe (2006)** for structure — player count
  2–6 and the geometry of §2.1. It is the only official edition covering more
  than four players and therefore the only basis the 6-seat board has.
- **Art. 51204 (2023 revision)** for mechanical clauses absent from 49020.
  Each such adoption is marked ⁵¹ below and is a deliberate cross-edition
  choice, never presented as reading 49020.

| | players | exact fit on goal entry | no-legal-move fallback | 6 unusable → re-roll forfeited |
|---|---|---|---|---|
| 49020 (2006) | 2–6 | — | — | — |
| 49324 (2016) | 2–4 | ✓ | — | — |
| 51204 (2023) | 2–4 | ✓ | ✓ | ✓ |

Enumerated so every clause is testable. Clauses marked **[V]** were verified
against the official text with the German source quoted in
[decisions.md](decisions.md).

1. One standard d6; turn order clockwise by seat index; the starting player is
   chosen by the engine per configuration (default: uniformly at random from
   the seeded RNG; campaigns counterbalance it, §7.3).
2. **[V]** Setup: each player receives 4 pieces. **One piece stands on the own
   entry field (A), the remaining three in the yard (B).** A 6 is required to
   bring each of the remaining three onto the entry field.
   *„Einen Stein stellt er auf das Feld A seiner Farbe, die übrigen drei
   werden auf die gleichfarbigen B-Felder gesetzt."* This is the
   `cold_start = one_piece_out` configuration of §2.4 and it is the **default**
   — see the correction note at the end of this section.
3. Rolling a 6 grants one extra roll (after the move). The extra roll is an
   ordinary roll and chains normally on a further 6. The
   `bonus_roll_forfeited` flag (§2.4) models 51204's contrary clause.
4. **[V]** Entry-field clearing: while own pieces remain in the yard and an own
   piece stands on the own entry field, moving that piece away is forced
   whenever legal. *„Solange noch weitere Spielfiguren auf den B-Feldern auf
   ihren Spieleinsatz warten, darf keine eigene Figur auf dem A-Feld stehen
   bleiben."*
5. **[V]** On a 6 with pieces in the yard, entering is forced — **subject to
   clause 4, which the rulebook states as an express exception inside the
   6-rule itself**: *„Ist dieses Feld noch von einer anderen eigenen
   Spielfigur besetzt, muss diese Figur erst mit der „6" weitergezogen
   werden."* The priority is textual, not an artefact of clause ordering.
   The forced clearing move **consumes the 6** (D-52, a project choice — the
   rulebook is silent); the free follow-up roll of clause 3 still applies.
   If the entry-field occupant cannot legally move 6 forward, the ordinary
   forced entry applies instead.
6. Landing on a field occupied by an opponent piece captures it (back to its
   yard). Landing on an own piece is illegal (no stacking) — unless the
   `barriers` flag changes this (§2.6). The base rules say expressly
   *„Es herrscht aber kein Schlagzwang."*, which is why `capture_mode`
   defaults to `optional`.
7. Pieces are never captured inside goal columns; goal columns are private,
   and no piece may enter a foreign goal column.
8. **[V]** A piece passing its own goal entry moves into the goal column. Goal
   fields are counted individually when advancing. **Entry into the goal
   column requires a fitting roll**⁵¹ — *„In die 4 Zielfelder kann nur mit
   einem passenden Wurf hineingezogen werden."* Jumping over own pieces
   *inside* the goal column is **allowed** in the baseline — *„Spielfiguren
   können im Ziel übersprungen werden."* — and forbidden only by the
   `goal_no_jump` flag. A roll that would carry a piece already inside the
   goal column past the last goal field generates no move for that piece
   (D-54, a project choice — the rulebook is silent).
9. Moving is compulsory: if at least one legal move exists, one must be made.
   Fallback cascade⁵¹: if the selected piece cannot move, another own piece
   must be moved; if that is impossible, the turn passes.
10. **The three-attempts rule is NOT a base rule.** See the correction note.
11. Game end: default `game_end_mode = play_out` — the game continues until
    all but one player have brought all four pieces into the goal; finished
    players are skipped in the turn order. Ranks are the realized finishing
    order (the single unfinished player is last). A `first_winner` mode (stop
    at the first finisher, remaining ranks by total progress, ties reported)
    exists as a config value but is not used by the v1 campaigns.

> **Correction to version 1 (D-51, D-55).** Version 1 asserted two rules as
> "the Schmidt baseline" that are not in the base rules at all:
>
> - It called `cold_start = strict` (all four pieces in the yard) the Schmidt
>   baseline and `one_piece_out` "the common softened house setup". These were
>   **inverted**: `one_piece_out` is literally the official setup and `strict`
>   appears in no official edition.
> - It called the three-attempts rule "baseline, per Schmidt". In all three
>   editions „Dreimal würfeln" appears under **„Spielvarianten"**. It is also
>   a *post-capture recovery* rule — *„weil alle Figuren geschlagen wurden"* —
>   not "three tries to get your first piece out", and given clause 2 it
>   cannot fire on turn one at all.
>
> Version 1's premise that these two variants "coincide with the Schmidt
> baseline" is therefore withdrawn. Both are now ordinary measured axes.

### 2.4 Optional rules as configuration flags (GM-4)

Normalized into axes. Two of them are **nested**, not independent, and the
config validator rejects inadmissible combinations with a named error rather
than coercing them.

| Flag | Values (default bold) | Policy | Semantics |
|---|---|---|---|
| `cold_start` | **one_piece_out** / strict / free_entry | mechanical | one_piece_out: the official setup (GM-3.2) — one piece on the entry field, three in the yard, a 6 required for those. strict: all four pieces begin in the yard. free_entry: all pieces begin in the yard but any roll value may be used to enter; the roll is consumed, entering is an ordinary legal move, never forced (D-7). |
| `dreimal_wuerfeln` | **off** / on | mechanical | on: the official „Dreimal würfeln" variant — a player meeting the D-1 condition (no piece on the ring track **and** no goal piece movable by any value 1–6) rolls up to three times. Nested: never fires under `free_entry`. |
| `bonus_roll_after_quick_entry` | **false** / true | mechanical | If the player enters with the 1st or 2nd of the three attempts, one additional roll is granted, stacking with GM-3.3's grant. **Requires `dreimal_wuerfeln = on`.** |
| `bonus_roll_forfeited` | **false** / true | mechanical | true: 51204's clause *„Können die 6 Felder nicht gezogen werden, entfällt das erneute Würfeln."* — the GM-3.3 extra roll is forfeited when the 6 cannot be moved. A genuine difference between official redactions, modelled as an axis rather than decided silently. |
| `goal_no_jump` | **false** / true | choice-mediated | true: jumping over own pieces inside the goal column is forbidden, **and** the last piece coming home can only enter on the first goal field — both sentences of the official variant. |
| `capture_mode` | **optional** / mandatory / mandatory_extended | choice-mediated | See §2.5. |
| `barriers` | **false** / true | choice-mediated | See §2.6. |

Structural axes measured alongside: `seats` (4/6), `players` (2–6, ≤ seats),
`seat_pattern` (§2.2), plus the §3 strategy assignment per player. Engine
config keys that are not measured axes: `game_end_mode ∈ {play_out,
first_winner}` (default `play_out`), `capture_enforcement ∈ {enforce,
penalize}` (v1: `enforce` only).

The **Policy** column marks whether a flag's measured effect depends on agent
policy (§1.1). Choice-mediated flags carry a bound statement wherever they are
published.

### 2.5 Capture-mode semantics (GM-5)

- `optional` (baseline): capturing moves are legal moves like any other;
  agents choose freely.
- `mandatory` ("Schlagzwang"): if the roll admits at least one capturing move,
  the legal-move set is restricted to the capturing moves.
- `mandatory_extended`: additionally, a capture must be taken even when the
  capturing path passes the own goal entry — the piece then skips the goal and
  continues on the ring for another lap. Track moves past the own goal entry,
  otherwise impossible under GM-3.8, become legal-and-forced exactly when they
  capture.

**Priority lattice (GM-5.1, D-9).** The order is **entry-clearing > forced
entry > mandatory capture**. Resolution procedure:

1. If entry-clearing (GM-3.4) is in force and legal → the legal set is the
   clearing moves; the capture restriction does not apply.
2. Else, if the roll is a 6, pieces remain in the yard, and the entry move is
   legal → the legal set is the entry move; the capture restriction does not
   apply.
3. Else → if any capturing move exists, the legal set is exactly those moves.

Under `mandatory_extended` the forced extra lap is likewise subordinate to
steps 1 and 2. Because a correct mandatory-mode log therefore contains
decisions where a capture was offered and a non-capturing forced move was
taken, the AK-5 gate is formulated over engine counters rather than over
decisions (§11).

**Enforcement mode (GM-5.2):** `capture_enforcement ∈ {enforce, penalize}`.
v1 implements only `enforce`: illegal moves are filtered out of the legal-move
set. The penalty branch ("pusten") requires fallible agents and is out of
scope (§12); the enum exists from day one so logs never need a schema break.

### 2.6 Barrier semantics (GM-6)

The barriers variant is official in all three editions: *„Als Ausnahme zur
Grundregel dürfen zwei Spielfiguren einer Farbe auf einem Feld stehen."* Any
statement elsewhere that two pieces never share a field is true of the
Grundregeln only. With `barriers = true`:

1. Landing on a **ring-track** field occupied by exactly one own piece is
   legal (overriding GM-3.6) and forms a barrier of two pieces. Barriers exist
   only on ring-track fields; goal columns remain strictly one piece per field
   (D-34).
2. No piece of any player — including the owner's own third piece — may pass
   over or land on a barrier field. Moves whose path crosses a barrier are
   illegal.
3. Barrier pieces cannot be captured.
4. Barriers are broken by choice or by compulsion: moving either piece
   dissolves the barrier. GM-3.9 is unchanged — if the only legal moves involve
   barrier pieces, the barrier must be broken.
5. Corner cases are pinned in D-4: a barrier on the own entry field does not
   suspend entry-clearing; a barrier on a goal entry blocks passage for the
   owner too; a capture onto a *forming* barrier field is impossible, since
   forming requires the target to hold exactly one own piece.

### 2.7 Legality as the single source of truth (GM-7)

One pure, total function `legal_moves(state, roll) → ordered move list`
implements *all* of §2.3–§2.6, parameterized by the rule flags. The engine,
every agent, the replay validator, and the UI's move display all consume this
one function. No agent ever re-implements legality.

**Canonical move ordering (D-3):** goal moves first, then ring moves; within
each group by piece id ascending, then by target field ascending. Entry moves
sort as ring moves with target = the own entry field. This also fixes the
goal-entry preference of the §3 agents.

---

## 3. Agents (strategies)

### 3.1 Agent contract (ST-1)

An agent is a pure function `choose(state, roll, legal, rng) → move` where
`legal` is the non-empty list from GM-7 and `rng` is the agent's own seeded
stream, distinct from the dice stream (§5 NF-1). Agents are stateless in v1.
Every agent must be total (always returns an element of `legal`) and
deterministic given `(state, roll, agent seed)`.

**Draw discipline (D-37).** An agent consumes exactly one draw per decision,
including when `len(legal) == 1` and including for deterministic agents that
ignore the value. Without this, a later short-circuit optimization would
desynchronize a seat's stream and silently invalidate published logs while
AK-2 still passed.

**Selection key (D-43a).** All non-random agents rank pieces by
`track_progress(piece)` = §6.1 `progress` restricted to pieces **on the ring**;
pieces in the yard and in the goal column are excluded from the ranking.

### 3.2 The five v1 agents

| Id | Policy |
|---|---|
| `RANDOM` | Uniform choice over `legal`. The control arm for every comparison. |
| `SPREAD` | Advance all pieces evenly: prefer entering from the yard when an entry move is legal; otherwise move the legal piece with the **least** `track_progress`. Deterministic tie-break: lowest piece id, then canonical move order. |
| `FOCUS_FRONT` | Single-piece focus, protagonist = the **most advanced** own piece on the ring, recomputed every decision. If a protagonist move is legal, play it. Fallback: entry move if legal, else the legal move of the least-advanced other piece (keeps non-protagonists back). |
| `FOCUS_REAR` | Single-piece focus, protagonist = the **least advanced** own piece on the ring, recomputed every decision. If a protagonist move is legal, play it. Fallback: entry move if legal, else the legal move of the **most**-advanced other piece — non-protagonists are pushed ahead rather than bunched with the protagonist. |
| `GREEDY_CAPTURE` | If at least one capturing move is legal, choose uniformly among the capturing moves; otherwise choose uniformly over `legal`. Deliberately `RANDOM` plus a capture filter and nothing else, so the `RANDOM → GREEDY_CAPTURE` contrast isolates capture-seeking exactly. |

Notes fixed here so nobody "improves" them mid-campaign:

- `FOCUS_REAR` is written out in full rather than defined as "same policy as
  `FOCUS_FRONT`". Under the inherited fallback its primary rule would be
  almost identical to `SPREAD`, which would make RQ-3's headline sub-question
  a property of the definition rather than of the game (D-36).
- **Empty-protagonist branch:** if no own piece is on the ring, the focus
  agents fall through to the entry move if legal, else to the canonically
  first legal move. Goal-column moves are eligible as "other piece" moves,
  ranked after all ring moves.
- `RANDOM`, `SPREAD`, `FOCUS_FRONT` and `FOCUS_REAR` have no capture
  preference or avoidance. Under `capture_mode = optional`, captures happen
  only incidentally. That is by design — RQ-3 measures exactly the named
  policies.
- **`GREEDY_CAPTURE` is a control for the RQ-1/RQ-2 estimands, not a strategy
  under study.** It appears in EX-2 and EX-6 and **not** in EX-3, which
  remains the four-agent RQ-3 design. §12's exclusion of capture-aware
  strategies is amended only for this one agent (D-45).
- **Pre-registered prediction (falsifiable).** Under `capture_mode =
  mandatory` the legal set is already capture-restricted wherever the
  restriction applies, so `GREEDY_CAPTURE` and `RANDOM` coincide except inside
  GM-5.1's two exceptions. The mandatory-arm difference between the two fields
  is therefore expected to be near zero; a large observed difference indicates
  an engine defect in the priority lattice, not an effect.
- A `FOCUS_STICKY` variant (protagonist fixed until finished or captured) is a
  v2 candidate (§12).

---

## 4. Logging

### 4.1 Event log (LG-1)

One JSONL file **per game** (granularity pinned; D-43d), controlled by the
config field `log_events: {mode, k, pinned_game_indices}`. A header record
(schema version, engine version, prereg version, full resolved config
including every rule flag, all seeds, seat assignment, **resolved
`starting_seat`**, agent ids per seat), then one record per event:

- `roll` (seat, value, attempt number)
- `move` (seat, piece, from, to, move kind: enter/ring/goal-enter/goal, the
  full legal-move set that was offered with `captures: {seat, piece} | null`
  per entry, the chosen index, and
  `restriction: none | capture | clearing | forced_entry`)
- `capture` (captor, victim seat+piece, field)
- `barrier_formed` / `barrier_broken`
- `pass` (no legal move)
- `finish` (seat's fourth piece reaches goal)
- `game_end` (ranks, §6.1)

Final record: the game-summary row (§4.2) inline, so a single file is
self-contained.

Design rule: every statistic that any analysis needs is a **first-class field**
of the summary row. Analyses never re-derive numbers by parsing event streams
when a summary field exists. The one deliberate exception is AK-9, whose whole
purpose is an independent re-derivation.

### 4.2 Summary row (LG-2)

One JSONL row per game with: ids/versions/config/seeds, `prereg_version`,
`cell_key`, `starting_seat`, `turn_offset_by_seat`, `n_requested`,
`n_effective`, balance block `B`, `rotation_index`, `starting_seat_index`,
winner seat, ranks, the complete metric battery of §6.2, and per-seat
counters. **The key set is fixed per `schema_version` and does not vary by
arm** — arm-specific fields such as the barrier counters are always present
and zero when inapplicable. Campaigns aggregate exclusively from summary rows.

### 4.3 Replay invariant (LG-3)

`header + engine version` reproduce the game byte-identically. A replay
validator re-simulates from the header and asserts event-stream equality.

**Canonical serialization (D-33):** UTF-8, explicit `\n`, fixed key order,
`separators=(",",":")`, shortest round-trip float representation — part of the
log schema version. Shards write `summary-<shard>.jsonl`; the runner seals a
campaign by concatenating in ascending shard index, rows in ascending global
game index.

**Version skew:** the replay validator refuses a log whose `engine_version`
differs from the running engine unless `--allow-version-skew` is passed.
Goldens are regenerated on every version bump with a ledger row; published
campaigns record the engine version they are valid under.

---

## 5. Determinism and performance (non-functional)

- **NF-1 Determinism.** One master seed determines everything. Per-game seed =
  `SHA-256(master_seed ‖ cell_key ‖ game_index)`, so arms are independent (not
  common-random-number paired) and §6.3's unpaired procedures are valid as
  written. Each game splits into independent named streams (dice, starting
  player, per-seat agent streams). Results are independent of
  `PYTHONHASHSEED`, worker count, node count, platform, and shard boundaries.
  **NF-1 extends to the analysis layer** — see NF-7.
- **NF-2 Performance.** Target: ≥ 1,000 complete baseline games per second
  single-core in pure Python (int/tuple state, no per-move object churn). This
  is a **target, not a measurement**: no runtime figure anywhere in this
  project is validated until AK-7 has run. §8's plan is stated in games for
  that reason. If the target is missed, the state representation is optimized
  *before* any feature work continues; every such optimization gets a ledger
  row.
- **NF-3 Parallelism.** Worker count is configurable with **no upper bound**;
  campaigns may run across multiple HPC nodes. The determinism invariant is
  the binding constraint: output is a deterministic function of the config
  alone, never of the worker layout, node count, or scheduling order. Sharding
  is by game index.
- **NF-4 Language.** All artifacts English. No site or person specifics in the
  repo.
- **NF-5 Decision ledger.** [decisions.md](decisions.md): every rule-ambiguity
  resolution, every measurement-relevant optimization or shortcut, every
  amendment under §14 — one row each, with status
  (`verified-official` / `project-choice` / `pinned`).
- **NF-6 Data management.** `summary.jsonl` is stored gzipped. `campaigns/` in
  git holds only `campaign.json` (resolved config + aggregate cells) plus the
  compressed summaries under a stated size cap; anything larger is a release
  asset referenced by SHA-256 from `campaign.json`. The reproducibility
  contract is **master seed + engine version + prereg tag**; raw rows are a
  convenience artifact.
- **NF-7 Analysis determinism.** An analysis run takes its own declarative
  config (input campaign dir, estimand list, `analysis_seed`, `bootstrap_B`,
  alpha) and writes `analysis.json` recording the resolved config, the
  environment (Python, NumPy/SciPy, BLAS versions) and the SHA-256 of the
  input `summary.jsonl`. `bootstrap_B = 10000` for headline numbers.
  **Simulation may fan out across nodes; analysis does not** — BLAS reduction
  order differs across architectures, and §6.4's rules are threshold rules, so
  a borderline verdict could otherwise flip between nodes.

---

## 6. Metric battery (fixed pre-registration)

### 6.1 Definitions

- `progress(piece)`: 0 in the yard; on the ring:
  `1 + (steps_since_entry mod ring_length)`; in the goal:
  `ring_length + 1 + goal_index`. `progress(seat)` = sum over its four pieces.
  Normalized progress = progress / max possible (§2.1: 170 / 202).
  **Under `mandatory_extended` progress is explicitly not monotone in time**:
  a piece forced past its own goal entry drops back to a low value rather than
  colliding with the goal encoding. `extra_laps_by_seat` records how often the
  rule fired. GM-3.8 re-applies on every subsequent pass, so no lap-count
  state is carried on the piece.
- Ranks at game end: the realized finishing order (`play_out`); the single
  unfinished player ranks last. In `first_winner` mode only: ranks by total
  progress, standard competition ranks, ties reported in `rank_ties`.
- `leader(t)`: the unique argmax of `progress(seat)`. On ties, `leader(t−1)`
  iff it is itself among the tied maxima, else the tied-maximum seat with the
  lowest seat index. `leader(0) := NULL`, and NULL persists until a strict
  maximum exists; a NULL→seat transition is not a lead change. `t` indexes
  global turns within the first-win segment.

### 6.2 Per-game metrics (summary-row fields)

Segment convention: games are played out fully (GM-3.11), but the dynamics
metrics — `lead_changes`, `time_in_lead_by_seat`, checkpoint ranks,
`comeback`, `final_margin` — are computed over the **first-win segment** (game
start until the first finisher). The play-out tail is contested by ever-fewer
seats and would dilute exactly the dynamics signal RQ-1 asks about. Capture
and pass counters run over the full game; length counters are recorded for
both segments.

| Field | Definition |
|---|---|
| `rounds`, `turns`, `dice_rolls` | A round is `players` consecutive turn slots from the drawn starting seat; a skipped finished seat consumes a slot but not a turn; `rounds = ceil(turn_slots / players)`, trailing partial cycle counted. Turns include extra rolls from 6s. Over the full played-out game. |
| `rounds_to_first_win`, `turns_to_first_win` | The same counters up to the first finisher. RQ-1's dispersion comparisons use `rounds_to_first_win`; it is measured on a segment whose endpoint is the event under study and must not be read as total game duration. |
| `captures_total`, `captures_by_seat`, `captured_by_seat` | Capture events. |
| `lead_changes`, `lead_changes_per_turn` | Transitions where `leader(t) ≠ leader(t−1)`, both endpoints non-NULL. The per-turn form is the k-comparable one. |
| `turns_without_leader` | Turns with no strict maximum; excluded from the entropy denominator. |
| `time_in_lead_by_seat`, `lead_entropy_norm` | Turns each seat was leader; `H(p)/ln(P)` over the P occupied seats, over the first-win segment, = 0 when P = 1 or no turn has a defined leader. |
| `winner_rank_at_50`, `winner_rank_at_75`, `winner_rank_at_50_tied` | The eventual winner's progress rank at `checkpoint(k) = state after turn ceil(k · turns_to_first_win)`, k ∈ {0.5, 0.75}. Standard competition ranks (1, 2, 2, 4); a tied winner takes the best rank of its group, flagged by the boolean. |
| `comeback`, `comeback_rank_threshold`, `comeback_depth` | Winner's checkpoint rank **≥ 2** (2–3 players) or **≥ 3** (4+ players) — always "≥". The threshold travels with the data; `comeback_depth = (rank−1)/(k−1)` is the k-comparable form. Comeback *rates* are compared only within a fixed player count. |
| `final_margin`, `final_margin_norm` | Progress gap winner vs. runner-up at the first win. Cross-`seats` comparisons use the normalized field. |
| `passes_by_seat`, `entry_waits_by_seat` | Turns with no legal move; turns in which the D-1 condition held at turn start. The two overlap by construction and must not be summed. |
| `barriers_formed`, `barrier_turns`, `barrier_turns_by_seat` | `barrier_turns` = turns during which at least one barrier stood at turn start. Always present, 0 when `barriers = false`. |
| `extra_laps_by_seat` | Forced extra laps under `mandatory_extended`. |
| `capture_forcing_offered`, `capture_forcing_violations`, `forced_extra_lap_offered`, `forced_extra_lap_violations` | Engine-asserted invariant counters (AK-5). *Offered* counts only decisions where the capture restriction actually applied — neither GM-5.1 exception in force. |

### 6.3 Estimands and methods

- **SQ-1 Win rates** per seat/strategy with Wilson 95% CIs — used only for a
  single proportion against a fixed reference.
- **SQ-2 Location effects** (means of battery metrics): difference between
  arms with BCa bootstrap CIs.
- **SQ-3 Dispersion effects** (the RQ-1 core): the **CV ratio** of
  `rounds_to_first_win` with a BCa bootstrap CI is primary. The raw variance
  ratio and the mean ratio are reported alongside so location and scale are
  visibly separated — a pure +10% location shift at constant CV produces a raw
  variance ratio of 1.21, which would otherwise read as a dynamics effect.
  Minimum practically relevant effect: **CV ratio ≥ 1.05**. Levene /
  Brown–Forsythe is uninformative at n ≥ 10k and is not used.
- **SQ-4 Winner predictability**: AUC of "current progress leader at the 50%
  checkpoint wins" per arm (AUC, because its 0.5 chance level is k-invariant);
  the skill score `(accuracy − 1/k)/(1 − 1/k)` is the reportable accuracy form.
  Lower = more dynamic games.
- **SQ-5 Interactions (RQ-4)**: logistic regression (win ~ strategy × rule ×
  players) and OLS on battery metrics as *descriptive* summaries with
  cluster-robust intervals; the primary evidence is always the direct
  cell-mean comparison of the factorial arms.
- **SQ-6 Unit of analysis**: the **game** is the independent unit. Every
  bootstrap resamples whole summary rows, never seat records; per-seat
  counters are aggregated at game level before resampling. Seat-to-seat and
  strategy-to-strategy contrasts within a cell use the multinomial difference
  variance — per-seat win indicators of one game are multinomial, so two
  independent Wilson intervals understate the SE of their difference (0.194 pp
  against the correct 0.224 pp at p = 0.25, n = 100k). Rotation strata are
  ignored rather than post-stratified, which is conservative.

**The homogeneous-field symmetry identity.** Where players = seats and every
seat runs the same policy, seat rotation is an exact automorphism (§2.1's
positions are pure functions of (seats, seat index), turn order is cyclic, the
starting player is balanced), so **each seat wins exactly 1/k for any rule
set**. Consequences, all binding: homogeneous-field win rates are not evidence
for RQ-2 or RQ-3; RQ-3 win-rate claims come exclusively from the 1-deviant and
2-player head-to-head cells; RQ-2's win-rate estimand is P(win | seat is the
starter) and the per-seat profile as a function of the flag; EX-5's 6-seat
`spread` arm and the 2-player `opposite` arm are a-priori symmetry checks in
the AK-4 family, not measurements.

### 6.4 Confirmatory hypotheses (the pre-registration proper)

**40 confirmatory hypotheses in four families.** Holm correction runs within
each family, over metrics × contrasts jointly. Every other quantity the plan
produces is **descriptive**: computed, published (§14 requires it), reported
with nominal 95% CIs, and explicitly labelled as not error-controlled.

| Family | Estimand | Contrasts | Metrics | Tests |
|---|---|---|---|---|
| RQ-1 | dispersion and dynamics in the headline cell (4 players, seats 4, all-`RANDOM`) | mandatory − optional; mandatory_extended − optional | CV ratio of `rounds_to_first_win`; `lead_changes_per_turn`; comeback rate; predictability skill score | 8 |
| RQ-2 | **main effect** of each rule axis, pooled over the EX-4 factorial | `cold_start`(2), `capture_mode`(2), `dreimal_wuerfeln`, `bonus_roll_after_quick_entry`, `goal_no_jump`, `barriers`, `bonus_roll_forfeited` = 9 | win rate by starting seat; `rounds_to_first_win` | 18 |
| RQ-3 | deviant win rate against a `RANDOM` field, 4 players | SPREAD, FOCUS_FRONT, FOCUS_REAR each vs. the 1/k reference; FOCUS_FRONT − FOCUS_REAR | deviant win rate | 4 |
| RQ-4 | named interaction contrasts | capture_mode × strategy (2); barriers × strategy (1); capture_mode × players (1); EX-5 pattern effect; EX-5 geometry effect | primary metric per §8 row | 10 |

**RQ-1 support criterion (decidable biconditional).** RQ-1 is **supported iff**
(i) the lower bound of the 95% BCa bootstrap CI on the CV ratio of
`rounds_to_first_win` (mandatory ÷ optional) exceeds 1, **and** (ii) at least
**2 of 3** of {`lead_changes_per_turn`, comeback rate, 1 − predictability skill
score} have Holm-adjusted 95% CIs excluding zero in the dynamism direction.
`captures_total` is a **manipulation check** with a pre-fixed expected
direction, not a confirmation conjunct — mandatory capture raises it by
construction. Any other outcome is reported as "not supported", with all metric
values published either way.

**Minimum relevant effect and sample size.** The smallest substantively
interesting win-rate difference is **0.5 pp**. §8's n is derived from that
target at 80% power under each family's Holm-adjusted alpha, never from the
compute budget. Additional compute capacity is not a reason to raise n.

Main effects **pool** across factorial cells: RQ-2's main effect of a two-level
axis is estimated from all 84 EX-4 cells at each level, a three-level axis from
56, so EX-4 resolves to 0.18 pp and 0.22 pp respectively at n = 20k per cell.
Named interaction contrasts do **not** pool — a 2×2 interaction uses exactly
four cells and carries twice the SE of a main effect at equal n — which is why
EX-6's confirmatory cells are the largest in the plan.

---

## 7. Campaign layer

- **7.1 Config-as-data.** A campaign is one declarative config file (JSON):
  rule flags, seats/players/pattern, agent assignment, n, master seed, output
  dir. The CLI runs configs; nothing statistical is decided in code at run
  time. The same discipline applies to analysis runs (NF-7).
- **7.2 Outputs.** `summary.jsonl` (one row per game, gzipped per NF-6),
  `campaign.json` (resolved config + aggregate cells, extended with per-cell n,
  win counts, CI bounds and pre-binned histograms for UI-6), event logs
  optionally (`--log-events all | winners | sample:k | none`; default
  `sample:100` per cell plus pinned game indices). The sampling is
  seed-deterministic and documented in the row.
- **7.3 Seat counterbalancing.** The strategy→seat assignment is rotated
  through all cyclic rotations with equal game counts; **full permutations are
  used exactly when a cell contains ≥ 2 distinct non-field strategies**. The
  starting player is likewise balanced, and **starting-seat balancing applies
  to homogeneous cells too**. EX-5's occupied block is rotated so the
  middle-seat contrast is within-rotation. Balance block
  `B = (#arrangements) × (#starting seats)`; `n_effective = ceil(n_requested /
  B) · B`, with all five balance fields written into every summary row.
  Per-seat effects are always reported separately before any averaging.

---

## 8. Experiment plan (v1 campaigns)

All rows carry an explicit board and pattern. All are **confirmatory**: no
campaign's arms are chosen after seeing another's results. Sample sizes are
derived in §6.4; confirmatory cells carry the error-controlled contrasts,
descriptive cells run at n = 20k.

| Id | Question | Design | Cells | n | Games |
|---|---|---|---|---|---|
| EX-1 | Calibration + seat symmetry | 4 players, seats 4, `adjacent`, baseline rules, all-`RANDOM`, rotation- and start-balanced | 1 | 400k | 0.40M |
| EX-1b | 6-seat calibration | 6 players, seats 6, `adjacent`, all-`RANDOM`, balanced | 1 | 400k | 0.40M |
| EX-2 | RQ-1 Schlagzwang | `capture_mode`(3) × players {2,3,4,6} × field {`RANDOM`, `SPREAD`, `GREEDY_CAPTURE`}; boards per §2.2 | 36 | 3 @ 250k, 33 @ 20k | 1.41M |
| EX-3 | RQ-3 strategies | 16 homogeneous cells (4 agents × 4 player counts) + 48 one-deviant cells (12 deviant/field combinations × 4 player counts) | 64 | 3 @ 200k, 61 @ 20k | 1.82M |
| EX-4 | RQ-2 rule main effects | Complete admissible factorial over the seven axes of §2.4, all-`RANDOM`, 4 players, seats 4 | 168 | 20k | 3.36M |
| EX-5 | Seating geometry | 3 players: 4-seat `adjacent`, 6-seat `spread`, **6-seat `adjacent`** × field {`RANDOM`, `SPREAD`}; plus 2 players `adjacent` vs. `opposite` × 2 fields | 10 | 6 @ 250k, 4 @ 20k | 1.58M |
| EX-6 | RQ-4 interactions | Six rows, each explicitly homogeneous-field or 1-deviant (§8.1) | 105 | 14 @ 400k, 91 @ 20k | 7.42M |
| | | | **385** | | **≈16.4M** |

**EX-4's enumeration.** 3 · 2 · 2 · 2 · 3 · 2 · 2 = 288 nominal combinations;
72 inadmissible (`bonus_roll_after_quick_entry = true` with
`dreimal_wuerfeln = off`) → 216 admissible; under `cold_start = free_entry`
both entry axes are inert, so 72 admissible cells collapse to 24 distinct
behaviours → **168 well-defined cells**. Effects of the two nested axes are
reported as *conditional* effects within the admissible sub-block, never as
marginal main effects.

**EX-5's decomposition** is pre-registered: pattern effect = 6-seat `adjacent`
vs. 6-seat `spread`; geometry effect = 4-seat `adjacent` vs. 6-seat
`adjacent`. The naive comparison of the original design is their **sum** and
must not be published as a pattern effect. The 6-seat `adjacent` control is
required rather than optional because on the 4-seat board every 3-of-4
occupancy is a rotation of `adjacent`, so no `spread` counterpart exists there.

### 8.1 EX-6 rows

All at `seat_pattern = adjacent`, rotation- and start-balanced. The five
agents in homogeneous rows are `RANDOM`, `SPREAD`, `FOCUS_FRONT`,
`FOCUS_REAR`, `GREEDY_CAPTURE`.

| Row | Design | Response | Cells |
|---|---|---|---|
| EX-6a | `capture_mode`(3) × homogeneous field(5), players 4, seats 4 | battery metrics (win rate is 1/k by symmetry) | 15 |
| EX-6b | `capture_mode`(3) × deviant(4) vs. `RANDOM` field, players 4, seats 4 | deviant win rate | 12 |
| EX-6c | `barriers`(2) × homogeneous field(5), players 4, seats 4 | battery metrics | 10 |
| EX-6d | `barriers`(2) × deviant(4) vs. `RANDOM` field, players 4, seats 4 | deviant win rate | 8 |
| EX-6e | `capture_mode`(3) × players(2,3,4,6), all at seats 6 | battery metrics | 12 |
| EX-6f | three-way `capture_mode`(3) × deviant(4) × players(2,3,4,6), seats 6 | deviant win rate | 48 |

Consolidated report: `docs/results.md` — dataset, per-question findings with
effect sizes and CIs, the confirmatory/descriptive label on every number,
limitations, reconciliation against this document.

---

## 9. Decision ledger

All rule-ambiguity resolutions live in [decisions.md](decisions.md), 59 rows
at version 2, each with a status:

- `verified-official` — checked against the official Schmidt text, German
  source quoted, edition cited. Includes the setup (GM-3.2), the clearing
  priority (GM-3.5), the three-attempts condition and its variant status,
  goal-column jumping and exact-fit entry, and the barriers variant.
- `project-choice` — the rulebook is demonstrably silent; an explicit
  documented choice. Includes die consumption on a forced clearing move,
  overshoot inside the goal column, and the GM-5.1 priority lattice.
- `pinned` — implementation and analysis decisions with no rulebook bearing.

No row is `pinned-unverified` at version 2.

---

## 10. Web UI

- **UI-1 Purpose.** Replay and inspection of logged games — an analysis
  instrument, not a play interface.
- **UI-2 Architecture.** Static single-page app (TypeScript + Vite), built to a
  **single self-contained HTML file** with all JS and CSS inlined: no ES-module
  entry script, no code splitting, no runtime asset fetch, so it genuinely runs
  from `file://`. Games load via file input / drag-and-drop of event-log JSONL.
- **UI-3 Board rendering.** One renderer for both geometries: the ring drawn as
  a ring (schematic), yards and goal columns per seat, seat colors, barriers
  marked. The classic cross layout for the 4-seat board is a nice-to-have skin.
- **UI-4 Replay controls.** Step forward/back, jump to any event, autoplay with
  speed control, event list with filters (captures, entries, barrier events,
  passes), current roll and the offered legal-move set highlighted on the board.
- **UI-5 Info panels.** Per-seat progress bars, capture counters, the game's
  resolved rule flags and seeds, the running §6 metrics — with the first-win
  segment boundary marked, since the dynamics metrics stop there.
- **UI-6 Aggregate view (should-have).** Loads `campaign.json`, which carries
  per-cell n, win counts, CI bounds and pre-binned histograms. `summary.jsonl`
  loading is permitted only per cell with a documented row cap. The UI never
  reimplements §6.3's estimators.
- **UI-7 Language.** English.

---

## 11. Acceptance criteria

| Id | Criterion |
|---|---|
| AK-1 | Rule-conformance unit tests per flag from hand-crafted scenarios: exact-fit goal entry, `goal_no_jump` incl. its last-piece clause, entry-clearing priority, the GM-5.1 lattice ("6 rolled, yard piece available, capture available elsewhere"), `dreimal_wuerfeln` incl. the goal-piece condition, bonus roll, `bonus_roll_forfeited`, mandatory capture incl. both exceptions, extended capture past the goal entry, barrier formation/blocking/forced breaking, all four `cold_start` interaction cases, and agent-totality scenarios (all pieces in yard; all in goal but one in yard; a single legal goal move). |
| AK-2 | Determinism: same master seed twice → byte-identical logs and summaries; **1 worker vs. 8 workers vs. the maximum configured worker count → byte-identical `summary.jsonl` and `campaign.json`**; same analysis config twice → byte-identical `analysis.json`. |
| AK-3 | Replay validator: ≥ 1,000 seed-random games across mixed configs re-simulated from headers with exact event-stream equality. |
| AK-4 | Seat symmetry, as an **equivalence test**: for every calibration cell (EX-1, EX-1b) and every seat, the two-sided 99% CI for (p_seat − 1/k) lies entirely within ±δ, δ = **0.5 pp** at n = 400k (half-width 0.176 pp, so a fault-free engine passes essentially always). Declared a harness and geometry gate, not a substantive seat estimate. Known limitation: four per-seat tests carry ≈3.9% family-wise spurious-failure probability, accepted in exchange for naming *which* seat deviates. |
| AK-5 | Log-level invariant, over engine counters rather than decisions: summed over all summary rows of every `mandatory` and `mandatory_extended` cell, `capture_forcing_violations = 0` and `forced_extra_lap_violations = 0`; plus a per-event spot check over the sampled logs. Formulated this way so it is independent of the GM-5.1 priority direction and does not require full event logs. |
| AK-6 | UI renders a golden reference game (fixed seed, checked-in log) correctly end-to-end from the built artifact opened off disk: every event steppable, final state matches the summary row. |
| AK-7 | NF-2 benchmark on two defined cells — baseline (4 players, seats 4, all-`RANDOM`) and worst case (6 players, seats 6, `barriers` + `mandatory_extended`, all-`SPREAD`) — both measured with logging at the campaign default and with the per-turn `leader(t)` recomputation inside the measured loop. Failure remedy is an optimization pass plus a ledger row, never a silent reduction of n. Runs in M1. |
| AK-8 | Estimator calibration: on synthetic data with known truth, Wilson and BCa intervals achieve nominal coverage within Monte-Carlo error, and the Holm procedure reproduces a hand-worked example. |
| AK-8b | Analytic calibration: on a 1-player configuration the simulated distribution of turns-to-first-entry matches the analytic geometric distribution with `p = 1 − (5/6)^attempts` (chi-square over the first 10 turn counts, n = 100k); the empirical die-face distribution over a full cell is uniform within its 99% CI. Catches the class of dice/entry errors AK-4 is structurally blind to, because a uniform bias hits every seat equally. |
| AK-9 | Metric cross-validation: for the AK-3 replay corpus, an independent reference implementation walking the event log reproduces every §6.2 summary field exactly. The one deliberate violation of §4.1's no-re-derivation rule. |

---

## 12. Out of scope (v1)

- `penalize` capture enforcement ("pusten") and any fallible-agent modeling.
- Threat-aware, barrier-aware and learned strategies (RL); `FOCUS_STICKY`.
  **`GREEDY_CAPTURE` (§3.2) is exempted** as a measurement control for the
  RQ-1/RQ-2 estimands; the exemption is deliberately narrow and does not admit
  it to RQ-3's strategy comparison.
- Boards other than the 4- and 6-seat geometries; house rules not in §2.4.
- Human play, online play, play-mode UI.

---

## 13. Repository layout

```
madnlab/
  engine/     board geometry, state, legal_moves, rule flags, game loop
  agents/     the five v1 policies (+ registry)
  eventlog/   event log writer, summary rows, replay validator
  run/        campaign runner (configs, sharding, CLI)
  analysis/   metric aggregation, bootstrap/CI helpers, report generation
ui/           static replay viewer (TypeScript + Vite)
tests/        AK-1..AK-9 acceptance + unit tests
docs/         requirements.md, decisions.md, spec-review.md, results.md
campaigns/    published measurement series (campaign.json + gzipped summaries)
```

`src/` layout, explicit `__init__.py`, `pyproject.toml`. The event-log package
is `eventlog/`, not `logging/`, to avoid shadowing the stdlib name for readers
and linters.

Milestones: **M1** engine + AK-1/2/3/7 green → **M2** analysis package +
AK-8/8b/9 → **M3** EX-1/EX-1b calibration + AK-4, first mandatory smoke cell +
AK-5 → **M4** UI + AK-6 → **M5** full experiment plan + `docs/results.md`.

---

## 14. Pre-registration status

1. **Freeze.** The frozen specification is the git tag `prereg-v1`. Every
   campaign config and every summary row records the `prereg_version` it ran
   under, and every published row reads `prereg-v1`.

   *Amendment (2026-08-01, D-73).* This clause read "created before EX-1
   runs", and that is not what happened: the tag was created after EX-1,
   EX-1b and the AK-5 smoke campaign had run and after the five main
   campaigns had been submitted, all under the placeholder `unfrozen`. All of
   that data was **discarded and regenerated** under the tag rather than
   relabelled — runs are deterministic from the master seed (NF-6), so
   regeneration costs wall-clock only. No §6.4 hypothesis had been evaluated
   at any point before the freeze, so the freeze still precedes the analysis.
   D-73 carries the full record.
2. **Amendments.** Any change to §6 or §8 after the freeze is an amendment with
   its own ledger row stating what data already existed when it was made.
3. **Confirmatory / exploratory.** EX-1 through EX-6 are all confirmatory: no
   campaign's arms depend on another's results. Any campaign added later
   without a pre-registered arm list is labelled exploratory.
4. **All results reported.** `docs/results.md` reports every §6.2 metric for
   every campaign cell, significant or not, with its confirmatory/descriptive
   label attached. This, together with the freeze, is what prevents
   cherry-picking — not the size of the multiplicity correction.

---

## 15. EX-7 — seat exposure

Does where you sit decide the game? On the 4-seat board two players sit
either next to each other or across from each other, and the two
arrangements are not equivalent.

### 15.1 The mechanism

Entry fields are `spacing` apart, so an occupancy pattern fixes the cyclic
gaps between them. A piece is exposed to an opponent over the stretch of ring
it occupies *downstream* of that opponent's entry field, because that is where
the opponent's freshly entering pieces move into it.

| Cell | occupied | entry fields | cyclic gaps |
|---|---|---|---|
| 4 seats, 2 players, `adjacent` | 0, 1 | 0, 10 | 10, 30 |
| 4 seats, 2 players, `opposite` | 0, 2 | 0, 20 | 20, 20 |
| 6 seats, 3 players, `adjacent` | 0, 1, 2 | 0, 8, 16 | 8, 8, 32 |
| 6 seats, 3 players, `spread` | 0, 2, 4 | 0, 16, 32 | 16, 16, 16 |

Under `adjacent` at two players, a seat-0 piece spends 30 of its 40 ring steps
downstream of seat 1's entry; a seat-1 piece spends 10 of 40 downstream of
seat 0's. **Prediction: seat 1 wins more.** Under `opposite` the gaps are equal and the
prediction is no asymmetry — a negative control the geometry supplies for free.

### 15.2 Confirmatory hypotheses (family RQ-5)

Estimand: `seat_asymmetry` = p(second occupied seat) − p(first occupied seat)
within one cell, using the multinomial difference variance (§6.3 SQ-6). Holm
within the family at alpha = 0.05. **8 hypotheses.**

The two seats are named **by position, in advance** — the first and second
entries of the occupied list — never as the observed maximum and minimum.
Picking the extreme pair out of the data and then testing it is a selection
the interval does not know about, and at three seats it inflates the
rejection rate by roughly a factor of three. For the three-player cells the
geometry gives the same prediction as at two: seat 0 carries the longest
downstream exposure and is predicted lowest, seat 1 highest.

| # | Contrast | Pre-registered prediction |
|---|---|---|
| 1 | `4s2p adjacent`, homogeneous SPREAD | asymmetry **> 0** and **> 5 pp** |
| 2 | `4s2p adjacent`, homogeneous RANDOM | asymmetry **> 0** |
| 3 | `4s2p opposite`, homogeneous SPREAD | **equivalent to 0** within ±1 pp |
| 4 | `4s2p opposite`, homogeneous RANDOM | **equivalent to 0** within ±1 pp |
| 5 | SPREAD − RANDOM asymmetry, `adjacent` | **> 0** (the strategy amplifies it) |
| 6 | `adjacent` − `opposite` asymmetry, SPREAD | **> 0** (the geometry causes it) |
| 7 | `6s3p adjacent` vs `6s3p spread`, SPREAD | adjacent asymmetry **larger** |
| 8 | `6s3p adjacent` vs `6s3p spread`, RANDOM | adjacent asymmetry **larger** |

**RQ-5 support criterion (decidable biconditional).** RQ-5 is **supported iff**
hypotheses **1, 5 and 6** are all Holm-rejected in the predicted direction
**and** hypothesis **3** passes its equivalence test. Any other outcome is
reported as not supported, with all values published either way.

Rationale for the conjunction: (1) alone would only restate the observation;
(6) is what attributes it to the seating geometry rather than to something
about SPREAD; (5) is what shows the strategy matters; and (3) is the negative
control that would fail if the estimator simply manufactured asymmetries.

### 15.3 Arms and sample size

14 cells at n = 200,000: seating pattern {`adjacent`, `opposite`} × five
homogeneous fields at 2 players on the 4-seat board (10 cells), plus
{`6s-adjacent`, `6s-spread`} × {RANDOM, SPREAD} at 3 players (4 cells).
**2.8M games.**

At n = 200,000 and two players the multinomial half-width of a seat difference
is 0.44 pp, which resolves both the 5 pp threshold of hypothesis 1 and the
±1 pp equivalence margin of hypothesis 3. The three non-headline fields
(FOCUS_FRONT, FOCUS_REAR, GREEDY_CAPTURE) carry no confirmatory hypothesis and
are descriptive: they say whether the effect is specific to SPREAD.

---

## 16. EX-8 — turn order, capture play, and the middle seat (family RQ-6)

Four questions the plan already had the machinery for and never asked. Nine
hypotheses, Holm within the family.

**Does going first help?** The starting-player advantage has been measured
since M3, has its own ledger row (D-25) and its own report section — and no
hypothesis. It is probably the first thing a reader of this project wants to
know. Tested against the fixed 1/k reference on both calibration cells, and as
a function of player count with the board held fixed at 6 seats (D-12), since
a naive count contrast would mix player count with geometry.

**Does playing *toward a rule* help?** RQ-3's three strategies are pure
movement heuristics and none of them worked. `GREEDY_CAPTURE` is the one agent
that plays toward a rule, and outside the 20k descriptive cells it is never
tested against a `RANDOM` field. Under `mandatory` the capture obligation
applies to everyone, so its edge should disappear — which makes the
interaction the interesting half.

**Is the middle seat disadvantaged?** §1 asks this in so many words and §2.2
gives the reason: an opponent directly behind, the other's start area directly
ahead. Nothing in the plan tested it. The estimand is seat 1 against the mean
of its neighbours, weights (−1/2, +1, −1/2), which is a multinomial contrast
rather than a difference of two seats.

**Did the mandatory arm do anything?** §6.4 names `captures_total` as a
manipulation check with a pre-fixed direction and no code ran it. Mandatory
capture must raise the capture count; if it does not, the arm is inert and
every RQ-1 result above it is meaningless.

| # | Contrast | Prediction |
|---|---|---|
| 1 | starter advantage, 4 players | **> 0** |
| 2 | starter advantage, 6 players | **> 0** |
| 3 | starter advantage, 2p − 6p (6 seats) | **> 0** (fewer players, bigger edge) |
| 4 | `GREEDY_CAPTURE` vs 1/k, `optional` | **> 0** |
| 5 | `GREEDY_CAPTURE` vs 1/k, `mandatory` | ≈ 0 |
| 6 | its edge, `optional` − `mandatory` | **> 0** |
| 7 | middle seat, 3p on 4 seats, RANDOM | §1 predicts **< 0** |
| 8 | middle seat, 3p on 4 seats, SPREAD | §1 predicts **< 0** |
| 9 | captures per game, `mandatory` − `optional` | **> 0** (manipulation check) |

**Arms.** EX-8 adds six cells at n = 250,000: the 6-seat board at 2, 3, 4 and
6 players all-`RANDOM`, and `GREEDY_CAPTURE` against a `RANDOM` field at 4
players under `optional` and `mandatory`. 1.5M games. Hypotheses 1, 2, 7, 8
and 9 read cells that already exist.

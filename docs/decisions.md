# Decision ledger (NF-5)

Every rule-ambiguity resolution (§9 of [requirements.md](requirements.md)),
every measurement-relevant shortcut, and every specification defect resolved
during implementation gets one row here.

**Status vocabulary**

| Status | Meaning |
|---|---|
| `pinned` | Decided. Binding for the engine, the campaigns and the analysis. |
| `verified-official` | Decided **and** checked against the official Schmidt Spiele rulebook, with the German source text quoted and the edition cited. |
| `project-choice` | Decided, and the rulebook is demonstrably **silent** on the question — §9's own escape clause. Never presented as conformance. |
| `pinned-unverified` | Decided, but the decision claims conformance with the official rulebook and that check has **not** been performed yet. |
| `open` | Identified, not yet decided. Blocks the work named in *Affects*. |

**Provenance.** D-1…D-7 are §9's own seven decision points, adopted with the
defaults §9 proposes. D-8…D-47 come from the specification review
([spec-review.md](spec-review.md)); the review's finding ids (B-*, MJ-*, C-*)
are cited per row. Four rows (D-9, D-10, D-44, D-46) were decided by the
project owner against a presented alternative and are marked accordingly.

**Rulebook verification.** Complete as of 2026-07-31, before the `prereg-v1`
freeze (D-73). Nine rows carry `verified-official` with the German source text
quoted and the edition cited; the rows resting on questions the rulebook is
demonstrably silent on carry `project-choice`. No row carries
`pinned-unverified` any more — the status stays in the vocabulary above
because rows added after the freeze may need it again.

---

## 1. Base rules and rule interaction

### D-1 — Scope of the three-attempts condition
**Status:** `verified-official` (the condition) · see D-51 (the rule's status)
**Decision.** The condition holds iff the player has no piece on the ring
track **and** no goal piece that any roll value 1–6 could legally move.
Conjunct (ii) is evaluated over all six die values **before** rolling, not
against the roll actually made. Pieces in the yard do not count as movable.
**Verified against.** Art. 51204 (2023), corroborated verbatim in 49020 (2006)
and 49324 (2016):

> „Wer keine Spielfiguren auf der Laufbahn hat, weil alle Figuren geschlagen
> wurden und auf den B-Feldern auf ihren Einsatz warten, darf dreimal
> würfeln. Das gilt auch, wenn schon ein oder mehrere Figuren ihre Zielfelder
> erreicht haben, aber nur dann, wenn sie dort nicht noch vorrücken könnten.
> (Beispiel: Eine Spielfigur steht bereits auf Feld c im Ziel, die anderen
> drei warten auf den B-Feldern. In dem Fall darf nicht dreimal gewürfelt
> werden, weil die Figur auf Feld c noch mit einer „1" vorrücken könnte)."

The worked example is what settles conjunct (ii): a piece on goal field c
blocks the three rolls because it *could* advance with a 1 — so the test is
over the whole die, pre-roll. §9.1's proposed wording was correct.
**Implementation notes.**
1. The yard-occupancy guard is deliberately **omitted**: each player has 4
   pieces and the goal column has 4 fields, so 0 on the track and 0 in the
   yard means all 4 are home, which is the win condition. The guard is
   entailed by the two stated conjuncts in every reachable non-terminal state.
2. Conjunct (ii) must be evaluated against the **active** rule set — whether a
   goal-column piece has a legal move depends on `goal_no_jump` (D-53).
   Hardcoding jump-or-no-jump here would silently change when the rule fires.
3. Condition (i) counts a piece on the own A-field as being on the track.
   Recorded as a reading, not a quotation: the rulebook defines „Laufbahn" as
   the white fields and describes A-fields separately, but the rule's own
   causal clause („weil alle Figuren geschlagen wurden") makes the point moot.
**Affects.** D-51, `entry_waits_by_seat`, AK-1.

### D-2 — Entry-clearing priority vs. a 6 (GM-3.4 / GM-3.5)
**Status:** `verified-official`
**Decision.** Entry-field clearing outranks entering. If an own piece stands
on the own entry field while own pieces remain in the yard, and moving that
piece away is legal, that move is forced — including on a 6.
**Verified against.** Art. 51204 (2023), 49324 (2016) and 49020 (2006) — three
redactions in agreement. The standing duty:

> „Solange noch weitere Spielfiguren auf den B-Feldern auf ihren Spieleinsatz
> warten, darf keine eigene Figur auf dem A-Feld stehen bleiben. Sie muss das
> Feld frei machen, sobald sie die Möglichkeit dazu hat."

And the decisive sentence, which sits **inside the 6-rule itself** as an
express exception:

> „Bei einer „6" muss eine neue Figur ins Spiel gebracht werden, solange noch
> Spielfiguren auf den eigenen B-Feldern stehen. Die neue Figur wird dann auf
> das A-Feld der eigenen Farbe gestellt. **Ist dieses Feld noch von einer
> anderen eigenen Spielfigur besetzt, muss diese Figur erst mit der „6"
> weitergezogen werden.**"

**Why this is recorded in detail.** The priority is *textual*, not an artefact
of the order in which the rulebook states its rules — the rulebook subordinates
the entry obligation to the clearing duty in the same breath in which it states
the entry obligation. A future reader will otherwise re-litigate this. The 2006
wording („muss **dieser Stein** erst…") is grammatically ambiguous in isolation;
the 2016 redaction already reads „muss **diese Figur** erst…", feminine,
agreeing with „einer anderen eigenen Spielfigur", so the referent can only be
the A-field occupant. German Wikipedia is **not** corroboration here in either
direction: it conditions forced entry on an empty start field and never states
the tie-break.
**See also D-52** for the sub-question the rulebook does *not* answer: whether
the 6 is consumed by the forced clearing move.
**Affects.** GM-3.4, GM-3.5, D-9, D-52, AK-1.

### D-3 — Canonical move ordering (GM-7)
**Status:** `pinned`
**Decision.** Goal moves first, then ring moves; within each group by piece
id ascending, then by target field ascending. Entry moves sort as ring moves
with target = the own entry field.
**Rationale.** §9.3's proposed default, adopted unchanged. This is the
placeholder the specification left as "decision D-?" in §3.2 (review C-3).
It also fixes the goal-entry preference of the §3 agents: when a piece has
both a ring move and a goal move legal, the goal move is chosen.
**Affects.** GM-7, all agents, `legal` index in the `move` event, AK-1.

### D-4 — Barrier corner cases (GM-6.5)
**Status:** `pinned`
**Decision.** (a) A barrier on the own entry field does **not** suspend
entry-clearing (D-2): clearing remains forced and dissolves the barrier if
that is the only legal clearing move. (b) A barrier standing on a goal entry
blocks passage like any other barrier; the owner's own piece is blocked too.
(c) A capture onto a *forming* barrier field is not possible — forming
requires the target field to hold exactly one own piece, and a field holding
an opponent piece is a capture target, never a formation target.
**Rationale.** §9.4's proposed defaults, adopted unchanged. See also D-34,
which restricts barriers to ring fields and removes a fourth corner case.
**Affects.** GM-6, D-34, AK-1.

### D-5 — Tie reporting in end-of-game ranks (§6.1)
**Status:** `pinned`
**Decision.** Under `play_out` (the v1 default) ranks are the realized
finishing order and ties cannot occur. Under `first_winner`, ranks are
standard competition ranks (1, 2, 2, 4) over `progress(seat)`, and each tie
group is reported in the summary row via `rank_ties: [[seat, seat], …]`.
**Rationale.** §9.5. The `play_out` half is a consequence of GM-3.11, not a
choice; the `first_winner` half aligns with D-19's checkpoint rank rule so
one ranking routine serves both.
**Affects.** §6.1, `ranks`, D-19, `game_end_mode` (D-35).

### D-6 — Starting player in uncounterbalanced single games
**Status:** `pinned`
**Decision.** Seeded uniform draw over the occupied seats, from the dedicated
`starting_player` stream (NF-1). In counterbalanced campaign cells the runner
overrides the draw with the balanced assignment; the resolved value is
recorded either way (D-25).
**Rationale.** §9.6's proposed default, adopted unchanged.
**Affects.** NF-1, §7.3, D-25, D-39.

### D-7 — Forcing semantics under `cold_start = free_entry`
**Status:** `pinned`
**Decision.** Entering is an ordinary legal move, never forced. Entry-field
clearing (D-2) still applies. The 6-forces-entry clause (GM-3.5) applies only
under `strict` and `one_piece_out`. Any roll value may be used to enter and
is consumed by the entry.
**Rationale.** §9.7's proposed default, adopted unchanged.
**Affects.** GM-3.5, `cold_start`, D-9, D-13, AK-1.

### D-8 — `progress` under `mandatory_extended` (extra-lap encoding)
**Status:** `pinned` · *review B-1 (blocker)*
**Decision.** Ring progress is `1 + (steps_since_entry mod ring_length)`. A
piece forced past its own goal entry therefore drops back to a low progress
value instead of colliding with the goal encoding. `max possible` for
normalization stays the lap-0 seat maximum: **170** on the 4-seat board,
**202** on the 6-seat board. Progress is explicitly **not monotone in time**
in this arm. A new summary field `extra_laps_by_seat` records how often the
rule fired. GM-3.8 re-applies on every subsequent pass of the goal entry, so
no lap-count state field is added to the piece representation.
**Rationale.** §6.1's encoding gives a ring piece on its goal entry
progress 40 on the 4-seat board and progress 41 one field further — which is
exactly the encoding of goal index 0. The accumulating reading would score a
lapped piece as if it had entered the goal and push normalized progress above
1; the modulo reading is also the semantically correct one, because
`progress` feeds `leader(t)`, which asks "how close to winning", and a piece
sent on an extra lap is genuinely further from winning.
**Affects.** §6.1, every §6.2 dynamics metric, all agents' piece selection,
D-18, EX-2, EX-6.

### D-9 — Priority lattice: clearing vs. forced entry vs. mandatory capture
**Status:** `pinned` · *decided by the project owner against the alternative*
· *review B-2 (blocker)*
**Decision.** The order is **entry-clearing > forced entry > mandatory
capture**. Resolution procedure for `capture_mode ∈ {mandatory,
mandatory_extended}`:

1. If entry-clearing (D-2) is in force and legal → the legal set is the
   clearing moves. The capture restriction does not apply (§2.5's stated
   exception).
2. Else, if the roll is a 6, pieces remain in the yard, and the entry move is
   legal → the legal set is the entry move. The capture restriction does not
   apply.
3. Else → the capture restriction applies: if any capturing move exists, the
   legal set is exactly the capturing moves.

Under `mandatory_extended`, the forced extra lap is likewise subordinate to
steps 1 and 2: a forced entry preempts a forced lap-continuing capture.
**Rationale.** GM-3.5 is a base rule of the Schmidt rule set; `capture_mode`
is an optional overlay. The base rule takes precedence over the overlay. The
alternative (capture restriction shapes the set first, so a 6 goes unused for
entry whenever another move captures) was presented and rejected.
**Consequence — AK-5 must be restated.** As written, AK-5 excuses only the
clearing exception. Under this decision a mandatory-mode log legitimately
contains decisions where a capture was offered and a non-capturing entry move
was chosen, so AK-5 as printed fails on correct data. See D-32 for the
restatement; the counter-based formulation there makes the gate independent of
this decision's direction.
**Affects.** GM-3.4, GM-3.5, GM-5, AK-1, AK-5, D-32, the entire `mandatory`
and `mandatory_extended` arms including the EX-2 headline cells.

### D-10 — Rolls consumed per turn in the entry phase
**Status:** `pinned` · *decided by the project owner against the alternatives*
· *review MJ-3*
**Decision.** A 6 terminates the three-attempt sequence immediately and grants
exactly one GM-3.3 extra roll. That extra roll is an ordinary roll: it never
re-opens the attempt window, and if it is itself a 6 it grants a further extra
roll under GM-3.3 as normal. With `bonus_roll_after_quick_entry = true`,
entering on the 1st or 2nd attempt grants a **second** extra roll that
**stacks** with the GM-3.3 grant.

**Superseded framing (D-51).** This row was written while the three-attempts
rule was believed to be baseline. It is an optional variant, so the whole
sequence exists only when `dreimal_wuerfeln = on`, and it is a post-capture
recovery rule rather than an entry-phase rule. The decision below is unchanged
in substance; the flag names and the trigger condition are.

Maximum dice consumed in one turn while the D-1 condition holds:

| `dreimal_wuerfeln` | `bonus_roll…` | Max rolls before ordinary 6-chaining resumes |
|---|---|---|
| off *(baseline)* | false | 1 |
| on | false | 3 (attempts) + 1 (GM-3.3 extra) = 4 |
| on | true | 3 + 1 + 1 = 5 |

Independently, `bonus_roll_forfeited = true` (D-56) removes the GM-3.3 extra
roll when the 6 cannot be moved, which subtracts 1 from rows 2 and 3 in that
case. And per D-52, a forced clearing move consumes the 6.

**Rationale.** Entering on attempt 1 or 2 necessarily means a 6 was rolled, so
the flag and GM-3.3 would otherwise describe the same grant. The non-stacking
reading makes the flag inert by construction, and EX-4 would then publish a
structural null that reads like a result. Dropping the flag from v1 was the
presented alternative and was rejected — the axis stays in EX-4.
**Affects.** GM-3.3, GM-3.10, `bonus_roll_after_quick_entry`, `dice_rolls`,
the `roll` event's attempt number, EX-4, AK-1.

### D-34 — Barriers exist only on ring-track fields
**Status:** `pinned` · *review C-6*
**Decision.** GM-6.1 applies to ring-track fields only. Goal columns remain
strictly one piece per field; GM-6.1 does not override GM-3.6 inside a goal
column, and no barrier can form there.
**Rationale.** GM-6.1 says "a field occupied by exactly one own piece" without
restricting to the ring, leaving a literal misreading open. GM-3.8's "last
free reachable goal field" already presupposes single occupancy.
**Affects.** GM-6, D-4, AK-1.

### D-35 — `game_end_mode` config key
**Status:** `pinned` · *review C-5*
**Decision.** The game-end mode is named `game_end_mode ∈ {play_out,
first_winner}`, default `play_out`. It is listed in the engine-config table
next to `capture_enforcement ∈ {enforce, penalize}` (v1: `enforce` only) and
is carried in the resolved config of every log header.
**Rationale.** §2.3 clause 11 names the values but no key, although §6.1
branches on the mode and LG-1 must record every rule flag.
**Affects.** §2.3, §4.1, §6.1, §7.1.

---

## 2. Agents

### D-36 — `FOCUS_REAR` written out in full
**Status:** `pinned` · *review MJ-2*
**Decision.** `FOCUS_REAR`: protagonist = the currently **least advanced** own
piece on the ring, recomputed every decision. If a protagonist move is legal,
play it. Fallback order: entry move if legal, else the legal move of the
**most**-advanced other piece — so non-protagonists are pushed ahead rather
than bunched with the protagonist.
**Rationale.** Defined by "same policy" as `FOCUS_FRONT`, `FOCUS_REAR` would
inherit a fallback ("the least-advanced other piece") that makes its primary
rule almost identical to `SPREAD`, differing only in entry priority — which
would weaken RQ-3's contrast and produce "rear-focus does not differ" as a
property of the definition rather than of the game. The inherited note "keeps
non-protagonists back" is also false when the protagonist *is* the rearmost
piece.
**Affects.** §3.2, RQ-3, EX-3, EX-6.

### D-44 — `GREEDY_CAPTURE` control agent
**Status:** `pinned` · *decided by the project owner against the alternative*
· *review MJ-20*
**Decision.** A fifth agent is added:

> `GREEDY_CAPTURE` — if at least one capturing move is legal, choose uniformly
> among the capturing moves; otherwise choose uniformly over `legal`.

It is deliberately `RANDOM` plus a capture filter, and nothing else, so the
`RANDOM` → `GREEDY_CAPTURE` contrast isolates capture-seeking exactly.

Its role is **control for the RQ-1/RQ-2 estimands, not a strategy under
study.** It appears in EX-2 and EX-6 (see D-46, D-47). It does **not** enter
EX-3, which remains the four-agent RQ-3 design.
**Rationale.** With capture-blind agents, the baseline capture rate under
`capture_mode = optional` is the incidental rate — the lowest attainable — so
the optional→mandatory contrast is a structural **upper bound** on the
Schlagzwang effect. A capture-seeking field already takes most of the captures
the rule would force. Measuring both fields turns the headline result from a
bound into an interval, at a few seconds of compute.
**Pre-registered prediction (falsifiable).** Under `capture_mode = mandatory`
the legal set is already capture-restricted wherever the restriction applies,
so `GREEDY_CAPTURE` and `RANDOM` coincide except inside D-9's clearing and
forced-entry exceptions. The mandatory-arm difference between the two fields
is therefore expected to be near zero, and a large observed difference
indicates an engine defect, not an effect. This doubles as a cheap
cross-check on the D-9 lattice.
**Affects.** §3.2, §12 (see D-45), EX-2, EX-6, RQ-1, RQ-2.

### D-45 — Scope amendment to §12
**Status:** `pinned` · *review MJ-20*
**Decision.** §12's exclusion of "capture-aware, threat-aware, or learned
strategies" is amended to exempt `GREEDY_CAPTURE` (D-44) as a measurement
control. Threat-aware, barrier-aware and learned strategies, and
`FOCUS_STICKY`, remain out of scope for v1. The exemption is deliberately
narrow: `GREEDY_CAPTURE` is not admitted to RQ-3's strategy comparison.
**Rationale.** The §12 line exists to keep RQ-3's strategy space clean.
`GREEDY_CAPTURE` is not a candidate answer to RQ-3; it is a second point on
the policy axis along which the RQ-1 effect size is bounded.
**Affects.** §12, §3.2, D-44.

### D-37 — Agent RNG draw discipline
**Status:** `pinned` · *review C-15*
**Decision.** An agent consumes exactly one draw from its stream per decision,
including when `len(legal) == 1` and including for deterministic agents that
do not use the value. Covered by a unit test.
**Rationale.** Without this, a later optimization that short-circuits the
single-legal-move case desynchronizes the seat's stream and silently
invalidates every previously published log — while AK-2 (same seed, same
build) still passes, so nothing catches it.
**Affects.** §3.1, NF-1, AK-2.

### D-43a — Agent totality and the `track_progress` selection key
**Status:** `pinned` · *review MJ-1*
**Decision.** One selection key serves all non-random agents:

> `track_progress(piece)` = §6.1 `progress` restricted to pieces **on the
> ring**. Pieces in the yard and in the goal column are excluded from the
> ranking entirely.

The empty-candidate branch is pinned explicitly: if no own piece is on the
ring, the focus agents fall through to the entry move if legal, else to the
canonically first legal move (D-3, i.e. goal moves first). Goal-column moves
**are** eligible as "other piece" moves in the fallback, ranked after all ring
moves. `SPREAD`'s "least track progress" means this key.
**Rationale.** §3.1 requires every agent to be total, but §3.2 defines the
protagonist over ring pieces only — a set that is empty at game start, after a
multi-capture, and in endgames where the remaining pieces are split between
yard and goal column. "Track progress" was defined nowhere and is not §6.1
`progress`, which ranks goal pieces above all ring pieces and would make
`SPREAD` never select a goal piece.
**Affects.** §3.1, §3.2, RQ-3, AK-1 (agent-totality scenarios: all pieces in
yard; all in goal but one in yard; a single legal goal move).

---

## 3. Metric definitions

### D-18 — `leader(t)` base case and tie rule
**Status:** `pinned` · *review MJ-4*
**Decision.** `leader(t)` = the unique argmax of `progress(seat)`. On ties:
`leader(t−1)` iff it is itself among the tied maxima, else the tied-maximum
seat with the lowest seat index. `leader(0) := NULL`, and NULL persists until
a strict maximum exists. `lead_changes` counts only transitions where both
endpoints are non-NULL; a NULL→seat transition is not a lead change. New field
`turns_without_leader`; those turns are excluded from the lead-entropy
denominator. `t` indexes global turns within the first-win segment.
**Rationale.** All seats start tied at progress 0, so "the previous leader
persists" has no base case; initialising to seat 0 would hand it every
leaderless opening turn — a per-seat artefact §7.3 forbids leaving in
silently. Read literally the persistence clause also does not require the
previous leader to still be among the tied maxima.
**Affects.** §6.1, `lead_changes`, `time_in_lead_by_seat`, D-21, RQ-1.

### D-19 — Checkpoint rounding and checkpoint rank ties
**Status:** `pinned` · *review MJ-6*
**Decision.** `checkpoint(k) = state after turn ceil(k · turns_to_first_win)`
for k ∈ {0.5, 0.75} — taken in **turns**, not rounds, so checkpoints align
with `leader(t)`. Checkpoint ranks are standard competition ranks (1, 2, 2, 4)
over `progress(seat)`. Where the winner is tied, its rank is the **best** rank
of its tie group, flagged by `winner_rank_at_50_tied: bool`.
**Rationale.** §6.2 gives the checkpoints as a fraction with no rounding
convention, and §9.5 pins ties only for end-of-game ranks. A tie rule awarding
rank 1 to both tied seats rather than ranks 1 and 2 flips `comeback` directly.
**Caveat to publish.** The checkpoint is located from the *realised* segment
length, so it is conditioned on the game's own duration. §6.3 must state this
next to the winner-predictability estimand.
**Affects.** `winner_rank_at_50/75`, `comeback`, winner predictability, D-5.

### D-20 — `comeback` predicate
**Status:** `pinned` · *review MJ-5*
**Decision.** `comeback` = winner's checkpoint rank **≥ 2** (2–3 players) or
**≥ 3** (4+ players) — always "≥". `comeback_rank_threshold` is emitted in the
summary row so the definition travels with the data. A k-normalised companion
`comeback_depth = (rank − 1) / (k − 1)` is emitted alongside. Comeback
**rates** are compared only within a fixed player count.
**Rationale.** §6.2's "rank ≥ 3 (4+ players) or rank 2 (2–3 players)" mixes an
inequality with a bare equality, so read literally the strongest comeback in
every 3-player cell is discarded — from a metric that is one of the three
conjuncts of the RQ-1 support criterion.
**Affects.** §6.2, D-15, RQ-1, EX-2.

### D-21 — k-normalised dynamics companions
**Status:** `pinned` · *review MJ-8*
**Decision.** Two companions are added to the summary row and used for any
cross-player-count statement:
`lead_changes_per_turn = lead_changes / turns_to_first_win`, and the
predictability skill score `(accuracy − 1/k) / (1 − 1/k)`, which is 0 at
chance for every k. AUC is preferred over raw accuracy for the predictability
estimand because AUC's 0.5 chance level is k-invariant; raw accuracy is
descriptive only.
**Rationale.** `lead_changes` counts argmax transitions over k seats, so it
rises mechanically with k under identical dynamics. Predictability accuracy
has chance floor 1/k, so §6.3's "lower accuracy = more dynamic" compares a
2-player accuracy against 0.5 and a 6-player accuracy against 0.167. EX-2
crosses `capture_mode` with players ∈ {2, 3, 4, 6} and feeds exactly this
criterion.
**Affects.** §6.2, §6.3, D-15, EX-2, EX-6.

### D-22 — `barrier_turns` definition and arm-invariant key set
**Status:** `pinned` · *review MJ-7*
**Decision.** `barrier_turns` = the number of turns during which at least one
barrier stood at the **start** of the turn. `barrier_turns_by_seat[s]` = the
same, counted per owning seat. `barriers_formed` = count of `barrier_formed`
events over the full game. All three are **always present** and are 0 when
`barriers = false`. The summary-row key set is fixed per `schema_version` and
does not vary by arm.
**Rationale.** §6.2's cell contains only a collection condition where every
other row supplies a definition, and the field admits at least three readings
differing by large factors — while being the only barrier-specific dynamics
metric behind EX-6's `barriers × strategy` factorial. Separately, §4.2
promises every row carries "the complete metric battery of §6", which a
conditional key set contradicts.
**Affects.** §6.2, §4.2, EX-4, EX-6.

### D-25 — Starting seat as a first-class field, and the turn-order estimand
**Status:** `pinned` · *review MJ-15*
**Decision.** `starting_seat` and `turn_offset_by_seat` become first-class
summary-row fields and are listed explicitly in the §4.1 log header. A new
estimand is pre-registered: **win rate by turn-order offset from the starting
seat**, with Wilson 95% CIs. §7.3 is extended to state that starting-seat
balancing applies to homogeneous cells too, and that EX-5's occupied block is
rotated so the middle-seat contrast is within-rotation.
**Rationale.** EX-1 promises "first quantification of the starting-player
advantage" but no field and no estimand existed for it, against §4.1's rule
that every statistic an analysis needs is a first-class field. The marginal
per-seat win rate is 1/k by construction under balancing (D-26), so it cannot
be the estimand. §4.3 also requires re-simulation from the header alone, and
under §7.3 the starting seat is assigned by the runner rather than derived
from the seed.
**Affects.** §4.1, §4.2, §6.3, §7.3, EX-1, EX-5, D-6, D-39.

### D-43b — Metric definitions left as prose in §6.2
**Status:** `pinned` · *review C-9, C-10, C-11, C-12*
**Decision.** Four glosses are replaced by definitions:

- `rounds`: a round is `players` consecutive turn slots counted from the drawn
  starting seat; a skipped finished seat consumes a slot but not a turn;
  `rounds = ceil(turn_slots / players)`. A trailing partial cycle counts.
- `entry_waits_by_seat`: turns in which the D-1 three-attempts condition held
  at turn start. It overlaps `passes_by_seat` by construction and must never
  be summed with it.
- Normalization constants: `max possible` progress per seat is **170** (4-seat)
  and **202** (6-seat). `final_margin_norm` is emitted alongside
  `final_margin`; any cross-`seats` comparison uses the normalized field.
- `lead_entropy_norm = H(p) / ln(P)` over the P occupied seats, computed over
  the first-win segment; = 0 when P = 1 or when no turn has a defined leader.

**Affects.** §6.2, §4.2, D-18.

---

## 4. Statistical plan

### D-14 — Holm families and primary metric per research question
**Status:** `pinned` · *review B-6 (blocker)*
**Decision.** A new §6.4 table lists, per research question, the ordered
metric family by §6.2 field name and the exact contrast set (arm pairs ×
cells) — and therefore *m*. Holm runs over **metrics × contrasts jointly**.
Primary metrics:

| RQ | Primary metric |
|---|---|
| RQ-1 | dispersion of `rounds_to_first_win` (scale-free form, D-16) |
| RQ-2 | win rate **and** `rounds_to_first_win` |
| RQ-3 | the deviant's win rate in the 1-deviant cells |
| RQ-4 | the interaction contrast named per EX-6 row (D-46) |

**Rationale.** §6.3 mandates "Holm correction within each research question's
metric family" while no section enumerates a family or says whether *m* counts
metrics only or metrics × contrasts. For RQ-1 alone *m* plausibly ranges from
5 to 80 over EX-2's cells — a first Holm threshold anywhere between 0.010 and
0.000625. §6.2 designated a primary metric only for RQ-1 length.
**Affects.** §6.3, all published significance statements, D-15, D-46.

### D-15 — Operational RQ-1 support criterion
**Status:** `pinned` · *review B-6 (blocker)*
**Decision.** RQ-1 ("mandatory capture increases the dynamics/variance of
games") is **supported iff**:

1. the lower bound of the 95% BCa bootstrap CI on the CV ratio of
   `rounds_to_first_win` (mandatory ÷ optional) exceeds 1, **and**
2. at least **2 of 3** of {`lead_changes_per_turn`, comeback rate,
   1 − predictability skill score} have Holm-adjusted 95% CIs excluding zero
   in the dynamism direction.

`captures_total` is reclassified as a **manipulation check** with a pre-fixed
expected direction, not a confirmation conjunct. Any other outcome is reported
as "not supported", with all metric values published either way (D-41).
**Rationale.** §6.3 states the criterion only as a necessary condition
("supported *only if* …"), so no sufficient condition existed anywhere, and
"the dynamics metrics move consistently" carried no threshold, count rule or
CI requirement. `captures_total` cannot be a confirmation conjunct because
mandatory capture raises it by construction.
**Affects.** §6.3, RQ-1, EX-2, `docs/results.md`.

### D-16 — Primary dispersion estimand is scale-free
**Status:** `pinned` · *review B-5 (blocker)*
**Decision.** The primary dispersion estimand is the **CV ratio** of
`rounds_to_first_win` with a BCa bootstrap CI over games. The raw variance
ratio and the mean ratio are reported alongside, so location and scale are
visibly separated. A minimum practically relevant effect is pre-declared at
**CV ratio ≥ 1.05**. Levene / Brown–Forsythe is declared uninformative at
n ≥ 10k and is dropped as a secondary check.
**Rationale.** A pure location shift at constant relative dispersion (+10%
mean, unchanged CV) yields a raw variance ratio of 1.21, whose CI excludes 1
with near-certainty at the pre-registered n. Mandatory capture is very likely
to shift mean game length, so RQ-1's condition would be satisfied by a pure
length effect published as a dynamics effect.
**Affects.** §6.3, D-15, RQ-1, EX-2.

### D-17 — Rule-effect estimands are policy-bounded
**Status:** `pinned` · *review MJ-20*
**Decision.** The bound direction becomes part of the pre-registered estimand,
not a post-hoc caveat. §1 and §6.3 state, and `docs/results.md` repeats beside
every affected number:

- `optional → mandatory` is an **upper bound** on the Schlagzwang effect under
  capture-blind play (and D-44 supplies the matching capture-greedy field, so
  the published result is an interval, not a one-sided bound);
- the `barriers` main effect is a **lower bound** under barrier-blind play;
- `goal_no_jump` is reachable only through canonical move order (D-3), not
  through any policy that values it.

§2.4 gains a **policy-sensitivity column** marking each flag choice-mediated
(`capture_mode`, `barriers`, `goal_no_jump`) or mechanical (`cold_start`,
`entry_attempts`, `bonus_roll_after_quick_entry`).
**Rationale.** §1 calls the restriction to defined policies "a feature (clean
attribution)". The attribution is clean *for the policy*; RQ-1 is precisely
the question where the policy choice sets the magnitude.
**Affects.** §1, §2.4, §6.3, D-44, `docs/results.md`.

### D-23 — Unit of analysis and bootstrap resampling unit
**Status:** `pinned` · *review MJ-10*
**Decision.** The **game** is the independent unit. Every bootstrap resamples
whole summary rows, never seat records; per-seat counters are aggregated at
game level before resampling. Seat-to-seat and strategy-to-strategy contrasts
**within a cell** use the multinomial difference variance (or an equivalent
paired game-level indicator). Wilson intervals are used only for a single
proportion against a fixed reference — which is what AK-4 legitimately does.
Rotation strata are ignored rather than post-stratified (the conservative
choice), and that is stated in §6.3.
**Rationale.** Per-seat win indicators of one game are multinomial (exactly
one is 1), so a seat contrast built from two independent Wilson intervals
understates the SE of the difference: 0.194 pp against the correct 0.224 pp at
p = 0.25, n = 100k. A strategy occupying 2 of 4 seats counted as 2n Bernoulli
trials inflates the effective n twofold.
**Affects.** §6.3, every published CI, D-24, D-40.

### D-24 — Determinism extends to the analysis layer
**Status:** `pinned` · *review MJ-12*
**Decision.** An analysis run takes its own declarative config — input
campaign directory, estimand list, `analysis_seed`, `bootstrap_B`, alpha — and
writes `analysis.json` recording the resolved config plus the SHA-256 of the
input `summary.jsonl`. `bootstrap_B = 10000` for all headline numbers. Every
published interval in `docs/results.md` carries its `analysis_seed`,
`bootstrap_B` and input hash. AK-2 is extended: same analysis config twice →
byte-identical `analysis.json`.
**Rationale.** NF-1's "one master seed determines everything" enumerates only
simulation streams, while §6.3's estimands are randomized throughout. §6.3's
rules are threshold rules ("CI excludes 1"), so a borderline verdict can flip
between runs on identical data — the simulation half byte-reproducible, the
published half not.
**Affects.** NF-1, §6.3, §7.1, AK-2, `analysis/`.

### D-26 — The homogeneous-field symmetry identity
**Status:** `pinned` · *review MJ-9*
**Decision.** Stated once in §6.3: where players = seats and every seat runs
the same policy, seat rotation is an exact automorphism (§2.1's positions are
pure functions of (seats, seat index), turn order is cyclic, the starting
player is balanced), so **each seat wins exactly 1/k for any rule set**.
Consequences, all binding:

- Homogeneous-field win rates are **not evidence** for RQ-2 or RQ-3. Those
  cells contribute battery metrics and reference distributions only.
- RQ-3 win-rate claims come exclusively from the 1-deviant cells and the
  2-player head-to-head cells.
- RQ-2's win-rate estimand is restated as something symmetry does not fix:
  P(win | seat is the starter), and the per-seat profile as a function of the
  flag (D-25).
- EX-5's 6-seat `spread` arm and the 2-player `opposite` arm are declared
  a-priori symmetry checks in the AK-4 family (D-29), not measurements.

**Rationale.** Without this, EX-5 would compare a measured asymmetry against
an identity and publish the difference as "the seating recommendation works".
**Affects.** §6.3, RQ-2, RQ-3, EX-3, EX-4, EX-5, D-25, D-29, D-46.

### D-40 — Power table and n re-allocation
**Status:** `pinned` · *review MJ-11*
**Decision.** §6.3 gains a per-estimand SE/MDES table at the chosen n and the
Holm-adjusted alpha, covering: win-rate main effect, 2-way interaction, 3-way
interaction, CV ratio, comeback rate. The "≈ 0.4 pp" figure in §6.3 is
annotated as applying to a single win rate only.

**Smallest substantively interesting win-rate difference: 0.5 pp** (project
owner's decision). The rule applies **plan-wide, not only to EX-6**: no
pre-registered contrast anywhere in §8 is left below the target. n is derived
from the target, never from the compute budget. This is the win-rate analogue
of D-16's pre-declared minimum relevant dispersion effect.

> "Wir machen nichts schwächer, wir setzen n so hoch wie notwendig."
> — project owner, 2026-07-31

Derivation. Reference values at n = 10k per cell (80% power, two-sided 5%,
before Holm): 1.71 pp for a two-arm win-rate difference at p = 0.25, 2.42 pp
for a 2×2 interaction, 3.43 pp for a three-way. Dividing by
(z₀.₉₇₅ + z₀.₈₀) = 2.80 gives the contrast SEs at n = 10k: 0.611 / 0.864 /
1.225 pp, each scaling as 1/√n. A comeback-rate contrast (p ≈ 0.30) has base
SE 0.648 pp, and a single proportion against a fixed reference (the 1/k
identity of D-26) has base SE 0.433 pp at k = 4, 0.500 pp at k = 2. The
Holm-adjusted multiplier is (z₁₋α/2 + 0.842) with α = 0.05 / (tests in that
research question's family, i.e. metrics × contrasts per D-14).

**The `chosen n` column below is superseded by D-59.** The derivation method is
retained because it is still how n is computed; what changed is the family
sizes it is fed, and the recognition that main effects pool across factorial
cells. D-59 holds the binding figures.

| Campaign | binding contrast | family size | Holm α | multiplier | required n | chosen n *(superseded)* |
|---|---|---|---|---|---|---|
| EX-1 / EX-1b | win rate by turn-order offset | 3 | 0.0167 | 3.236 | 132k | 400k (set by AK-4, D-29) |
| EX-2 | comeback rate, mandatory vs. optional | 96 | 5.21e-4 | 4.314 | 313k | **320k** |
| EX-3 | deviant win rate vs. the 1/k reference | 48 | 1.04e-3 | 4.121 | 170k | **250k** |
| EX-4 | win rate by starting seat, flag vs. baseline | 334 | 1.50e-4 | 4.633 | 321k | **325k** |
| EX-5 | per-seat win rate, pattern and geometry effect | 12 | 4.17e-3 | 3.706 | 245k | **250k** |
| EX-6a–6e | battery-metric contrast, 2-way interaction | 3–8 | 0.00625 | 3.576 | 428k | **450k** |
| EX-6f | win rate, 3-way interaction | 18 | 0.00278 | 3.831 | 881k | **900k** |

EX-3 is set to 250k rather than the derived 170k by explicit instruction —
RQ-3 is a headline question and the extra margin is free. EX-6a–6e carry
battery metrics rather than win rates as their response (win rate is fixed by
D-26 in the homogeneous rows), which costs ~12% more n than the win-rate
figure, hence 450k rather than 400k.

**The binding constraint is multiplicity, not effect size.** At these family
sizes the Holm multiplier ranges from 3.24 to 4.46 against the unadjusted
2.80, so n is fighting the correction rather than the phenomenon. EX-4 is the
clearest case: its 166-test family (83 flag contrasts × 2 metrics) forces
300k/cell, where a family declared as *5 axis main effects × 2 metrics = 10
tests* would need 200k — a 8.4M-game difference from the family definition
alone. This is a real lever and a cheaper one than n, but it is a
**pre-registration** decision (which contrasts are confirmatory and which are
descriptive), not a power decision, and it must be taken in D-14's §6.4 table
before any campaign runs — never after seeing results.

**Consequence of D-46's broad EX-6f.** The 3×4×4 design has 18 three-way
contrasts against the narrow 2×2×3 design's 2, which raises the multiplier
from 3.08 to 3.83 — a 24% larger MDES at equal n, requiring 1.55× the sample
to hold 0.5 pp. That is why 6f runs at 900k.
**Rationale.** §6.3 fixes n with no SE or MDES for any contrast the document
names, so RQ-4 as originally budgeted would mostly return underpowered nulls.
Matching main-effect resolution costs 4× n for two-way and 8× for three-way;
at the NF-2 target 40k games/cell is ~5 s on 8 workers.
**Cross-reference.** The power table is stated for **battery metrics and
deviant-cell win rates**. Under D-26 a homogeneous-field win rate is constant
by construction, so a win-rate power figure for those cells would describe a
response that cannot vary.
**Affects.** §6.3, EX-6, D-46, D-47.

### D-59 — The §6.4 table: confirmatory sets, and n re-derived from them
**Status:** `pinned` · *resolves the D-14 open item* · *supersedes the n values
in D-13, D-40 and D-46*
**Decision.** The project pre-registers **40 confirmatory hypotheses** in four
families. Every other quantity the plan produces is **descriptive**: computed,
published (D-41 requires it), reported with nominal 95% CIs, and explicitly
labelled as not error-controlled. Holm runs within each confirmatory family
only.

| Family | Estimand | Contrasts | Metrics | Tests |
|---|---|---|---|---|
| RQ-1 | dispersion and dynamics of `mandatory` vs. baseline, in the headline cell (4 players, seats 4, all-`RANDOM`) | mandatory − optional; mandatory_extended − optional | CV ratio of `rounds_to_first_win`; `lead_changes_per_turn`; comeback rate; predictability skill score | 8 |
| RQ-2 | **main effect** of each rule axis, pooled over the EX-4 factorial | `cold_start`(2), `capture_mode`(2), `dreimal_wuerfeln`, `bonus_roll_after_quick_entry`, `goal_no_jump`, `barriers`, `bonus_roll_forfeited` = 9 | win rate by starting seat; `rounds_to_first_win` | 18 |
| RQ-3 | deviant win rate against a `RANDOM` field, 4 players | SPREAD, FOCUS_FRONT, FOCUS_REAR each vs. the 1/k reference; FOCUS_FRONT − FOCUS_REAR | deviant win rate | 4 |
| RQ-4 | named interaction contrasts | capture_mode × strategy (2); barriers × strategy (1); capture_mode × players (1); EX-5 pattern effect; EX-5 geometry effect | primary metric per row | 10 |

**Why this is the right structure, not a concession.** RQ-2 asks literally for
the *main effect* of each flag. Treating all 167 EX-4 cell-to-cell contrasts as
confirmatory pre-registers 167 hypotheses that appear in no research question,
and it is what drove the family to 334 tests and n to 325k per cell. Three
consequences follow, and all three favour the small set:

1. **The headline claims get stronger.** Holm's first threshold moves from
   1.5·10⁻⁴ (334 tests) to 2.8·10⁻³ (18 tests) — the same data, more power on
   exactly the questions a claim is made about.
2. **Nothing is measured less or reported less.** Every cell still runs and
   D-41 still requires every §6.2 metric for every cell. What prevents
   cherry-picking is the `prereg-v1` freeze plus the report-everything rule,
   not the size of the correction.
3. **Main effects pool.** This is the largest single effect and it was missed
   in D-40's first derivation. In a full factorial the main effect of an axis
   is estimated from *all* 168 EX-4 cells — 84 per level for a two-level axis,
   56 for a three-level one — so the effective sample per level is 56–84× the
   per-cell n.

**Re-derived sample sizes.** Two tiers: confirmatory cells sized so the
Holm-adjusted MDES of their family's binding contrast is ≤ 0.5 pp at 80% power
(D-40's target, unchanged), and descriptive cells at a uniform n = 20k, which
is twice the specification's original figure and gives a single cell's win rate
an SE of 0.31 pp.

| Campaign | confirmatory cells | descriptive cells | binding contrast | resulting MDES |
|---|---|---|---|---|
| EX-1 / EX-1b | 2 @ 400k | — | set by AK-4's equivalence margin (D-29), not by this table | — |
| EX-2 | 3 @ 250k | 33 @ 20k | comeback rate, family 8, mult 3.576 | 0.49 pp |
| EX-3 | 3 @ 200k | 61 @ 20k | FOCUS_FRONT − FOCUS_REAR, family 4, mult 3.340 | 0.46 pp |
| EX-4 | — (main effects pool over all cells) | 168 @ 20k | 3-level axis main effect, family 18, mult 3.831 | **0.22 pp** |
| EX-5 | 6 @ 250k | 4 @ 20k | per-seat win rate, family 10, mult 3.706 | 0.49 pp |
| EX-6 | 14 @ 400k | 91 @ 20k | 2×2 interaction, family 10, mult 3.706 | 0.49 pp |

EX-4 needs no confirmatory tier at all: at n = 20k its two-level main effects
resolve to **0.18 pp** and its three-level main effects to **0.22 pp**, both
comfortably past the target, because 84 and 56 cells respectively pool into
each level. The 325k figure in D-13 was an artefact of the wrong estimand.

Interaction contrasts are the expensive case and do **not** pool: a named 2×2
interaction uses exactly four cells and carries twice the SE of a main effect
at equal n, which is why EX-6's fourteen confirmatory cells sit at 400k while
its other 91 run at 20k.
**Affects.** §6.3, §6.4 (new), D-13, D-14, D-15, D-40, D-46, D-47, D-41,
`docs/results.md`.

---

## 5. Campaign layer and experiment plan

### D-11 — Default board and seat pattern per player count
**Status:** `pinned` · *review B-3 (blocker)*
**Decision.** `seats = 4` for players ≤ 4; `seats = 6` for players ∈ {5, 6}.
`seat_pattern = adjacent` unless an EX row states otherwise. Every EX row
carries an explicit board + pattern column, and `(seats, seat_pattern,
occupied_seats)` is written into every summary row and forms part of the cell
key.
**Rationale.** §2.4 declares `seats` and `seat_pattern` measured structural
axes and §7.1 makes them config fields, yet EX-1, EX-2, EX-3, EX-4 and EX-6
name only a player count. For players ∈ {2, 3, 4} both boards are admissible
and, whenever players < seats, all three patterns are — so those cells could
not be enumerated, seeded or aggregated.
**Affects.** §2.2, §7.1, §7.2, all EX rows, D-12.

### D-12 — Player-count effects are estimated within a fixed `seats` level
**Status:** `pinned` · *review B-3 (blocker)*
**Decision.** No player-count contrast is published across board sizes. Any
cell set supporting a player-count statement replicates players ∈ {2, 3, 4} at
`seats = 6`, and the 6-player cell is reported only against 6-seat companions.
EX-6's `capture_mode × players` factorial runs entirely at `seats = 6`
(D-46e).
**Rationale.** §2.4's `players ≤ seats` constraint forces every 6-player cell
onto the 48-ring/spacing-8 board, so a naive player-count effect mixes player
count with board geometry — a factor RQ-4 lists separately and EX-5 treats as
headline-sized. This is not fixable by a default; it needs the extra cells.
**Affects.** EX-2, EX-6, RQ-4, D-11, D-47.

### D-13 — EX-4 design: full admissible factorial, no fraction
**Status:** `pinned` · *review B-4 (blocker)*
**Decision.** EX-4 drops the fraction and runs the **complete 84-cell
admissible design**. `entry_attempts` and `bonus_roll_after_quick_entry` are
pinned to their defaults under `cold_start = free_entry` (where they are
provably inert, D-7), and `bonus_roll = true` is admitted only with
`entry_attempts = 3` (D-10). Their effects are reported as **conditional**
effects within the admissible sub-block, never as marginal main effects. The
config validator rejects inadmissible combinations with a named error and
never coerces. §2.4's preamble is corrected: the axes are **nested**, not
independent.

**Enumeration, recomputed after the rulebook verification.** The axis set
changed twice: `entry_attempts` became `dreimal_wuerfeln` (D-51, same
cardinality, corrected semantics and default), and `bonus_roll_forfeited` was
added as a seventh axis (D-56).

`cold_start`(3) · `dreimal_wuerfeln`(2) · `bonus_roll_after_quick_entry`(2) ·
`goal_no_jump`(2) · `capture_mode`(3) · `barriers`(2) ·
`bonus_roll_forfeited`(2) = **288** nominal combinations.

- Admissible (`dreimal_wuerfeln`, `bonus_roll`) pairs are
  {(off, false), (on, false), (on, true)} — 3 of 4 — so 72 are inadmissible
  → **216 admissible**.
- Under `cold_start = free_entry` both entry axes are inert (entering never
  requires a 6, so neither the three-roll recovery nor the quick-entry bonus
  can fire): 72 admissible cells collapse to 24 distinct behaviours → 48
  duplicates.
- **168 well-defined cells.**

**Sample size superseded by D-59.** An intermediate derivation put this
campaign at n = 325k per cell (54.6M games) by treating all 167 cell-to-cell
contrasts as confirmatory. RQ-2's estimand is the *main effect*, which pools
over all 168 cells, so **n = 20k per cell (3.36M games)** resolves a
three-level main effect to 0.22 pp — better than the target the 325k figure
was chasing.
**Rationale.** "Fractional factorial" named no fraction, resolution, defining
relation, generators or alias structure, and a design that is not written down
cannot be pre-registered. No standard regular fraction applies to a nested
design anyway. At 105 s the fraction buys nothing.
**Status change.** With D-46, EX-4 is no longer a screening gate; it is a
descriptive full factorial. Nothing downstream is conditioned on its results.
**Affects.** §2.4, EX-4, EX-6, D-46, D-41.

### D-27 — EX-5 geometry control arm
**Status:** `pinned` · *review MJ-13*
**Decision.** EX-5 gains the cell the plan never listed: **3 players
`adjacent` on the 6-seat board** (seats 0, 1, 2), at the same n as the other
headline arms. The decomposition is pre-registered:

- **pattern effect** = 6-seat `adjacent` vs. 6-seat `spread`
- **geometry effect** = 4-seat `adjacent` vs. 6-seat `adjacent`
- the originally planned contrast is their **sum** and must not be published
  as a pattern effect.

§8 states why the control is required rather than optional: on the 4-seat
board every 3-of-4 occupancy is a rotation of `adjacent`, so no `spread`
counterpart exists there and the confound cannot be broken within that board.
**Rationale.** EX-5's two arms differ simultaneously in seat pattern and in
board (ring 40/spacing 10 vs. ring 48/spacing 8). Ring length dominates game
length and exposure frequency, and §1 RQ-4 lists board geometry as its own
factor.
**Affects.** EX-5, RQ-4, D-26, D-47.

### D-28 — EX-6 row split: homogeneous vs. 1-deviant
**Status:** `pinned` · *review MJ-14*
**Decision.** Every EX-6 row is explicitly one of two designs, never
unqualified "× strategy":

- **homogeneous-field rows** — response = battery metrics. Win rate is 1/k by
  construction (D-26) and is not an admissible response.
- **1-deviant rows** — response = the deviant's win rate; deviant and field
  agent are named per cell.

`players`, `seats` and `seat_pattern` are fixed for every EX-6 row, and the
primary response is named per row (D-14).
**Rationale.** EX-3 distinguishes the two designs carefully; EX-6 wrote
"capture_mode × strategy" with no qualifier and no player count. The two
readings are different experiments, and EX-6 carries RQ-4, whose cells §6.3
calls "the primary evidence".
**Affects.** EX-6, RQ-4, D-14, D-26, D-46.

### D-46 — EX-6 arms pre-registered unconditionally
**Status:** `pinned` · *decided by the project owner against the alternative*
· *review MJ-21*
**Decision.** EX-6's complete arm list is fixed here, before any campaign
runs. EX-4 is demoted from screening gate to descriptive full factorial
(D-13); nothing in the plan is conditioned on prior results, so the entire §8
plan is **confirmatory**. All rows: `seat_pattern = adjacent`, rotation- and
starting-seat-balanced (D-39).

| Row | Design | Cells | n | Games |
|---|---|---|---|---|
| EX-6a | `capture_mode`(3) × homogeneous field(5 agents), players 4, seats 4 | 15 | 450k | 6.75M |
| EX-6b | `capture_mode`(3) × deviant(4: SPREAD, FOCUS_FRONT, FOCUS_REAR, GREEDY_CAPTURE) vs. `RANDOM` field, players 4, seats 4 | 12 | 450k | 5.40M |
| EX-6c | `barriers`(2) × homogeneous field(5), players 4, seats 4 | 10 | 450k | 4.50M |
| EX-6d | `barriers`(2) × deviant(4) vs. `RANDOM` field, players 4, seats 4 | 8 | 450k | 3.60M |
| EX-6e | `capture_mode`(3) × players(2, 3, 4, 6), **all at seats 6** (D-12), all-`RANDOM` | 12 | 450k | 5.40M |
| EX-6f | three-way `capture_mode`(3) × deviant(4) × players(2, 3, 4, 6) at seats 6 | 48 | 900k | 43.20M |
| | | **105** | | **68.85M** |

**Sample sizes superseded by D-59:** 14 cells carrying the RQ-4 confirmatory
interaction contrasts run at 400k, the other 91 at 20k — 7.42M games rather
than the 68.85M in the table above. The cell structure is unchanged.

The five agents in the homogeneous rows are `RANDOM`, `SPREAD`,
`FOCUS_FRONT`, `FOCUS_REAR`, `GREEDY_CAPTURE` (D-44).

**EX-6f is the broad 3×4×4 design** (project owner's decision, against a
narrow 2×2×3 alternative): all three capture modes × all four deviants × all
four player counts, so RQ-4's stated three-way question is answered
completely rather than on a chosen slice. The cost is multiplicity, not
compute — 18 three-way contrasts instead of 2 — which D-40 absorbs by running
this row at n = 900k rather than 400k.
**Rationale.** With EX-6's arms chosen after EX-4's results, every EX-6 number
would be exploratory by construction while carrying the document's RQ-4
headline. The whole §8 plan costs minutes (D-47), so compute never justified
the adaptive design.
**Open for review.** This row contains genuine design choices (which agents in
which rows, EX-6f's narrowing, n allocation) rather than a mechanical default.
It should be read before EX-1 runs.
**Affects.** EX-4, EX-6, RQ-4, §1's pre-registration claim, D-13, D-28, D-41.

### D-47 — EX-2 arm list, and the total compute budget
**Status:** `pinned` · *review B-3, MJ-11, MJ-20*
**Decision.** EX-2's fields become {`RANDOM`, `SPREAD`, `GREEDY_CAPTURE`}
(D-44), boards per D-11. The resolved §8 budget at the NF-2 target
(1,000 games/s/core):

**The budget is denominated in games, not in time.** Runtime is a derived,
currently unvalidated quantity — see the throughput caveat below.

Sample sizes are those of **D-59**, which supersedes the earlier uniform-n
figures of D-13, D-40 and D-46.

| Campaign | Cells | n (confirmatory / descriptive) | Games | share | board |
|---|---|---|---|---|---|
| EX-1 (4 players, seats 4) — D-29 | 1 | 400k | 0.40M | 2.4% | 4-seat |
| EX-1b (6 players, seats 6) — D-29 | 1 | 400k | 0.40M | 2.4% | 6-seat |
| EX-2 — D-59 | 36 | 3 @ 250k / 33 @ 20k | 1.41M | 8.6% | mixed |
| EX-3 (16 homogeneous + 48 one-deviant) — D-59 | 64 | 3 @ 200k / 61 @ 20k | 1.82M | 11.1% | mixed |
| EX-4 — D-13, D-59 | 168 | 20k (main effects pool) | 3.36M | 20.5% | 4-seat |
| EX-5 (6 headline + 4 two-player) — D-27, D-59 | 10 | 6 @ 250k / 4 @ 20k | 1.58M | 9.6% | mixed |
| EX-6 — D-46, D-59 | 105 | 14 @ 400k / 91 @ 20k | 7.42M | 45.3% | mixed, 6f all 6-seat |
| **Total** | **385** | | **≈16.4M** | | |

**Rationale and history.** The plan is ≈5.7× the §8 original (≈2.9M games),
after peaking at 154.3M mid-design. Every step is recorded rather than
absorbed:

| Step | Effect |
|---|---|
| §8 as written | ≈2.9M |
| + `GREEDY_CAPTURE` field (D-44), 6-seat calibration cell and n = 400k calibration upgrade (D-29), EX-5 geometry control (D-27) | ≈6.5M |
| + EX-6 pre-registered unconditionally, broad 3×4×4 (D-46) and D-40's 0.5 pp target applied plan-wide | ≈124.9M |
| + seventh EX-4 axis from the rulebook verification (D-56) | ≈154.3M |
| **− D-59: confirmatory sets defined, main-effect pooling recognised** | **≈16.4M** |

The last row is a 9.4× reduction that *improves* the resolution of every
published claim. It is worth stating plainly why the plan was ever at 154M:
the sample sizes were being derived against an estimand nobody had asked for —
all pairwise cell contrasts as confirmatory hypotheses — rather than against
the main effects and named interactions the research questions actually name.
Defining the confirmatory sets first, and sizing n against those, is the
correct order of operations. It was performed before any campaign ran.

**The growth is multiplicity, not ambition.** Not one contrast in this plan
targets an effect smaller than 0.5 pp. The n inflation comes from Holm
families of 48 to 166 tests, which raise the required multiplier from 2.80 to
between 3.24 and 4.46. Tightening the confirmatory/descriptive split in D-14's
§6.4 table is a legitimate and much cheaper lever than sample size — but it is
a pre-registration decision that must be taken before any campaign runs.

**Sample size is set by the resolution target, not by the budget.** D-40 fixes
n from the smallest substantively interesting effect (0.5 pp). Additional
compute capacity is explicitly *not* a reason to raise n further; doing so
would require a new D-40 decision with its own justification.

**Throughput caveat — no runtime figure in this ledger is validated.** Any
wall-clock number for this plan is `games ÷ (throughput × cores)`, and the
only available throughput is NF-2's *target* of ≥ 1,000 baseline games per
second per core — a goal set for an engine that does not exist yet, not a
measurement, and not a per-game time limit. Two independent uncertainties sit
on top of it:

1. **The target may not be met.** A played-out 4-player game runs roughly
   300–400 turns, each requiring legal-move generation with path checks for up
   to four pieces, an agent decision, a state update, and the per-turn
   `leader(t)` recomputation. That is order 10⁴–10⁵ CPython operations per
   game, which places a tight pure-Python implementation somewhere between
   **100 and 1,000 games/s/core**. NF-2's figure is the optimistic end and
   depends on exactly the int/tuple discipline NF-2 itself prescribes.
2. **The plan is not made of baseline games.** NF-2's target is stated for
   *baseline* games (4 players, 4-seat board, default flags). A large share of
   this plan is not that: EX-6 (45% of all games) is largely 6-seat, which has
   24 pieces instead of 16, a 48-field ring instead of 40, materially more
   turns per game in `play_out` mode with up to 6 players, and a `leader(t)`
   recomputation over 6 seats. EX-6c/6d add barrier path checks. A
   plan-weighted cost of **2–3× the baseline game** is plausible. Note also
   that D-55 changed what a baseline game *is* — starting with one piece
   already on the track shortens the opening — so even NF-2's own reference
   cell is not the one the target was written against.

Multiplying the two bands gives roughly **10 to 140 CPU-hours** for the 16.4M
games — on a 128-core node, between ~5 minutes and ~65 minutes. Quoting a
single figure would be false precision.

**Resolution.** AK-7's benchmark collapses the band, and D-43c already moved
AK-7 into milestone M1 with two cells for exactly this reason: a baseline cell
(4 players, seats 4, all-`RANDOM`) and a worst case (6 players, seats 6,
`barriers` + `mandatory_extended`, all-`SPREAD`), both measured with logging at
the campaign default and with the `leader(t)` recomputation inside the measured
loop. Until those two numbers exist, this ledger states the plan in games only.
If the measured throughput lands at the low end, the response is a ledger row
and an optimization pass — never a silent reduction of n, which D-40 fixes from
the resolution target rather than from the budget.

**Storage.** ≈16.4M summary rows. At an estimated 400–650 bytes per compact
JSON row this is ≈6.6–10.7 GB uncompressed and ≈1–1.5 GB gzipped. D-42's rules
still apply — raw rows are not committed to git — but the compressed
per-campaign artifacts are now small enough to attach to a release rather than
requiring an external archive.
**Affects.** §8, NF-2, AK-7, D-13, D-29, D-40, D-42, D-46, D-48.

### D-38 — Seed derivation scope
**Status:** `pinned` · *review C-16*
**Decision.** Per-game seed = `SHA-256(master_seed ‖ cell_key ‖ game_index)`.
Arms are therefore **independent**, not common-random-number paired, so
§6.3's unpaired BCa and variance-ratio procedures are valid as written. The
`cell_key` construction is defined once (ordered concatenation of every
resolved config field that varies across the campaign) and recorded verbatim
in every summary row.
**Rationale.** NF-1 does not say whether the game index is scoped per cell or
per campaign, and no cell key was defined. The CRN regime would make the
stated procedures conservative rather than wrong, but the choice must be
pinned for the CIs to mean what §6.3 says they mean.
**Affects.** NF-1, §6.3, §7.1, D-23, D-39.

### D-39 — Counterbalancing remainder rule and permutation trigger
**Status:** `pinned` · *review C-17*
**Decision.** Balance block `B = (#arrangements) × (#starting seats)`;
`n_effective = ceil(n_requested / B) · B`. `n_requested`, `n_effective`, `B`,
`rotation_index` and `starting_seat_index` are written into every summary row.
**Full permutations** are used exactly when a cell contains ≥ 2 distinct
non-field strategies; cyclic rotations otherwise.
**Rationale.** §7.3's "equal game counts" is unachievable at the
pre-registered n for several cells (10,000 mod 9 = 1; mod 36 = 28; mod 96 =
16), and "full permutations when players ≤ 4 and the design needs it" had no
trigger. The residual imbalance is statistically irrelevant, but the produced
row count must be a documented function of the config.
**Affects.** §7.3, §7.2, D-6, D-25.

---

## 6. Acceptance criteria

### D-29 — AK-4 as an equivalence test, plus a 6-seat calibration cell
**Status:** `pinned` · *review MJ-16*
**Decision.** Add **EX-1b** (6 players, `seats = 6`, all-`RANDOM`, rotation-
and starting-seat-balanced). AK-4 is restated as an equivalence test applied
to each calibration cell: *for every seat, the two-sided 99% CI for
(p_seat − 1/k) lies entirely within ±δ*. AK-4 is declared a **harness and
geometry gate**, not a substantive seat estimate.

**δ = 0.5 pp, and both calibration cells run at n = 400k** (raised from 100k).
Decided by the project owner against the alternatives (χ² goodness-of-fit gate
at α = 0.001; or δ = 1.0 pp at n = 100k).
**Rationale.** As written AK-4 passes on a failure-to-reject with no
equivalence margin; four per-seat checks give a family-wise spurious-failure
probability of 1 − 0.99⁴ ≈ 3.9%, so a correct engine fails roughly one run in
25. More seriously, §11 contained no symmetry or geometry criterion for the
48-ring board, which carries EX-5's `spread` arm and every 6-player cell — a
wrong start-field spacing or goal-entry offset there would pass all seven
gates, and AK-3 checks only replay self-consistency.
**Why n = 400k.** The margin must clear the CI half-width with room to spare,
or a correct engine fails the gate. At n = 100k the 99% half-width is
2.576 · √(0.1875/100000) = 0.353 pp, leaving only 0.147 pp = 1.08 SE of slack
against δ = 0.5 pp — a fault-free engine would pass a single seat with
probability ≈ 72% and all four seats with probability ≈ 30%, i.e. it would
fail about two runs in three. At n = 400k the half-width drops to 0.176 pp,
leaving 0.324 pp = 4.7 SE of slack, so a fault-free engine passes essentially
always. Cost: 800k games across both calibration cells instead of 200k.
**Known limitation, accepted.** Four per-seat tests carry a family-wise
spurious-failure probability of 1 − 0.99⁴ ≈ 3.9%, which the single-test χ²
alternative would have removed. Retained for interpretability: a per-seat
interval names *which* seat deviates, a χ² statistic does not.
**Affects.** AK-4, EX-1, EX-1b, §8, D-26, D-47.

### D-30 — Analytic calibration gate
**Status:** `pinned` · *review MJ-17*
**Decision.** New gate: on a 1-player configuration, the simulated
distribution of turns-to-first-entry matches the analytic geometric
distribution with `p = 1 − (5/6)^entry_attempts` (chi-square over the first 10
turn counts, n = 100k); and the empirical die-face distribution over a full
cell is uniform within its 99% CI. Under the D-1 default (`entry_attempts =
3`), p = 1 − (5/6)³ = 0.4213 and the mean is 2.374 turns.
**Rationale.** Every gate in §11 is a self-consistency check: rules against
scenarios written by the engine's own author, replay against the same engine,
symmetry against an identity that holds by construction, throughput against a
self-set target. A systematic error in the dice stream, the three-attempts
loop or the entry logic would pass all seven — AK-4 is blind to it because a
uniform bias hits every seat equally. This gate costs seconds.
**Affects.** §11, EX-1, D-1.

### D-31 — Acceptance gates for the analysis layer (AK-8, AK-9)
**Status:** `pinned` · *review MJ-22*
**Decision.**

- **AK-8 (estimator calibration).** On synthetic data with known truth, Wilson
  and BCa intervals achieve nominal coverage within Monte-Carlo error, and the
  Holm procedure reproduces a hand-worked example.
- **AK-9 (metric cross-validation).** For the AK-3 replay corpus, an
  independent reference implementation that walks the event log reproduces
  every §6.2 summary field exactly.

The analysis package gets its own milestone **before EX-2**, since EX-1
already publishes CIs.
**Rationale.** §1 says the measurement series are the product and the games a
by-product, yet all seven acceptance criteria test the by-product. §4.1's rule
that analyses never re-derive numbers when a summary field exists removes the
only redundant path, which makes this cross-check load-bearing: a wrong
`lead_changes` or `winner_rank_at_50` passes AK-1…AK-7 unchanged and goes
straight into `docs/results.md`. AK-9 is the one place §4.1's rule is violated
on purpose.
**Affects.** §11, §13 milestones, `analysis/`, D-24.

### D-32 — AK-5 verification medium and population
**Status:** `pinned` · *review MJ-18, and consequence of D-9*
**Decision.** The invariant is decoupled from the log medium. The engine
asserts it inline on **every** game and writes first-class summary-row
counters: `capture_forcing_offered`, `capture_forcing_violations`,
`forced_extra_lap_offered`, `forced_extra_lap_violations`. A move is counted
as *offered* only when the capture restriction actually applied — i.e. neither
D-9's clearing exception nor its forced-entry exception was in force.

AK-5 is restated as: *summed over all summary rows of every `mandatory` and
`mandatory_extended` cell, `capture_forcing_violations` = 0 and
`forced_extra_lap_violations` = 0*, plus a per-event spot check over the
sampled logs. §7.2's `sample:100` default is unchanged.

Each logged legal-move entry additionally carries `captures: {seat, piece} |
null`, and the `move` event carries `restriction: none | capture | clearing |
forced_entry`.
**Rationale.** Two problems at once. (a) AK-5 demanded "full campaign logs"
while §7.2 writes 100 games per cell — 0.1% of a 100k cell — so the gate would
silently degrade to a spot check while being published as a campaign-wide
invariant. (b) Under D-9 a correct mandatory-mode log legitimately contains
decisions where a capture was offered and a non-capturing entry move was
taken, so AK-5's original wording fails on correct data — and an implementer
would be tempted to "fix" the engine until the gate passes, letting the
acceptance gate silently redefine the rule. The counter formulation is
independent of D-9's direction.
**Affects.** AK-5, §4.1, §4.2, §7.2, D-9, GM-5.

### D-33 — Canonical serialization, shard ordering, engine-version skew
**Status:** `pinned` · *review MJ-19*
**Decision.** Canonical JSON: UTF-8, explicit `\n` line terminator, fixed key
order, `separators=(",",":")`, shortest round-trip float representation — all
part of the log schema version. Shards write `summary-<shard>.jsonl`; the
runner seals a campaign by concatenating in ascending shard index, rows in
ascending global game index. **AK-2's second clause becomes byte-identity** of
`summary.jsonl` and `campaign.json` across worker counts, not set equality of
rows. The replay validator refuses a log whose `engine_version` differs from
the running engine unless `--allow-version-skew` is passed; goldens are
regenerated on every version bump with an NF-5 row; published campaigns record
the engine version they are valid under.
**Rationale.** NF-3 requires output to be a deterministic function of the
config alone, but AK-2 tested only "identical row sets" — set equality passes
while row order, byte-identity and any position-dependent bootstrap vary with
scheduling. "Byte-identical" was asserted without fixing encoding, key order,
separators or float formatting. And §4.3 conditions replay on "header + engine
version" without stating what a version bump does to the checked-in golden log.
**Affects.** LG-3, AK-2, AK-3, AK-6, NF-3, §7.2, D-42.

### D-43c — AK-1 and AK-7 scope corrections
**Status:** `pinned` · *review C-8, C-20, C-21*
**Decision.**

- **AK-1** gains `cold_start` scenarios: the `one_piece_out` initial state;
  `free_entry` entry as a non-forced ordinary move with the roll consumed;
  `free_entry` with entry-clearing still in force; and the inertness assertion
  for `entry_attempts` / `bonus_roll` under `free_entry` — which also defines
  EX-4's valid cell set (D-13). Plus the D-9 lattice scenario ("6 rolled, yard
  piece available, capture available elsewhere") and D-43a's agent-totality
  scenarios.
- **AK-7** — "benchmark met, **or** the deviation ledgered" is unfalsifiable
  and weaker than NF-2's blocking wording. "Measure and ledger" moves into the
  failure remedy. Two benchmark cells are defined: baseline (4 players,
  seats 4, all-`RANDOM`) and worst case (6 players, seats 6, `barriers` +
  `mandatory_extended`, all-`SPREAD`), both measured with logging at the
  campaign default and with the per-turn `leader(t)` recomputation inside the
  measured loop. AK-7 moves into milestone M1.
- **AK-5** moves out of milestone M2: EX-1 is baseline rules
  (`capture_mode = optional`), so AK-5 has no data there. It attaches to the
  first mandatory campaign, or M2 adds a small mandatory smoke cell.

**Affects.** AK-1, AK-5, AK-7, §13 milestones.

---

## 7. Process, engineering and publication

### D-41 — Pre-registration status (new §14)
**Status:** `pinned` · *review MJ-21*
**Decision.** A new §14 records:

1. **Freeze.** The frozen specification is a git tag `prereg-v1`, created
   before EX-1 runs. Every campaign config and every summary row records the
   `prereg_version` it ran under.
2. **Amendments.** Any change to §6 or §8 after the freeze is an amendment
   with its own ledger row here, stating what data already existed when the
   change was made.
3. **Confirmatory/exploratory.** With D-46, EX-1…EX-6 are all **confirmatory**.
   Any campaign added later without a pre-registered arm list is labelled
   exploratory in `docs/results.md`.
4. **All results reported.** `docs/results.md` reports every §6.2 metric for
   every campaign cell, significant or not, with its label attached.

**Rationale.** §1 claims "the metric battery is fixed before any campaign runs,
so results cannot be cherry-picked" while four standard pre-registration
components were absent: no freeze (the document lives in the same mutable repo
as the code), no amendment policy (NF-5 covered rule ambiguities and
optimizations only), no confirmatory/exploratory split despite an explicitly
adaptive plan, and no commitment to report nulls.
**Affects.** §1, §5 NF-5, §8, `docs/results.md`, D-13, D-46.

### D-48 — NF-3's worker cap is lifted; HPC execution
**Status:** `pinned` · *amendment to NF-3, prompted by available HPC capacity*
**Decision.** NF-3's "hard cap 8 workers" is replaced by a **configurable
worker count with no upper bound**. Campaigns may run across multiple HPC
nodes (128 cores each). The determinism invariant is unchanged and becomes the
binding constraint: *output is a deterministic function of the config alone,
never of the worker layout, node count, or scheduling order.*

AK-2's worker clause is strengthened accordingly: **1 worker vs. 8 workers vs.
the maximum configured worker count** must all produce byte-identical
`summary.jsonl` and `campaign.json` (D-33's canonical serialization and
ascending shard/game-index sealing make this achievable).

**No new correctness work is required.** D-38 derives each game's seed as
`SHA-256(master_seed ‖ cell_key ‖ game_index)`, independent of which worker or
node executes it, and D-33 fixes the concatenation order. The 8-worker cap was
a machine-courtesy convention inherited from FitchAsATP, not a correctness
constraint — which is exactly why it can be lifted without touching NF-1.
**Rationale.** D-47's plan is ≈16.4M games, i.e. somewhere between 10 and 140
CPU-hours depending on the measured throughput (D-47's caveat). At the
pessimistic end an 8-worker cap would mean more than a day of wall-clock per
full re-run, which would reintroduce budget pressure on a design that D-40 and
D-59 fix from scientific relevance alone. Lifting the cap removes that pressure
regardless of where the AK-7 benchmark lands — which is the point: the decision
must not depend on a throughput number nobody has measured yet. The cap is
lifted even though the plan shrank 9.4× in D-59, because re-runs after an
engine fix are routine and the correctness argument is unaffected either way.
**Guardrail.** Extra capacity changes wall-clock only. It is not a reason to
raise n (see D-47), to add unregistered arms (D-41), or to re-run a campaign
until it comes out well — the prereg tag and the amendment rule govern that
regardless of how cheap a re-run becomes.
**Affects.** NF-3, AK-2, D-33, D-38, D-47, D-49.

### D-49 — Analysis-layer environment is pinned to a single node
**Status:** `pinned` · *consequence of D-48*
**Decision.** Simulation may fan out across nodes; **analysis does not**. An
analysis run executes single-node in a pinned environment (Python, NumPy/SciPy
and BLAS versions recorded in `analysis.json` alongside D-24's seed, B and
input hash). Re-running the analysis on a different node with a different BLAS
is treated as a new analysis run, not a reproduction.
**Rationale.** D-24 makes the bootstrap reproducible given a seed, but
floating-point reduction order in BLAS-backed operations can differ across CPU
architectures and library builds. Since §6.3's rules are threshold rules
("CI excludes 1"), a borderline verdict could flip between nodes — the same
failure D-24 was written to prevent, reintroduced through the cluster. The
simulation half is unaffected: the engine is integer/tuple state with no
floating-point arithmetic.
**Affects.** D-24, D-48, AK-2, AK-8, `analysis/`.

### D-42 — Data management (new NF-6)
**Status:** `pinned` · *review C-19*
**Decision.** `summary.jsonl` is stored gzipped (`.jsonl.gz`). `campaigns/` in
git holds only `campaign.json` (resolved config + aggregate cells) plus the
compressed summaries under a stated size cap; anything larger is a release
asset or archive deposit referenced by SHA-256 from `campaign.json`. The
reproducibility contract is **master seed + engine version + prereg tag**; raw
rows are a convenience artifact, not the contract.
**Rationale.** The §8 plan produces roughly 6.5M summary rows of 30+ fields —
several GB before event logs — and §13 puts `campaigns/` in the repository
tree with no compression format, size cap, retention rule or archival
location. Discovering this after EX-2 means rewriting history in a repo that
claims byte-reproducible logs. Since NF-2 makes regeneration cost minutes
(D-47), the raw rows do not need to be the durable artifact.
**Affects.** §5, §13, §7.2, D-33, D-47.

### D-43 — UI build target
**Status:** `pinned` · *review C-22, C-23*
**Decision.** The UI builds to a **single self-contained HTML file** with all
JS and CSS inlined: no ES-module entry script, no code splitting, no runtime
fetch of bundled assets. AK-6 opens the built artifact directly from disk.
UI-6's aggregate view reads `campaign.json` — extended with per-cell n, win
counts, CI bounds and pre-binned histograms — rather than `summary.jsonl`;
`summary.jsonl` loading is permitted only per cell with a documented row cap.
**Rationale.** A default `vite build` emits `<script type="module">`, which
browsers refuse to load over `file://` (opaque origin, CORS-governed module
loading), so the shell renders blank — contradicting UI-2's "runs offline from
`file://`". Cheap to pin now, real rework after M3. Pointing UI-6 at
`summary.jsonl` would additionally require reimplementing §6.3's Wilson CIs in
TypeScript, creating a second estimator implementation with no AK-8 coverage.
**Affects.** UI-2, UI-6, AK-6, §7.2, D-24.

### D-43d — Documentation hygiene and repository layout
**Status:** `pinned` · *review C-1…C-4, C-7, C-13, C-14, C-18, C-24, C-25*
**Decision.** Applied to the specification when it is next edited:

- **Cross-reference drift** (nine occurrences from an earlier renumbering) is
  corrected: §1 RQ-2 "§3.3" and §2.3 clause 6 "(§3.3)" → §2.4 (barriers §2.6);
  §1 scope note "§5" and §2.4 "the §5 strategy assignment" → §3; §3.1 "see
  §7.1" → §5/NF-1; §2.5 GM-5.1 "(§10)", §3.2 "(§10)" ×2 → §12; §12 "(§2.5.1)"
  → GM-5.1. A doc lint resolves every §N.M reference against the heading list
  and fails on any unresolved `-?` placeholder.
- **§1 RQ-2's "project baseline (§3.2)"** is disambiguated to the baseline
  **rule set** (§2.3 + §2.4 defaults), with the baseline agent field named
  separately.
- **Identifier families**: §9's items are numbered D-1…D-7 (done, above);
  §6.3's bullets are numbered SQ-1…SQ-6 (win rates, location, dispersion,
  predictability, interactions, sample sizes); §7's items CA-1…CA-3. The lint
  requires every declared family prefix to have at least one instance.
- **§4.1 header** lists `starting_seat` explicitly (D-25), or is marked
  non-exhaustive under "full resolved config".
- **Event-log granularity** is pinned to one file per game before AK-3 and the
  UI loader are built against it; §7.2's prose is replaced by a config field
  `log_events: {mode, k, pinned_game_indices}`.
- **§8 EX-2 headline cells** are named exhaustively rather than "the 4-player
  optional-vs-mandatory pair" (D-47 does this).
- **GM-3.8's goal-column jumping clause** is added to the rulebook-verification
  list; it is currently asserted without a citation.
- **`madnlab/logging/`** is renamed to `madnlab/eventlog/`. Under Python 3
  absolute imports it does not actually shadow the stdlib; the cost is linter
  noise, reader ambiguity and a trap for anyone adding a `sys.path` shortcut.
  Packaging shape pinned: `src/` layout, explicit `__init__.py`,
  `pyproject.toml`.
- **§6.2** notes that `rounds_to_first_win` is measured on a segment whose
  endpoint is the event under study — fine for cross-arm comparison, but it
  must not be read as total game duration.

**Affects.** the specification text, `docs/results.md`, repository layout.

---

## 8. Rulebook verification (2026-07-31)

Three official Schmidt Spiele PDFs were downloaded from `schmidtspiele.de`,
extracted with `pdftotext` and read in full: **Art. 49020/49021** „Standard-
ausgabe" (2006, 2–6 players, two-sided board, 24 figures), **Art. 49324**
„Reise" (2016, 2–4 players), **Art. 51204** (2023 revision, 2–4 players). All
three carry the Schmidt Spiele GmbH imprint. No finding below rests on a
secondary source, a rules portal, or German Wikipedia.

The verification confirmed D-1, D-2 and GM-3.8 — and found that the
specification **misidentifies its own baseline** in two places. Those
corrections are D-51 and D-55.

### D-50 — The baseline is 49020 for structure, 51204 for mechanics
**Status:** `pinned` · *project owner's decision*
**Decision.** "The Schmidt Spiele standard rule set" is not a single document,
so §2.3's baseline is pinned as a **named pair**:

- **Art. 49020/49021 (2006)** supplies structure: player count 2–6 and the
  board geometry of §2.1. It is the only official edition covering more than
  four players, and therefore the only basis the 6-seat board has.
- **Art. 51204 (2023)** supplies mechanical clarifications absent from 49020.
  Each adoption is recorded **individually** as a cross-edition choice and is
  never presented as reading 49020: exact-fit entry into the goal (D-53), the
  no-legal-move fallback (D-57), and the forfeited re-roll (D-56, modelled as
  a flag rather than adopted into the baseline).

| | players | exact fit on goal entry | no-legal-move fallback | 6 unusable → re-roll forfeited |
|---|---|---|---|---|
| 49020 (2006) | **2–6** | — | — | — |
| 49324 (2016) | 2–4 | ✓ | — | — |
| 51204 (2023) | 2–4 | ✓ | ✓ | ✓ |

**Rationale.** Pinning to 51204 alone would leave the 6-seat board — and thus
EX-1b, EX-6e and all of EX-6f — without any official basis. Pinning to 49020
alone would turn three rules the engine needs into unsupported project
choices. The pair keeps the geometry legitimate and the mechanics citable, at
the cost of one honest label per borrowed clause.
**Affects.** §2.1, §2.3, D-53, D-56, D-57, `docs/results.md`.

### D-51 — The three-attempts rule is an optional variant, default OFF
**Status:** `verified-official` · *corrects GM-3.10*
**Decision.** GM-3.10's claim that the three-attempts rule is "baseline, per
Schmidt" is **wrong**. In all three editions „Dreimal würfeln:" appears under
the heading **„Spielvarianten"**, between „Rückwärtsschlagen:" and
„Überspringen im Ziel verboten:". The base rules grant exactly one roll plus
the free follow-up after a 6.

The flag `entry_attempts ∈ {1, 3}` is replaced by
**`dreimal_wuerfeln ∈ {off (default), on}`**, and its semantics are corrected:
it is a **post-capture recovery rule**, not "three tries to get your first
piece out". The rule's own causal clause is „weil alle Figuren geschlagen
wurden". Combined with D-55's setup (one piece starts on the A-field), it
**cannot fire on turn one at all**.
**Rationale.** The popular house rule — three rolls to enter at the start of
the game — is not what Schmidt writes, and implementing it as such would put a
mislabelled rule into the baseline of every campaign. §2.4's preamble claim
that this variant "coincides with the Schmidt baseline" is deleted.
**Affects.** GM-3.10, §2.4, D-1, D-10, D-13, EX-4, AK-1.

### D-52 — The 6 is consumed by a forced clearing move
**Status:** `project-choice` · *rulebook silent* · *project owner's decision*
**Decision.** When the A-field occupant is forced to move on with a 6 (D-2),
that move **is** the turn's move: the waiting yard piece does not also enter on
the same 6. The free follow-up roll after a 6 stands, so the waiting piece
typically enters on the next roll anyway.
**Why this is a choice and not a reading.** The operative word is „erst" in
„muss diese Figur **erst** mit der „6" weitergezogen werden", which is
genuinely readable both as *"that is your move"* and as *"first, before the new
one comes in"*. No official edition disambiguates it. Two arguments support the
chosen reading, and both are recorded **as arguments**, not as citations:
(i) the general turn rule is singular — „Wer an der Reihe ist, würfelt und
setzt **die eigene Spielfigur** um die gewürfelte Augenzahl … vor"; (ii) it
costs almost nothing, because „Wer eine „6" würfelt, hat nach dem Zug einen
weiteren Wurf frei."
**Second, narrower silence — also a project choice.** If the A-field occupant
*cannot* legally move 6 forward, may the yard piece enter on that same 6
instead? Decision: **yes** — the clearing obligation applies only "sobald sie
die Möglichkeit dazu hat", so an impossible clearing move does not block the
ordinary forced entry. D-2 as drafted already conditions on the clearing move
being legal.
**Affects.** D-2, D-9, GM-3.3, `dice_rolls`, AK-1.

### D-53 — `goal_no_jump` confirmed as a variant; GM-3.8 narrowed to entry
**Status:** `verified-official`
**Decision.** Jumping over own pieces inside the goal column is **allowed in
the baseline** — 51204 and 49324 base rules: „Spielfiguren können im Ziel
übersprungen werden."; 49020: „Spielsteine können übersprungen werden." The
prohibition is an explicit optional variant in all three editions, so
`goal_no_jump` is correctly modelled as off-by-default.

Two corrections to the specification:

1. **The variant has a second sentence the spec does not model.**
   „Überspringen im Ziel verboten: Auf den Zielfeldern dürfen keine
   Spielfiguren übersprungen werden. **Die letzte Figur, die „nach Hause
   kommt", kann nur auf Feld a ins Ziel einrücken.**" That clause is part of
   the flag's semantics and must be implemented with it.
2. **GM-3.8's exact-fit wording is broader than the rulebook.** What is
   verified is exact fit on **entry** into the goal column — „In die 4
   Zielfelder kann nur mit einem passenden Wurf hineingezogen werden."
   (51204; 49324 equivalent). Overshoot *within* the column is a separate
   question the rulebook does not address — see D-54. GM-3.8 is reworded to
   "entry into the goal column requires a fitting roll".
   **Edition note:** this sentence is absent from 49020 entirely, so adopting
   it is a D-50 cross-edition choice, not a reading of the Standardausgabe.

Also confirmed in all three editions and worth recording: goal fields are
counted individually when advancing („Auch die Zielfelder werden beim
Vorrücken einzeln gezählt"), and no piece may enter a foreign goal column
(„Fremde Zielfelder dürfen nicht betreten werden").
**Affects.** GM-3.8, `goal_no_jump`, D-1 note 2, D-50, D-54, AK-1.

### D-54 — Overshoot inside the goal column: the move is not generated
**Status:** `project-choice` · *rulebook silent*
**Decision.** A roll that would carry a piece already inside the goal column
past the last goal field produces **no legal move for that piece**. No
bounce-back, no forfeiture semantics.
**Why this is a choice.** No edition addresses a piece already in the goal
whose roll overruns the end — a piece on field c rolling a 3 appears nowhere in
49020, 49324 or 51204. Two textual hints point this way but neither is
dispositive, and both are recorded as inference: „Auch die Zielfelder werden
beim Vorrücken einzeln gezählt" fixes how far a piece moves but not what
happens when the count runs off the end; and the „noch mit einer „1"
vorrücken könnte" example sits **inside the optional Dreimal-würfeln variant**,
so it is a worked example of a variant, not a base-rule statement.
**Affects.** GM-3.8, D-53, `legal_moves`, AK-1.

### D-55 — Baseline `cold_start` corrected to `one_piece_out`
**Status:** `verified-official` · *project owner's decision* · *corrects §2.4*
**Decision.** The default becomes **`cold_start = one_piece_out`**: each
player starts with one piece on the own A-field and three in the yard, and a 6
is required to bring the remaining three in. `strict` is demoted from default
to an ordinary variant arm.
**Verified against.** 49020 Spielvorbereitung, materially identical in 49324
and 51204:

> „Jeder Spieler erhält 4 Steine einer Farbe. **Einen Stein stellt er auf das
> Feld A seiner Farbe, die übrigen drei werden auf die gleichfarbigen B-Felder
> gesetzt.**"

**What was wrong.** §2.4 labels `strict` "the Schmidt baseline" and
`one_piece_out` "the common softened house setup". The two are **inverted**:
`one_piece_out` is literally the official setup, and `strict` — all four
pieces in the yard — appears in no official edition. §2.4's preamble sentence
about variants that "coincide with the Schmidt baseline (cold start, three
attempts)" names the only two cases where they demonstrably do not, and is
deleted along with D-51.
**Consequences.**
- Every "measured against the project baseline" statement (§1 RQ-2, EX-4)
  now refers to a different reference arm. `strict` becomes a measured arm.
- D-2's clearing duty fires from turn one, which is the correct Schmidt
  dynamic and materially changes opening play.
- Baseline game length, and therefore RQ-1's `rounds_to_first_win`
  distribution, shifts. No pre-registered threshold changes (D-15/D-16 are
  ratios), but no pre-EX-1 intuition about game length carries over.
- `capture_mode = optional` needs no correction: the base rules say
  expressly „Es herrscht aber kein Schlagzwang."
**Affects.** §2.3, §2.4, §1 RQ-2, D-7, D-13, D-51, all EX rows, AK-1.

### D-56 — `bonus_roll_forfeited` as a new variant axis
**Status:** `pinned` · *project owner's decision*
**Decision.** GM-3.3 keeps its baseline form (a 6 always grants one extra
roll). 51204's contrary clause — „**Können die 6 Felder nicht gezogen werden,
entfällt das erneute Würfeln.**" — becomes a named flag
`bonus_roll_forfeited ∈ {false (default), true}` and enters EX-4 as a seventh
axis.
**Rationale.** This is a genuine difference between official redactions (absent
from 49020 and 49324), not an ambiguity. Deciding it silently in either
direction would bury a real rule difference; modelling it as an axis matches
the project's own logic of making every rule a measurable dimension. Cost: one
more EX-4 axis (D-13).
**Affects.** GM-3.3, §2.4, D-10, D-13, D-50, EX-4, AK-1.

### D-57 — No-legal-move fallback
**Status:** `verified-official` (51204) · cross-edition adoption per D-50
**Decision.** GM-3.9's compulsory-move rule is confirmed and its fallback
stated per 51204: „Wurde kein passender Wurf gewürfelt, muss mit einer anderen
eigenen Spielfigur gezogen werden. Ist das nicht möglich, bleiben die Figuren
stehen und die nächste Person ist an der Reihe."
**Edition note.** 49020 and 49324 are silent on the fallback cascade; adopting
it is a D-50 cross-edition choice.
**Affects.** GM-3.9, `passes_by_seat`, D-50.

### D-58 — The barriers variant is official
**Status:** `verified-official`
**Decision.** GM-6.1's stacking exception is confirmed as an official variant
in all three editions: „Als Ausnahme zur Grundregel dürfen zwei Spielfiguren
einer Farbe auf einem Feld stehen." Any blanket statement in the spec that two
pieces never share a field is therefore true of the Grundregeln only and must
be qualified.
**Affects.** GM-3.6, GM-6, D-4, D-34.

---

## 9. Implementation decisions (M1)

### D-60 — Exactly one entry move is generated per turn
**Status:** `pinned` · *found by the M1 smoke tests, 2026-08-01*
**Decision.** When a seat has pieces in the yard and entering is legal,
`legal_moves` generates **exactly one** `ENTER` move, for the **lowest-index**
yard piece — not one per yard piece.
**Rationale.** Pieces in the yard are indistinguishable, so one move per yard
piece puts behavioural duplicates in the legal set. This is not cosmetic:
`RANDOM` chooses uniformly over `legal`, so with four pieces in the yard and
one other legal move, entering would be chosen with probability 4/5 instead of
1/2 — a bias proportional to how many pieces are still in the yard, present in
every campaign containing a `RANDOM` field, and largest exactly in the opening
and after a capture. It would also inflate `SPREAD`'s entry preference and
distort the RQ-1 dynamics metrics through the capture-recovery path.
**Consequence for the log.** The `move` event records which piece entered, and
that piece is now always the lowest-index yard piece rather than an agent
choice. Nothing downstream depends on the identity — yard pieces are
interchangeable by construction — but the replay validator's event-stream
equality does, which is why the rule is "lowest index" rather than "any".
**Generalization to check.** Any other place where indistinguishable options
could produce duplicate legal moves would bias a uniform-choosing agent the
same way. The M1 engine review covers this explicitly.
**Affects.** GM-7, §3.2 `RANDOM` and `SPREAD`, LG-3, AK-1.
**Superseded in scope by D-61**, which generalizes the rule from yard pieces
to any co-located pieces. D-60's tie-break and its rationale stand unchanged.

### D-61 — One move per distinct origin position (generalizes D-60)
**Status:** `pinned` · *blocker found by the M1 engine review, 2026-08-01*
**Decision.** `legal_moves` emits at most **one move per distinct origin
position per seat**, for the lowest global piece index — the same tie-break
D-60 uses, so LG-3's replay event-stream equality stays well defined.
**What D-60 missed.** D-60 fixed the yard case with a boolean guard and closed
with "any other place where indistinguishable options could produce duplicate
legal moves would bias a uniform-choosing agent the same way". There is
exactly one other place: under `barriers`, two of a seat's pieces stand on one
ring field, and since `Board.ring_field` is injective over `1..ring_length`
they necessarily share a position. Move generation reads only
`(pos, seat, roll, rules, occupancy)` and never the piece index, so they
produced identical `Move` records differing only in that index — through all
three generating branches (ring, goal entry, extra lap) and into the clearing
and forced-capture filters.
**Measured impact, which is why this was a blocker and not a tidy-up.**
`RANDOM` chooses uniformly over `legal`, so the barrier-breaking option
carried weight 2 against every other option's 1: uniform agents broke barriers
at roughly twice the intended rate while formation stayed unbiased, i.e. a
one-directional bias. Three independent random-play harnesses put it at
3.1–3.4% of all decisions on the 4-seat `barriers = true` board (6.6% of
decisions with more than one option) and **−15% to −16.4% on
`barrier_turns`** — against D-40's 0.5 pp relevance threshold. Affected
pre-registered cells: RQ-2's `barriers` main effect (84 EX-4 cells), RQ-4's
confirmatory `barriers × strategy` interaction (EX-6c/6d, several at n = 400k
with a 0.49 pp MDES), and the D-22 barrier battery. It also falsified §1.1's
stated estimand: the barrier main effect was supposed to be a *clean* lower
bound under barrier-blind play, and a biased bound is not that.
**Implementation.** A `seen_positions` set skipped unconditionally at the top
of the per-piece loop, rather than a per-branch emit guard: two pieces at the
same position either both produce a move or both produce none, so processing
the second is redundant either way, and the unconditional form cannot miss a
branch. Zero cost when `barriers = false`.
**The invariant to test, which is stronger than the rule.** Every returned
move must lead to a **distinct successor state**, judged on the moving seat's
own position multiset. That is checkable in every arm rather than only under
barriers, and it guards against the next variant of this bug rather than this
one. Verified over 8,000 decision points across 36 rule sets and both boards.
**Affects.** GM-7, §1.1, §3.2, §6.2 barrier battery, LG-1, LG-3, AK-1, D-60.

### D-62 — Domain of `roll`
**Status:** `pinned` · *review, minor*
**Decision.** `legal_moves` is defined on `roll ∈ 1..6` (GM-3.1, one standard
d6) and raises a named `ValueError` outside it. Independently, the goal branch
checks the **lower** bound of its target index, not only the upper one, so a
`GOAL` record whose `to_pos` falls back onto the ring — violating the position
encoding every consumer relies on — cannot be constructed at all.
**Rationale.** A named error rather than an assert: the check is once per call
against roughly 520 calls per game, which is not where NF-2's budget goes, and
`-O` silently removing a domain guard from the one function GM-7 makes
authoritative is a bad trade.
**Affects.** GM-7, D-54, AK-1.

### D-63 — Domain of `seat`, and what `legal_moves` knows about occupancy
**Status:** `pinned` · *review, minor*
**Decision.** `legal_moves` is defined for `0 <= seat < board.seats` and
raises a named `ValueError` outside it. It is deliberately **blind to which
seats are in play**: the game loop skips seats outside `seats_in_play`, as
`initial_state` already pins.
**Rationale.** Without the check a negative seat reads another seat's pieces
through Python's negative indexing and returns a plausible-looking move — a
silent wrong answer rather than a loud failure.
**Open for M2.** Whether `seats_in_play` belongs in `GameState` is a design
question for the game loop, not an M1 fix.
**Affects.** GM-7.

### D-64 — Domain of `Board.ring_field`, and the load-bearing modulo
**Status:** `pinned` · *review, minor*
**Decision.** `pos` may exceed the ring length and is reduced modulo it. The
modulo is **required**, not defensive: `mandatory_extended`'s extra-lap path
scan walks positions up to `ring_length + 5` and relies on them wrapping onto
the correct lap fields.
**Why this is worth a row.** The obvious shape of an NF-2 optimization pass is
a precomputed per-seat lookup table indexed `1..ring_length`. That would break
exactly the barrier path checks in the one arm carrying the forced-extra-lap
counters, and nothing else — a failure that would look like a barrier bug in a
capture arm. `Board.goal_entry_field` is now expressed through `ring_field` so
the seat offset has one definition.
**Affects.** GM-1, GM-5, NF-2.

### D-65 — Semantics of `seat_pattern = spread`
**Status:** `pinned` · *review, minor*
**Decision.** `spread` means **maximally even spacing**, `step = seats //
players`, requiring `players` to divide `seats`. §2.2's prose is amended to
match; even spacing rather than a literal "every second seat" is the property
EX-5 tests.
**Rationale.** The two readings agree on the only spread configuration §8
instantiates — 3 players on the 6-seat board gives (0, 2, 4), §2.2's own
worked example — and diverge only at (6 seats, 2 players), which no measured
cell uses. Nothing measured changes; what is closed is the possibility of the
pattern name and the tuple written into a cell key disagreeing once configs
outside §8 exist.
**Affects.** §2.2, §7.1 cell keys, EX-5.

### D-66 — Where AK-8b's 1-player configuration comes from
**Status:** `pinned` · *review, minor*
**Decision.** `occupied_seats` keeps its `players >= 2` floor — that is §2.4's
measured-axis range and all three seat patterns are degenerate at one player.
AK-8b's single-player analytic calibration cell builds its seat tuple by
passing it to `initial_state` directly, which is a first-class path that never
touches the helper. The player-count guard is split so each bound carries its
own message and citation.
**Affects.** §2.2, AK-8b, D-30.

### D-68 — AK-7 result, and NF-2 restated per turn
**Status:** `pinned` · *amends NF-2* · *measured 2026-08-01*
**Result.** AK-7 **missed**: 235–282 games/s on the baseline cell and 32–34 on
the worst case, against NF-2's 1,000.
**Why the target as written is not one budget.** The two cells differ 6.5× in
*game length* — 442 turns against 2,894 — because a 6-player play-out game is
simply longer. Per turn they are within 1.3× of each other (8.0 µs against
10.3 µs). NF-2's figure is stated per game and calibrated on baseline games,
so it silently means a different budget in every cell, and no optimization can
close a 32× gap that is mostly a rule property.
**Amendment.** NF-2's target is restated as **≤ 2.3 µs per turn** (the per-turn
equivalent of 1,000 baseline games/s). Measured: **8.0 µs**, i.e. 3.5× over —
which is the quantity an optimization pass can actually move.
**NF-2's blocking clause is lifted.** "Optimized before any feature work
continues" was written when NF-3 capped workers at 8. D-48 removed the cap,
and the D-59 plan measures at **60 CPU-hours — 28 minutes on one 128-core
node, 7 on four**, weighted over twelve representative configurations rather
than extrapolated. Performance is therefore not on the critical path and does
not gate AK-1 or the milestones after it.
**Optimization candidate, recorded not acted on.** `_ring_occupancy` is
rebuilt from scratch on every `legal_moves` call (~78k calls per 150 baseline
games) and drives most of the 586k `ring_field` calls. Carrying occupancy
incrementally is an M2 design question at the `GameState` boundary, and it
should run against a green AK-1 suite rather than blind.
**Affects.** NF-2, NF-3, AK-7, D-43c, D-48, D-59.

### D-69 — Stalemate: a game with no legal move anywhere ends
**Status:** `pinned` · *found by AK-3's random-config sweep, 2026-08-01*
**Decision.** If no unfinished seat has a legal move on **any** die value, the
game ends as a **stalemate**. Ranks fall back to total progress — the rule §6.1
already gives `first_winner` — with ties in ascending seat order. `stalemate`
is a summary-row field.
**Why the cheap test is not enough.** A round in which nobody moves is
ordinary, not a deadlock: under `strict` a round where no one rolls a 6 has no
legal move anywhere. Only the all-die-values test distinguishes the two, so the
round counter is the trigger and the six-value scan is the decision.
**Affects.** GM-3.9, GM-3.11, §6.1, LG-2.

### D-70 — Abandonment: the turn bound is an outcome, not an error
**Status:** `pinned` · *found by AK-3's random-config sweep, 2026-08-01*
**Decision.** A game that reaches **20,000 turns** with more than one seat
unfinished is **abandoned**, ranked by progress like a stalemate, and flagged
`abandoned` in the summary row. Exceeding the bound is *not* an exception and
not a defect signal.
**Why.** AK-3's sweep produced games that never end in practice under
`cold_start = free_entry` + `capture_mode = mandatory` at 6 players. The
mechanism is not a deadlock — pieces keep moving — but a restoring force:
free re-entry makes a captured piece cost almost nothing, mandatory capture on
a crowded 48-ring board makes captures constant, and progress toward the goal
is undone faster than it accumulates. After 20,000 turns three of six seats
still had nothing in the goal. Such a game would terminate eventually; its
expected length is astronomical.
Raising on it would crash a campaign on a property of the arm. Recording it
makes the rate measurable, which is what this project does with everything
else.
**Measured, so the bound is not arbitrary.** Every cell the D-59 plan actually
contains terminates:

| cell | abandonment | mean turns | longest |
|---|---|---|---|
| EX-1b 6s/6p all-`RANDOM` baseline | 0% | 1,218 | 1,721 |
| EX-2 6s/6p all-`RANDOM` mandatory | 0% | 1,783 | 3,014 |
| EX-2 6s/6p all-`GREEDY_CAPTURE` extended | 0% | 1,964 | 2,786 |
| EX-6f 6s/6p all-`SPREAD` extended + barriers | 0% | 2,808 | 4,286 |
| EX-6f 6s/6p mixed, extended + barriers + no-jump | 0% | 2,435 | 3,829 |
| *(control)* `free_entry` + mandatory, 6 players | **100%** | — | — |

The bound is ~4.7× the longest game observed in any planned cell. At 4 players
— which is what EX-4 actually runs, and the only campaign containing
`free_entry` — **none** of the 36 axis combinations abandons or stalemates;
`free_entry` + mandatory is merely slow there (1,700–2,400 turns against the
baseline's 442). So the pathological combination is not in the plan.
**Binding on the analysis layer.** No estimand may be published from a cell
with a non-negligible abandonment rate without stating it, since abandoned
games have no winner and their ranks come from a different rule.
**Affects.** GM-3.11, §6.1, LG-2, EX-4, the analysis layer.

### D-71 — `pass` events are per roll; `passes_by_seat` counts turns
**Status:** `pinned` · *found by AK-9, 2026-08-01*
**Decision.** §4.1's `pass` event is emitted **once per unusable roll**;
§6.2's `passes_by_seat` counts **turns in which no legal move existed**. A turn
of three attempts that never moves is *one* pass and *three* events. Any
analysis deriving pass counts from an event log must group by turn — a turn
boundary being a `roll` event with `attempt == 1`.
**How it surfaced.** The two implementations disagreed the first time AK-9 ran
them against each other: the game loop counted turns, the event-log
re-derivation counted events, and the gap was exactly the number of extra rolls
inside pass turns. Neither number is wrong; they answer different questions,
and nothing in §4.1 or §6.2 said so.
**Why it matters beyond this field.** `passes_by_seat` and
`entry_waits_by_seat` are the two §6.2 counters most exposed to the
`dreimal_wuerfeln` axis, which multiplies rolls per turn. Counting events would
have made an EX-4 axis look like it changed pass behaviour when it had only
changed how many dice were thrown.
**This is what AK-9 is for.** §4.1 forbids analyses from re-deriving a field
the summary row already carries, which removes the only redundant path. AK-9
is the one place that rule is broken on purpose, and the first thing it did was
find a real definitional divergence.
**Affects.** §4.1, §6.2, `analysis/reference.py`, AK-9.

### D-72 — AK-4 reports *inconclusive* separately from *failed*
**Status:** `pinned` · *found by the AK-5 smoke run, 2026-08-01*
**Decision.** The AK-4 equivalence test returns three verdicts, not two:
**PASS**, **FAIL**, and **INCONCLUSIVE**. It is inconclusive when the CI
half-width is not smaller than the margin δ, in which case the test cannot pass
on *any* data. An inconclusive cell does not fail the campaign, and the report
says what n would resolve it.
**How it surfaced.** The AK-5 smoke cells run at n = 20,000, where the 99%
half-width is 0.784 pp against δ = 0.5 pp. Every seat was reported FAIL and the
campaign verdict was FAIL — on data whose largest deviation was 0.53 pp, well
inside anything the test could have distinguished.
**Why this is the same error as the one D-29 fixed, pointed the other way.**
D-29 replaced the original AK-4 because it passed on a *failure to reject*, so
a cell too small to reject anything passed automatically — "no evidence of
asymmetry" read as "evidence of symmetry". The equivalence form removes that,
and introduces the mirror: a cell too small to *establish* equivalence fails
automatically — "cannot conclude" read as "concluded negative". Both conflate
the power of the instrument with the state of the world, and a gate that does
either is worse than no gate, because its verdict looks like evidence.
**Scope.** AK-4 is a calibration gate (D-29) and belongs to the calibration
cells. Running it on every cell of every campaign is harmless once inconclusive
is distinguished, and is worth keeping: a large non-calibration cell that
*does* show asymmetry beyond δ is something the project wants to hear about.
**Affects.** AK-4, D-29, `analysis/aggregate.py`.

---

## 10. Pre-registration freeze

### D-73 — The `prereg-v1` freeze, and the data discarded to make it honest
**Status:** `pinned` · *amendment under §14.2* · *2026-08-01*

**Defect.** §14.1 requires the tag `prereg-v1` to exist **before EX-1 runs**.
It did not. `PREREG_VERSION` in `run/game.py` was the placeholder `"unfrozen"`,
and it stayed that way through M3 and M5: EX-1, EX-1b and the AK-5 smoke
campaign ran under it, and five HPC campaigns were submitted under it.
Separately, `campaigns/ex2..ex6.json` — the §8 plan the runs were executing —
were untracked, so a tag created at that moment would not even have covered
the plan under test.

**What §14.2 requires stated: the data that existed when this amendment was
made.** At the moment of the freeze there existed
- `campaigns/results/ex1-*`, `ex1b-*` and `ak5-*`: 800,002 games of
  calibration plus the AK-5 smoke cell, all stamped `unfrozen`;
- one completed HPC campaign, EX-5 (1,580,012 rows), and four partial ones
  (EX-2, EX-3, EX-4, EX-6) cancelled ~10 minutes in, likewise `unfrozen`.

**No confirmatory result had been read.** Nothing beyond AK-4/AK-5 gate
verdicts and throughput lines had been computed from any of it, and no §6.4
hypothesis had been evaluated. The freeze therefore still precedes the
analysis, which is the property pre-registration actually protects.

**Decision.** The tag is created now, at the commit that carries the §8 plan
and the corrected constant, and **every campaign is re-run under it**. The
`unfrozen` data is discarded rather than relabelled. Runs are deterministic
from the master seed (NF-6), so regeneration costs wall-clock and nothing
else — which is exactly why relabelling would have been the worse trade: it
saves an hour and buys a provenance claim that no longer matches the bytes.

**Why not simply document the deviation.** That was the cheaper option and it
is defensible — the substance was intact. It was rejected because §14's whole
function is to make "the plan predates the data" checkable by someone who does
not trust the authors, and a `prereg_version` field reading `unfrozen` on
every row of the published dataset defeats that for the sake of one hour of
cluster time.

**Consequence for the record.** This row is the permanent trace of the
deviation: the published dataset carries `prereg-v1` throughout, and the fact
that an earlier `unfrozen` generation existed and was discarded is recorded
here rather than being invisible.

**Affects.** §14, D-41, `run/game.py`, every campaign, `docs/results.md`.

---

### D-74 — AK-4's gate applied outside its scope, and its report contradicted itself
**Status:** `pinned` · *post-freeze code fix* · *2026-08-01*

**Two defects, found by running the campaigns.** Analysis jobs for EX-3, EX-5
and EX-6 exited 1.

1. **The report contradicted its own verdict.** `AK4Result.verdict` correctly
   returns `INCONCLUSIVE` when the CI half-width exceeds the margin, but
   `report()` ended with `'PASS' if self.passed else 'FAIL'`, printing **FAIL**
   three lines below its own sentence *"This is not evidence of asymmetry."*
   D-72 was implemented in the property and missed in the line a reader
   actually trusts.
2. **The gate ran outside its scope.** §11 defines AK-4 "for every calibration
   cell (EX-1, EX-1b)". The CLI applied it to every cell of every campaign and
   let any conclusive failure set the exit code — with a comment on that very
   line calling it a calibration gate. D-72 had judged campaign-wide reporting
   "harmless once inconclusive is distinguished"; that was right about
   under-powering and incomplete about cells that are **asymmetric by design**.

**Why the failures were not engine faults.** The gate's null is *every seat
wins 1/k*. It holds only where seats are exchangeable by construction, and the
failing cells were exactly the ones where they are not:

- **EX-5's adjacent arms.** Three players sitting adjacent leave one of them a
  long run of ring containing no opponent entry field. `6s-adjacent/spread`
  measured 25.0 / 39.0 / 36.0 %. The evenly-spaced control passes
  (`6s-spread/random` 33.2 / 33.3 / 33.5 %). This *is* EX-5, and D-27 put the
  `6s-adjacent` control in the plan precisely to separate board size from
  seating pattern. The gate was firing on the finding.
- **EX-3's deviant cells.** One seat plays a different policy on purpose, so
  1/k is not the reference its win rate belongs against — that comparison is
  RQ-3's estimand.

**Fix.** `seats_exchangeable(occupied, seats, agents)`: identical agents **and**
equal cyclic gaps between occupied seats. Cells failing it are still reported
in full — D-72's descriptive value stands, and an unexpected asymmetry is still
something the project wants to hear about — but they do not gate.

**Why this is not moving the goalposts after seeing the data.** The check that
matters: **the calibration cells pass, and passed before this change.** EX-1
(four seats, half-width 0.176 pp) and EX-1b (six seats, 0.152 pp) are green on
every seat. Not one interval, rate or CI changes anywhere — the fix alters one
printed word and which cells set an exit code, nothing computed. And §11
already scoped AK-4 to the calibration cells, so this moves the code to the
frozen spec rather than the spec to the code.

**Root cause.** AK-4 and AK-5 had **no tests at all**. Both defects are
invisible to ruff and mypy because both are semantically well-formed. Added
`tests/test_ak4_gate.py`: the trichotomy, the report-line agreement, and nine
exchangeability cases including both EX-5 arms and a deviant cell.

**Data that existed when this was made (§14.2).** All eight campaigns had run
under `prereg-v1` and their `analysis.json` files existed. No §6.4 hypothesis
had been evaluated. The re-analysis reuses the same summary rows — the engine
did not re-run, because nothing about the engine changed.

**Affects.** §11 AK-4, D-27, D-29, D-72, `analysis/aggregate.py`, `run/cli.py`.

---

## Open items

**None.** Both rows that stood here are resolved, and the table is empty at the
`prereg-v1` freeze (D-73) — which is the point: a pre-registration cannot be
frozen while an open item blocks the freeze.

*Resolved 2026-08-01:*
- **NF-2 / AK-7** — AK-7 was run. D-68 records the measurement (235–282
  games/s baseline, 32–34 worst case), restates NF-2 per turn because the
  per-game figure meant a different budget in every cell, and lifts the
  blocking clause. The HPC runs since then measured 2,700–9,000 games/s on 48
  workers, well inside the plan.
- **§2.4, §2.3, §1, §6** — the specification was rewritten as version 2 before
  the freeze. `cold_start = one_piece_out` is now labelled the official setup
  (§2.4), the three-attempts rule is a variant (D-51), §6.4 carries the 40
  confirmatory hypotheses, and §8 carries the re-derived sample sizes.

<details>
<summary>The two rows as they stood</summary>

| Id | Item | Blocks |
|---|---|---|
| NF-2 / AK-7 | **Early indication: the throughput target is missed by ~4–5×.** Two independent toy loops over the M1 engine — no logging, no `leader(t)`, no event log — measured **199 and 235 games/s** single-core at ~520 `legal_moves` calls per baseline 4-seat game, i.e. 5.0–5.5 µs/call against NF-2's implied 1.91 µs budget. This is **not** AK-7: those loops omit exactly the costs D-43c requires inside the measured loop. NF-2 pre-authorizes an optimization pass plus a ledger row as the remedy, and D-43c places AK-7 in M1, so it is run before the game loop is written against a cost model that is about to change. **Plan impact is bounded**: at the measured rate D-59's 16.4M games is ≈23 CPU-hours, ≈11 minutes on one 128-core node under D-48. Structural questions (incremental occupancy carried in `GameState` vs. rebuilt per call) are taken with the AK-7 number in hand, not before. | game loop |
| §2.4, §2.3, §1, §6 | The specification text still carries the corrected claims (D-51, D-55: `strict` labelled "the Schmidt baseline", three attempts labelled "baseline, per Schmidt", the §2.4 preamble sentence about variants that "coincide"), and does not yet contain §6.4 (D-59) or the corrected §8 sample sizes. The ledger is authoritative until the spec is rewritten, which must happen **before** the `prereg-v1` freeze (D-41). | D-41 freeze |

</details>

*Resolved 2026-07-31:*
- D-14 settled by D-59: confirmatory sets defined per research question, all n
  re-derived against them, plan reduced from 154.3M to 16.4M games with better
  resolution on every confirmatory claim.
- The D-40 resolution target applies plan-wide, not only to EX-6.
- Rulebook verification complete (§8 above). D-1, D-2 and GM-3.8 are
  `verified-official`; D-52 and D-54 are recorded as project choices on
  questions where the rulebook is demonstrably silent; D-51 and D-55 correct
  two baseline misidentifications in the specification.

## Source documents

| Art. | Edition | URL |
|---|---|---|
| 49020 / 49021 | Standardausgabe, 2006, 2–6 players | `schmidtspiele.de/files/Produkte/4/49020 - Standardausgabe/49020_49021_Mensch_aergere_Dich_nicht_DE.pdf` |
| 49324 | Reise, 2016, 2–4 players | `schmidtspiele.de/files/Produkte/4/49324 - Reise Mensch ärgere Dich nicht®/49324_Mensch_aergere_Dich_nicht_REISE_DE.pdf` |
| 51204 | current revision, 2023, 2–4 players | `schmidtspiele.de/files/Produkte/5/51204 - Mensch Ärgere Dich nicht®/51204_Maedn_DE.pdf` |

Index of all official Spielanleitungen: `schmidtspiele.de/spielanleitungen.html`
(use the `www` host; a `dev.` subdomain also surfaces in search results).

**Correction (2026-07-31).** An earlier version of this table listed
"D-1…D-7, D-34" as awaiting rulebook verification. That over-claimed: only
**D-1** (scope of the three-attempts condition) and **D-2** (clearing priority
vs. entering on a 6) were pending, plus the baseline clause **GM-3.8**
(jumping over own pieces inside the goal column), which §2.3 asserts without
a citation. D-3 to D-7 and D-34 concern points on which the rulebook is silent
or which are pure implementation choices, and fall under §9's own clause
"where the rulebook is silent, by an explicit documented choice". They are
`pinned`, not pending.

All three pending items were then verified against the editions above and
carry `verified-official`, which is the state frozen at `prereg-v1` (D-73).

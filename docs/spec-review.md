# MadnLab `requirements.md` (version 1) — Specification Review

Reviewed document: `requirements.md`, version 1.
Target repository state at review time: empty (fresh Python repo, no code).

---

## Verdict

The document is unusually complete for a v1 specification. The rule model
(§2.3–§2.7), the logging contract (§4), the determinism requirements (§5) and
most acceptance gates (§11) are implementable as written, and the majority of
raw review findings collapsed into documentation hygiene rather than defects.

What is *not* yet implementable is concentrated in three places:

1. **The `mandatory_extended` arm.** Its extra-lap piece has no progress
   encoding, and the encoding it implicitly inherits collides with the goal
   fields. Every §6.1-derived metric in that arm is undefined.
2. **The experiment layer.** Five of six EX rows cannot be enumerated into a
   campaign config because `seats` and `seat_pattern` are never fixed; EX-4
   names a design type without a design; EX-6's `strategy` factor has two
   readings that are different experiments.
3. **The analysis layer.** §6.3's decision rules — Holm family size, primary
   metric per RQ, "move consistently", the EX-4→EX-6 promotion threshold —
   leave the pre-registered verdicts undecidable, and one primary estimand is
   not merely unspecified but wrong.

Engine work on §2.3/§2.4/§2.6/§2.7, §4 and §5 can start today. §6.1's
`progress`, the §8 campaign configs and the `analysis/` package cannot.

**The single biggest risk** is structural: the document calls itself a
pre-registration, and the analysis rules that convert numbers into claims are
the least specified part of it. As written, every published significance
statement is a post-hoc choice — which is precisely what §1 claims the
document prevents.

---

## How this review was produced

Six independent review lenses (cross-references, game-rule fidelity,
under-specification, statistical validity, experiment plan, engineering
feasibility) each read the document in full and reported findings backed by
verbatim quotes. Every finding then passed through an adversarial verifier
instructed to *refute by default*, with explicit instruction to reject
anything §9 (decision points) or §12 (out of scope) already covers.

- 76 raw findings → 13 refuted outright, 63 survived (most as *partial*, i.e.
  a real defect but misdiagnosed or overstated; the verifier's corrected
  statement was kept).
- The synthesis was then audited by a completeness critic which re-derived
  every arithmetic claim independently, found three factual errors and one
  misfiled severity in the synthesis, and added 11 findings the six lenses had
  structurally missed. Those corrections are applied below.

Arithmetic in this document has been computed twice, independently.

---

## A. Blockers

Six items. A blocker means: an implementer cannot correctly write the code, or
a published number would be wrong, without a decision.

### B-1 — `mandatory_extended` has no progress encoding (§2.5 GM-5 + §6.1)

§2.5 puts a piece back on the ring beyond its own goal entry
("the piece then skips the goal and continues on the ring for another lap"),
but §6.1 maps ring position to "steps advanced since the entry field + 1" and
goal position to "ring length + 1 + goal index", with no lap term.

On the 4-seat board (ring 40), a piece on its goal entry has progress 40; one
field further on the extra lap gives 41 — which is exactly the encoding of
goal index 0. Under the accumulating reading a lapped piece scores as if it
were in the goal and normalized progress exceeds 1; under the modulo reading
progress is non-monotone in time. Nothing in the document picks one.

Everything downstream depends on the choice: `leader(t)`, `lead_changes`,
`time_in_lead_by_seat`, `winner_rank_at_50/75`, `comeback`, `final_margin`,
and the piece selection of `SPREAD` / `FOCUS_FRONT` / `FOCUS_REAR`. Two
implementers produce different, both-defensible numbers and no test in §11
catches it.

**Proposal.** Ring progress is `1 + (steps_since_entry mod ring_length)`: a
piece that skips its goal entry drops back to a low value instead of
overtaking goal pieces. State explicitly that progress is therefore *not*
monotone in time in this arm. `max possible` stays the lap-0 seat maximum
(170 on 4 seats, 202 on 6). Add `extra_laps_by_seat` to the summary row so the
rule's cost is measurable. GM-3.8 re-applies on every subsequent pass, so no
lap-count state field is needed. Every agent consumes the one `progress()`
function, GM-7 style.

### B-2 — The forced-entry / mandatory-capture priority is unpinned (§2.3 GM-3.5 vs §2.5)

§2.5 pins only clearing-vs-capture; §9.2 pins only clearing-vs-entering.
Nothing states what happens on a 6 with a piece in the yard *and* a capture
available elsewhere: does the capture restriction shape the legal set first
(so entry is simply not legal and GM-3.5's own fallback fires), or does
forced entry outrank the restriction?

The two readings give measurably different games across the entire
`capture_mode = mandatory` arm — including the 100k headline cell of EX-2.

This also has a nasty second-order effect: AK-5's wording ("modulo the
clearing exception") presupposes the first reading. Under the second reading
AK-5 fails on every campaign log *for a legal reason*, and an implementer will
be tempted to "fix" the engine so the gate passes — the acceptance gate
silently redefining the rule.

**Proposal.** Fix the full three-way lattice, default
`clearing > mandatory-capture > forced-entry`: the capture restriction shapes
the legal set; entry is forced only within that restricted set; if no entry
move captures while another move does, the capture is played and the 6 is not
used for entry. Add an AK-1 scenario "6 rolled, yard piece available, capture
available elsewhere". If the opposite order is chosen instead, AK-5 must be
restated as "modulo the clearing exception *and* the forced-entry exception".

### B-3 — `players = 6` is perfectly confounded with the 6-seat geometry (§8 vs §2.4)

**The confound is the headline here, not the enumerability.**

§2.4 constrains `players ≤ seats`, so a `players = 6` cell must run on the
48-ring board with start-field spacing 8. Any "player-count main effect", and
specifically EX-6's `capture_mode × players` interaction, therefore mixes
player count with board geometry — a factor §1 RQ-4 lists separately and EX-5
treats as headline-sized. This cannot be fixed by a default; it needs
additional cells.

Secondary, but blocking for configuration: §2.4 declares `seats` and
`seat_pattern` measured structural axes and §7.1 makes them config fields, yet
EX-2, EX-3, EX-4 and EX-6 state only a player count, and EX-1 states none
either (it is inferable as `seats = 4` only from AK-4's 25% target). For
players ∈ {2, 3, 4} both boards are admissible, and whenever players < seats
all three patterns are admissible — so those cells cannot be enumerated,
seeded or aggregated from the document as written.

**Proposal.** Estimate player-count effects only *within* a fixed `seats`
level: replicate players ∈ {2, 3, 4} at `seats = 6` wherever a player-count
contrast is published, and report the 6-player cell only against 6-seat
companions. Make `(seats, seat_pattern)` part of every cell key: an explicit
board+pattern column on every EX row, `(seats, seat_pattern, occupied_seats)`
written into every summary row, and defaults pinned in §2.2 (`seats = 4` for
players ≤ 4, `seats = 6` for players ∈ {5, 6}; `seat_pattern = adjacent`
unless a row says otherwise). Also pin `seats` for EX-5's 2-player
`adjacent` vs `opposite` sub-design.

### B-4 — EX-4 names a design type without a design (§8 vs §2.4)

EX-4 says only "Fractional factorial over the six rule axes of §2.4": no
fraction, resolution, defining relation, generators, run count or alias
structure, and §9 pins none of it. A fractional factorial that is not written
down cannot be pre-registered.

Worse, the axes are not crossable. §2.4 itself states `entry_attempts` "never
triggers under `free_entry`" and `bonus_roll_after_quick_entry` "Requires
`entry_attempts = 3`", which contradicts the section's own preamble
("normalized into independent axes"). No standard regular fraction applies to
a nested design.

Arithmetic: 3·2·2·2·3·2 = **144** nominal combinations. 36 are inadmissible
(`bonus_roll = true` with `entry_attempts = 1`), leaving 108 admissible. Under
`free_entry` there are 36 admissible cells collapsing to 12 distinct
behaviours, so **24 are behavioural duplicates** → **84 well-defined cells**.
Only 24 of the 72 `bonus_roll = true` combinations are behaviourally active.

Nothing says whether the runner drops, coerces or errors on inadmissible
configs — and coercion would alias `bonus_roll` with `entry_attempts`
outright. Since EX-4 is the screening gate deciding which axes reach EX-6,
main effects attenuated to 1/3 (bonus roll) and 2/3 (entry attempts) mean a
real entry-rule effect can fail the "CI excluding zero" screen for a purely
structural reason.

**Proposal.** Correct §2.4's "independent axes" wording to state the nesting.
Then drop the fraction entirely: the complete 84-cell design at n = 10k is
840k games ≈ 105 s at the NF-2 throughput target — the fraction buys nothing.
Treat `entry_attempts` and `bonus_roll_after_quick_entry` as conditional
factors and report conditional, not marginal, effects for them. Check the
enumerated cell list into the campaign config. The config validator rejects
inadmissible combinations with a named error and never coerces.

### B-5 — The RQ-1 primary estimand measures location, not scale (§6.3)

This is the one blocker that is not an omission: it is specified, and it is
wrong.

§6.3 makes the **raw variance ratio** of game length the core RQ-1 estimand. A
pure location shift at constant relative dispersion (+10% mean, unchanged
coefficient of variation) produces a variance ratio of 1.1² = **1.21**. At the
pre-registered n the bootstrap CI excludes 1 with near-certainty. Mandatory
capture is very likely to shift mean game length — so RQ-1's necessary
condition would be satisfied by a pure *length* effect, reported as a
*dynamics* effect. The Brown–Forsythe check cannot catch this; at these n it
rejects unconditionally.

The consequence is a confident, significant, published "Schlagzwang increases
variance" produced by a mean shift.

**Proposal.** Make a scale-free measure primary: CV ratio, variance ratio on
`log(rounds_to_first_win)`, or IQR/median — each with a BCa bootstrap CI over
games. Report the raw variance ratio and the mean ratio alongside so location
and scale are visibly separated. Pre-declare a minimum practically relevant
effect (e.g. CV ratio ≥ 1.05) and state that at n ≥ 10k significance tests on
dispersion are not informative.

### B-6 — No pre-registered verdict is decidable (§6.3 + §8 EX-4 + §6.2)

Four coupled holes make every published claim a post-hoc choice:

1. **Holm families are never enumerated.** §6.3 mandates "Holm correction
   within each research question's metric family" but no section lists a
   family or says whether *m* counts metrics only or metrics × arm-contrasts.
   For RQ-1 alone *m* plausibly ranges from 5 (the metrics §1 names) to 80
   (5 metrics × 16 non-baseline contrasts over EX-2's 24 cells) — a first-step
   threshold anywhere between 0.010 and 0.000625.
2. **No primary metric outside RQ-1 length.** §6.2 designates one, so EX-4's
   promotion rule "CI excluding zero on a primary metric" is inert for RQ-2,
   and EX-6's arm set (and cost) is chosen after seeing EX-4's results.
3. **"Move consistently" has no threshold**, no count rule and no CI
   requirement.
4. **The support rule is only a necessary condition** ("supported *only if*"),
   so no sufficient condition for support exists anywhere in the document.

**Proposal.** Add a §6.4 table listing, per research question, the ordered
metric family by §6.2 field name and the exact contrast set (arm pairs ×
cells) — and therefore *m*; state that Holm runs over metrics × contrasts
jointly. Designate a primary metric per RQ (RQ-1: `rounds_to_first_win`
dispersion; RQ-2: win rate + `rounds_to_first_win`; RQ-3: deviant win rate in
the 1-deviant cells; RQ-4: the interaction contrast). Restate the RQ-1 support
rule as a decidable biconditional, e.g.: supported **iff** the lower bound of
the 95% bootstrap CI on the CV ratio exceeds 1 **and** ≥ 2 of {`lead_changes`,
comeback rate, 1 − predictability accuracy} have Holm-adjusted CIs excluding
zero in the dynamism direction — with `captures_total` moved out of the
confirmation set and relabelled a manipulation check. Replace EX-4's "worth
pursuing" with a numeric rule, or pre-register EX-6's arms unconditionally.

> Cost note: the whole §8 plan at the pre-registered n is ≈2.9M games ≈ 2,900
> CPU-seconds ≈ **49 CPU-minutes ≈ 6.1 minutes wall-clock on 8 workers** at
> the NF-2 target. Compute never justifies an adaptive design here.

---

## B. Major findings

Twenty-one items, grouped by theme. Each will cause rework or a misleading
result, but none blocks starting the engine.

### Rules and agents

**MJ-1 (§3.2 vs §3.1) — The focus agents are not total.**
§3.1 requires every agent to be total, but §3.2 defines the protagonist as the
most/least advanced own piece **on the ring**. At game start, after a
multi-capture, and in the endgame with pieces split between yard and goal
column, the candidate set is empty and no protagonist exists; the fallback
("the legal move of the least-advanced other piece") is written relative to a
protagonist that does not exist. The same gap hits `SPREAD`: "track progress"
is defined nowhere and is *not* §6.1's `progress` (which ranks goal pieces
above all ring pieces). Since RQ-3's entire contrast is the piece-selection
rule, this is a hole in the estimand itself.
*Proposal:* define one selection key `track_progress(piece)` = §6.1 `progress`
restricted to ring pieces, with yard and goal pieces excluded from the
ranking; pin the empty-candidate branch (entry move if legal, else the
canonically first legal move); state whether goal-column moves are eligible as
"other piece" moves. Add agent-totality scenarios to AK-1.

**MJ-2 (§3.2) — `FOCUS_REAR` is nearly `SPREAD`.**
Its primary rule (always move the least-advanced own piece when legal) is
almost exactly `SPREAD`'s, differing mainly in entry priority. RQ-3's
four-agent contrast is therefore weaker than intended, and EX-3 would likely
report "front-focus differs, rear-focus does not" as a property of rear-focus
rather than of the definition. The inherited parenthetical "(keeps
non-protagonists back)" is also false when the protagonist *is* the rearmost
piece.
*Proposal:* spell `FOCUS_REAR` out in full rather than by "same policy" — e.g.
fallback = the legal move of the **most**-advanced other piece, so
non-protagonists are pushed ahead rather than bunched with the protagonist.
State each agent's intended invariant separately.

**MJ-3 (§2.3 GM-3.3 / GM-3.10 + §2.4) — Dice consumed per entry turn is
unpinned, twice.**
(a) GM-3.3 grants an extra roll after every 6, and
`bonus_roll_after_quick_entry` grants "one additional roll" for entering on
attempt 1 or 2 — but entering on attempt 1 or 2 necessarily *means* a 6 was
rolled. The literal reading stacks both grants; an implementer can equally
read the flag as redundant, in which case EX-4 publishes a null main effect
for an axis made inert by construction. (b) Whether a 6 inside the
three-attempt sequence also triggers GM-3.3's extra roll is unstated. Both
move the pre-registered `dice_rolls` field, and LG-3's replay validator cannot
catch either because it re-simulates with the same engine.
*Proposal:* a 6 terminates the attempt sequence immediately and grants exactly
one GM-3.3 extra roll, which is an ordinary roll and never re-opens the
attempt window; `bonus_roll_after_quick_entry = true` grants a second extra
roll that stacks. State the resulting maximum rolls per turn explicitly. (Or
drop the flag from v1 and from EX-4's axis count, which then becomes five.)

### Metric definitions

**MJ-4 (§6.1/§6.2) — `leader(t)` has no base case.**
All seats start tied at progress 0, and "on ties the previous leader persists"
has no previous leader at segment start, so the opening value is
implementation-defined — and initialising to seat 0 hands it every leaderless
opening turn, exactly the kind of silent per-seat artefact §7.3 forbids. Read
literally, the persistence clause also does not require the previous leader to
be among the tied maxima.
*Proposal:* `leader(t)` = unique argmax of `progress(seat)`; on ties,
`leader(t−1)` iff it is itself among the tied maxima, else the tied-maximum
seat with the lowest index; `leader(0) := NULL`, persisting until a strict
maximum exists; `lead_changes` counts only transitions where both endpoints
are non-NULL. Add `turns_without_leader` and exclude those turns from the
entropy denominator.

**MJ-5 (§6.2) — `comeback` is non-monotone.**
"Winner was rank ≥ 3 (4+ players) or rank 2 (2–3 players)" uses an inequality
in one branch and bare equality in the other, so read literally the strongest
comeback in every 3-player cell is discarded. Comeback rate is one of the
three dynamics metrics the RQ-1 support criterion depends on.
*Proposal:* always "≥". Emit `comeback_rank_threshold` so the definition
travels with the data, add a k-normalised companion ((rank−1)/(k−1)), and
pre-register that comeback *rates* are compared only within a fixed player
count.

**MJ-6 (§6.2 + §9.5) — Checkpoints have no rounding rule and checkpoint ranks
no tie rule.**
The checkpoint index is a fraction of `rounds_to_first_win` with no floor/ceil
convention, and §9.5 pins tie reporting only for *end-of-game* ranks. Both
feed `winner_rank_at_50/75`, `comeback` and the winner-predictability
estimand; a tie rule awarding rank 1 to both tied seats rather than ranks 1
and 2 flips `comeback` directly.
*Proposal:* `checkpoint(k) = state after turn ceil(k · turns_to_first_win)`
for k ∈ {0.5, 0.75} — taken in *turns*, aligning with `leader(t)`. Standard
competition ranks (1, 2, 2, 4) over `progress(seat)`; a tied winner takes the
best rank of its tie group, flagged by `winner_rank_at_50_tied`. Add a §6.3
caveat that the checkpoint is located from realised length and is therefore
conditioned on the game's own duration.

**MJ-7 (§6.2 vs §4.2) — `barrier_turns` is never defined, and the summary-row
key set varies by arm.**
The table cell contains only a collection condition where every other row
supplies a definition. `barrier_turns` admits at least a per-turn indicator, a
barrier-turn integral and a per-seat variant, differing by large factors — and
it is the only barrier-specific dynamics metric behind EX-6's
`barriers × strategy` factorial. Separately, §4.2 promises every row carries
"the complete metric battery of §6" while §6.2 conditions these fields on the
arm.
*Proposal:* `barrier_turns` = turns during which at least one barrier stood at
turn start; `barrier_turns_by_seat[s]` likewise; `barriers_formed` = count of
`barrier_formed` events over the full game. All present always, 0 when
`barriers = false`. Fix the summary-row key set per `schema_version`.

**MJ-8 (§6.2 + §6.3 vs §8 EX-2) — Two more dynamics metrics are not on a
common scale across player count.**
`lead_changes` counts transitions of the argmax over k seats, so its expected
value rises mechanically with k even under identical dynamics. Winner
predictability is an accuracy whose chance floor is 1/k, so a 2-player
accuracy is judged against 0.5 and a 6-player accuracy against 0.167 — yet
§6.3 reads "lower accuracy = more dynamic games". EX-2 crosses `capture_mode`
with players ∈ {2, 3, 4, 6} and feeds exactly this criterion.
*Proposal:* extend the within-k rule to the whole dynamics triple. Add
`lead_changes_per_turn` and a skill-score predictability
`(accuracy − 1/k) / (1 − 1/k)` (0 at chance for every k). Prefer AUC over
accuracy, since AUC's 0.5 chance level is k-invariant; label raw accuracy
descriptive only.

### Statistics

**MJ-9 (§1 RQ-2/RQ-3 + §8) — Homogeneous-field win rates are 1/k by symmetry.**
Where players = seats and every seat runs the same policy, §2.1's "positions
are pure functions of (seats, seat index)" plus clockwise order and a balanced
starting player make seat rotation an exact automorphism: each seat wins
exactly 1/k for any rule set and any single policy. So EX-4's all-`RANDOM`
cells carry no raw win-rate contrast for RQ-2 ("main effect … including win
rates"), EX-3's homogeneous cells carry none for RQ-3, and EX-5's 6-seat
`spread` arm returns exactly 1/3 per seat before a game is played —
publishing that as evidence that Wikipedia's seating recommendation removes
the middle-seat disadvantage would report a symmetry identity as a result.
(EX-3's players < seats cells are exempt; those seats are genuinely
asymmetric.)
*Proposal:* state the 1/k identity once in §6.3, as both the reason AK-4 works
and the reason homogeneous win rates are not evidence. Restate RQ-3 so
win-rate claims come exclusively from the 1-deviant and 2-player head-to-head
cells. Restate RQ-2's win-rate estimand as something symmetry does not fix —
P(win | seat is the starter), and the per-seat profile as a function of the
flag — and/or add 1-deviant cells to EX-4/EX-6. Declare EX-5's `spread` arm
and the 2-player `opposite` arm a-priori symmetry checks in the AK-4 family.

**MJ-10 (§6.3) — The bootstrap resampling unit is never stated, and per-seat
outcomes within a game are treated as independent.**
Per-seat win indicators of one game are multinomial (exactly one is 1), so a
seat-to-seat contrast built from two independent Wilson intervals understates
the SE of the difference: 0.194 pp against the correct 0.224 pp at p = 0.25,
n = 100k. Per-seat count fields are clustered within the game, and a strategy
occupying 2 of 4 seats counted as 2n Bernoulli trials inflates the effective n
twofold. §6.3 mentions clustering only for the descriptive RQ-4 regression.
*Proposal:* state that the game is the independent unit and every bootstrap
resamples whole summary rows, never seat records; aggregate per-seat counters
at game level before resampling. Use the multinomial difference variance (or a
paired game-level indicator) for within-cell seat and strategy contrasts; keep
Wilson only for a single proportion against a fixed reference, as AK-4
legitimately does. State whether rotation strata are ignored (conservative) or
post-stratified.

**MJ-11 (§6.3 + §8 EX-6) — No power analysis anywhere; the cells that need the
most data get the least.**
§6.3 fixes n with no SE or minimum detectable effect for any contrast the
document names. At n = 10k per cell the MDES (80% power, two-sided 5%, before
Holm) is 1.71 pp for a two-arm win-rate difference, 2.42 pp for a 2×2
interaction and 3.43 pp for the three-way `win ~ strategy × rule × players`
(≈4.26 pp after Holm over six contrasts) — likely larger than real interaction
effects in a dice game, so RQ-4 as budgeted will mostly return underpowered
nulls. Matching main-effect resolution costs 4× n for two-way and 8× for
three-way; at NF-2 throughput 40k games/cell is ~5 s on 8 workers.
*Proposal:* add a per-estimand SE/MDES table to §6.3 at the chosen n and the
Holm-adjusted alpha. Raise EX-6 two-way cells to 40k and three-way contrasts
to 80k. Note explicitly that the "≈ 0.4 pp" figure applies to a single win
rate only.
*Cross-reference:* this table must be stated for **battery metrics and
deviant-cell win rates** — under MJ-9, homogeneous-field win rate is constant
by construction, so a win-rate power table for those cells describes a
response that cannot vary.

**MJ-12 (§5 NF-1 + §6.3 + §7.1) — Determinism stops at the simulator.**
NF-1's "one master seed determines everything" enumerates only simulation
streams. §6.3's estimands are randomized — BCa bootstrap everywhere — and no
section gives the bootstrap a seed, a resample count B, or a place to record
either. §7.1's "nothing statistical is decided in code at run time" is
asserted for the runner while the analysis layer has no config-as-data
counterpart at all. Re-running the analysis on byte-identical input therefore
yields different CI bounds in the last digits, and §6.3's rules are
*threshold* rules ("CI excludes 1"), so a borderline verdict can flip between
runs of the same data. This defeats the point of AK-2: the simulation half is
byte-reproducible and the published half is not.
*Proposal:* extend NF-1 to the analysis layer — an analysis run takes its own
declarative config (input campaign dir, estimand list, `analysis_seed`,
`bootstrap_B`, alpha) and writes `analysis.json` recording the resolved config
plus the input `summary.jsonl` hash. Pin `bootstrap_B = 10000` for headline
numbers, require seed/B/hash beside every published interval in
`docs/results.md`, and add the reproducibility clause to AK-2.

### Experiment design

**MJ-13 (§8 EX-5 + §1 RQ-4) — The seating headline confounds pattern with
geometry and has no control arm.**
EX-5's two arms differ simultaneously in seat pattern (`adjacent` vs `spread`)
*and* in board (ring 40/spacing 10 vs ring 48/spacing 8). Ring length dominates
game length and exposure frequency, so any difference mixes the seating effect
with a whole-geometry effect §1 lists as a separate factor. The confound
cannot be broken inside the 4-seat board: with 3 of 4 seats occupied, every
occupancy set is a rotation of `adjacent`, so no `spread` counterpart exists
there. The missing cell is the one the document never lists — 3 players
`adjacent` on the 6-seat board (seats 0, 1, 2).
*Proposal:* add that cell at the same n and pre-register the decomposition —
pattern effect = 6-seat `adjacent` vs 6-seat `spread`; geometry effect =
4-seat `adjacent` vs 6-seat `adjacent`; the currently planned contrast is
their **sum** and must not be published as a pattern effect. State in §8 why
the 6-seat control is required rather than optional.

**MJ-14 (§8 EX-6 vs EX-3) — EX-6's `strategy` factor has two readings that are
different experiments.**
EX-3 carefully distinguishes "all homogeneous fields" from "1 deviant vs.
field of X", but EX-6 writes "capture_mode × strategy" and "barriers ×
strategy" with no qualifier and no player count. Under the homogeneous
reading the win rate is fixed at 1/k for every level of the rule axis (MJ-9),
so the interaction on win rate is identically zero and only battery metrics
carry signal; under the deviant reading the win rate is the natural response
but the cell count multiplies and the design must name the deviant. EX-6
answers RQ-4 and its cells are §6.3's "primary evidence" — this is the same
non-enumerability as B-3, on the axis that carries the research question.
*Proposal:* split into two explicitly named rows — (a) homogeneous-field cells
with battery metrics (not win rate) as the response, (b) 1-deviant cells with
the deviant's win rate as the response, naming deviant and field agent per
cell. Fix `players` for every EX-6 row and state which response is primary.

**MJ-15 (§8 EX-1 + §6.2 + §7.3) — EX-1's headline deliverable has no field and
no estimand.**
EX-1 promises "first quantification of the starting-player advantage", but
§6.2 lists no `starting_seat` or turn-order-offset field and §6.3
pre-registers no corresponding estimand — while §4.1 requires that "every
statistic that any analysis needs is a first-class field of the summary row".
The marginal per-seat win rate is 25% by construction, so it is not the
estimand. Separately, §7.3 scopes balancing to "every mixed-strategy cell",
yet EX-1, EX-5 and EX-3's homogeneous cells are labelled "rotation-balanced"
where strategy rotation is vacuous.
*Proposal:* add `starting_seat` and `turn_offset_by_seat` as first-class
fields and the estimand "win rate by turn-order offset from the starting seat,
Wilson 95% CI" to §6.3. Extend §7.3 to state that starting-seat balancing
applies to homogeneous cells too, and that EX-5's occupied block is rotated so
the middle-seat contrast is within-rotation.

**MJ-16 (§11 AK-4 + §8 EX-1) — The symmetry gate accepts the null, and the
6-seat board has no calibration gate at all.**
AK-4 passes when each seat's Wilson 99% CI covers 25%: a failure-to-reject
with no equivalence margin, four per-seat checks (family-wise spurious-failure
probability 1 − 0.99⁴ ≈ **3.9%**, so a correct engine fails roughly one run in
25), and blindness to any asymmetry below the **0.353 pp** half-width at
n = 100k. More seriously, §11 has no symmetry or geometry criterion for the
48-ring board, which carries EX-5's `spread` arm and every players = 6 cell; a
wrong start-field spacing or goal-entry offset there would pass all seven
gates, and AK-3 only checks replay self-consistency.
*Proposal:* add EX-1b (6 players, `seats = 6`, all-`RANDOM`, balanced,
n = 100k) and restate AK-4 as an equivalence test: for every seat, the
two-sided 99% CI for (p_seat − 1/k) lies entirely within ±δ, applied jointly
or as a single multinomial goodness-of-fit test on the seat counts. **Justify
δ against the half-width**: δ = 0.5 pp leaves only 0.147 pp of slack over the
0.353 pp half-width, so a correct engine with a trivial true asymmetry can
still fail — either raise δ or raise n with it. State that AK-4 validates
harness/geometry symmetry, not a substantive seat estimate.

**MJ-17 (§8 EX-1 + §11) — The instrument is never validated against anything
outside itself.**
Every gate in §11 is a self-consistency check: rules against scenarios written
by the engine's own author, replay against the same engine, symmetry against
an identity that holds by construction, throughput against a self-set target.
For a document whose product is published measurements there is no external
reference point. Yet cheap analytic ground truth exists in this exact model:
under GM-3.10's three attempts, P(entry in a turn) = 1 − (5/6)³ = 0.4213, mean
2.374 turns. A systematic error in the dice stream, the three-attempts loop or
the entry logic would shift this and pass all seven gates — AK-4 is blind to
it because a uniform bias hits all seats equally.
*Proposal:* add an analytic calibration gate: on a 1-player configuration the
simulated distribution of turns-to-first-entry matches the analytic geometric
distribution with p = 1 − (5/6)^`entry_attempts` (chi-square over the first 10
turn counts, n = 100k), and the empirical die-face distribution over a full
cell is uniform within its 99% CI. Both cost seconds. State that EX-1 is a
symmetry calibration only.

### Engineering

**MJ-18 (§11 AK-5 vs §7.2/§4.2) — AK-5's verification population is
undefined.**
AK-5 demands "full campaign logs" while §7.2 defaults `--log-events` to
`sample:100` per cell — 0.1% of a 100k cell. The gate either silently degrades
to a 0.1% spot check while being published as a campaign-wide invariant, or
every mandatory cell must run with `all`, exactly the case §7.2 calls too
large. No summary-row field carries the invariant, and `mandatory_extended`
has no campaign-level analogue. Discovering this after EX-2 forces a re-run,
since the fix is a schema change.
*Proposal:* decouple the invariant from the log medium — the engine asserts it
inline for every game and writes first-class counters
`capture_forcing_offered`, `capture_forcing_violations` and
`forced_extra_lap_offered` / `forced_extra_lap_violations`. Restate AK-5 as
"summed over all summary rows of every `mandatory` and `mandatory_extended`
cell, violations = 0", plus a per-event spot check over the sampled logs.
Optionally add `captures: {seat, piece} | null` to each logged legal-move
entry and `restriction: none | capture | clearing` to the `move` event.

**MJ-19 (§4.3 LG-3 / §11 AK-2 vs §5 NF-3) — "Byte-identical" is asserted with
no canonical serialization, and AK-2 is weaker than NF-3 requires.**
NF-3 requires output to be "a deterministic function of the config alone,
never of the worker layout", but AK-2 only tests "identical row *sets*" — set
equality passes while row order, and therefore byte-identity and any
position-dependent bootstrap, varies with scheduling. Byte-identity is claimed
without fixing encoding, key order, separators or float formatting. And §4.3
conditions replay on "header + engine version" without stating what a version
bump does to AK-6's checked-in golden log or to campaigns already published;
the failure surfaces as an ambiguous "replay mismatch" rather than a version
error.
*Proposal:* pin a canonical serialization (UTF-8, explicit `\n`, fixed key
order, `separators=(",",":")`, shortest round-trip floats) as part of the log
schema version. Shards write `summary-<shard>.jsonl`; the runner seals by
concatenating in ascending shard index, rows in ascending global game index.
Strengthen AK-2 to byte-identity of `summary.jsonl` and `campaign.json` across
worker counts. Add a version policy: the replay validator refuses mismatched
`engine_version` unless `--allow-version-skew`; goldens are regenerated on
every bump with an NF-5 row.

### Meta / process

**MJ-20 (§1 + §3.2 + §8) — Every rule-effect result is a bound set by the
policy, and §1 claims the opposite.**
§3.2 states no agent has capture preference or avoidance, so under
`capture_mode = optional` the baseline capture rate is the *incidental* rate —
the lowest it can be. The optional-vs-mandatory contrast is therefore a
structural **upper bound** on the Schlagzwang effect: a capture-seeking player
already takes most of the captures the rule would force, so the same
experiment with a capture-aware agent returns a strictly smaller (possibly
null) effect. The mirror holds for `barriers`: with no barrier-aware policy,
barriers form incidentally and dissolve at random, so the barrier main effect
is a structural **lower bound** measuring only mechanical blocking.
`goal_no_jump` is reachable only through canonical move order, not through any
policy that values it. None of these directions is stated, yet §1 calls the
restriction to defined policies "a feature (clean attribution)" — the
attribution is clean *for the policy*, and RQ-1 is exactly the question where
the policy choice sets the magnitude. §12 puts capture-aware agents out of
scope, so this cannot be fixed with an extra arm; it must be fixed in the
estimand's interpretation.
*Proposal:* pre-register the bound direction as part of the estimand, not as a
post-hoc caveat: state in §1/§6.3 that `optional → mandatory` is an upper
bound under capture-blind play and the `barriers` main effect a lower bound
under barrier-blind play, and require both statements beside every such number
in `docs/results.md`. Add a "policy sensitivity" column to §2.4 marking each
flag choice-mediated (`capture_mode`, `barriers`, `goal_no_jump`) or
mechanical (`cold_start`, `entry_attempts`, `bonus_roll`). If one extra agent
is affordable, a `GREEDY_CAPTURE` control (capture whenever legal) turns the
bound into a measured interval at ~10k games per affected cell and is worth
exempting from §12.

**MJ-21 (§1 + §5 NF-5 + §8) — The pre-registration has no freeze, no amendment
rule, no confirmatory/exploratory split and no all-results-reported rule.**
(1) *No freeze*: the document lives in the same mutable repo as the code and
nothing requires it to be tagged or hashed before EX-1 runs, so "fixed before
any campaign runs" is unenforceable and unverifiable after the fact.
(2) *No amendment policy*: NF-5's ledger covers rule ambiguities and
optimizations only, so a post-hoc change to §6.2 or §6.3 leaves no trace
anywhere — precisely the cherry-picking §1 claims to prevent.
(3) *No confirmatory/exploratory labelling*, although the plan is explicitly
adaptive: EX-6's arm set is chosen after EX-4's results, so every EX-6 number
is exploratory by construction and nothing says so.
(4) *No commitment to report all pre-registered metrics regardless of
outcome*; `docs/results.md`'s "per-question findings" permits silently
dropping the nulls.
*Proposal:* add a §14 "Pre-registration status": the frozen version is a git
tag (`prereg-v1`) created before EX-1 runs; every campaign config and summary
row records the `prereg_version` it ran under; any later change to §6 or §8 is
an amendment with its own ledger row stating what data already existed when it
was made. Label EX-1..EX-5 confirmatory and EX-6 exploratory (or pre-register
EX-6's arms unconditionally). Require `docs/results.md` to report every §6.2
metric for every cell, significant or not, with its label attached.

**MJ-22 (§11 + §13 + §1) — The deliverable has no acceptance criterion.**
§1 says the product is measurement series and simulated games are a
by-product, yet all seven acceptance criteria test the by-product. Nothing
validates `analysis/`: no CI-coverage check on the Wilson/BCa implementations,
no check that Holm is correct, no cross-validation that §6.2 summary fields
equal an independent re-derivation from the event log. §4.1's design rule
("Analyses never re-derive numbers by parsing event streams when a summary
field exists") deliberately removes the only redundant path, which makes the
absent cross-check load-bearing: a wrong `lead_changes` or `winner_rank_at_50`
passes AK-1..AK-7 unchanged and goes straight into `docs/results.md`. The
milestone list mirrors the gap — `analysis/` first appears implicitly at M4,
after which nothing gates it.
*Proposal:* add **AK-8 (estimator calibration)** — on synthetic data with
known truth, Wilson and BCa achieve nominal coverage within Monte-Carlo error
and Holm reproduces a hand-worked example; and **AK-9 (metric
cross-validation)** — for the AK-3 replay corpus, an independent reference
implementation walking the event log reproduces every §6.2 field exactly (the
one place §4.1's no-re-derivation rule is violated on purpose). Give the
analysis package its own milestone before EX-2, since M2's EX-1 already
publishes CIs.

---

## C. Minor findings

Clarity and consistency. Numbered for reference; each is one line of fix.

**Cross-references and identifiers**

1. **Renumbering drift, nine occurrences**, all recoverable from context but
   none resolving: §1 RQ-2 "each rule flag in §3.3" and §2.3 clause 6 "(§3.3)"
   → §2.4 (barriers: §2.6); §1 scope note "agent policies of §5" and §2.4 "the
   §5 strategy assignment" → §3; §3.1 ST-1 "see §7.1" for the RNG contract →
   §5/NF-1; §2.5 GM-5.1 "(§10)", §3.2 "future axis (§10)" and "listed in §10"
   → §12; §12 "(§2.5.1)" → GM-5.1. Add a doc lint resolving every §N.M
   reference against the heading list.
2. §1 RQ-2's "the project baseline (§3.2)" is ambiguous in a way that changes
   meaning — §3.2 is the agent table and defines no rule baseline. State
   whether "baseline" means the baseline rule set (§2.3 + §2.4 defaults) or
   the baseline agent field (all-`RANDOM`).
3. Unfilled placeholder "pinned as decision D-? in §9", and §9's seven items
   carry no ids for it to resolve to although NF-5 requires citable rows.
   Number them D-1…D-7, replace D-? with D-3, and make the lint fail on "-?".
4. §6.3 is titled "Estimands and methods (**SQ-\***)" and then contains six
   unnumbered bullets — no SQ id exists anywhere. Every other family (GM-, ST-,
   LG-, NF-, UI-, AK-, EX-, RQ-) has stable ids, and §8 requires
   `docs/results.md` to perform "reconciliation against this document". Number
   them SQ-1…SQ-6 and §7's items CA-1…CA-3; extend the lint so every declared
   family prefix must have at least one instance.

**Rules and config**

5. The game-end mode has named values (`play_out`, `first_winner`) but no
   config key, although §6.1 branches on it and LG-1 must record every flag.
   Name it `game_end_mode` and list it next to `capture_enforcement`.
6. §2.6 GM-6.1 does not textually restrict barrier formation to ring fields,
   leaving the goal column open to a literal misreading. Add to §9.4: barriers
   exist only on ring-track fields.
7. §2.3 GM-3.8's goal-column jumping clause is asserted without a rulebook
   citation and is not on §9's list, so the document's own "resolved against
   the official Schmidt rulebook" procedure will never be applied to it —
   unlike cold start and three attempts, which §2.4's preamble names as
   verified baseline-coincidence cases.
8. §11 AK-1 names no `cold_start` scenario, although that axis carries the
   most interaction constraints and §9.7 flags its forcing semantics as open.
   Add: the `one_piece_out` initial state; `free_entry` entry as a non-forced
   ordinary move with the roll consumed; `free_entry` with entry-clearing
   still in force; and the inertness assertion for `entry_attempts` /
   `bonus_roll` under `free_entry` (which also defines EX-4's valid cell set).

**Metrics**

9. §6.2 `entry_waits_by_seat` — "turns spent stuck in the yard state" is a
   gloss, not a definition. Tie it to the GM-3.10 / §9.1 condition and state
   that it overlaps `passes_by_seat` by construction and must not be summed
   with it.
10. §6.2 `rounds` — "full seat cycles" does not fix the cycle origin, whether a
    trailing partial cycle counts, or whether a skipped finished seat consumes
    a slot. Pin: a round is `players` consecutive turn slots from the drawn
    starting seat; a skipped finished seat consumes a slot but not a turn;
    `rounds = ceil(turn_slots / players)`.
11. §6.1's "max possible" is never given numerically (170 on 4 seats, 202 on
    6) and the document never says which metrics are raw and which normalised,
    so a raw `final_margin` is not comparable across cells differing in
    `seats`. Pin the constants, emit `final_margin_norm`, require normalised
    fields for cross-`seats` comparisons.
12. §6.2 `time_in_lead_by_seat` — the normalized lead entropy has no field name
    (§4.1 requires first-class fields) and no value for degenerate cases. Add
    `lead_entropy_norm = H(p)/ln(P)` over occupied seats P, computed over the
    first-win segment, = 0 when P = 1 or no turn has a defined leader.

**Campaign and logging**

13. §4.1 leaves event-log granularity as an unresolved either/or ("one JSONL
    file per game (or per shard, with game ids)") with no framing convention
    for the shard case, and "plus every game the UI demo needs" is a
    config-external selection. Pin one granularity before AK-3 and the UI
    loader are built against it; replace the prose with a config field, e.g.
    `log_events: {mode: "sample", k: 100, pinned_game_indices: [...]}`.
14. §4.1's header enumeration says "seat assignment" (player→seat) but never
    names the resolved *starting* seat, which under §7.3 is assigned by the
    runner rather than derived from the seed — while §4.3 requires
    re-simulation from the header alone. List `starting_seat` explicitly.
15. §3.1/§5 — it is undefined whether an agent consumes an RNG draw when
    `len(legal) == 1`. Under a stream model, a later optimization that
    short-circuits that call desyncs the seat's stream and silently invalidates
    every previously published log, while AK-2 (same seed, same build) still
    passes. Pin "exactly one draw per decision, including when
    `len(legal) == 1`" and add a unit test.
16. §5 NF-1 does not say whether the game index used for seed derivation is
    scoped per cell (independent arms) or per campaign (common random
    numbers), and no cell key is defined. The CRN regime makes §6.3's unpaired
    procedures conservative rather than wrong, but the choice must be pinned
    and `cell_key` recorded in every row.
17. §7.3's "equal game counts" is unachievable at the pre-registered n for some
    cells (10,000 mod 9 = 1; mod 36 = 28; mod 96 = 16), and "full permutations
    when players ≤ 4 and the design needs it" has no trigger. Residual
    imbalance ≤ 28 games is statistically irrelevant, but the row count must be
    a documented function of the config: state the remainder rule and the
    permutation trigger.
18. §8 EX-2's "the 4-player optional-vs-mandatory pair at 100k" does not say
    whether the upgrade covers the all-`RANDOM` field only or both, so the
    headline cell count is 2 or 4 — and the `optional` vs `mandatory_extended`
    contrast RQ-1 also names stays at 10k. Name the headline cells
    exhaustively (3 × 100k = 300k games ≈ 38 s) and state the precision
    asymmetry deliberately.
19. **No storage or retention policy.** §13 puts `campaigns/` in the repository
    tree; the §8 plan at the pre-registered n is roughly 3M summary rows of 30+
    fields — several GB before event logs. Nothing states a compression
    format, size cap, retention rule, whether these are committed to git or
    attached to a release, or where the archival copy lives. Discovering this
    after EX-2 means rewriting history in a repo that claims byte-reproducible
    logs. Add an NF-6 row: gzipped `summary.jsonl`, `campaigns/` in git holds
    only `campaign.json` plus compressed summaries under a stated cap,
    anything larger is a release asset referenced by hash. Since NF-2 makes
    regeneration cost minutes, state that the reproducibility contract is
    master seed + engine version + prereg tag, and raw rows are a convenience
    artifact.

**Acceptance, milestones, layout, UI**

20. §11 AK-7 — "NF-2 benchmark met, **or** the deviation measured and
    ledgered" is unfalsifiable and weaker than NF-2's blocking "optimized
    *before* any feature work continues"; the benchmark also pins no player
    count, board or hardware. Move "measure and ledger" into the failure
    remedy and define two benchmark cells (baseline 4/4 all-`RANDOM`; worst
    case 6/6 `barriers` + `mandatory_extended` all-`SPREAD`), with the
    per-turn `leader(t)` recomputation inside the measured loop.
21. §13 milestones — M2 pairs AK-5 with EX-1, but EX-1 is baseline rules
    (`capture_mode = optional`) and the first mandatory arms appear in EX-2 at
    M4, so AK-5 has no data at M2. AK-7 appears in no milestone at all despite
    NF-2 being blocking. Move AK-5 to the first mandatory campaign (or add a
    mandatory smoke cell at M2) and put AK-7 in M1.
22. §10 UI-2 — a default `vite build` emits `<script type="module">`, which
    browsers refuse to load over `file://` (opaque origin, CORS-governed module
    loading), so the shell renders blank, contradicting "runs offline from
    `file://`". Pin the build target as a single self-contained HTML file with
    inlined JS/CSS and no code splitting, and extend AK-6 to open the built
    artifact from disk. Cheap now, real rework after M3.
23. §10 UI-6 points a backend-less `file://` SPA at `summary.jsonl`, which §7.2
    defines as campaign-scoped, one row per game, with no size cap or per-cell
    split — and it would reimplement §6.3's Wilson CIs in TypeScript. Point
    UI-6 at `campaign.json` extended with per-cell n, win counts, CI bounds and
    pre-binned histograms; permit `summary.jsonl` loading only per cell with a
    documented row cap.
24. §13 — `madnlab/logging/` shares a name with the stdlib `logging` module.
    Under Python 3 absolute imports this does not actually break imports; the
    cost is linter noise, reader ambiguity, and a real trap for anyone who adds
    a `sys.path` shortcut. Rename to `eventlog/` and pin the packaging shape
    (`src/` layout, explicit `__init__.py`, `pyproject.toml`).
25. §6.2 — the segment convention is stated well, but note that
    `rounds_to_first_win` as the primary length metric is measured on a segment
    whose endpoint is itself the event under study; this is fine for
    comparison across arms but should be labelled so `docs/results.md` does not
    read it as total game duration.

---

## D. Proposed additions to the §9 decision ledger

§9 currently has seven items. These are the topics it does not cover, each
with a default concrete enough to adopt as-is. Numbering continues from D-8.

| Id | Topic | Proposed default |
|---|---|---|
| D-8 | `progress` under `mandatory_extended` | Ring progress = `1 + (steps_since_entry mod ring_length)`; `max possible` stays the lap-0 seat maximum (170 / 202); progress explicitly not monotone in this arm; add `extra_laps_by_seat`; GM-3.8 re-applies per pass, no lap-count state. |
| D-9 | Priority lattice clearing / mandatory capture / forced entry | `clearing > mandatory-capture > forced-entry`. The capture restriction shapes the legal set; entry is forced only within it. AK-5's exception list stays "clearing only". |
| D-10 | Rolls consumed per entry turn | A 6 terminates the attempt sequence and grants exactly one GM-3.3 extra roll, which never re-opens the attempt window; `bonus_roll_after_quick_entry` grants a second extra roll that stacks. Maximum stated explicitly. |
| D-11 | Default board and pattern per player count | `seats = 4` for players ≤ 4, `seats = 6` for players ∈ {5,6}; `seat_pattern = adjacent` unless a row says otherwise; `(seats, seat_pattern, occupied_seats)` in every summary row and in every cell key. |
| D-12 | Player-count effects are within-`seats` only | Any published player-count contrast replicates players ∈ {2,3,4} at `seats = 6`; the 6-player cell is reported only against 6-seat companions. |
| D-13 | EX-4 design | Drop the fraction; run the complete 84-cell admissible design. `entry_attempts` / `bonus_roll` pinned to defaults under `free_entry` (provably inert), `bonus_roll = true` admitted only with `entry_attempts = 3`; effects reported conditionally. Validator rejects inadmissible combinations by name, never coerces. |
| D-14 | Holm families and primary metric per RQ | New §6.4 table: per RQ the ordered metric family by field name and the exact contrast set; Holm over metrics × contrasts jointly. Primary metrics as listed in B-6. |
| D-15 | RQ-1 support criterion | Supported iff CV-ratio CI lower bound > 1 **and** ≥ 2 of {`lead_changes`, comeback rate, 1 − predictability} have Holm-adjusted CIs excluding zero in the dynamism direction. `captures_total` is a manipulation check with a pre-fixed direction. |
| D-16 | Primary dispersion scale | CV ratio (or variance ratio on log length) with BCa CI; raw variance ratio and mean ratio reported alongside; minimum relevant effect CV ratio ≥ 1.05; Brown–Forsythe declared uninformative at n ≥ 10k. |
| D-17 | Rule-effect estimands are policy-bounded | `optional → mandatory` is an upper bound under capture-blind play; the `barriers` main effect is a lower bound under barrier-blind play. Both stated beside every such number. §2.4 gains a policy-sensitivity column. |
| D-18 | `leader(t)` base case and ties | Unique argmax; on ties `leader(t−1)` iff among the tied maxima, else lowest tied index; `leader(0) := NULL`; NULL→seat is not a lead change; add `turns_without_leader`, excluded from the entropy denominator. |
| D-19 | Checkpoint rounding and rank ties | `checkpoint(k) = state after turn ceil(k · turns_to_first_win)`, k ∈ {0.5, 0.75}; standard competition ranks; tied winner takes the best rank of its group, flagged by `winner_rank_at_50_tied`. |
| D-20 | `comeback` predicate | Always "≥": rank ≥ 2 (2–3 players), ≥ 3 (4+). Emit `comeback_rank_threshold` and a k-normalised companion; compared only within fixed player count. |
| D-21 | k-normalised dynamics companions | Add `lead_changes_per_turn` and predictability skill score `(acc − 1/k)/(1 − 1/k)`; prefer AUC for the predictability estimand; raw accuracy descriptive only. |
| D-22 | `barrier_turns` and arm-invariant key set | `barrier_turns` = turns with ≥ 1 barrier standing at turn start; per-seat variant; `barriers_formed` = event count. Always present, 0 when `barriers = false`; key set fixed per `schema_version`. |
| D-23 | Unit of analysis and bootstrap unit | The game is the independent unit; bootstraps resample whole summary rows; per-seat counters aggregated at game level first; multinomial difference variance for within-cell contrasts; Wilson only against a fixed reference. |
| D-24 | Analysis-layer determinism | Analysis takes its own config (`analysis_seed`, `bootstrap_B`, alpha, input hash) and writes `analysis.json`; `bootstrap_B = 10000` for headline numbers; seed/B/hash published beside every interval; AK-2 extended to analysis reproducibility. |
| D-25 | Starting seat as a first-class field | Add `starting_seat` and `turn_offset_by_seat`; add the estimand "win rate by turn-order offset, Wilson 95% CI"; §7.3 states starting-seat balancing applies to homogeneous cells too. |
| D-26 | Homogeneous-field symmetry identity | State the 1/k identity in §6.3 once; homogeneous win rates are not evidence; RQ-3 win-rate claims come only from 1-deviant and 2-player cells; EX-5 `spread` and 2-player `opposite` are a-priori symmetry checks. |
| D-27 | EX-5 geometry control | Add 3 players `adjacent` on the 6-seat board at the same n; pattern effect = 6-seat adjacent vs spread, geometry effect = 4-seat vs 6-seat adjacent; the planned contrast is their sum. |
| D-28 | EX-6 row split | Separate homogeneous-field rows (battery metrics as response) from 1-deviant rows (deviant win rate as response), naming deviant and field agent; `players` fixed per row; primary response named per row. |
| D-29 | AK-4 as equivalence test + 6-seat calibration | Add EX-1b (6 players, `seats = 6`, n = 100k). AK-4: for every seat, the 99% CI for (p_seat − 1/k) lies within ±δ, applied jointly or as a multinomial goodness-of-fit test; δ justified against the 0.353 pp half-width. |
| D-30 | Analytic calibration gate | 1-player turns-to-first-entry matches the geometric distribution with p = 1 − (5/6)^`entry_attempts` (chi-square, n = 100k); die-face distribution uniform within its 99% CI. |
| D-31 | Analysis-layer acceptance gates | AK-8 estimator calibration (Wilson/BCa nominal coverage on synthetic truth; Holm against a hand-worked example); AK-9 metric cross-validation (independent event-log re-derivation reproduces every §6.2 field on the AK-3 corpus). |
| D-32 | AK-5 medium and population | Engine asserts inline per game; `capture_forcing_offered` / `_violations` and `forced_extra_lap_*` in every summary row; AK-5 = violations summed over all rows of every mandatory cell = 0, plus a spot check over sampled logs. §7.2's default is unchanged. |
| D-33 | Canonical serialization and version skew | UTF-8, explicit `\n`, fixed key order, `separators=(",",":")`, shortest round-trip floats — part of the schema version. Shards seal by ascending shard index, rows by ascending global game index. AK-2 becomes byte-identity across worker counts. Replay refuses `engine_version` mismatch unless `--allow-version-skew`. |
| D-34 | Barriers on ring fields only | GM-6.1 does not override GM-3.6 inside goal columns, which stay one piece per field. Added to §9.4 and to AK-1's barrier scenarios. |
| D-35 | `game_end_mode` config key | `game_end_mode ∈ {play_out, first_winner}`, default `play_out`, listed next to `capture_enforcement ∈ {enforce, penalize}` (v1: `enforce`), carried in every log header. |
| D-36 | `FOCUS_REAR` written out in full | Protagonist = least-advanced ring piece; fallback = entry move if legal, else the legal move of the **most**-advanced other piece. Each agent's invariant stated separately. |
| D-37 | Agent RNG draw discipline | Exactly one draw per decision, including when `len(legal) == 1`; covered by a unit test. |
| D-38 | Seed derivation scope | Per-game seed = SHA-256(master_seed ‖ cell_key ‖ game_index) — arms independent, so §6.3's unpaired procedures are valid as written. `cell_key` defined once and recorded per row. |
| D-39 | Counterbalancing remainder and permutation trigger | Balance block B = (#arrangements) × (#starting seats); `n_effective = ceil(n_requested / B) · B`; `n_requested`, `n_effective`, `B`, `rotation_index`, `starting_seat_index` written per row. Full permutations exactly when a cell holds ≥ 2 distinct non-field strategies. |
| D-40 | Power table and n re-allocation | Per-estimand SE/MDES table at the chosen n and Holm-adjusted alpha; EX-6 two-way cells to n = 40k, three-way to n = 80k (≈5 s / ≈10 s per cell on 8 workers). |
| D-41 | Pre-registration status (§14) | Frozen as git tag `prereg-v1` before EX-1; `prereg_version` in every config and row; changes to §6/§8 are amendments with a ledger row stating what data already existed. EX-1..EX-5 confirmatory, EX-6 exploratory unless its arms are pre-registered. `docs/results.md` reports every §6.2 metric for every cell regardless of outcome. |
| D-42 | Data management (NF-6) | `summary.jsonl` gzipped; `campaigns/` in git holds `campaign.json` plus compressed summaries under a stated cap; larger artifacts are release assets referenced by hash. Reproducibility contract = master seed + engine version + prereg tag. |
| D-43 | UI build target | Single self-contained HTML file, all JS/CSS inlined, no module entry script, no code splitting, no runtime asset fetch. AK-6 opens the built artifact from disk. |

---

## E. What this review did *not* find

Stated explicitly, because a review that only lists problems misrepresents the
document.

- **The rule model is sound.** GM-7's single-source-of-truth legality
  function, the canonical move ordering requirement, the `capture_enforcement`
  enum reserved from day one, and the deliberate definition of relaxed
  counterparts where the Wikipedia variant coincides with the Schmidt baseline
  are all good design, and no lens found a rule that is unimplementable other
  than the two pinned above.
- **No termination or deadlock risk was confirmed.** The rules lens looked
  specifically for non-terminating games and lock-ups (barrier on an entry
  field, forced extra laps, compulsory-move deadlocks) and found no case where
  a game cannot progress. `mandatory_extended` is under-specified in its
  *encoding*, not in its termination behaviour.
- **The logging contract is adequate** for the replay invariant, given the
  header additions in C-14.
- **NF-2's throughput target is plausible** for the state representation the
  document describes, with the caveat that §4.1's requirement to log the full
  offered legal-move set for every move is in tension with it — the benchmark
  cells in C-20 should be measured with logging at the campaign default, not
  disabled.
- **The segment convention in §6.2** (dynamics metrics over the first-win
  segment, counters over the full game) is a genuinely good decision and is
  well argued in the document itself.
- 13 of 76 raw findings were refuted outright, most commonly because §9 or §12
  already covered the point. That the refutation rate is this low is itself a
  signal: the reviewed surface was mostly real.

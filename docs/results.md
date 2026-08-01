# MadnLab results

Measured effects of the optional rules and movement strategies of *Mensch ärgere Dich nicht*, against the pre-registration frozen at `prereg-v1`.

| | |
|---|---|
| Pre-registration | `prereg-v1` |
| Engine | `0.1.0` |
| Campaigns | ak5-smoke, ex1, ex1b, ex2, ex3, ex4, ex5, ex6 |
| Cells | 387 |
| Games | 16,430,642 |
| Analysis seed | `20260801` |
| Bootstrap resamples | 1,000 |

## 1. Reading this document

Sections 2 and 3 are **confirmatory**: 40 hypotheses fixed in §6.4 before any campaign ran, Holm-corrected within each family. Sections 4 to 6 are **descriptive** — computed, published, and explicitly not error-controlled. §14.4 requires every §6.2 metric of every cell to appear whether or not anything depends on it, which is why section 6 is long and unselective.

Game outcomes: **0 abandoned**, **0 stalemated** out of 16,430,642. Both are measured outcomes of the rule set (D-69, D-70), not errors; no estimand is published from a cell with a non-negligible rate without saying so.

## 2. Confirmatory results

### RQ-1

8 tests, Holm-corrected within the family at alpha = 0.05.

| Contrast | Estimate | 95% CI | p | Holm alpha | Verdict |
|---|---:|---|---:|---:|---|
| CV ratio rounds_to_first_win :: mandatory-optional | 1.1689 | [1.1642, 1.1734] | &lt;1e-300 | 0.00625 | **rejected** |
| lead changes per turn :: mandatory-optional | -0.0058 | [-0.0059, -0.0057] | &lt;1e-300 | 0.00714 | **rejected** |
| comeback rate :: mandatory-optional | 0.0063 | [0.0040, 0.0085] | 6.46e-08 | 0.02500 | **rejected** |
| leader-at-50% wins :: mandatory-optional | -0.0018 | [-0.0045, 0.0010] | 0.2131 | 0.05000 | not rejected |
| CV ratio rounds_to_first_win :: mandatory_extended-optional | 1.2341 | [1.2293, 1.2390] | &lt;1e-300 | 0.00833 | **rejected** |
| lead changes per turn :: mandatory_extended-optional | -0.0072 | [-0.0073, -0.0070] | &lt;1e-300 | 0.01000 | **rejected** |
| comeback rate :: mandatory_extended-optional | 0.0163 | [0.0140, 0.0186] | &lt;1e-300 | 0.01250 | **rejected** |
| leader-at-50% wins :: mandatory_extended-optional | -0.0101 | [-0.0129, -0.0074] | 7.12e-13 | 0.01667 | **rejected** |

**7 of 8 rejected** after Holm correction.

### RQ-2

18 tests, Holm-corrected within the family at alpha = 0.05.

| Contrast | Estimate | 95% CI | p | Holm alpha | Verdict |
|---|---:|---|---:|---:|---|
| win rate by starting seat :: cold_start:strict-one_piece_out | -0.0009 | [-0.0019, 0.0001] | 0.0753 | 0.00833 | not rejected |
| rounds to first win :: cold_start:strict-one_piece_out | 2.1699 | [2.0694, 2.2601] | &lt;1e-300 | 0.00278 | **rejected** |
| win rate by starting seat :: cold_start:free_entry-one_piece_out | -0.0033 | [-0.0047, -0.0019] | 5.11e-06 | 0.00500 | **rejected** |
| rounds to first win :: cold_start:free_entry-one_piece_out | 207.8 | [207.3, 208.4] | &lt;1e-300 | 0.00294 | **rejected** |
| win rate by starting seat :: capture_mode:mandatory-optional | -0.0016 | [-0.0028, -0.0005] | 0.0053 | 0.00625 | **rejected** |
| rounds to first win :: capture_mode:mandatory-optional | 64.3 | [64.1, 64.5] | &lt;1e-300 | 0.00313 | **rejected** |
| win rate by starting seat :: capture_mode:mandatory_extended-optional | -0.0014 | [-0.0026, -0.0003] | 0.0136 | 0.00714 | not rejected |
| rounds to first win :: capture_mode:mandatory_extended-optional | 92.2 | [92.0, 92.5] | &lt;1e-300 | 0.00333 | **rejected** |
| win rate by starting seat :: dreimal_wuerfeln:on-off | 0.0005 | [-0.0004, 0.0014] | 0.2922 | 0.01250 | not rejected |
| rounds to first win :: dreimal_wuerfeln:on-off | -70.0 | [-70.2, -69.7] | &lt;1e-300 | 0.00357 | **rejected** |
| win rate by starting seat :: bonus_roll_after_quick_entry:true-false | -0.0007 | [-0.0017, 0.0004] | 0.2101 | 0.01000 | not rejected |
| rounds to first win :: bonus_roll_after_quick_entry:true-false | -45.9 | [-46.1, -45.7] | &lt;1e-300 | 0.00385 | **rejected** |
| win rate by starting seat :: goal_no_jump:true-false | 0.0001 | [-0.0009, 0.0010] | 0.8685 | 0.02500 | not rejected |
| rounds to first win :: goal_no_jump:true-false | 7.0980 | [6.8512, 7.3389] | &lt;1e-300 | 0.00417 | **rejected** |
| win rate by starting seat :: barriers:true-false | 0.0001 | [-0.0009, 0.0010] | 0.9081 | 0.05000 | not rejected |
| rounds to first win :: barriers:true-false | -0.4144 | [-0.6478, -0.1773] | 0.0007 | 0.00556 | **rejected** |
| win rate by starting seat :: bonus_roll_forfeited:true-false | -0.0002 | [-0.0012, 0.0007] | 0.6140 | 0.01667 | not rejected |
| rounds to first win :: bonus_roll_forfeited:true-false | 2.1583 | [1.9128, 2.4082] | &lt;1e-300 | 0.00455 | **rejected** |

**11 of 18 rejected** after Holm correction.

### RQ-3

4 tests, Holm-corrected within the family at alpha = 0.05.

| Contrast | Estimate | 95% CI | p | Holm alpha | Verdict |
|---|---:|---|---:|---:|---|
| deviant win rate vs 1/k :: SPREAD | 0.0000 | [-0.0019, 0.0019] | 0.9794 | 0.05000 | not rejected |
| deviant win rate vs 1/k :: FOCUS_FRONT | 0.0009 | [-0.0010, 0.0028] | 0.3316 | 0.01250 | not rejected |
| deviant win rate vs 1/k :: FOCUS_REAR | 0.0004 | [-0.0015, 0.0023] | 0.6495 | 0.01667 | not rejected |
| deviant win rate :: FOCUS_FRONT - FOCUS_REAR | 0.0005 | [-0.0022, 0.0032] | 0.7153 | 0.02500 | not rejected |

**0 of 4 rejected** after Holm correction.

### RQ-4

10 tests, Holm-corrected within the family at alpha = 0.05.

| Contrast | Estimate | 95% CI | p | Holm alpha | Verdict |
|---|---:|---|---:|---:|---|
| deviant edge shift :: capture_mode:mandatory x strategy | 0.0004 | [-0.0015, 0.0023] | 0.6985 | 0.02500 | not rejected |
| deviant edge shift :: capture_mode:mandatory_extended x strategy | 0.0015 | [-0.0004, 0.0034] | 0.1173 | 0.01250 | not rejected |
| deviant edge shift :: barriers x strategy | -0.0009 | [-0.0028, 0.0010] | 0.3318 | 0.01667 | not rejected |
| deviant edge shift :: capture_mode:mandatory x strategy x players | 0.0018 | [-0.0001, 0.0037] | 0.0606 | 0.00833 | not rejected |
| deviant edge shift :: capture_mode:mandatory_extended x strategy x players | 0.0017 | [-0.0002, 0.0036] | 0.0865 | 0.01000 | not rejected |
| deviant edge shift :: barriers x strategy x players | 0.0002 | [-0.0017, 0.0021] | 0.8606 | 0.05000 | not rejected |
| rounds to first win, interaction :: capture_mode x players | -46.4 | [-46.7, -46.2] | &lt;1e-300 | 0.00500 | **rejected** |
| rounds to first win, interaction :: capture_mode x players x board | 9.5011 | [8.8238, 10.2] | &lt;1e-300 | 0.00556 | **rejected** |
| rounds to first win :: EX-5 pattern effect | -2.0464 | [-2.1526, -1.9523] | &lt;1e-300 | 0.00625 | **rejected** |
| rounds to first win :: EX-5 geometry effect | -11.7 | [-11.8, -11.6] | &lt;1e-300 | 0.00714 | **rejected** |

**4 of 10 rejected** after Holm correction.

### RQ-1 support criterion

§6.4 states the criterion as a decidable biconditional: RQ-1 is supported **iff** (i) the lower bound of the 95% BCa CI on the CV ratio of `rounds_to_first_win` (mandatory ÷ optional) exceeds 1, **and** (ii) at least 2 of 3 dynamism conjuncts have Holm-adjusted CIs excluding zero in the dynamism direction.

- (i) CV ratio 1.1689, 95% CI lower bound 1.1642 > 1
- (ii) lead_changes_per_turn: -0.005775 (dynamism direction no), Holm rejected at alpha=0.00714 -> does not count
- (ii) comeback_rate: +0.006256 (dynamism direction yes), Holm rejected at alpha=0.02500 -> counts
- (ii) predictability_skill: -0.001760 (dynamism direction yes), Holm not rejected at alpha=0.05000 -> does not count

Conjuncts satisfied: **1 of 3** (2 required).

## RQ-1 is **NOT SUPPORTED**

Reported as not supported, with every metric value published either way (§6.4). A failure to meet a pre-registered criterion is a result, not a reason to look for another criterion.

## 3. Calibration and invariants

AK-4 is a harness and geometry gate scoped to the calibration cells (§11, D-74). It is reported for every cell — a large non-calibration cell showing asymmetry beyond δ is something the project wants to hear about — but only cells whose seats are exchangeable by construction gate the run. `INCONCLUSIVE` means the interval is wider than the margin, so the test could not pass on any data; it is not evidence of asymmetry (D-72).

| Cell | AK-4 | gates | half-width pp | AK-5 capture | AK-5 extra-lap |
|---|---|---|---:|---|---|
| `ak5/4s4p/greedy/extended` | INCONCLUSIVE | yes | 0.7840 | 1,206,016 / 0 | 41,912 / 0 |
| `ak5/4s4p/random/mandatory` | INCONCLUSIVE | yes | 0.7838 | 1,011,531 / 0 | 0 / 0 |
| `ex1/4s4p/random/baseline` | PASS | yes | 0.1763 | — | — |
| `ex1b/6s6p/random/baseline` | PASS | yes | 0.1521 | — | — |
| `ex2/4s2p/greedy_capture/mandatory` | INCONCLUSIVE | no | 0.9105 | 162,365 / 0 | 0 / 0 |
| `ex2/4s2p/greedy_capture/mandatory_extended` | INCONCLUSIVE | no | 0.9093 | 188,658 / 0 | 9,909 / 0 |
| `ex2/4s2p/greedy_capture/optional` | INCONCLUSIVE | no | 0.9105 | — | — |
| `ex2/4s2p/random/mandatory` | INCONCLUSIVE | no | 0.9105 | 163,334 / 0 | 0 / 0 |
| `ex2/4s2p/random/mandatory_extended` | INCONCLUSIVE | no | 0.9084 | 187,327 / 0 | 10,212 / 0 |
| `ex2/4s2p/random/optional` | INCONCLUSIVE | no | 0.9097 | — | — |
| `ex2/4s2p/spread/mandatory` | INCONCLUSIVE | no | 0.8907 | 163,989 / 0 | 0 / 0 |
| `ex2/4s2p/spread/mandatory_extended` | INCONCLUSIVE | no | 0.8950 | 198,228 / 0 | 10,910 / 0 |
| `ex2/4s2p/spread/optional` | INCONCLUSIVE | no | 0.8717 | — | — |
| `ex2/4s3p/greedy_capture/mandatory` | INCONCLUSIVE | no | 0.8567 | 498,864 / 0 | 0 / 0 |
| `ex2/4s3p/greedy_capture/mandatory_extended` | INCONCLUSIVE | no | 0.8716 | 588,308 / 0 | 24,512 / 0 |
| `ex2/4s3p/greedy_capture/optional` | INCONCLUSIVE | no | 0.8589 | — | — |
| `ex2/4s3p/random/mandatory` | INCONCLUSIVE | no | 0.8609 | 502,371 / 0 | 0 / 0 |
| `ex2/4s3p/random/mandatory_extended` | INCONCLUSIVE | no | 0.8708 | 585,515 / 0 | 24,324 / 0 |
| `ex2/4s3p/random/optional` | INCONCLUSIVE | no | 0.8625 | — | — |
| `ex2/4s3p/spread/mandatory` | INCONCLUSIVE | no | 0.8381 | 658,473 / 0 | 0 / 0 |
| `ex2/4s3p/spread/mandatory_extended` | INCONCLUSIVE | no | 0.8420 | 814,348 / 0 | 34,172 / 0 |
| `ex2/4s3p/spread/optional` | INCONCLUSIVE | no | 0.8328 | — | — |
| `ex2/4s4p/greedy_capture/mandatory` | INCONCLUSIVE | yes | 0.7897 | 1,011,228 / 0 | 0 / 0 |
| `ex2/4s4p/greedy_capture/mandatory_extended` | INCONCLUSIVE | yes | 0.7854 | 1,203,338 / 0 | 42,005 / 0 |
| `ex2/4s4p/greedy_capture/optional` | INCONCLUSIVE | yes | 0.7862 | — | — |
| `ex2/4s4p/random/mandatory` | PASS | yes | 0.2232 | 12,640,525 / 0 | 0 / 0 |
| `ex2/4s4p/random/mandatory_extended` | PASS | yes | 0.2234 | 15,087,115 / 0 | 526,546 / 0 |
| `ex2/4s4p/random/optional` | PASS | yes | 0.2227 | — | — |
| `ex2/4s4p/spread/mandatory` | INCONCLUSIVE | yes | 0.7914 | 1,412,373 / 0 | 0 / 0 |
| `ex2/4s4p/spread/mandatory_extended` | INCONCLUSIVE | yes | 0.7875 | 1,786,484 / 0 | 61,674 / 0 |
| `ex2/4s4p/spread/optional` | INCONCLUSIVE | yes | 0.7911 | — | — |
| `ex2/6s6p/greedy_capture/mandatory` | INCONCLUSIVE | yes | 0.6762 | 3,509,529 / 0 | 0 / 0 |
| `ex2/6s6p/greedy_capture/mandatory_extended` | INCONCLUSIVE | yes | 0.6701 | 4,163,365 / 0 | 78,162 / 0 |
| `ex2/6s6p/greedy_capture/optional` | INCONCLUSIVE | yes | 0.6830 | — | — |
| `ex2/6s6p/random/mandatory` | INCONCLUSIVE | yes | 0.6748 | 3,505,971 / 0 | 0 / 0 |
| `ex2/6s6p/random/mandatory_extended` | INCONCLUSIVE | yes | 0.6801 | 4,174,444 / 0 | 78,129 / 0 |
| `ex2/6s6p/random/optional` | INCONCLUSIVE | yes | 0.6906 | — | — |
| `ex2/6s6p/spread/mandatory` | INCONCLUSIVE | yes | 0.6717 | 5,320,163 / 0 | 0 / 0 |
| `ex2/6s6p/spread/mandatory_extended` | INCONCLUSIVE | yes | 0.6762 | 6,561,168 / 0 | 108,662 / 0 |
| `ex2/6s6p/spread/optional` | INCONCLUSIVE | yes | 0.6770 | — | — |
| `ex3/deviant/4s2p/focus_front-vs-focus_rear` | INCONCLUSIVE | no | 0.9102 | — | — |
| `ex3/deviant/4s2p/focus_front-vs-random` | INCONCLUSIVE | no | 0.9103 | — | — |
| `ex3/deviant/4s2p/focus_front-vs-spread` | INCONCLUSIVE | no | 0.9104 | — | — |
| `ex3/deviant/4s2p/focus_rear-vs-focus_front` | INCONCLUSIVE | no | 0.9101 | — | — |
| `ex3/deviant/4s2p/focus_rear-vs-random` | INCONCLUSIVE | no | 0.9067 | — | — |
| `ex3/deviant/4s2p/focus_rear-vs-spread` | INCONCLUSIVE | no | 0.8820 | — | — |
| `ex3/deviant/4s2p/random-vs-focus_front` | INCONCLUSIVE | no | 0.9105 | — | — |
| `ex3/deviant/4s2p/random-vs-focus_rear` | INCONCLUSIVE | no | 0.9059 | — | — |
| `ex3/deviant/4s2p/random-vs-spread` | INCONCLUSIVE | no | 0.9039 | — | — |
| `ex3/deviant/4s2p/spread-vs-focus_front` | INCONCLUSIVE | no | 0.9101 | — | — |
| `ex3/deviant/4s2p/spread-vs-focus_rear` | INCONCLUSIVE | no | 0.8833 | — | — |
| `ex3/deviant/4s2p/spread-vs-random` | INCONCLUSIVE | no | 0.9040 | — | — |
| `ex3/deviant/4s3p/focus_front-vs-focus_rear` | INCONCLUSIVE | no | 0.8584 | — | — |
| `ex3/deviant/4s3p/focus_front-vs-random` | INCONCLUSIVE | no | 0.8638 | — | — |
| `ex3/deviant/4s3p/focus_front-vs-spread` | INCONCLUSIVE | no | 0.8599 | — | — |
| `ex3/deviant/4s3p/focus_rear-vs-focus_front` | INCONCLUSIVE | no | 0.8704 | — | — |
| `ex3/deviant/4s3p/focus_rear-vs-random` | INCONCLUSIVE | no | 0.8569 | — | — |
| `ex3/deviant/4s3p/focus_rear-vs-spread` | INCONCLUSIVE | no | 0.8352 | — | — |
| `ex3/deviant/4s3p/random-vs-focus_front` | INCONCLUSIVE | no | 0.8672 | — | — |
| `ex3/deviant/4s3p/random-vs-focus_rear` | INCONCLUSIVE | no | 0.8473 | — | — |
| `ex3/deviant/4s3p/random-vs-spread` | INCONCLUSIVE | no | 0.8459 | — | — |
| `ex3/deviant/4s3p/spread-vs-focus_front` | INCONCLUSIVE | no | 0.8728 | — | — |
| `ex3/deviant/4s3p/spread-vs-focus_rear` | INCONCLUSIVE | no | 0.8381 | — | — |
| `ex3/deviant/4s3p/spread-vs-random` | INCONCLUSIVE | no | 0.8534 | — | — |
| `ex3/deviant/4s4p/focus_front-vs-focus_rear` | INCONCLUSIVE | no | 0.7908 | — | — |
| `ex3/deviant/4s4p/focus_front-vs-random` | PASS | no | 0.2497 | — | — |
| `ex3/deviant/4s4p/focus_front-vs-spread` | INCONCLUSIVE | no | 0.7897 | — | — |
| `ex3/deviant/4s4p/focus_rear-vs-focus_front` | INCONCLUSIVE | no | 0.7894 | — | — |
| `ex3/deviant/4s4p/focus_rear-vs-random` | PASS | no | 0.2495 | — | — |
| `ex3/deviant/4s4p/focus_rear-vs-spread` | INCONCLUSIVE | no | 0.7854 | — | — |
| `ex3/deviant/4s4p/random-vs-focus_front` | INCONCLUSIVE | no | 0.7870 | — | — |
| `ex3/deviant/4s4p/random-vs-focus_rear` | INCONCLUSIVE | no | 0.7883 | — | — |
| `ex3/deviant/4s4p/random-vs-spread` | INCONCLUSIVE | no | 0.7834 | — | — |
| `ex3/deviant/4s4p/spread-vs-focus_front` | INCONCLUSIVE | no | 0.7875 | — | — |
| `ex3/deviant/4s4p/spread-vs-focus_rear` | INCONCLUSIVE | no | 0.7950 | — | — |
| `ex3/deviant/4s4p/spread-vs-random` | FAIL | no | 0.2494 | — | — |
| `ex3/deviant/6s6p/focus_front-vs-focus_rear` | INCONCLUSIVE | no | 0.6862 | — | — |
| `ex3/deviant/6s6p/focus_front-vs-random` | INCONCLUSIVE | no | 0.6780 | — | — |
| `ex3/deviant/6s6p/focus_front-vs-spread` | INCONCLUSIVE | no | 0.6799 | — | — |
| `ex3/deviant/6s6p/focus_rear-vs-focus_front` | INCONCLUSIVE | no | 0.6800 | — | — |
| `ex3/deviant/6s6p/focus_rear-vs-random` | INCONCLUSIVE | no | 0.6815 | — | — |
| `ex3/deviant/6s6p/focus_rear-vs-spread` | INCONCLUSIVE | no | 0.6786 | — | — |
| `ex3/deviant/6s6p/random-vs-focus_front` | INCONCLUSIVE | no | 0.6838 | — | — |
| `ex3/deviant/6s6p/random-vs-focus_rear` | INCONCLUSIVE | no | 0.6854 | — | — |
| `ex3/deviant/6s6p/random-vs-spread` | INCONCLUSIVE | no | 0.6731 | — | — |
| `ex3/deviant/6s6p/spread-vs-focus_front` | INCONCLUSIVE | no | 0.6738 | — | — |
| `ex3/deviant/6s6p/spread-vs-focus_rear` | INCONCLUSIVE | no | 0.6774 | — | — |
| `ex3/deviant/6s6p/spread-vs-random` | INCONCLUSIVE | no | 0.6802 | — | — |
| `ex3/homogeneous/4s2p/focus_front` | INCONCLUSIVE | no | 0.9100 | — | — |
| `ex3/homogeneous/4s2p/focus_rear` | INCONCLUSIVE | no | 0.8891 | — | — |
| `ex3/homogeneous/4s2p/random` | INCONCLUSIVE | no | 0.9101 | — | — |
| `ex3/homogeneous/4s2p/spread` | INCONCLUSIVE | no | 0.8729 | — | — |
| `ex3/homogeneous/4s3p/focus_front` | INCONCLUSIVE | no | 0.8715 | — | — |
| `ex3/homogeneous/4s3p/focus_rear` | INCONCLUSIVE | no | 0.8410 | — | — |
| `ex3/homogeneous/4s3p/random` | INCONCLUSIVE | no | 0.8569 | — | — |
| `ex3/homogeneous/4s3p/spread` | INCONCLUSIVE | no | 0.8302 | — | — |
| `ex3/homogeneous/4s4p/focus_front` | INCONCLUSIVE | yes | 0.7919 | — | — |
| `ex3/homogeneous/4s4p/focus_rear` | INCONCLUSIVE | yes | 0.7909 | — | — |
| `ex3/homogeneous/4s4p/random` | INCONCLUSIVE | yes | 0.7883 | — | — |
| `ex3/homogeneous/4s4p/spread` | INCONCLUSIVE | yes | 0.7907 | — | — |
| `ex3/homogeneous/6s6p/focus_front` | INCONCLUSIVE | yes | 0.6786 | — | — |
| `ex3/homogeneous/6s6p/focus_rear` | INCONCLUSIVE | yes | 0.6782 | — | — |
| `ex3/homogeneous/6s6p/random` | INCONCLUSIVE | yes | 0.6790 | — | — |
| `ex3/homogeneous/6s6p/spread` | INCONCLUSIVE | yes | 0.6805 | — | — |
| `ex4/4s4p/random/barriers=True` | INCONCLUSIVE | yes | 0.7870 | — | — |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.7822 | 1,389,304 / 0 | 0 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7848 | 1,433,603 / 0 | 0 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.7887 | 1,388,220 / 0 | 0 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7852 | 1,431,792 / 0 | 0 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.7862 | 1,676,064 / 0 | 49,436 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7873 | 1,729,115 / 0 | 53,987 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.7892 | 1,677,539 / 0 | 49,805 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7927 | 1,728,055 / 0 | 54,159 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-cold_start=strict-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.7896 | — | — |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7832 | — | — |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.7889 | — | — |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7888 | — | — |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.7896 | 1,380,123 / 0 | 0 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7865 | 1,418,741 / 0 | 0 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-capture_mode=mandatory-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.7861 | 1,384,330 / 0 | 0 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-capture_mode=mandatory-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7867 | 1,416,787 / 0 | 0 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.7827 | 1,667,562 / 0 | 49,204 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7863 | 1,720,729 / 0 | 54,121 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-capture_mode=mandatory_extended-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.7884 | 1,680,856 / 0 | 49,733 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-capture_mode=mandatory_extended-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7916 | 1,716,584 / 0 | 53,787 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-cold_start=strict-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.7917 | — | — |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7916 | — | — |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.7914 | — | — |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7872 | — | — |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True` | INCONCLUSIVE | yes | 0.7885 | — | — |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory` | INCONCLUSIVE | yes | 0.7911 | 1,008,797 / 0 | 0 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=free_entry` | INCONCLUSIVE | yes | 0.7908 | 9,304,455 / 0 | 0 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=free_entry-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7865 | 9,589,294 / 0 | 0 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=strict` | INCONCLUSIVE | yes | 0.7900 | 999,726 / 0 | 0 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.7824 | 1,255,948 / 0 | 0 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7921 | 1,300,735 / 0 | 0 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=strict-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7888 | 1,040,910 / 0 | 0 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.7889 | 1,258,662 / 0 | 0 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7927 | 1,295,389 / 0 | 0 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7890 | 1,057,651 / 0 | 0 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended` | INCONCLUSIVE | yes | 0.7876 | 1,211,711 / 0 | 42,467 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=free_entry` | INCONCLUSIVE | yes | 0.7908 | 11,161,815 / 0 | 64,545 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=free_entry-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7897 | 11,465,546 / 0 | 71,138 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=strict` | INCONCLUSIVE | yes | 0.7921 | 1,199,216 / 0 | 43,093 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.7881 | 1,516,969 / 0 | 48,669 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7888 | 1,577,575 / 0 | 53,462 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=strict-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7943 | 1,251,748 / 0 | 48,778 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.7947 | 1,521,445 / 0 | 48,305 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7896 | 1,567,493 / 0 | 53,111 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7859 | 1,267,531 / 0 | 49,283 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-cold_start=free_entry` | INCONCLUSIVE | yes | 0.7876 | — | — |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-cold_start=free_entry-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7904 | — | — |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-cold_start=strict` | INCONCLUSIVE | yes | 0.7850 | — | — |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-cold_start=strict-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.7870 | — | — |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7891 | — | — |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-cold_start=strict-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7905 | — | — |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.7906 | — | — |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7882 | — | — |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7874 | — | — |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory` | INCONCLUSIVE | yes | 0.7847 | 1,001,441 / 0 | 0 / 0 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory-cold_start=free_entry` | INCONCLUSIVE | yes | 0.7848 | 9,235,969 / 0 | 0 / 0 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory-cold_start=free_entry-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7883 | 9,514,203 / 0 | 0 / 0 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory-cold_start=strict` | INCONCLUSIVE | yes | 0.7852 | 982,827 / 0 | 0 / 0 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.7900 | 1,250,046 / 0 | 0 / 0 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7867 | 1,284,881 / 0 | 0 / 0 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory-cold_start=strict-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7896 | 1,028,648 / 0 | 0 / 0 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.7881 | 1,251,718 / 0 | 0 / 0 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7847 | 1,285,999 / 0 | 0 / 0 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7941 | 1,048,020 / 0 | 0 / 0 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory_extended` | INCONCLUSIVE | yes | 0.7858 | 1,201,257 / 0 | 42,443 / 0 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory_extended-cold_start=free_entry` | INCONCLUSIVE | yes | 0.7886 | 11,105,543 / 0 | 64,697 / 0 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory_extended-cold_start=free_entry-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7881 | 11,415,584 / 0 | 70,359 / 0 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory_extended-cold_start=strict` | INCONCLUSIVE | yes | 0.7913 | 1,189,896 / 0 | 42,558 / 0 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.7874 | 1,509,070 / 0 | 48,515 / 0 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7902 | 1,560,535 / 0 | 53,524 / 0 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory_extended-cold_start=strict-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7940 | 1,240,034 / 0 | 48,935 / 0 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory_extended-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.7913 | 1,506,233 / 0 | 48,240 / 0 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory_extended-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7913 | 1,568,218 / 0 | 53,679 / 0 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory_extended-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7919 | 1,251,483 / 0 | 48,891 / 0 |
| `ex4/4s4p/random/barriers=True-cold_start=free_entry` | INCONCLUSIVE | yes | 0.7916 | — | — |
| `ex4/4s4p/random/barriers=True-cold_start=free_entry-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7818 | — | — |
| `ex4/4s4p/random/barriers=True-cold_start=strict` | INCONCLUSIVE | yes | 0.7895 | — | — |
| `ex4/4s4p/random/barriers=True-cold_start=strict-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.7891 | — | — |
| `ex4/4s4p/random/barriers=True-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7850 | — | — |
| `ex4/4s4p/random/barriers=True-cold_start=strict-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7820 | — | — |
| `ex4/4s4p/random/barriers=True-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.7869 | — | — |
| `ex4/4s4p/random/barriers=True-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7865 | — | — |
| `ex4/4s4p/random/barriers=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7942 | — | — |
| `ex4/4s4p/random/baseline` | INCONCLUSIVE | yes | 0.7915 | — | — |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.7894 | 1,406,397 / 0 | 0 / 0 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7854 | 1,452,820 / 0 | 0 / 0 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.7860 | 1,414,066 / 0 | 0 / 0 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7897 | 1,448,698 / 0 | 0 / 0 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.7920 | 1,691,841 / 0 | 49,028 / 0 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7928 | 1,739,746 / 0 | 53,298 / 0 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.7841 | 1,683,572 / 0 | 48,768 / 0 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7945 | 1,748,229 / 0 | 53,844 / 0 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-cold_start=strict-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.7905 | — | — |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7887 | — | — |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.7874 | — | — |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7923 | — | — |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.7903 | 1,400,314 / 0 | 0 / 0 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7878 | 1,433,678 / 0 | 0 / 0 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-capture_mode=mandatory-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.7872 | 1,397,304 / 0 | 0 / 0 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-capture_mode=mandatory-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7901 | 1,441,074 / 0 | 0 / 0 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.7915 | 1,681,004 / 0 | 48,854 / 0 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7915 | 1,723,076 / 0 | 53,350 / 0 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-capture_mode=mandatory_extended-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.7831 | 1,686,438 / 0 | 48,804 / 0 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-capture_mode=mandatory_extended-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7931 | 1,733,806 / 0 | 53,591 / 0 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-cold_start=strict-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.7855 | — | — |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7874 | — | — |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.7863 | — | — |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7873 | — | — |
| `ex4/4s4p/random/bonus_roll_forfeited=True` | INCONCLUSIVE | yes | 0.7883 | — | — |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory` | INCONCLUSIVE | yes | 0.7885 | 1,018,646 / 0 | 0 / 0 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=free_entry` | INCONCLUSIVE | yes | 0.7870 | 9,534,587 / 0 | 0 / 0 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=free_entry-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7889 | 9,794,878 / 0 | 0 / 0 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=strict` | INCONCLUSIVE | yes | 0.7922 | 1,007,687 / 0 | 0 / 0 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.7861 | 1,266,049 / 0 | 0 / 0 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7867 | 1,305,064 / 0 | 0 / 0 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=strict-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7894 | 1,050,051 / 0 | 0 / 0 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.7876 | 1,266,346 / 0 | 0 / 0 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7883 | 1,306,205 / 0 | 0 / 0 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7939 | 1,062,885 / 0 | 0 / 0 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory_extended` | INCONCLUSIVE | yes | 0.7861 | 1,218,133 / 0 | 42,290 / 0 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=free_entry` | INCONCLUSIVE | yes | 0.7858 | 11,354,430 / 0 | 63,680 / 0 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=free_entry-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7866 | 11,739,041 / 0 | 70,295 / 0 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=strict` | INCONCLUSIVE | yes | 0.7917 | 1,204,947 / 0 | 42,049 / 0 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.7949 | 1,531,477 / 0 | 47,970 / 0 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7864 | 1,576,663 / 0 | 52,892 / 0 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=strict-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7901 | 1,258,436 / 0 | 48,544 / 0 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory_extended-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.7856 | 1,529,529 / 0 | 47,769 / 0 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory_extended-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7855 | 1,572,956 / 0 | 52,803 / 0 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory_extended-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7913 | 1,272,354 / 0 | 48,333 / 0 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-cold_start=free_entry` | INCONCLUSIVE | yes | 0.7835 | — | — |
| `ex4/4s4p/random/bonus_roll_forfeited=True-cold_start=free_entry-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7957 | — | — |
| `ex4/4s4p/random/bonus_roll_forfeited=True-cold_start=strict` | INCONCLUSIVE | yes | 0.7868 | — | — |
| `ex4/4s4p/random/bonus_roll_forfeited=True-cold_start=strict-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.7879 | — | — |
| `ex4/4s4p/random/bonus_roll_forfeited=True-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7867 | — | — |
| `ex4/4s4p/random/bonus_roll_forfeited=True-cold_start=strict-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7871 | — | — |
| `ex4/4s4p/random/bonus_roll_forfeited=True-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.7888 | — | — |
| `ex4/4s4p/random/bonus_roll_forfeited=True-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7900 | — | — |
| `ex4/4s4p/random/bonus_roll_forfeited=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7909 | — | — |
| `ex4/4s4p/random/capture_mode=mandatory` | INCONCLUSIVE | yes | 0.7867 | 1,014,333 / 0 | 0 / 0 |
| `ex4/4s4p/random/capture_mode=mandatory-cold_start=free_entry` | INCONCLUSIVE | yes | 0.7909 | 9,508,455 / 0 | 0 / 0 |
| `ex4/4s4p/random/capture_mode=mandatory-cold_start=free_entry-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7814 | 9,709,914 / 0 | 0 / 0 |
| `ex4/4s4p/random/capture_mode=mandatory-cold_start=strict` | INCONCLUSIVE | yes | 0.7892 | 1,001,069 / 0 | 0 / 0 |
| `ex4/4s4p/random/capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.7880 | 1,259,761 / 0 | 0 / 0 |
| `ex4/4s4p/random/capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7902 | 1,295,218 / 0 | 0 / 0 |
| `ex4/4s4p/random/capture_mode=mandatory-cold_start=strict-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7927 | 1,039,431 / 0 | 0 / 0 |
| `ex4/4s4p/random/capture_mode=mandatory-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.7938 | 1,256,364 / 0 | 0 / 0 |
| `ex4/4s4p/random/capture_mode=mandatory-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7903 | 1,298,332 / 0 | 0 / 0 |
| `ex4/4s4p/random/capture_mode=mandatory-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7877 | 1,053,069 / 0 | 0 / 0 |
| `ex4/4s4p/random/capture_mode=mandatory_extended` | INCONCLUSIVE | yes | 0.7918 | 1,204,103 / 0 | 41,812 / 0 |
| `ex4/4s4p/random/capture_mode=mandatory_extended-cold_start=free_entry` | INCONCLUSIVE | yes | 0.7870 | 11,321,767 / 0 | 63,595 / 0 |
| `ex4/4s4p/random/capture_mode=mandatory_extended-cold_start=free_entry-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7837 | 11,598,977 / 0 | 70,141 / 0 |
| `ex4/4s4p/random/capture_mode=mandatory_extended-cold_start=strict` | INCONCLUSIVE | yes | 0.7880 | 1,189,922 / 0 | 41,381 / 0 |
| `ex4/4s4p/random/capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.7881 | 1,517,027 / 0 | 47,697 / 0 |
| `ex4/4s4p/random/capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7892 | 1,563,025 / 0 | 52,593 / 0 |
| `ex4/4s4p/random/capture_mode=mandatory_extended-cold_start=strict-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7863 | 1,248,415 / 0 | 48,022 / 0 |
| `ex4/4s4p/random/capture_mode=mandatory_extended-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.7924 | 1,509,614 / 0 | 47,666 / 0 |
| `ex4/4s4p/random/capture_mode=mandatory_extended-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7857 | 1,565,056 / 0 | 52,673 / 0 |
| `ex4/4s4p/random/capture_mode=mandatory_extended-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7854 | 1,259,059 / 0 | 48,090 / 0 |
| `ex4/4s4p/random/cold_start=free_entry` | INCONCLUSIVE | yes | 0.7894 | — | — |
| `ex4/4s4p/random/cold_start=free_entry-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7922 | — | — |
| `ex4/4s4p/random/cold_start=strict` | INCONCLUSIVE | yes | 0.7906 | — | — |
| `ex4/4s4p/random/cold_start=strict-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.7893 | — | — |
| `ex4/4s4p/random/cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7892 | — | — |
| `ex4/4s4p/random/cold_start=strict-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7879 | — | — |
| `ex4/4s4p/random/dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.7909 | — | — |
| `ex4/4s4p/random/dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.7911 | — | — |
| `ex4/4s4p/random/goal_no_jump=True` | INCONCLUSIVE | yes | 0.7858 | — | — |
| `ex5/2p/adjacent/random` | INCONCLUSIVE | no | 0.9100 | — | — |
| `ex5/2p/adjacent/spread` | INCONCLUSIVE | no | 0.8702 | — | — |
| `ex5/2p/opposite/random` | INCONCLUSIVE | yes | 0.9105 | — | — |
| `ex5/2p/opposite/spread` | INCONCLUSIVE | yes | 0.9105 | — | — |
| `ex5/3p/4s-adjacent/random` | FAIL | no | 0.2428 | — | — |
| `ex5/3p/4s-adjacent/spread` | FAIL | no | 0.2358 | — | — |
| `ex5/3p/6s-adjacent/random` | FAIL | no | 0.2421 | — | — |
| `ex5/3p/6s-adjacent/spread` | FAIL | no | 0.2231 | — | — |
| `ex5/3p/6s-spread/random` | PASS | yes | 0.2426 | — | — |
| `ex5/3p/6s-spread/spread` | PASS | yes | 0.2428 | — | — |
| `ex6a/4s4p/focus_front/mandatory` | INCONCLUSIVE | yes | 0.7891 | 646,762 / 0 | 0 / 0 |
| `ex6a/4s4p/focus_front/mandatory_extended` | INCONCLUSIVE | yes | 0.7922 | 723,454 / 0 | 21,770 / 0 |
| `ex6a/4s4p/focus_front/optional` | INCONCLUSIVE | yes | 0.7894 | — | — |
| `ex6a/4s4p/focus_rear/mandatory` | INCONCLUSIVE | yes | 0.7814 | 1,329,266 / 0 | 0 / 0 |
| `ex6a/4s4p/focus_rear/mandatory_extended` | INCONCLUSIVE | yes | 0.7915 | 1,681,175 / 0 | 59,769 / 0 |
| `ex6a/4s4p/focus_rear/optional` | INCONCLUSIVE | yes | 0.7864 | — | — |
| `ex6a/4s4p/greedy_capture/mandatory` | INCONCLUSIVE | yes | 0.7910 | 1,010,314 / 0 | 0 / 0 |
| `ex6a/4s4p/greedy_capture/mandatory_extended` | INCONCLUSIVE | yes | 0.7890 | 1,203,032 / 0 | 41,702 / 0 |
| `ex6a/4s4p/greedy_capture/optional` | INCONCLUSIVE | yes | 0.7925 | — | — |
| `ex6a/4s4p/random/mandatory` | INCONCLUSIVE | yes | 0.7888 | 1,011,327 / 0 | 0 / 0 |
| `ex6a/4s4p/random/mandatory_extended` | INCONCLUSIVE | yes | 0.7886 | 1,209,642 / 0 | 42,210 / 0 |
| `ex6a/4s4p/random/optional` | INCONCLUSIVE | yes | 0.7879 | — | — |
| `ex6a/4s4p/spread/mandatory` | INCONCLUSIVE | yes | 0.7857 | 1,424,874 / 0 | 0 / 0 |
| `ex6a/4s4p/spread/mandatory_extended` | INCONCLUSIVE | yes | 0.7885 | 1,775,082 / 0 | 60,813 / 0 |
| `ex6a/4s4p/spread/optional` | INCONCLUSIVE | yes | 0.7863 | — | — |
| `ex6b/4s4p/focus_front-vs-random/mandatory` | PASS | no | 0.1766 | 18,335,466 / 0 | 0 / 0 |
| `ex6b/4s4p/focus_front-vs-random/mandatory_extended` | PASS | no | 0.1766 | 21,575,952 / 0 | 756,580 / 0 |
| `ex6b/4s4p/focus_front-vs-random/optional` | PASS | no | 0.1762 | — | — |
| `ex6b/4s4p/focus_rear-vs-random/mandatory` | INCONCLUSIVE | no | 0.7956 | 1,083,464 / 0 | 0 / 0 |
| `ex6b/4s4p/focus_rear-vs-random/mandatory_extended` | INCONCLUSIVE | no | 0.7913 | 1,307,490 / 0 | 47,540 / 0 |
| `ex6b/4s4p/focus_rear-vs-random/optional` | INCONCLUSIVE | no | 0.7821 | — | — |
| `ex6b/4s4p/greedy_capture-vs-random/mandatory` | INCONCLUSIVE | no | 0.7912 | 1,011,540 / 0 | 0 / 0 |
| `ex6b/4s4p/greedy_capture-vs-random/mandatory_extended` | INCONCLUSIVE | no | 0.7891 | 1,207,206 / 0 | 42,204 / 0 |
| `ex6b/4s4p/greedy_capture-vs-random/optional` | INCONCLUSIVE | no | 0.7856 | — | — |
| `ex6b/4s4p/spread-vs-random/mandatory` | PASS | no | 0.1764 | 21,883,706 / 0 | 0 / 0 |
| `ex6b/4s4p/spread-vs-random/mandatory_extended` | PASS | no | 0.1766 | 26,586,379 / 0 | 968,256 / 0 |
| `ex6b/4s4p/spread-vs-random/optional` | PASS | no | 0.1763 | — | — |
| `ex6c/4s4p/focus_front/barriers=False` | INCONCLUSIVE | yes | 0.7903 | — | — |
| `ex6c/4s4p/focus_front/barriers=True` | INCONCLUSIVE | yes | 0.7897 | — | — |
| `ex6c/4s4p/focus_rear/barriers=False` | INCONCLUSIVE | yes | 0.7856 | — | — |
| `ex6c/4s4p/focus_rear/barriers=True` | INCONCLUSIVE | yes | 0.7917 | — | — |
| `ex6c/4s4p/greedy_capture/barriers=False` | INCONCLUSIVE | yes | 0.7911 | — | — |
| `ex6c/4s4p/greedy_capture/barriers=True` | INCONCLUSIVE | yes | 0.7825 | — | — |
| `ex6c/4s4p/random/barriers=False` | INCONCLUSIVE | yes | 0.7875 | — | — |
| `ex6c/4s4p/random/barriers=True` | INCONCLUSIVE | yes | 0.7884 | — | — |
| `ex6c/4s4p/spread/barriers=False` | INCONCLUSIVE | yes | 0.7901 | — | — |
| `ex6c/4s4p/spread/barriers=True` | INCONCLUSIVE | yes | 0.7905 | — | — |
| `ex6d/4s4p/focus_front-vs-random/barriers=False` | PASS | no | 0.1763 | — | — |
| `ex6d/4s4p/focus_front-vs-random/barriers=True` | PASS | no | 0.1764 | — | — |
| `ex6d/4s4p/focus_rear-vs-random/barriers=False` | INCONCLUSIVE | no | 0.7886 | — | — |
| `ex6d/4s4p/focus_rear-vs-random/barriers=True` | INCONCLUSIVE | no | 0.7861 | — | — |
| `ex6d/4s4p/greedy_capture-vs-random/barriers=False` | INCONCLUSIVE | no | 0.7892 | — | — |
| `ex6d/4s4p/greedy_capture-vs-random/barriers=True` | INCONCLUSIVE | no | 0.7953 | — | — |
| `ex6d/4s4p/spread-vs-random/barriers=False` | PASS | no | 0.1765 | — | — |
| `ex6d/4s4p/spread-vs-random/barriers=True` | PASS | no | 0.1763 | — | — |
| `ex6e/6s2p/random/mandatory` | FAIL | no | 0.2036 | 3,793,872 / 0 | 0 / 0 |
| `ex6e/6s2p/random/mandatory_extended` | INCONCLUSIVE | no | 0.9075 | 214,317 / 0 | 9,487 / 0 |
| `ex6e/6s2p/random/optional` | FAIL | no | 0.2033 | — | — |
| `ex6e/6s3p/random/mandatory` | INCONCLUSIVE | no | 0.8683 | 592,061 / 0 | 0 / 0 |
| `ex6e/6s3p/random/mandatory_extended` | INCONCLUSIVE | no | 0.8855 | 685,688 / 0 | 23,457 / 0 |
| `ex6e/6s3p/random/optional` | INCONCLUSIVE | no | 0.8546 | — | — |
| `ex6e/6s4p/random/mandatory` | INCONCLUSIVE | no | 0.8006 | 1,258,877 / 0 | 0 / 0 |
| `ex6e/6s4p/random/mandatory_extended` | INCONCLUSIVE | no | 0.8193 | 1,474,799 / 0 | 39,274 / 0 |
| `ex6e/6s4p/random/optional` | INCONCLUSIVE | no | 0.7929 | — | — |
| `ex6e/6s6p/random/mandatory` | PASS | yes | 0.1514 | 70,274,094 / 0 | 0 / 0 |
| `ex6e/6s6p/random/mandatory_extended` | INCONCLUSIVE | yes | 0.6800 | 4,173,458 / 0 | 77,910 / 0 |
| `ex6e/6s6p/random/optional` | PASS | yes | 0.1517 | — | — |
| `ex6f/6s2p/focus_front-vs-random/mandatory` | INCONCLUSIVE | no | 0.9062 | 169,712 / 0 | 0 / 0 |
| `ex6f/6s2p/focus_front-vs-random/mandatory_extended` | INCONCLUSIVE | no | 0.9031 | 187,941 / 0 | 7,088 / 0 |
| `ex6f/6s2p/focus_front-vs-random/optional` | INCONCLUSIVE | no | 0.9096 | — | — |
| `ex6f/6s2p/focus_rear-vs-random/mandatory` | INCONCLUSIVE | no | 0.9081 | 202,274 / 0 | 0 / 0 |
| `ex6f/6s2p/focus_rear-vs-random/mandatory_extended` | INCONCLUSIVE | no | 0.9105 | 235,917 / 0 | 10,454 / 0 |
| `ex6f/6s2p/focus_rear-vs-random/optional` | INCONCLUSIVE | no | 0.9021 | — | — |
| `ex6f/6s2p/greedy_capture-vs-random/mandatory` | INCONCLUSIVE | no | 0.9105 | 190,300 / 0 | 0 / 0 |
| `ex6f/6s2p/greedy_capture-vs-random/mandatory_extended` | INCONCLUSIVE | no | 0.9074 | 213,724 / 0 | 9,491 / 0 |
| `ex6f/6s2p/greedy_capture-vs-random/optional` | INCONCLUSIVE | no | 0.9103 | — | — |
| `ex6f/6s2p/spread-vs-random/mandatory` | INCONCLUSIVE | no | 0.9065 | 206,225 / 0 | 0 / 0 |
| `ex6f/6s2p/spread-vs-random/mandatory_extended` | INCONCLUSIVE | no | 0.9104 | 240,762 / 0 | 11,117 / 0 |
| `ex6f/6s2p/spread-vs-random/optional` | INCONCLUSIVE | no | 0.8971 | — | — |
| `ex6f/6s3p/focus_front-vs-random/mandatory` | INCONCLUSIVE | no | 0.8805 | 528,950 / 0 | 0 / 0 |
| `ex6f/6s3p/focus_front-vs-random/mandatory_extended` | INCONCLUSIVE | no | 0.8933 | 601,229 / 0 | 19,746 / 0 |
| `ex6f/6s3p/focus_front-vs-random/optional` | INCONCLUSIVE | no | 0.8693 | — | — |
| `ex6f/6s3p/focus_rear-vs-random/mandatory` | INCONCLUSIVE | no | 0.8555 | 644,089 / 0 | 0 / 0 |
| `ex6f/6s3p/focus_rear-vs-random/mandatory_extended` | INCONCLUSIVE | no | 0.8806 | 764,661 / 0 | 26,603 / 0 |
| `ex6f/6s3p/focus_rear-vs-random/optional` | INCONCLUSIVE | no | 0.8468 | — | — |
| `ex6f/6s3p/greedy_capture-vs-random/mandatory` | INCONCLUSIVE | no | 0.8629 | 594,415 / 0 | 0 / 0 |
| `ex6f/6s3p/greedy_capture-vs-random/mandatory_extended` | INCONCLUSIVE | no | 0.8849 | 682,454 / 0 | 23,288 / 0 |
| `ex6f/6s3p/greedy_capture-vs-random/optional` | INCONCLUSIVE | no | 0.8601 | — | — |
| `ex6f/6s3p/spread-vs-random/mandatory` | INCONCLUSIVE | no | 0.8579 | 655,783 / 0 | 0 / 0 |
| `ex6f/6s3p/spread-vs-random/mandatory_extended` | INCONCLUSIVE | no | 0.8752 | 779,830 / 0 | 27,286 / 0 |
| `ex6f/6s3p/spread-vs-random/optional` | INCONCLUSIVE | no | 0.8487 | — | — |
| `ex6f/6s4p/focus_front-vs-random/mandatory` | INCONCLUSIVE | no | 0.8167 | 1,126,434 / 0 | 0 / 0 |
| `ex6f/6s4p/focus_front-vs-random/mandatory_extended` | INCONCLUSIVE | no | 0.8324 | 1,306,607 / 0 | 35,531 / 0 |
| `ex6f/6s4p/focus_front-vs-random/optional` | INCONCLUSIVE | no | 0.8088 | — | — |
| `ex6f/6s4p/focus_rear-vs-random/mandatory` | INCONCLUSIVE | no | 0.7917 | 1,358,858 / 0 | 0 / 0 |
| `ex6f/6s4p/focus_rear-vs-random/mandatory_extended` | INCONCLUSIVE | no | 0.8184 | 1,611,685 / 0 | 44,155 / 0 |
| `ex6f/6s4p/focus_rear-vs-random/optional` | INCONCLUSIVE | no | 0.7898 | — | — |
| `ex6f/6s4p/greedy_capture-vs-random/mandatory` | INCONCLUSIVE | no | 0.7952 | 1,262,263 / 0 | 0 / 0 |
| `ex6f/6s4p/greedy_capture-vs-random/mandatory_extended` | INCONCLUSIVE | no | 0.8308 | 1,471,626 / 0 | 39,364 / 0 |
| `ex6f/6s4p/greedy_capture-vs-random/optional` | INCONCLUSIVE | no | 0.7980 | — | — |
| `ex6f/6s4p/spread-vs-random/mandatory` | INCONCLUSIVE | no | 0.7966 | 1,379,344 / 0 | 0 / 0 |
| `ex6f/6s4p/spread-vs-random/mandatory_extended` | INCONCLUSIVE | no | 0.8192 | 1,638,022 / 0 | 45,076 / 0 |
| `ex6f/6s4p/spread-vs-random/optional` | INCONCLUSIVE | no | 0.7906 | — | — |
| `ex6f/6s6p/focus_front-vs-random/mandatory` | INCONCLUSIVE | no | 0.6778 | 3,205,145 / 0 | 0 / 0 |
| `ex6f/6s6p/focus_front-vs-random/mandatory_extended` | INCONCLUSIVE | no | 0.6812 | 3,795,535 / 0 | 73,985 / 0 |
| `ex6f/6s6p/focus_front-vs-random/optional` | INCONCLUSIVE | no | 0.6808 | — | — |
| `ex6f/6s6p/focus_rear-vs-random/mandatory` | INCONCLUSIVE | no | 0.6772 | 3,697,628 / 0 | 0 / 0 |
| `ex6f/6s6p/focus_rear-vs-random/mandatory_extended` | INCONCLUSIVE | no | 0.6842 | 4,415,362 / 0 | 82,947 / 0 |
| `ex6f/6s6p/focus_rear-vs-random/optional` | INCONCLUSIVE | no | 0.6742 | — | — |
| `ex6f/6s6p/greedy_capture-vs-random/mandatory` | INCONCLUSIVE | no | 0.6754 | 3,512,321 / 0 | 0 / 0 |
| `ex6f/6s6p/greedy_capture-vs-random/mandatory_extended` | INCONCLUSIVE | no | 0.6916 | 4,190,359 / 0 | 78,533 / 0 |
| `ex6f/6s6p/greedy_capture-vs-random/optional` | INCONCLUSIVE | no | 0.6799 | — | — |
| `ex6f/6s6p/spread-vs-random/mandatory` | INCONCLUSIVE | no | 0.6730 | 3,716,301 / 0 | 0 / 0 |
| `ex6f/6s6p/spread-vs-random/mandatory_extended` | INCONCLUSIVE | no | 0.6858 | 4,458,073 / 0 | 84,538 / 0 |
| `ex6f/6s6p/spread-vs-random/optional` | INCONCLUSIVE | no | 0.6764 | — | — |

## 4. Seat profiles where seats are not exchangeable

Where the field is homogeneous and the seats are exchangeable, §6.3's symmetry identity fixes every seat at 1/k for any rule set, so a per-seat rate there states arithmetic rather than a measurement. These are the cells where that does not hold — an uneven seating gap, or one seat playing a different policy — and the profile is the finding. AK-4 reports these as failures and deliberately does not gate on them (D-74): the asymmetry is what EX-5 set out to measure.

| Cell | n | per-seat win rates | spread |
|---|---:|---|---:|
| `ex2/4s2p/greedy_capture/mandatory` | 20,000 | 50.61% / 49.39% | 1.22 pp |
| `ex2/4s2p/greedy_capture/mandatory_extended` | 20,000 | 52.59% / 47.41% | 5.18 pp |
| `ex2/4s2p/greedy_capture/optional` | 20,000 | 49.80% / 50.20% | 0.39 pp |
| `ex2/4s2p/random/mandatory` | 20,000 | 50.32% / 49.68% | 0.64 pp |
| `ex2/4s2p/random/mandatory_extended` | 20,000 | 53.41% / 46.59% | 6.83 pp |
| `ex2/4s2p/random/optional` | 20,000 | 47.83% / 52.18% | 4.35 pp |
| `ex2/4s2p/spread/mandatory` | 20,000 | 39.61% / 60.39% | 20.78 pp |
| `ex2/4s2p/spread/mandatory_extended` | 20,000 | 40.80% / 59.20% | 18.40 pp |
| `ex2/4s2p/spread/optional` | 20,000 | 35.55% / 64.45% | 28.91 pp |
| `ex2/4s3p/greedy_capture/mandatory` | 20,001 | 33.07% / 34.24% / 32.69% | 1.55 pp |
| `ex2/4s3p/greedy_capture/mandatory_extended` | 20,001 | 35.54% / 33.16% / 31.30% | 4.24 pp |
| `ex2/4s3p/greedy_capture/optional` | 20,001 | 33.40% / 33.81% / 32.79% | 1.02 pp |
| `ex2/4s3p/random/mandatory` | 20,001 | 33.71% / 33.86% / 32.43% | 1.43 pp |
| `ex2/4s3p/random/mandatory_extended` | 20,001 | 35.39% / 33.71% / 30.90% | 4.48 pp |
| `ex2/4s3p/random/optional` | 20,001 | 33.97% / 34.14% / 31.88% | 2.26 pp |
| `ex2/4s3p/spread/mandatory` | 20,001 | 30.45% / 36.44% / 33.10% | 5.99 pp |
| `ex2/4s3p/spread/mandatory_extended` | 20,001 | 30.96% / 36.39% / 32.65% | 5.42 pp |
| `ex2/4s3p/spread/optional` | 20,001 | 29.78% / 37.37% / 32.85% | 7.58 pp |
| `ex3/deviant/4s2p/focus_front-vs-focus_rear` | 20,000 | 51.34% / 48.66% | 2.68 pp |
| `ex3/deviant/4s2p/focus_front-vs-random` | 20,000 | 51.14% / 48.86% | 2.28 pp |
| `ex3/deviant/4s2p/focus_front-vs-spread` | 20,000 | 50.89% / 49.11% | 1.78 pp |
| `ex3/deviant/4s2p/focus_rear-vs-focus_front` | 20,000 | 51.50% / 48.50% | 3.00 pp |
| `ex3/deviant/4s2p/focus_rear-vs-random` | 20,000 | 45.40% / 54.61% | 9.21 pp |
| `ex3/deviant/4s2p/focus_rear-vs-spread` | 20,000 | 37.59% / 62.41% | 24.83 pp |
| `ex3/deviant/4s2p/random-vs-focus_front` | 20,000 | 50.43% / 49.56% | 0.87 pp |
| `ex3/deviant/4s2p/random-vs-focus_rear` | 20,000 | 44.94% / 55.06% | 10.13 pp |
| `ex3/deviant/4s2p/random-vs-spread` | 20,000 | 43.96% / 56.04% | 12.07 pp |
| `ex3/deviant/4s2p/spread-vs-focus_front` | 20,000 | 51.48% / 48.52% | 2.96 pp |
| `ex3/deviant/4s2p/spread-vs-focus_rear` | 20,000 | 37.85% / 62.14% | 24.29 pp |
| `ex3/deviant/4s2p/spread-vs-random` | 20,000 | 44.03% / 55.97% | 11.94 pp |
| `ex3/deviant/4s3p/focus_front-vs-focus_rear` | 20,007 | 33.35% / 34.09% / 32.56% | 1.53 pp |
| `ex3/deviant/4s3p/focus_front-vs-random` | 20,007 | 34.21% / 33.55% / 32.24% | 1.97 pp |
| `ex3/deviant/4s3p/focus_front-vs-spread` | 20,007 | 33.58% / 34.08% / 32.33% | 1.75 pp |
| `ex3/deviant/4s3p/focus_rear-vs-focus_front` | 20,007 | 35.35% / 32.94% / 31.71% | 3.64 pp |
| `ex3/deviant/4s3p/focus_rear-vs-random` | 20,007 | 33.11% / 34.50% / 32.39% | 2.10 pp |
| `ex3/deviant/4s3p/focus_rear-vs-spread` | 20,007 | 30.10% / 36.27% / 33.63% | 6.17 pp |
| `ex3/deviant/4s3p/random-vs-focus_front` | 20,007 | 34.79% / 33.23% / 31.98% | 2.81 pp |
| `ex3/deviant/4s3p/random-vs-focus_rear` | 20,007 | 31.70% / 34.93% / 33.37% | 3.22 pp |
| `ex3/deviant/4s3p/random-vs-spread` | 20,007 | 31.51% / 35.43% / 33.06% | 3.91 pp |
| `ex3/deviant/4s3p/spread-vs-focus_front` | 20,007 | 35.78% / 33.17% / 31.05% | 4.73 pp |
| `ex3/deviant/4s3p/spread-vs-focus_rear` | 20,007 | 30.47% / 36.45% / 33.07% | 5.98 pp |
| `ex3/deviant/4s3p/spread-vs-random` | 20,007 | 32.59% / 34.95% / 32.46% | 2.48 pp |
| `ex3/deviant/4s4p/focus_front-vs-focus_rear` | 20,000 | 25.21% / 24.65% / 25.02% / 25.11% | 0.55 pp |
| `ex3/deviant/4s4p/focus_front-vs-random` | 200,000 | 25.09% / 24.98% / 24.91% / 25.01% | 0.18 pp |
| `ex3/deviant/4s4p/focus_front-vs-spread` | 20,000 | 25.11% / 24.98% / 25.02% / 24.89% | 0.21 pp |
| `ex3/deviant/4s4p/focus_rear-vs-focus_front` | 20,000 | 25.08% / 25.21% / 25.00% / 24.70% | 0.51 pp |
| `ex3/deviant/4s4p/focus_rear-vs-random` | 200,000 | 25.04% / 25.09% / 24.76% / 25.11% | 0.34 pp |
| `ex3/deviant/4s4p/focus_rear-vs-spread` | 20,000 | 24.70% / 24.79% / 25.49% / 25.03% | 0.79 pp |
| `ex3/deviant/4s4p/random-vs-focus_front` | 20,000 | 24.85% / 25.16% / 25.74% / 24.25% | 1.50 pp |
| `ex3/deviant/4s4p/random-vs-focus_rear` | 20,000 | 24.98% / 24.73% / 24.95% / 25.35% | 0.61 pp |
| `ex3/deviant/4s4p/random-vs-spread` | 20,000 | 24.51% / 24.98% / 25.07% / 25.44% | 0.93 pp |
| `ex3/deviant/4s4p/spread-vs-focus_front` | 20,000 | 24.89% / 24.87% / 25.16% / 25.07% | 0.29 pp |
| `ex3/deviant/4s4p/spread-vs-focus_rear` | 20,000 | 25.62% / 25.36% / 24.54% / 24.48% | 1.13 pp |
| `ex3/deviant/4s4p/spread-vs-random` | 200,000 | 25.00% / 25.17% / 24.70% / 25.13% | 0.47 pp |
| `ex3/deviant/6s6p/focus_front-vs-focus_rear` | 20,016 | 17.15% / 16.20% / 16.80% / 16.52% / 16.88% / 16.47% | 0.95 pp |
| `ex3/deviant/6s6p/focus_front-vs-random` | 20,016 | 16.64% / 16.55% / 16.22% / 17.06% / 16.99% / 16.55% | 0.84 pp |
| `ex3/deviant/6s6p/focus_front-vs-spread` | 20,016 | 16.75% / 16.56% / 16.41% / 16.66% / 16.66% / 16.97% | 0.56 pp |
| `ex3/deviant/6s6p/focus_rear-vs-focus_front` | 20,016 | 16.76% / 16.45% / 16.88% / 16.78% / 16.58% / 16.56% | 0.43 pp |
| `ex3/deviant/6s6p/focus_rear-vs-random` | 20,016 | 16.85% / 16.15% / 16.79% / 16.64% / 16.97% / 16.61% | 0.81 pp |
| `ex3/deviant/6s6p/focus_rear-vs-spread` | 20,016 | 16.67% / 16.47% / 16.94% / 17.03% / 16.20% / 16.70% | 0.83 pp |
| `ex3/deviant/6s6p/random-vs-focus_front` | 20,016 | 17.00% / 17.36% / 16.25% / 16.13% / 16.98% / 16.29% | 1.22 pp |
| `ex3/deviant/6s6p/random-vs-focus_rear` | 20,016 | 17.10% / 16.45% / 16.53% / 16.49% / 16.53% / 16.91% | 0.65 pp |
| `ex3/deviant/6s6p/random-vs-spread` | 20,016 | 16.34% / 16.48% / 17.33% / 16.50% / 16.77% / 16.59% | 0.99 pp |
| `ex3/deviant/6s6p/spread-vs-focus_front` | 20,016 | 16.38% / 16.50% / 16.75% / 16.60% / 17.10% / 16.67% | 0.72 pp |
| `ex3/deviant/6s6p/spread-vs-focus_rear` | 20,016 | 16.60% / 16.60% / 16.92% / 16.84% / 16.63% / 16.42% | 0.49 pp |
| `ex3/deviant/6s6p/spread-vs-random` | 20,016 | 16.77% / 16.77% / 16.69% / 16.88% / 16.58% / 16.31% | 0.57 pp |
| `ex3/homogeneous/4s2p/focus_front` | 20,000 | 51.76% / 48.24% | 3.52 pp |
| `ex3/homogeneous/4s2p/focus_rear` | 20,000 | 39.22% / 60.78% | 21.57 pp |
| `ex3/homogeneous/4s2p/random` | 20,000 | 48.45% / 51.55% | 3.10 pp |
| `ex3/homogeneous/4s2p/spread` | 20,000 | 35.77% / 64.23% | 28.46 pp |
| `ex3/homogeneous/4s3p/focus_front` | 20,001 | 35.52% / 32.26% / 32.21% | 3.31 pp |
| `ex3/homogeneous/4s3p/focus_rear` | 20,001 | 30.83% / 36.42% / 32.75% | 5.59 pp |
| `ex3/homogeneous/4s3p/random` | 20,001 | 33.09% / 34.17% / 32.74% | 1.43 pp |
| `ex3/homogeneous/4s3p/spread` | 20,001 | 29.47% / 37.59% / 32.94% | 8.12 pp |
| `ex5/2p/adjacent/random` | 20,000 | 48.27% / 51.73% | 3.46 pp |
| `ex5/2p/adjacent/spread` | 20,000 | 35.27% / 64.72% | 29.45 pp |
| `ex5/3p/4s-adjacent/random` | 250,002 | 33.30% / 33.88% / 32.82% | 1.06 pp |
| `ex5/3p/4s-adjacent/spread` | 250,002 | 29.88% / 37.19% / 32.93% | 7.31 pp |
| `ex5/3p/6s-adjacent/random` | 250,002 | 32.94% / 34.82% / 32.23% | 2.59 pp |
| `ex5/3p/6s-adjacent/spread` | 250,002 | 25.02% / 38.99% / 35.99% | 13.97 pp |
| `ex6b/4s4p/focus_front-vs-random/mandatory` | 400,000 | 25.12% / 25.03% / 24.92% / 24.94% | 0.20 pp |
| `ex6b/4s4p/focus_front-vs-random/mandatory_extended` | 400,000 | 25.10% / 25.07% / 24.95% / 24.87% | 0.23 pp |
| `ex6b/4s4p/focus_front-vs-random/optional` | 400,000 | 24.94% / 24.81% / 25.08% / 25.17% | 0.36 pp |
| `ex6b/4s4p/focus_rear-vs-random/mandatory` | 20,000 | 25.67% / 25.20% / 24.62% / 24.50% | 1.17 pp |
| `ex6b/4s4p/focus_rear-vs-random/mandatory_extended` | 20,000 | 25.26% / 25.11% / 24.53% / 25.11% | 0.73 pp |
| `ex6b/4s4p/focus_rear-vs-random/optional` | 20,000 | 24.39% / 25.39% / 24.96% / 25.26% | 1.00 pp |
| `ex6b/4s4p/greedy_capture-vs-random/mandatory` | 20,000 | 25.25% / 24.81% / 24.91% / 25.04% | 0.44 pp |
| `ex6b/4s4p/greedy_capture-vs-random/mandatory_extended` | 20,000 | 25.05% / 24.55% / 24.99% / 25.41% | 0.86 pp |
| `ex6b/4s4p/greedy_capture-vs-random/optional` | 20,000 | 24.71% / 25.24% / 24.77% / 25.27% | 0.56 pp |
| `ex6b/4s4p/spread-vs-random/mandatory` | 400,000 | 25.01% / 24.93% / 24.92% / 25.14% | 0.22 pp |
| `ex6b/4s4p/spread-vs-random/mandatory_extended` | 400,000 | 25.12% / 24.96% / 24.94% / 24.98% | 0.18 pp |
| `ex6b/4s4p/spread-vs-random/optional` | 400,000 | 24.97% / 25.00% / 25.02% / 25.01% | 0.05 pp |
| `ex6d/4s4p/focus_front-vs-random/barriers=False` | 400,000 | 24.99% / 24.96% / 25.10% / 24.95% | 0.15 pp |
| `ex6d/4s4p/focus_front-vs-random/barriers=True` | 400,000 | 25.01% / 24.98% / 25.06% / 24.95% | 0.12 pp |
| `ex6d/4s4p/focus_rear-vs-random/barriers=False` | 20,000 | 25.00% / 25.00% / 24.74% / 25.26% | 0.52 pp |
| `ex6d/4s4p/focus_rear-vs-random/barriers=True` | 20,000 | 24.77% / 25.01% / 24.90% / 25.32% | 0.56 pp |
| `ex6d/4s4p/greedy_capture-vs-random/barriers=False` | 20,000 | 25.05% / 25.41% / 24.80% / 24.73% | 0.68 pp |
| `ex6d/4s4p/greedy_capture-vs-random/barriers=True` | 20,000 | 25.64% / 24.93% / 24.52% / 24.91% | 1.12 pp |
| `ex6d/4s4p/spread-vs-random/barriers=False` | 400,000 | 25.07% / 24.92% / 24.97% / 25.04% | 0.15 pp |
| `ex6d/4s4p/spread-vs-random/barriers=True` | 400,000 | 24.98% / 24.99% / 24.98% / 25.05% | 0.07 pp |
| `ex6e/6s2p/random/mandatory` | 400,000 | 50.32% / 49.68% | 0.64 pp |
| `ex6e/6s2p/random/mandatory_extended` | 20,000 | 54.11% / 45.89% | 8.22 pp |
| `ex6e/6s2p/random/optional` | 400,000 | 47.01% / 52.99% | 5.98 pp |
| `ex6e/6s3p/random/mandatory` | 20,001 | 34.94% / 33.91% / 31.15% | 3.79 pp |
| `ex6e/6s3p/random/mandatory_extended` | 20,001 | 38.37% / 32.99% / 28.64% | 9.72 pp |
| `ex6e/6s3p/random/optional` | 20,001 | 32.74% / 34.60% / 32.65% | 1.95 pp |
| `ex6e/6s4p/random/mandatory` | 20,000 | 26.17% / 25.85% / 24.97% / 23.00% | 3.17 pp |
| `ex6e/6s4p/random/mandatory_extended` | 20,000 | 28.18% / 26.12% / 24.44% / 21.27% | 6.91 pp |
| `ex6e/6s4p/random/optional` | 20,000 | 25.41% / 27.15% / 25.46% / 21.98% | 5.18 pp |
| `ex6f/6s2p/focus_front-vs-random/mandatory` | 20,000 | 54.87% / 45.13% | 9.74 pp |
| `ex6f/6s2p/focus_front-vs-random/mandatory_extended` | 20,000 | 56.39% / 43.60% | 12.79 pp |
| `ex6f/6s2p/focus_front-vs-random/optional` | 20,000 | 52.25% / 47.74% | 4.51 pp |
| `ex6f/6s2p/focus_rear-vs-random/mandatory` | 20,000 | 46.32% / 53.68% | 7.36 pp |
| `ex6f/6s2p/focus_rear-vs-random/mandatory_extended` | 20,000 | 50.42% / 49.58% | 0.85 pp |
| `ex6f/6s2p/focus_rear-vs-random/optional` | 20,000 | 43.23% / 56.77% | 13.55 pp |
| `ex6f/6s2p/greedy_capture-vs-random/mandatory` | 20,000 | 50.29% / 49.71% | 0.57 pp |
| `ex6f/6s2p/greedy_capture-vs-random/mandatory_extended` | 20,000 | 54.14% / 45.86% | 8.29 pp |
| `ex6f/6s2p/greedy_capture-vs-random/optional` | 20,000 | 48.87% / 51.13% | 2.26 pp |
| `ex6f/6s2p/spread-vs-random/mandatory` | 20,000 | 45.27% / 54.73% | 9.46 pp |
| `ex6f/6s2p/spread-vs-random/mandatory_extended` | 20,000 | 49.28% / 50.72% | 1.45 pp |
| `ex6f/6s2p/spread-vs-random/optional` | 20,000 | 41.43% / 58.57% | 17.14 pp |
| `ex6f/6s3p/focus_front-vs-random/mandatory` | 20,007 | 37.29% / 33.07% / 29.64% | 7.65 pp |
| `ex6f/6s3p/focus_front-vs-random/mandatory_extended` | 20,007 | 40.37% / 31.98% / 27.65% | 12.73 pp |
| `ex6f/6s3p/focus_front-vs-random/optional` | 20,007 | 35.14% / 33.80% / 31.05% | 4.09 pp |
| `ex6f/6s3p/focus_rear-vs-random/mandatory` | 20,007 | 32.89% / 34.39% / 32.72% | 1.67 pp |
| `ex6f/6s3p/focus_rear-vs-random/mandatory_extended` | 20,007 | 37.31% / 33.96% / 28.73% | 8.58 pp |
| `ex6f/6s3p/focus_rear-vs-random/optional` | 20,007 | 31.64% / 35.89% / 32.46% | 4.25 pp |
| `ex6f/6s3p/greedy_capture-vs-random/mandatory` | 20,007 | 34.05% / 34.50% / 31.45% | 3.05 pp |
| `ex6f/6s3p/greedy_capture-vs-random/mandatory_extended` | 20,007 | 38.25% / 33.62% / 28.13% | 10.12 pp |
| `ex6f/6s3p/greedy_capture-vs-random/optional` | 20,007 | 33.60% / 34.34% / 32.05% | 2.29 pp |
| `ex6f/6s3p/spread-vs-random/mandatory` | 20,007 | 33.26% / 35.34% / 31.39% | 3.95 pp |
| `ex6f/6s3p/spread-vs-random/mandatory_extended` | 20,007 | 36.22% / 34.72% / 29.06% | 7.16 pp |
| `ex6f/6s3p/spread-vs-random/optional` | 20,007 | 31.90% / 35.70% / 32.40% | 3.79 pp |
| `ex6f/6s4p/focus_front-vs-random/mandatory` | 20,000 | 27.88% / 25.45% / 23.89% / 22.78% | 5.11 pp |
| `ex6f/6s4p/focus_front-vs-random/mandatory_extended` | 20,000 | 29.73% / 26.10% / 22.95% / 21.21% | 8.52 pp |
| `ex6f/6s4p/focus_front-vs-random/optional` | 20,000 | 27.02% / 25.85% / 25.04% / 22.10% | 4.93 pp |
| `ex6f/6s4p/focus_rear-vs-random/mandatory` | 20,000 | 25.30% / 26.28% / 25.77% / 22.64% | 3.64 pp |
| `ex6f/6s4p/focus_rear-vs-random/mandatory_extended` | 20,000 | 28.08% / 26.14% / 24.07% / 21.71% | 6.37 pp |
| `ex6f/6s4p/focus_rear-vs-random/optional` | 20,000 | 25.11% / 26.83% / 26.37% / 21.68% | 5.15 pp |
| `ex6f/6s4p/greedy_capture-vs-random/mandatory` | 20,000 | 25.64% / 26.52% / 25.17% / 22.66% | 3.86 pp |
| `ex6f/6s4p/greedy_capture-vs-random/mandatory_extended` | 20,000 | 29.54% / 26.61% / 23.21% / 20.64% | 8.89 pp |
| `ex6f/6s4p/greedy_capture-vs-random/optional` | 20,000 | 25.91% / 26.80% / 25.54% / 21.75% | 5.05 pp |
| `ex6f/6s4p/spread-vs-random/mandatory` | 20,000 | 25.77% / 26.16% / 25.36% / 22.71% | 3.46 pp |
| `ex6f/6s4p/spread-vs-random/mandatory_extended` | 20,000 | 28.17% / 26.15% / 24.73% / 20.95% | 7.21 pp |
| `ex6f/6s4p/spread-vs-random/optional` | 20,000 | 25.19% / 27.25% / 25.74% / 21.82% | 5.43 pp |
| `ex6f/6s6p/focus_front-vs-random/mandatory` | 20,016 | 16.63% / 16.88% / 16.63% / 16.31% / 16.94% / 16.62% | 0.63 pp |
| `ex6f/6s6p/focus_front-vs-random/mandatory_extended` | 20,016 | 16.83% / 16.39% / 16.66% / 16.75% / 16.92% / 16.45% | 0.53 pp |
| `ex6f/6s6p/focus_front-vs-random/optional` | 20,016 | 16.81% / 16.51% / 16.68% / 16.84% / 16.75% / 16.41% | 0.43 pp |
| `ex6f/6s6p/focus_rear-vs-random/mandatory` | 20,016 | 16.59% / 16.46% / 16.70% / 16.96% / 16.49% / 16.81% | 0.50 pp |
| `ex6f/6s6p/focus_rear-vs-random/mandatory_extended` | 20,016 | 17.02% / 16.57% / 16.61% / 16.58% / 16.76% / 16.46% | 0.56 pp |
| `ex6f/6s6p/focus_rear-vs-random/optional` | 20,016 | 16.41% / 16.31% / 16.68% / 16.62% / 17.02% / 16.96% | 0.71 pp |
| `ex6f/6s6p/greedy_capture-vs-random/mandatory` | 20,016 | 16.48% / 17.07% / 16.72% / 16.73% / 16.68% / 16.33% | 0.74 pp |
| `ex6f/6s6p/greedy_capture-vs-random/mandatory_extended` | 20,016 | 17.49% / 16.41% / 16.50% / 16.71% / 16.38% / 16.52% | 1.11 pp |
| `ex6f/6s6p/greedy_capture-vs-random/optional` | 20,016 | 16.75% / 16.44% / 16.30% / 16.63% / 16.88% / 17.00% | 0.69 pp |
| `ex6f/6s6p/spread-vs-random/mandatory` | 20,016 | 16.33% / 17.18% / 16.68% / 16.39% / 16.76% / 16.67% | 0.84 pp |
| `ex6f/6s6p/spread-vs-random/mandatory_extended` | 20,016 | 17.12% / 16.82% / 16.38% / 15.77% / 17.23% / 16.69% | 1.46 pp |
| `ex6f/6s6p/spread-vs-random/optional` | 20,016 | 16.54% / 16.76% / 16.40% / 16.64% / 16.70% / 16.98% | 0.58 pp |

## 5. Starting-player advantage

D-25's estimand, on the two calibration cells.

| Cell | offset | win rate | 95% CI |
|---|---:|---:|---|
| `ex1/4s4p/random/baseline` | starter | 25.517% | [25.382, 25.653] |
| `ex1/4s4p/random/baseline` | +1 | 25.089% | [24.955, 25.224] |
| `ex1/4s4p/random/baseline` | +2 | 24.811% | [24.678, 24.946] |
| `ex1/4s4p/random/baseline` | +3 | 24.582% | [24.449, 24.716] |
| `ex1b/6s6p/random/baseline` | starter | 16.916% | [16.800, 17.033] |
| `ex1b/6s6p/random/baseline` | +1 | 16.678% | [16.563, 16.794] |
| `ex1b/6s6p/random/baseline` | +2 | 16.659% | [16.544, 16.774] |
| `ex1b/6s6p/random/baseline` | +3 | 16.624% | [16.509, 16.740] |
| `ex1b/6s6p/random/baseline` | +4 | 16.545% | [16.430, 16.660] |
| `ex1b/6s6p/random/baseline` | +5 | 16.578% | [16.463, 16.694] |

## 6. Full metric battery (descriptive)

Every §6.2 metric for every cell, per §14.4. Per-seat fields are summed to a game total, which is the k-comparable form; the per-seat profiles are what the gates in section 3 read. `conf` marks a cell carrying a confirmatory contrast; `desc` marks everything else. **Nominal 95% intervals apply to this section and it is not error-controlled** — no claim in it has survived a multiplicity correction.

| Cell | label | n | turns | rounds | rolls | rounds→win | captures | captured | passes | entry waits | lead chg | no leader | barriers | barrier turns | extra laps | rank@50 | rank@75 | cb depth | margin | margin norm |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ak5/4s4p/greedy/extended` | desc | 20,000 | 661.3 | 183.5 | 793.4 | 131.7 | 74.8 | 74.8 | 129.3 | 132.0 | 22.3 | 0.0000 | 0.0000 | 0.0000 | 2.1347 | 1.7898 | 1.5407 | 0.2633 | 46.6 | 0.2739 |
| `ak5/4s4p/random/mandatory` | desc | 20,000 | 570.9 | 158.8 | 685.1 | 113.4 | 63.1 | 63.1 | 111.5 | 110.7 | 19.9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7643 | 1.5003 | 0.2547 | 46.5 | 0.2735 |
| `ex1/4s4p/random/baseline` | conf | 400,000 | 438.0 | 122.2 | 525.6 | 87.1 | 41.7 | 41.7 | 66.0 | 59.0 | 17.3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7558 | 1.4767 | 0.2519 | 41.1 | 0.2418 |
| `ex1b/6s6p/random/baseline` | conf | 400,002 | 1,241 | 241.3 | 1,489 | 146.9 | 145.2 | 145.2 | 211.2 | 217.4 | 29.1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.0658 | 1.6146 | 0.2132 | 54.9 | 0.2716 |
| `ex2/4s2p/greedy_capture/mandatory` | desc | 20,000 | 137.4 | 68.9 | 164.8 | 68.9 | 9.4718 | 9.4718 | 14.7 | 11.3 | 7.0537 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3098 | 1.2169 | 0.3099 | 54.6 | 0.3214 |
| `ex2/4s2p/greedy_capture/mandatory_extended` | desc | 20,000 | 150.3 | 75.4 | 180.5 | 75.4 | 10.9 | 10.9 | 15.8 | 12.6 | 7.4315 | 0.0000 | 0.0000 | 0.0000 | 0.5022 | 1.3267 | 1.2274 | 0.3266 | 55.0 | 0.3238 |
| `ex2/4s2p/greedy_capture/optional` | desc | 20,000 | 137.9 | 69.2 | 165.5 | 69.2 | 9.5579 | 9.5579 | 14.6 | 11.2 | 7.0784 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3140 | 1.2184 | 0.3140 | 53.6 | 0.3151 |
| `ex2/4s2p/random/mandatory` | desc | 20,000 | 137.5 | 69.0 | 165.0 | 69.0 | 9.5192 | 9.5192 | 14.5 | 11.2 | 7.0553 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3154 | 1.2210 | 0.3154 | 54.0 | 0.3177 |
| `ex2/4s2p/random/mandatory_extended` | desc | 20,000 | 150.1 | 75.3 | 180.0 | 75.3 | 10.8 | 10.8 | 16.0 | 12.9 | 7.3673 | 0.0000 | 0.0000 | 0.0000 | 0.5184 | 1.3265 | 1.2249 | 0.3265 | 55.8 | 0.3284 |
| `ex2/4s2p/random/optional` | desc | 20,000 | 117.5 | 59.0 | 140.9 | 59.0 | 5.6723 | 5.6723 | 9.1238 | 5.6342 | 7.0173 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3115 | 1.2135 | 0.3115 | 42.3 | 0.2486 |
| `ex2/4s2p/spread/mandatory` | desc | 20,000 | 146.0 | 73.3 | 175.1 | 73.3 | 9.7371 | 9.7371 | 13.9 | 10.1 | 7.4081 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3133 | 1.1927 | 0.3132 | 53.2 | 0.3130 |
| `ex2/4s2p/spread/mandatory_extended` | desc | 20,000 | 163.3 | 81.9 | 196.0 | 81.9 | 11.6 | 11.6 | 15.4 | 11.8 | 7.9775 | 0.0000 | 0.0000 | 0.0000 | 0.5455 | 1.3253 | 1.2030 | 0.3252 | 54.6 | 0.3214 |
| `ex2/4s2p/spread/optional` | desc | 20,000 | 120.4 | 60.5 | 144.5 | 60.5 | 5.2943 | 5.2943 | 8.7687 | 5.0751 | 6.8484 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3001 | 1.1946 | 0.3001 | 38.9 | 0.2286 |
| `ex2/4s3p/greedy_capture/mandatory` | desc | 20,001 | 317.0 | 113.0 | 380.4 | 91.6 | 30.2 | 30.2 | 49.1 | 44.9 | 13.8 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5796 | 1.3878 | 0.2898 | 46.6 | 0.2739 |
| `ex2/4s3p/greedy_capture/mandatory_extended` | desc | 20,001 | 359.7 | 128.1 | 431.6 | 104.0 | 35.2 | 35.2 | 55.9 | 52.8 | 15.1 | 0.0000 | 0.0000 | 0.0000 | 1.2475 | 1.5856 | 1.4124 | 0.2928 | 47.5 | 0.2792 |
| `ex2/4s3p/greedy_capture/optional` | desc | 20,001 | 316.5 | 112.9 | 379.8 | 91.3 | 30.1 | 30.1 | 49.0 | 44.7 | 13.8 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5664 | 1.3911 | 0.2832 | 46.7 | 0.2744 |
| `ex2/4s3p/random/mandatory` | desc | 20,001 | 318.3 | 113.4 | 382.0 | 91.9 | 30.4 | 30.4 | 49.4 | 45.1 | 13.9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5782 | 1.3832 | 0.2891 | 46.5 | 0.2735 |
| `ex2/4s3p/random/mandatory_extended` | desc | 20,001 | 358.3 | 127.7 | 430.0 | 103.5 | 35.1 | 35.1 | 55.7 | 52.6 | 15.0 | 0.0000 | 0.0000 | 0.0000 | 1.2371 | 1.5860 | 1.4122 | 0.2930 | 47.3 | 0.2783 |
| `ex2/4s3p/random/optional` | desc | 20,001 | 250.5 | 89.2 | 300.6 | 72.6 | 19.2 | 19.2 | 28.9 | 22.5 | 12.5 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5593 | 1.3657 | 0.2796 | 40.2 | 0.2363 |
| `ex2/4s3p/spread/mandatory` | desc | 20,001 | 402.3 | 144.0 | 482.7 | 114.8 | 40.8 | 40.8 | 58.8 | 53.1 | 16.9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.6401 | 1.3989 | 0.3200 | 55.4 | 0.3259 |
| `ex2/4s3p/spread/mandatory_extended` | desc | 20,001 | 476.5 | 170.4 | 571.8 | 136.1 | 50.0 | 50.0 | 69.2 | 65.1 | 19.1 | 0.0000 | 0.0000 | 0.0000 | 1.7085 | 1.6424 | 1.4260 | 0.3212 | 57.4 | 0.3374 |
| `ex2/4s3p/spread/optional` | desc | 20,001 | 316.3 | 113.3 | 379.5 | 90.2 | 26.3 | 26.3 | 33.1 | 25.3 | 14.8 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.6666 | 1.3739 | 0.3333 | 50.0 | 0.2943 |
| `ex2/4s4p/greedy_capture/mandatory` | desc | 20,000 | 570.9 | 158.7 | 685.1 | 113.5 | 63.1 | 63.1 | 111.4 | 110.7 | 19.9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7749 | 1.5103 | 0.2583 | 46.3 | 0.2724 |
| `ex2/4s4p/greedy_capture/mandatory_extended` | desc | 20,000 | 660.0 | 183.1 | 792.0 | 131.5 | 74.5 | 74.5 | 129.0 | 131.4 | 22.4 | 0.0000 | 0.0000 | 0.0000 | 2.1385 | 1.8022 | 1.5311 | 0.2674 | 46.2 | 0.2717 |
| `ex2/4s4p/greedy_capture/optional` | desc | 20,000 | 570.2 | 158.5 | 684.5 | 113.4 | 63.2 | 63.2 | 111.1 | 110.3 | 20.0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7746 | 1.5075 | 0.2582 | 46.0 | 0.2708 |
| `ex2/4s4p/random/mandatory` | conf | 250,000 | 570.9 | 158.7 | 685.1 | 113.6 | 63.1 | 63.1 | 111.5 | 110.7 | 19.9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7700 | 1.5081 | 0.2567 | 46.1 | 0.2715 |
| `ex2/4s4p/random/mandatory_extended` | conf | 250,000 | 661.2 | 183.4 | 793.5 | 131.9 | 74.8 | 74.8 | 129.1 | 131.7 | 22.4 | 0.0000 | 0.0000 | 0.0000 | 2.1464 | 1.7935 | 1.5406 | 0.2645 | 46.0 | 0.2707 |
| `ex2/4s4p/random/optional` | conf | 250,000 | 438.1 | 122.2 | 525.7 | 87.1 | 41.7 | 41.7 | 66.0 | 59.0 | 17.3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7574 | 1.4771 | 0.2525 | 41.2 | 0.2421 |
| `ex2/4s4p/spread/mandatory` | desc | 20,000 | 769.2 | 214.6 | 923.0 | 150.6 | 90.7 | 90.7 | 143.7 | 142.2 | 26.1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.8256 | 1.5119 | 0.2752 | 55.7 | 0.3275 |
| `ex2/4s4p/spread/mandatory_extended` | desc | 20,000 | 940.8 | 261.6 | 1,129 | 184.9 | 113.7 | 113.7 | 175.2 | 178.7 | 30.5 | 0.0000 | 0.0000 | 0.0000 | 3.0837 | 1.8459 | 1.5573 | 0.2820 | 55.8 | 0.3280 |
| `ex2/4s4p/spread/optional` | desc | 20,000 | 622.7 | 174.2 | 747.2 | 121.6 | 65.7 | 65.7 | 85.8 | 76.9 | 23.2 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.8693 | 1.4995 | 0.2898 | 53.0 | 0.3117 |
| `ex2/6s6p/greedy_capture/mandatory` | desc | 20,004 | 1,738 | 335.3 | 2,085 | 205.3 | 224.4 | 224.4 | 383.7 | 419.8 | 36.1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.0867 | 1.6577 | 0.2173 | 60.0 | 0.2972 |
| `ex2/6s6p/greedy_capture/mandatory_extended` | desc | 20,004 | 2,036 | 390.8 | 2,442 | 241.9 | 264.9 | 264.9 | 450.4 | 499.6 | 41.0 | 0.0000 | 0.0000 | 0.0000 | 3.9876 | 2.1299 | 1.7007 | 0.2260 | 58.7 | 0.2908 |
| `ex2/6s6p/greedy_capture/optional` | desc | 20,004 | 1,734 | 334.5 | 2,080 | 204.8 | 223.9 | 223.9 | 382.2 | 418.1 | 36.0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.0820 | 1.6361 | 0.2164 | 59.9 | 0.2965 |
| `ex2/6s6p/random/mandatory` | desc | 20,004 | 1,735 | 335.0 | 2,082 | 204.8 | 224.2 | 224.2 | 382.9 | 418.9 | 35.9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.0827 | 1.6421 | 0.2165 | 60.2 | 0.2982 |
| `ex2/6s6p/random/mandatory_extended` | desc | 20,004 | 2,041 | 391.7 | 2,449 | 243.2 | 265.7 | 265.7 | 452.4 | 502.0 | 41.4 | 0.0000 | 0.0000 | 0.0000 | 3.9855 | 2.1510 | 1.7052 | 0.2302 | 58.3 | 0.2884 |
| `ex2/6s6p/random/optional` | desc | 20,004 | 1,240 | 241.2 | 1,488 | 146.9 | 145.1 | 145.1 | 211.2 | 217.4 | 29.1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.0550 | 1.6195 | 0.2110 | 54.8 | 0.2714 |
| `ex2/6s6p/spread/mandatory` | desc | 20,004 | 2,590 | 501.7 | 3,108 | 297.9 | 349.0 | 349.0 | 547.4 | 601.0 | 51.9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.1590 | 1.6758 | 0.2318 | 70.8 | 0.3504 |
| `ex2/6s6p/spread/mandatory_extended` | desc | 20,004 | 3,158 | 607.9 | 3,789 | 366.3 | 428.6 | 428.6 | 670.3 | 747.0 | 61.3 | 0.0000 | 0.0000 | 0.0000 | 5.4320 | 2.1784 | 1.7088 | 0.2357 | 69.8 | 0.3455 |
| `ex2/6s6p/spread/optional` | desc | 20,004 | 2,025 | 393.5 | 2,430 | 232.4 | 255.1 | 255.1 | 317.5 | 330.7 | 44.5 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.1642 | 1.6478 | 0.2328 | 69.0 | 0.3417 |
| `ex3/deviant/4s2p/focus_front-vs-focus_rear` | desc | 20,000 | 116.5 | 58.5 | 139.9 | 58.5 | 6.0827 | 6.0827 | 9.9262 | 6.1791 | 6.4753 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.2803 | 1.1684 | 0.2803 | 54.4 | 0.3198 |
| `ex3/deviant/4s2p/focus_front-vs-random` | desc | 20,000 | 111.2 | 55.9 | 133.4 | 55.9 | 5.1912 | 5.1912 | 9.2225 | 5.6601 | 6.4932 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.2894 | 1.1946 | 0.2894 | 45.5 | 0.2679 |
| `ex3/deviant/4s2p/focus_front-vs-spread` | desc | 20,000 | 118.0 | 59.3 | 141.6 | 59.3 | 6.2714 | 6.2714 | 10.0 | 6.2612 | 6.5002 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.2897 | 1.1569 | 0.2897 | 56.5 | 0.3323 |
| `ex3/deviant/4s2p/focus_rear-vs-focus_front` | desc | 20,000 | 116.6 | 58.6 | 140.0 | 58.6 | 6.0780 | 6.0780 | 9.9295 | 6.1685 | 6.5306 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.2887 | 1.1670 | 0.2887 | 53.8 | 0.3165 |
| `ex3/deviant/4s2p/focus_rear-vs-random` | desc | 20,000 | 121.7 | 61.1 | 146.1 | 61.1 | 6.0889 | 6.0889 | 9.4119 | 5.7446 | 7.1115 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3182 | 1.2003 | 0.3182 | 44.3 | 0.2607 |
| `ex3/deviant/4s2p/focus_rear-vs-spread` | desc | 20,000 | 121.7 | 61.1 | 146.1 | 61.1 | 5.5810 | 5.5810 | 8.9258 | 5.2116 | 6.9240 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.2970 | 1.1924 | 0.2970 | 40.6 | 0.2389 |
| `ex3/deviant/4s2p/random-vs-focus_front` | desc | 20,000 | 111.1 | 55.8 | 133.3 | 55.8 | 5.2203 | 5.2203 | 9.1661 | 5.6395 | 6.4052 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.2865 | 1.1925 | 0.2865 | 45.9 | 0.2698 |
| `ex3/deviant/4s2p/random-vs-focus_rear` | desc | 20,000 | 121.9 | 61.2 | 146.3 | 61.2 | 6.0794 | 6.0794 | 9.3898 | 5.6841 | 7.0848 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3194 | 1.2080 | 0.3194 | 44.2 | 0.2602 |
| `ex3/deviant/4s2p/random-vs-spread` | desc | 20,000 | 121.1 | 60.8 | 145.3 | 60.8 | 5.9314 | 5.9314 | 9.2306 | 5.6395 | 7.0823 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3185 | 1.2035 | 0.3185 | 45.2 | 0.2657 |
| `ex3/deviant/4s2p/spread-vs-focus_front` | desc | 20,000 | 117.9 | 59.2 | 141.4 | 59.2 | 6.2570 | 6.2570 | 10.2 | 6.4163 | 6.5436 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.2897 | 1.1585 | 0.2898 | 57.2 | 0.3365 |
| `ex3/deviant/4s2p/spread-vs-focus_rear` | desc | 20,000 | 121.4 | 61.0 | 145.8 | 61.0 | 5.5404 | 5.5404 | 8.9922 | 5.2458 | 6.9185 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3003 | 1.1868 | 0.3003 | 40.5 | 0.2385 |
| `ex3/deviant/4s2p/spread-vs-random` | desc | 20,000 | 121.7 | 61.1 | 146.0 | 61.1 | 5.9876 | 5.9876 | 9.2268 | 5.5966 | 7.1086 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3220 | 1.2038 | 0.3220 | 44.8 | 0.2634 |
| `ex3/deviant/4s3p/focus_front-vs-focus_rear` | desc | 20,007 | 263.1 | 95.8 | 315.7 | 72.1 | 20.6 | 20.6 | 30.3 | 22.9 | 11.3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5052 | 1.2673 | 0.2526 | 54.0 | 0.3176 |
| `ex3/deviant/4s3p/focus_front-vs-random` | desc | 20,007 | 231.0 | 82.9 | 277.3 | 65.8 | 16.8 | 16.8 | 27.5 | 20.7 | 11.0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5086 | 1.3197 | 0.2543 | 41.6 | 0.2447 |
| `ex3/deviant/4s3p/focus_front-vs-spread` | desc | 20,007 | 270.0 | 98.7 | 324.0 | 73.1 | 21.3 | 21.3 | 30.9 | 23.5 | 11.4 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5180 | 1.2454 | 0.2590 | 57.5 | 0.3381 |
| `ex3/deviant/4s3p/focus_rear-vs-focus_front` | desc | 20,007 | 223.4 | 80.6 | 268.1 | 62.7 | 16.1 | 16.1 | 27.7 | 20.5 | 10.4 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.4862 | 1.3000 | 0.2431 | 41.8 | 0.2457 |
| `ex3/deviant/4s3p/focus_rear-vs-random` | desc | 20,007 | 266.2 | 95.1 | 319.4 | 76.4 | 21.1 | 21.1 | 30.1 | 23.4 | 12.8 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5698 | 1.3511 | 0.2849 | 43.6 | 0.2568 |
| `ex3/deviant/4s3p/focus_rear-vs-spread` | desc | 20,007 | 313.3 | 112.2 | 376.0 | 89.5 | 26.1 | 26.1 | 33.2 | 25.6 | 14.7 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.6445 | 1.3675 | 0.3223 | 49.7 | 0.2921 |
| `ex3/deviant/4s3p/random-vs-focus_front` | desc | 20,007 | 211.7 | 75.8 | 254.1 | 60.6 | 14.3 | 14.3 | 26.4 | 19.5 | 10.4 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5032 | 1.3353 | 0.2516 | 37.1 | 0.2183 |
| `ex3/deviant/4s3p/random-vs-focus_rear` | desc | 20,007 | 285.4 | 102.3 | 342.5 | 81.4 | 23.2 | 23.2 | 31.3 | 24.2 | 13.4 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5980 | 1.3543 | 0.2990 | 47.1 | 0.2771 |
| `ex3/deviant/4s3p/random-vs-spread` | desc | 20,007 | 291.4 | 104.8 | 349.7 | 82.3 | 23.8 | 23.8 | 31.6 | 24.4 | 13.5 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.6122 | 1.3385 | 0.3061 | 50.1 | 0.2946 |
| `ex3/deviant/4s3p/spread-vs-focus_front` | desc | 20,007 | 224.9 | 81.2 | 269.9 | 62.9 | 16.4 | 16.4 | 27.7 | 20.5 | 10.4 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.4787 | 1.2867 | 0.2394 | 42.5 | 0.2497 |
| `ex3/deviant/4s3p/spread-vs-focus_rear` | desc | 20,007 | 310.9 | 111.2 | 373.2 | 88.9 | 26.0 | 26.0 | 33.0 | 25.4 | 14.6 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.6499 | 1.3721 | 0.3249 | 49.2 | 0.2893 |
| `ex3/deviant/4s3p/spread-vs-random` | desc | 20,007 | 267.9 | 95.9 | 321.5 | 76.6 | 21.2 | 21.2 | 30.1 | 23.4 | 12.8 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5831 | 1.3394 | 0.2916 | 44.9 | 0.2642 |
| `ex3/deviant/4s4p/focus_front-vs-focus_rear` | desc | 20,000 | 492.3 | 141.4 | 590.8 | 89.0 | 48.3 | 48.3 | 71.2 | 61.6 | 16.1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.6562 | 1.3391 | 0.2187 | 56.2 | 0.3308 |
| `ex3/deviant/4s4p/focus_front-vs-random` | conf | 200,000 | 402.3 | 113.4 | 482.8 | 77.8 | 36.7 | 36.7 | 61.7 | 53.7 | 15.1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.6982 | 1.4268 | 0.2327 | 42.5 | 0.2499 |
| `ex3/deviant/4s4p/focus_front-vs-spread` | desc | 20,000 | 510.3 | 147.4 | 612.3 | 90.3 | 50.5 | 50.5 | 72.4 | 63.1 | 16.1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.6601 | 1.3148 | 0.2200 | 59.4 | 0.3497 |
| `ex3/deviant/4s4p/focus_rear-vs-focus_front` | desc | 20,000 | 357.1 | 102.1 | 428.5 | 67.9 | 30.5 | 30.5 | 56.6 | 46.9 | 13.4 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.6690 | 1.4170 | 0.2230 | 37.8 | 0.2222 |
| `ex3/deviant/4s4p/focus_rear-vs-random` | conf | 200,000 | 466.8 | 130.8 | 560.1 | 91.8 | 45.5 | 45.5 | 69.0 | 61.6 | 18.0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7618 | 1.4632 | 0.2539 | 43.9 | 0.2581 |
| `ex3/deviant/4s4p/focus_rear-vs-spread` | desc | 20,000 | 613.3 | 171.4 | 736.0 | 120.2 | 64.6 | 64.6 | 85.0 | 76.0 | 22.9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.8594 | 1.5027 | 0.2865 | 52.3 | 0.3078 |
| `ex3/deviant/4s4p/random-vs-focus_front` | desc | 20,000 | 340.4 | 96.2 | 408.3 | 66.2 | 28.0 | 28.0 | 54.5 | 45.0 | 13.5 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.6989 | 1.4480 | 0.2330 | 35.3 | 0.2078 |
| `ex3/deviant/4s4p/random-vs-focus_rear` | desc | 20,000 | 541.2 | 151.9 | 649.5 | 105.2 | 55.3 | 55.3 | 76.9 | 68.3 | 20.2 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7851 | 1.4668 | 0.2617 | 49.7 | 0.2922 |
| `ex3/deviant/4s4p/random-vs-spread` | desc | 20,000 | 562.1 | 158.5 | 674.4 | 107.8 | 57.8 | 57.8 | 78.7 | 70.4 | 20.5 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.8016 | 1.4373 | 0.2672 | 51.9 | 0.3053 |
| `ex3/deviant/4s4p/spread-vs-focus_front` | desc | 20,000 | 358.7 | 102.8 | 430.5 | 67.9 | 30.9 | 30.9 | 56.6 | 47.0 | 13.3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.6764 | 1.4163 | 0.2255 | 38.3 | 0.2253 |
| `ex3/deviant/4s4p/spread-vs-focus_rear` | desc | 20,000 | 598.2 | 166.9 | 717.8 | 117.7 | 62.7 | 62.7 | 83.6 | 74.2 | 22.5 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.8515 | 1.5122 | 0.2838 | 51.1 | 0.3004 |
| `ex3/deviant/4s4p/spread-vs-random` | conf | 200,000 | 471.0 | 132.3 | 565.2 | 92.2 | 46.1 | 46.1 | 69.3 | 62.0 | 18.0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7615 | 1.4544 | 0.2539 | 44.5 | 0.2618 |
| `ex3/deviant/6s6p/focus_front-vs-focus_rear` | desc | 20,016 | 1,576 | 318.6 | 1,891 | 151.8 | 190.0 | 190.0 | 248.4 | 251.5 | 27.3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.8536 | 1.3742 | 0.1707 | 78.1 | 0.3867 |
| `ex3/deviant/6s6p/focus_front-vs-random` | desc | 20,016 | 1,127 | 223.1 | 1,353 | 126.6 | 128.4 | 128.4 | 192.3 | 194.3 | 24.6 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.9666 | 1.5290 | 0.1933 | 56.5 | 0.2797 |
| `ex3/deviant/6s6p/focus_front-vs-spread` | desc | 20,016 | 1,652 | 336.8 | 1,983 | 153.9 | 200.0 | 200.0 | 254.6 | 259.2 | 27.4 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.8156 | 1.3396 | 0.1631 | 81.0 | 0.4012 |
| `ex3/deviant/6s6p/focus_rear-vs-focus_front` | desc | 20,016 | 827.6 | 167.5 | 993.0 | 93.5 | 84.9 | 84.9 | 148.6 | 139.8 | 19.3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.9839 | 1.5979 | 0.1968 | 43.4 | 0.2150 |
| `ex3/deviant/6s6p/focus_rear-vs-random` | desc | 20,016 | 1,317 | 257.7 | 1,581 | 153.9 | 156.2 | 156.2 | 220.4 | 227.0 | 30.1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.0581 | 1.6024 | 0.2116 | 56.7 | 0.2806 |
| `ex3/deviant/6s6p/focus_rear-vs-spread` | desc | 20,016 | 2,013 | 390.5 | 2,415 | 232.2 | 253.4 | 253.4 | 316.6 | 329.4 | 44.5 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.1706 | 1.6542 | 0.2341 | 68.8 | 0.3404 |
| `ex3/deviant/6s6p/random-vs-focus_front` | desc | 20,016 | 802.4 | 159.9 | 962.8 | 92.6 | 81.2 | 81.2 | 145.3 | 136.3 | 19.4 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.0179 | 1.6255 | 0.2036 | 42.1 | 0.2086 |
| `ex3/deviant/6s6p/random-vs-focus_rear` | desc | 20,016 | 1,751 | 342.3 | 2,100 | 198.6 | 216.4 | 216.4 | 280.7 | 289.8 | 37.9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.1135 | 1.6050 | 0.2227 | 66.2 | 0.3278 |
| `ex3/deviant/6s6p/random-vs-spread` | desc | 20,016 | 1,833 | 360.4 | 2,200 | 204.4 | 227.5 | 227.5 | 288.5 | 299.4 | 39.0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.1040 | 1.5908 | 0.2208 | 68.9 | 0.3410 |
| `ex3/deviant/6s6p/spread-vs-focus_front` | desc | 20,016 | 830.0 | 168.4 | 996.2 | 93.7 | 85.4 | 85.4 | 148.5 | 139.7 | 19.3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.9973 | 1.6098 | 0.1995 | 43.1 | 0.2132 |
| `ex3/deviant/6s6p/spread-vs-focus_rear` | desc | 20,016 | 1,933 | 373.9 | 2,320 | 224.9 | 242.5 | 242.5 | 308.2 | 319.4 | 43.1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.1695 | 1.6691 | 0.2339 | 67.6 | 0.3345 |
| `ex3/deviant/6s6p/spread-vs-random` | desc | 20,016 | 1,320 | 258.6 | 1,584 | 153.7 | 156.2 | 156.2 | 220.3 | 227.2 | 30.1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.0538 | 1.5887 | 0.2108 | 57.1 | 0.2828 |
| `ex3/homogeneous/4s2p/focus_front` | desc | 20,000 | 103.0 | 51.8 | 123.6 | 51.8 | 3.9358 | 3.9358 | 8.5817 | 5.0340 | 6.4444 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.2978 | 1.2181 | 0.2978 | 37.6 | 0.2213 |
| `ex3/homogeneous/4s2p/focus_rear` | desc | 20,000 | 123.5 | 62.0 | 148.2 | 62.0 | 5.9146 | 5.9146 | 9.2775 | 5.4233 | 7.0610 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3041 | 1.1888 | 0.3041 | 42.0 | 0.2470 |
| `ex3/homogeneous/4s2p/random` | desc | 20,000 | 117.8 | 59.2 | 141.4 | 59.2 | 5.7226 | 5.7226 | 9.2043 | 5.6574 | 6.9973 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3106 | 1.2131 | 0.3105 | 42.3 | 0.2487 |
| `ex3/homogeneous/4s2p/spread` | desc | 20,000 | 119.9 | 60.2 | 144.0 | 60.2 | 5.2178 | 5.2178 | 8.7783 | 5.1258 | 6.8247 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.2981 | 1.1905 | 0.2981 | 38.8 | 0.2282 |
| `ex3/homogeneous/4s3p/focus_front` | desc | 20,001 | 194.3 | 69.2 | 233.2 | 56.4 | 11.8 | 11.8 | 24.6 | 17.4 | 10.3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5411 | 1.3734 | 0.2705 | 31.9 | 0.1876 |
| `ex3/homogeneous/4s3p/focus_rear` | desc | 20,001 | 308.5 | 110.2 | 370.2 | 88.7 | 25.8 | 25.8 | 33.1 | 25.4 | 14.7 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.6350 | 1.3899 | 0.3175 | 47.6 | 0.2799 |
| `ex3/homogeneous/4s3p/random` | desc | 20,001 | 250.2 | 89.2 | 300.2 | 72.4 | 19.1 | 19.1 | 29.0 | 22.7 | 12.3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5602 | 1.3669 | 0.2801 | 40.2 | 0.2363 |
| `ex3/homogeneous/4s3p/spread` | desc | 20,001 | 316.5 | 113.4 | 379.8 | 90.3 | 26.4 | 26.4 | 33.1 | 25.4 | 14.8 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.6586 | 1.3700 | 0.3293 | 49.9 | 0.2937 |
| `ex3/homogeneous/4s4p/focus_front` | desc | 20,000 | 315.2 | 88.4 | 378.4 | 62.5 | 24.4 | 24.4 | 51.2 | 41.0 | 13.3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7268 | 1.4882 | 0.2423 | 31.7 | 0.1864 |
| `ex3/homogeneous/4s4p/focus_rear` | desc | 20,000 | 592.4 | 165.0 | 710.9 | 117.1 | 62.0 | 62.0 | 83.5 | 74.0 | 22.4 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.8434 | 1.5148 | 0.2811 | 50.0 | 0.2940 |
| `ex3/homogeneous/4s4p/random` | desc | 20,000 | 438.4 | 122.2 | 526.1 | 87.3 | 41.7 | 41.7 | 66.1 | 59.2 | 17.3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7410 | 1.4707 | 0.2470 | 41.2 | 0.2425 |
| `ex3/homogeneous/4s4p/spread` | desc | 20,000 | 619.5 | 173.4 | 743.4 | 120.8 | 65.4 | 65.4 | 85.2 | 76.1 | 23.1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.8745 | 1.4987 | 0.2915 | 53.4 | 0.3139 |
| `ex3/homogeneous/6s6p/focus_front` | desc | 20,004 | 746.7 | 147.1 | 896.0 | 88.3 | 72.9 | 72.9 | 137.5 | 126.7 | 19.0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.0739 | 1.6693 | 0.2148 | 39.4 | 0.1949 |
| `ex3/homogeneous/6s6p/focus_rear` | desc | 20,004 | 1,916 | 370.7 | 2,300 | 223.4 | 240.3 | 240.3 | 306.6 | 317.5 | 42.7 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.1517 | 1.6620 | 0.2303 | 66.7 | 0.3304 |
| `ex3/homogeneous/6s6p/random` | desc | 20,004 | 1,244 | 241.8 | 1,493 | 147.7 | 145.9 | 145.9 | 211.7 | 218.1 | 29.3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.0799 | 1.6243 | 0.2160 | 54.7 | 0.2708 |
| `ex3/homogeneous/6s6p/spread` | desc | 20,004 | 2,023 | 392.5 | 2,427 | 233.7 | 254.7 | 254.7 | 317.9 | 331.2 | 44.6 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.1845 | 1.6539 | 0.2369 | 68.8 | 0.3408 |
| `ex4/4s4p/random/barriers=True` | desc | 20,000 | 429.9 | 119.9 | 515.9 | 85.4 | 39.8 | 39.8 | 64.4 | 55.5 | 16.9 | 0.0000 | 10.7 | 58.8 | 0.0000 | 1.7648 | 1.4763 | 0.2549 | 40.6 | 0.2390 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True` | desc | 20,000 | 566.7 | 155.4 | 911.1 | 116.4 | 86.3 | 86.3 | 68.6 | 74.6 | 23.9 | 1.3754 | 14.6 | 66.8 | 0.0000 | 1.7852 | 1.5204 | 0.2617 | 39.5 | 0.2321 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | desc | 20,000 | 590.4 | 161.7 | 944.3 | 121.8 | 89.0 | 89.0 | 77.1 | 76.3 | 24.8 | 1.3615 | 14.9 | 69.3 | 0.0000 | 1.7638 | 1.5057 | 0.2546 | 36.0 | 0.2115 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory-dreimal_wuerfeln=True` | desc | 20,000 | 562.6 | 154.3 | 885.8 | 115.5 | 86.1 | 86.1 | 63.2 | 65.3 | 24.9 | 0.0000 | 14.5 | 66.5 | 0.0000 | 1.7801 | 1.5111 | 0.2600 | 39.6 | 0.2327 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory-dreimal_wuerfeln=True-goal_no_jump=True` | desc | 20,000 | 585.8 | 160.6 | 918.1 | 120.5 | 88.7 | 88.7 | 71.5 | 66.8 | 25.8 | 0.0000 | 14.7 | 68.3 | 0.0000 | 1.7619 | 1.5022 | 0.2540 | 36.2 | 0.2129 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True` | desc | 20,000 | 662.5 | 181.4 | 1,068 | 136.3 | 103.6 | 103.6 | 76.7 | 88.2 | 27.4 | 1.3939 | 17.1 | 77.9 | 2.5238 | 1.8117 | 1.5422 | 0.2706 | 39.7 | 0.2337 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | desc | 20,000 | 688.8 | 188.5 | 1,106 | 141.9 | 106.7 | 106.7 | 84.1 | 90.8 | 28.6 | 1.3801 | 17.4 | 80.1 | 2.7571 | 1.7932 | 1.5385 | 0.2644 | 37.3 | 0.2196 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-dreimal_wuerfeln=True` | desc | 20,000 | 659.8 | 180.8 | 1,044 | 135.3 | 103.5 | 103.5 | 71.6 | 79.1 | 28.6 | 0.0000 | 17.0 | 77.2 | 2.5410 | 1.8054 | 1.5484 | 0.2685 | 40.1 | 0.2357 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-dreimal_wuerfeln=True-goal_no_jump=True` | desc | 20,000 | 684.1 | 187.4 | 1,079 | 140.8 | 106.4 | 106.4 | 78.4 | 80.8 | 29.7 | 0.0000 | 17.4 | 79.6 | 2.7646 | 1.7820 | 1.5305 | 0.2607 | 37.3 | 0.2195 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-cold_start=strict-dreimal_wuerfeln=True` | desc | 20,000 | 402.7 | 111.2 | 611.8 | 82.0 | 47.2 | 47.2 | 44.0 | 38.4 | 17.6 | 1.3638 | 11.9 | 56.7 | 0.0000 | 1.7849 | 1.4883 | 0.2616 | 33.8 | 0.1990 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | desc | 20,000 | 428.5 | 118.1 | 644.5 | 87.8 | 49.2 | 49.2 | 55.0 | 39.2 | 18.5 | 1.3968 | 12.2 | 59.9 | 0.0000 | 1.7575 | 1.5171 | 0.2525 | 28.5 | 0.1677 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-dreimal_wuerfeln=True` | desc | 20,000 | 399.6 | 110.5 | 587.6 | 81.2 | 47.2 | 47.2 | 38.6 | 28.8 | 19.0 | 0.0000 | 11.8 | 56.1 | 0.0000 | 1.7779 | 1.4883 | 0.2593 | 33.7 | 0.1984 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-dreimal_wuerfeln=True-goal_no_jump=True` | desc | 20,000 | 425.4 | 117.4 | 620.7 | 87.0 | 49.3 | 49.3 | 49.4 | 29.6 | 19.9 | 0.0000 | 12.2 | 59.6 | 0.0000 | 1.7617 | 1.5172 | 0.2539 | 28.3 | 0.1665 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True` | desc | 20,000 | 559.0 | 153.6 | 903.9 | 114.3 | 85.8 | 85.8 | 64.9 | 73.7 | 23.4 | 1.3818 | 14.6 | 66.6 | 0.0000 | 1.7626 | 1.4903 | 0.2542 | 42.4 | 0.2495 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | desc | 20,000 | 580.4 | 159.1 | 934.4 | 119.5 | 88.1 | 88.1 | 72.5 | 75.1 | 24.4 | 1.3731 | 14.8 | 68.5 | 0.0000 | 1.7519 | 1.4872 | 0.2506 | 38.0 | 0.2236 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-capture_mode=mandatory-dreimal_wuerfeln=True` | desc | 20,000 | 556.4 | 152.7 | 880.3 | 114.0 | 85.9 | 85.9 | 59.6 | 64.3 | 24.9 | 0.0000 | 14.5 | 65.9 | 0.0000 | 1.7718 | 1.5016 | 0.2573 | 41.7 | 0.2454 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-capture_mode=mandatory-dreimal_wuerfeln=True-goal_no_jump=True` | desc | 20,000 | 575.7 | 157.9 | 907.6 | 118.3 | 87.8 | 87.8 | 66.8 | 65.3 | 25.5 | 0.0000 | 14.7 | 67.8 | 0.0000 | 1.7490 | 1.4844 | 0.2497 | 38.2 | 0.2245 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True` | desc | 20,000 | 656.0 | 179.7 | 1,062 | 134.6 | 103.1 | 103.1 | 73.6 | 87.5 | 27.1 | 1.3602 | 17.1 | 77.7 | 2.5124 | 1.7866 | 1.5297 | 0.2622 | 42.0 | 0.2473 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | desc | 20,000 | 681.2 | 186.6 | 1,100 | 140.2 | 106.2 | 106.2 | 80.2 | 89.9 | 28.2 | 1.3730 | 17.4 | 79.8 | 2.7604 | 1.7843 | 1.5214 | 0.2614 | 38.8 | 0.2280 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-capture_mode=mandatory_extended-dreimal_wuerfeln=True` | desc | 20,000 | 656.0 | 179.8 | 1,043 | 134.5 | 103.7 | 103.7 | 68.1 | 78.2 | 28.5 | 0.0000 | 17.2 | 78.1 | 2.5377 | 1.7971 | 1.5342 | 0.2657 | 41.8 | 0.2459 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-capture_mode=mandatory_extended-dreimal_wuerfeln=True-goal_no_jump=True` | desc | 20,000 | 676.4 | 185.3 | 1,073 | 139.1 | 105.8 | 105.8 | 74.4 | 80.0 | 29.4 | 0.0000 | 17.4 | 79.1 | 2.7411 | 1.7805 | 1.5185 | 0.2601 | 38.9 | 0.2287 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-cold_start=strict-dreimal_wuerfeln=True` | desc | 20,000 | 396.3 | 109.5 | 606.3 | 80.6 | 46.8 | 46.8 | 40.5 | 37.6 | 17.5 | 1.3704 | 11.9 | 56.2 | 0.0000 | 1.7597 | 1.4786 | 0.2532 | 35.8 | 0.2104 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | desc | 20,000 | 419.4 | 115.6 | 637.2 | 86.0 | 48.6 | 48.6 | 49.9 | 38.2 | 18.4 | 1.3777 | 12.2 | 59.2 | 0.0000 | 1.7517 | 1.5026 | 0.2506 | 30.6 | 0.1800 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-dreimal_wuerfeln=True` | desc | 20,000 | 393.6 | 108.8 | 582.9 | 80.0 | 46.9 | 46.9 | 35.2 | 28.3 | 18.7 | 0.0000 | 11.8 | 55.9 | 0.0000 | 1.7567 | 1.4682 | 0.2522 | 35.8 | 0.2104 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-dreimal_wuerfeln=True-goal_no_jump=True` | desc | 20,000 | 416.5 | 114.9 | 613.6 | 85.2 | 48.6 | 48.6 | 44.6 | 28.9 | 19.6 | 0.0000 | 12.1 | 58.7 | 0.0000 | 1.7325 | 1.4916 | 0.2441 | 30.5 | 0.1793 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True` | desc | 20,000 | 438.5 | 122.3 | 522.2 | 87.2 | 40.3 | 40.3 | 68.6 | 57.0 | 17.1 | 0.0000 | 10.8 | 59.6 | 0.0000 | 1.7793 | 1.4937 | 0.2598 | 38.5 | 0.2263 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory` | desc | 20,000 | 576.5 | 160.1 | 687.9 | 115.2 | 62.6 | 62.6 | 115.2 | 109.9 | 20.1 | 0.0000 | 11.5 | 63.1 | 0.0000 | 1.7928 | 1.5386 | 0.2643 | 43.1 | 0.2535 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=free_entry` | desc | 20,000 | 1,835 | 495.1 | 2,197 | 382.3 | 498.5 | 498.5 | 15.1 | 66.9 | 76.8 | 0.0000 | 77.0 | 493.9 | 0.0000 | 1.7693 | 1.4672 | 0.2564 | 67.7 | 0.3981 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=free_entry-goal_no_jump=True` | desc | 20,000 | 1,901 | 512.7 | 2,274 | 397.7 | 513.6 | 513.6 | 21.7 | 68.6 | 79.4 | 0.0000 | 78.9 | 507.7 | 0.0000 | 1.7482 | 1.4502 | 0.2494 | 64.7 | 0.3807 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=strict` | desc | 20,000 | 594.3 | 164.7 | 709.3 | 119.1 | 62.1 | 62.1 | 134.2 | 132.5 | 17.0 | 5.0277 | 11.6 | 63.9 | 0.0000 | 1.8107 | 1.5310 | 0.2702 | 44.1 | 0.2594 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True` | desc | 20,000 | 595.1 | 164.1 | 834.1 | 120.6 | 78.8 | 78.8 | 64.6 | 67.6 | 21.7 | 1.4058 | 12.7 | 68.1 | 0.0000 | 1.7490 | 1.4759 | 0.2497 | 42.9 | 0.2525 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | desc | 20,000 | 622.1 | 171.4 | 867.8 | 126.7 | 81.4 | 81.4 | 73.6 | 69.1 | 22.7 | 1.3783 | 13.0 | 71.0 | 0.0000 | 1.7297 | 1.4684 | 0.2432 | 38.9 | 0.2290 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=strict-goal_no_jump=True` | desc | 20,000 | 627.0 | 173.2 | 746.5 | 127.0 | 64.5 | 64.5 | 148.1 | 136.8 | 17.9 | 5.0138 | 11.9 | 67.4 | 0.0000 | 1.7615 | 1.5221 | 0.2538 | 38.4 | 0.2260 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory-dreimal_wuerfeln=True` | desc | 20,000 | 589.6 | 162.7 | 810.2 | 119.4 | 78.8 | 78.8 | 59.1 | 58.2 | 22.9 | 0.0000 | 12.7 | 67.8 | 0.0000 | 1.7400 | 1.4759 | 0.2466 | 42.8 | 0.2515 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory-dreimal_wuerfeln=True-goal_no_jump=True` | desc | 20,000 | 614.3 | 169.4 | 840.6 | 124.9 | 81.0 | 81.0 | 68.0 | 59.4 | 23.7 | 0.0000 | 12.9 | 70.2 | 0.0000 | 1.7272 | 1.4768 | 0.2424 | 38.8 | 0.2281 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory-goal_no_jump=True` | desc | 20,000 | 610.4 | 168.9 | 726.8 | 123.2 | 65.4 | 65.4 | 128.8 | 113.8 | 21.0 | 0.0000 | 11.9 | 67.1 | 0.0000 | 1.7521 | 1.5270 | 0.2507 | 37.9 | 0.2229 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended` | desc | 20,000 | 669.9 | 185.5 | 799.9 | 134.0 | 74.6 | 74.6 | 133.7 | 131.4 | 22.5 | 0.0000 | 13.5 | 73.9 | 2.1637 | 1.8067 | 1.5575 | 0.2689 | 44.2 | 0.2599 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=free_entry` | desc | 20,000 | 2,195 | 590.8 | 2,628 | 460.2 | 597.4 | 597.4 | 15.7 | 81.6 | 90.8 | 0.0000 | 91.6 | 587.6 | 3.6223 | 1.7772 | 1.4925 | 0.2591 | 65.2 | 0.3835 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=free_entry-goal_no_jump=True` | desc | 20,000 | 2,264 | 609.8 | 2,710 | 474.7 | 613.5 | 613.5 | 20.8 | 84.1 | 92.8 | 0.0000 | 93.6 | 600.8 | 3.9592 | 1.7587 | 1.4669 | 0.2529 | 63.5 | 0.3738 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=strict` | desc | 20,000 | 686.8 | 189.7 | 820.2 | 138.4 | 73.9 | 73.9 | 152.1 | 153.7 | 19.8 | 4.9077 | 13.4 | 73.7 | 2.1959 | 1.8318 | 1.5722 | 0.2773 | 43.4 | 0.2556 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True` | desc | 20,000 | 695.5 | 191.6 | 976.1 | 141.0 | 94.5 | 94.5 | 71.8 | 79.4 | 25.0 | 1.3786 | 14.9 | 79.4 | 2.4832 | 1.7870 | 1.5137 | 0.2623 | 43.3 | 0.2546 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | desc | 20,000 | 727.0 | 200.1 | 1,018 | 147.9 | 98.1 | 98.1 | 79.8 | 82.0 | 26.0 | 1.3671 | 15.3 | 82.3 | 2.7275 | 1.7547 | 1.4980 | 0.2516 | 40.2 | 0.2365 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=strict-goal_no_jump=True` | desc | 20,000 | 722.5 | 199.4 | 861.7 | 146.2 | 77.0 | 77.0 | 165.3 | 159.5 | 20.7 | 4.9992 | 13.8 | 76.7 | 2.4832 | 1.7871 | 1.5461 | 0.2623 | 39.6 | 0.2330 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-dreimal_wuerfeln=True` | desc | 20,000 | 690.5 | 190.3 | 953.1 | 139.8 | 94.7 | 94.7 | 66.5 | 70.1 | 26.0 | 0.0000 | 14.9 | 79.6 | 2.4651 | 1.7756 | 1.5061 | 0.2585 | 42.9 | 0.2525 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-dreimal_wuerfeln=True-goal_no_jump=True` | desc | 20,000 | 717.4 | 197.6 | 988.0 | 145.7 | 97.3 | 97.3 | 74.5 | 72.1 | 26.9 | 0.0000 | 15.1 | 81.5 | 2.7073 | 1.7334 | 1.5045 | 0.2445 | 39.8 | 0.2339 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-goal_no_jump=True` | desc | 20,000 | 708.0 | 195.7 | 844.1 | 142.9 | 77.8 | 77.8 | 147.1 | 137.6 | 23.6 | 0.0000 | 13.7 | 76.7 | 2.5111 | 1.7864 | 1.5441 | 0.2621 | 39.0 | 0.2292 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-cold_start=free_entry` | desc | 20,000 | 554.4 | 153.6 | 660.8 | 110.8 | 91.0 | 91.0 | 13.2 | 8.7787 | 23.9 | 0.0000 | 27.2 | 167.7 | 0.0000 | 1.7335 | 1.4147 | 0.2445 | 47.4 | 0.2791 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-cold_start=free_entry-goal_no_jump=True` | desc | 20,000 | 600.5 | 166.3 | 712.7 | 120.8 | 96.4 | 96.4 | 26.3 | 8.9566 | 25.2 | 0.0000 | 28.4 | 178.5 | 0.0000 | 1.6945 | 1.4083 | 0.2315 | 39.7 | 0.2335 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-cold_start=strict` | desc | 20,000 | 454.9 | 126.4 | 541.9 | 91.2 | 39.6 | 39.6 | 87.4 | 79.7 | 14.0 | 5.0016 | 10.8 | 59.8 | 0.0000 | 1.7788 | 1.5010 | 0.2596 | 39.2 | 0.2307 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-cold_start=strict-dreimal_wuerfeln=True` | desc | 20,000 | 443.4 | 122.6 | 595.9 | 90.0 | 46.7 | 46.7 | 43.5 | 37.0 | 17.5 | 1.3601 | 11.4 | 61.8 | 0.0000 | 1.7565 | 1.4685 | 0.2521 | 36.7 | 0.2159 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | desc | 20,000 | 471.3 | 130.2 | 629.1 | 96.2 | 48.7 | 48.7 | 55.0 | 37.9 | 18.2 | 1.3772 | 11.7 | 65.4 | 0.0000 | 1.7300 | 1.4827 | 0.2433 | 31.1 | 0.1832 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-cold_start=strict-goal_no_jump=True` | desc | 20,000 | 486.9 | 134.8 | 577.9 | 98.6 | 41.6 | 41.6 | 102.0 | 81.8 | 14.8 | 5.0098 | 11.1 | 64.6 | 0.0000 | 1.7752 | 1.5351 | 0.2584 | 32.0 | 0.1885 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-dreimal_wuerfeln=True` | desc | 20,000 | 436.8 | 121.1 | 570.6 | 88.2 | 46.6 | 46.6 | 38.0 | 27.5 | 18.5 | 0.0000 | 11.3 | 61.3 | 0.0000 | 1.7331 | 1.4585 | 0.2444 | 37.4 | 0.2200 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-dreimal_wuerfeln=True-goal_no_jump=True` | desc | 20,000 | 464.9 | 128.6 | 603.7 | 94.6 | 48.6 | 48.6 | 49.3 | 28.3 | 19.4 | 0.0000 | 11.7 | 65.5 | 0.0000 | 1.7288 | 1.4765 | 0.2429 | 31.2 | 0.1836 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-goal_no_jump=True` | desc | 20,000 | 469.0 | 130.3 | 556.6 | 94.3 | 42.1 | 42.1 | 82.9 | 59.0 | 17.9 | 0.0000 | 11.1 | 64.4 | 0.0000 | 1.7621 | 1.5329 | 0.2540 | 31.6 | 0.1859 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory` | desc | 20,000 | 568.0 | 157.9 | 681.7 | 112.9 | 62.1 | 62.1 | 110.6 | 107.7 | 19.8 | 0.0000 | 11.5 | 62.9 | 0.0000 | 1.7752 | 1.5105 | 0.2584 | 45.7 | 0.2688 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory-cold_start=free_entry` | desc | 20,000 | 1,817 | 490.7 | 2,181 | 378.0 | 495.0 | 495.0 | 11.8 | 65.5 | 76.2 | 0.0000 | 76.8 | 491.5 | 0.0000 | 1.7667 | 1.4665 | 0.2555 | 69.3 | 0.4074 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory-cold_start=free_entry-goal_no_jump=True` | desc | 20,000 | 1,880 | 507.5 | 2,256 | 392.0 | 509.6 | 509.6 | 17.4 | 67.4 | 78.8 | 0.0000 | 78.5 | 503.3 | 0.0000 | 1.7470 | 1.4376 | 0.2490 | 66.5 | 0.3910 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory-cold_start=strict` | desc | 20,000 | 582.6 | 161.6 | 699.1 | 116.5 | 61.1 | 61.1 | 129.0 | 129.8 | 16.8 | 4.9629 | 11.5 | 63.1 | 0.0000 | 1.7864 | 1.5208 | 0.2621 | 46.3 | 0.2722 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True` | desc | 20,000 | 587.7 | 162.0 | 827.4 | 119.3 | 78.5 | 78.5 | 60.9 | 66.6 | 21.8 | 1.3462 | 12.7 | 67.6 | 0.0000 | 1.7507 | 1.4637 | 0.2502 | 44.5 | 0.2619 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | desc | 20,000 | 611.4 | 168.5 | 858.1 | 124.4 | 80.5 | 80.5 | 69.0 | 67.8 | 22.4 | 1.3616 | 12.9 | 70.0 | 0.0000 | 1.7299 | 1.4586 | 0.2433 | 41.0 | 0.2410 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory-cold_start=strict-goal_no_jump=True` | desc | 20,000 | 615.2 | 170.0 | 738.2 | 124.5 | 63.8 | 63.8 | 141.6 | 134.2 | 17.8 | 5.0068 | 11.8 | 66.6 | 0.0000 | 1.7704 | 1.5090 | 0.2568 | 40.5 | 0.2384 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory-dreimal_wuerfeln=True` | desc | 20,000 | 582.4 | 160.9 | 803.7 | 117.6 | 78.5 | 78.5 | 55.5 | 57.1 | 22.7 | 0.0000 | 12.7 | 67.4 | 0.0000 | 1.7387 | 1.4569 | 0.2462 | 44.9 | 0.2641 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory-dreimal_wuerfeln=True-goal_no_jump=True` | desc | 20,000 | 605.1 | 166.8 | 833.0 | 122.9 | 80.4 | 80.4 | 63.3 | 58.3 | 23.5 | 0.0000 | 12.9 | 69.5 | 0.0000 | 1.7173 | 1.4591 | 0.2391 | 40.8 | 0.2400 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory-goal_no_jump=True` | desc | 20,000 | 600.6 | 166.3 | 720.8 | 120.9 | 64.8 | 64.8 | 123.1 | 111.7 | 20.8 | 0.0000 | 11.9 | 66.5 | 0.0000 | 1.7563 | 1.5146 | 0.2521 | 40.1 | 0.2358 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory_extended` | desc | 20,000 | 660.2 | 183.2 | 792.3 | 131.4 | 74.0 | 74.0 | 128.4 | 128.8 | 22.2 | 0.0000 | 13.4 | 73.4 | 2.1620 | 1.7965 | 1.5427 | 0.2655 | 46.5 | 0.2733 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory_extended-cold_start=free_entry` | desc | 20,000 | 2,178 | 586.5 | 2,613 | 455.7 | 594.3 | 594.3 | 12.4 | 80.5 | 90.6 | 0.0000 | 91.6 | 585.0 | 3.6273 | 1.7703 | 1.4897 | 0.2568 | 67.1 | 0.3947 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory_extended-cold_start=free_entry-goal_no_jump=True` | desc | 20,000 | 2,247 | 605.5 | 2,697 | 470.8 | 610.9 | 610.9 | 16.6 | 82.8 | 92.8 | 0.0000 | 93.5 | 599.2 | 3.9285 | 1.7512 | 1.4656 | 0.2504 | 64.9 | 0.3820 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory_extended-cold_start=strict` | desc | 20,000 | 678.3 | 187.6 | 814.0 | 136.3 | 73.4 | 73.4 | 147.9 | 152.1 | 19.4 | 5.0219 | 13.4 | 73.4 | 2.1681 | 1.8119 | 1.5501 | 0.2706 | 45.9 | 0.2701 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True` | desc | 20,000 | 688.0 | 189.6 | 969.5 | 139.2 | 94.1 | 94.1 | 68.4 | 78.4 | 24.8 | 1.3747 | 14.9 | 79.5 | 2.4737 | 1.7670 | 1.4907 | 0.2557 | 45.3 | 0.2662 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | desc | 20,000 | 716.0 | 197.2 | 1,007 | 145.5 | 97.2 | 97.2 | 75.5 | 80.8 | 25.7 | 1.3553 | 15.2 | 81.4 | 2.7271 | 1.7452 | 1.4927 | 0.2484 | 41.7 | 0.2453 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory_extended-cold_start=strict-goal_no_jump=True` | desc | 20,000 | 711.7 | 196.5 | 854.0 | 143.9 | 76.3 | 76.3 | 159.3 | 157.2 | 20.5 | 5.0171 | 13.7 | 75.8 | 2.4895 | 1.7970 | 1.5456 | 0.2656 | 41.6 | 0.2449 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory_extended-dreimal_wuerfeln=True` | desc | 20,000 | 681.1 | 187.9 | 943.4 | 137.6 | 93.8 | 93.8 | 62.8 | 68.8 | 25.7 | 0.0000 | 14.8 | 78.9 | 2.4623 | 1.7606 | 1.4999 | 0.2535 | 44.9 | 0.2640 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory_extended-dreimal_wuerfeln=True-goal_no_jump=True` | desc | 20,000 | 711.8 | 196.1 | 985.5 | 144.7 | 97.4 | 97.4 | 70.0 | 71.6 | 26.8 | 0.0000 | 15.2 | 81.3 | 2.7351 | 1.7401 | 1.4834 | 0.2467 | 41.5 | 0.2440 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory_extended-goal_no_jump=True` | desc | 20,000 | 694.5 | 192.1 | 833.4 | 139.9 | 76.9 | 76.9 | 140.4 | 134.2 | 23.4 | 0.0000 | 13.6 | 75.4 | 2.4880 | 1.7660 | 1.5214 | 0.2553 | 41.4 | 0.2437 |
| `ex4/4s4p/random/barriers=True-cold_start=free_entry` | desc | 20,000 | 545.2 | 151.3 | 654.2 | 108.7 | 90.1 | 90.1 | 10.0 | 8.4804 | 23.4 | 0.0000 | 27.1 | 166.6 | 0.0000 | 1.7234 | 1.3837 | 0.2411 | 49.9 | 0.2935 |
| `ex4/4s4p/random/barriers=True-cold_start=free_entry-goal_no_jump=True` | desc | 20,000 | 587.5 | 162.8 | 705.0 | 118.0 | 95.1 | 95.1 | 20.7 | 8.7189 | 24.8 | 0.0000 | 28.2 | 176.2 | 0.0000 | 1.6921 | 1.4016 | 0.2307 | 41.9 | 0.2466 |
| `ex4/4s4p/random/barriers=True-cold_start=strict` | desc | 20,000 | 448.3 | 124.8 | 537.8 | 89.7 | 39.3 | 39.3 | 83.4 | 78.5 | 13.9 | 5.0043 | 10.8 | 59.6 | 0.0000 | 1.7812 | 1.4915 | 0.2604 | 41.0 | 0.2411 |
| `ex4/4s4p/random/barriers=True-cold_start=strict-dreimal_wuerfeln=True` | desc | 20,000 | 436.2 | 120.9 | 590.3 | 88.2 | 46.3 | 46.3 | 40.0 | 36.4 | 17.3 | 1.3832 | 11.3 | 60.7 | 0.0000 | 1.7466 | 1.4438 | 0.2489 | 39.5 | 0.2323 |
| `ex4/4s4p/random/barriers=True-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | desc | 20,000 | 461.1 | 127.4 | 621.3 | 93.9 | 48.0 | 48.0 | 49.7 | 37.1 | 18.0 | 1.3535 | 11.6 | 64.4 | 0.0000 | 1.7195 | 1.4669 | 0.2398 | 33.6 | 0.1976 |
| `ex4/4s4p/random/barriers=True-cold_start=strict-goal_no_jump=True` | desc | 20,000 | 476.3 | 132.0 | 571.6 | 96.3 | 41.1 | 41.1 | 95.6 | 80.2 | 14.6 | 4.9052 | 11.2 | 64.1 | 0.0000 | 1.7600 | 1.5042 | 0.2533 | 34.2 | 0.2013 |
| `ex4/4s4p/random/barriers=True-dreimal_wuerfeln=True` | desc | 20,000 | 430.0 | 119.3 | 565.4 | 86.6 | 46.2 | 46.2 | 34.7 | 26.9 | 18.2 | 0.0000 | 11.3 | 60.7 | 0.0000 | 1.7406 | 1.4398 | 0.2469 | 39.6 | 0.2331 |
| `ex4/4s4p/random/barriers=True-dreimal_wuerfeln=True-goal_no_jump=True` | desc | 20,000 | 455.9 | 126.1 | 597.9 | 92.8 | 48.1 | 48.1 | 44.6 | 27.7 | 19.2 | 0.0000 | 11.6 | 64.4 | 0.0000 | 1.7293 | 1.4644 | 0.2431 | 33.2 | 0.1952 |
| `ex4/4s4p/random/barriers=True-goal_no_jump=True` | desc | 20,000 | 459.9 | 127.9 | 551.9 | 92.4 | 41.8 | 41.8 | 76.9 | 57.7 | 17.7 | 0.0000 | 11.1 | 63.1 | 0.0000 | 1.7454 | 1.5005 | 0.2485 | 34.0 | 0.1997 |
| `ex4/4s4p/random/baseline` | desc | 20,000 | 439.0 | 122.4 | 526.7 | 87.3 | 41.8 | 41.8 | 66.2 | 59.1 | 17.3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7508 | 1.4804 | 0.2502 | 41.3 | 0.2427 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True` | desc | 20,000 | 566.7 | 155.5 | 916.8 | 116.1 | 87.9 | 87.9 | 67.3 | 76.5 | 23.9 | 1.3653 | 0.0000 | 0.0000 | 0.0000 | 1.7862 | 1.5057 | 0.2621 | 40.3 | 0.2373 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | desc | 20,000 | 591.1 | 162.0 | 950.8 | 121.7 | 90.6 | 90.6 | 75.7 | 78.3 | 25.0 | 1.3638 | 0.0000 | 0.0000 | 0.0000 | 1.7496 | 1.5051 | 0.2499 | 36.4 | 0.2139 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory-dreimal_wuerfeln=True` | desc | 20,000 | 565.6 | 155.3 | 896.1 | 115.7 | 88.3 | 88.3 | 62.2 | 67.5 | 25.2 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7571 | 1.4981 | 0.2524 | 40.7 | 0.2396 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory-dreimal_wuerfeln=True-goal_no_jump=True` | desc | 20,000 | 586.4 | 160.9 | 924.1 | 120.5 | 90.2 | 90.2 | 70.2 | 68.7 | 26.1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7515 | 1.4977 | 0.2505 | 36.7 | 0.2161 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True` | desc | 20,000 | 662.4 | 181.6 | 1,073 | 135.6 | 105.1 | 105.1 | 75.6 | 90.3 | 27.4 | 1.3955 | 0.0000 | 0.0000 | 2.5005 | 1.7966 | 1.5320 | 0.2655 | 41.0 | 0.2410 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | desc | 20,000 | 686.8 | 188.0 | 1,109 | 141.2 | 107.9 | 107.9 | 82.6 | 92.5 | 28.6 | 1.3800 | 0.0000 | 0.0000 | 2.7188 | 1.7913 | 1.5303 | 0.2637 | 37.9 | 0.2230 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-dreimal_wuerfeln=True` | desc | 20,000 | 656.7 | 180.1 | 1,045 | 134.3 | 104.4 | 104.4 | 70.2 | 80.6 | 28.8 | 0.0000 | 0.0000 | 0.0000 | 2.4882 | 1.8017 | 1.5387 | 0.2672 | 40.5 | 0.2383 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-dreimal_wuerfeln=True-goal_no_jump=True` | desc | 20,000 | 685.0 | 187.8 | 1,088 | 140.6 | 108.2 | 108.2 | 77.5 | 83.7 | 29.8 | 0.0000 | 0.0000 | 0.0000 | 2.7456 | 1.7689 | 1.5333 | 0.2563 | 37.9 | 0.2229 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-cold_start=strict-dreimal_wuerfeln=True` | desc | 20,000 | 408.8 | 112.9 | 625.0 | 83.4 | 49.6 | 49.6 | 43.6 | 40.2 | 18.3 | 1.3819 | 0.0000 | 0.0000 | 0.0000 | 1.7715 | 1.4979 | 0.2572 | 34.1 | 0.2003 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | desc | 20,000 | 433.5 | 119.5 | 656.9 | 88.7 | 51.7 | 51.7 | 53.7 | 41.0 | 19.1 | 1.3724 | 0.0000 | 0.0000 | 0.0000 | 1.7628 | 1.5155 | 0.2542 | 29.5 | 0.1736 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-dreimal_wuerfeln=True` | desc | 20,000 | 405.3 | 112.0 | 600.5 | 82.4 | 49.6 | 49.6 | 38.1 | 30.6 | 19.5 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7662 | 1.4890 | 0.2554 | 34.3 | 0.2016 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-dreimal_wuerfeln=True-goal_no_jump=True` | desc | 20,000 | 428.6 | 118.2 | 630.0 | 87.6 | 51.3 | 51.3 | 48.1 | 31.4 | 20.2 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7494 | 1.5163 | 0.2498 | 29.2 | 0.1716 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True` | desc | 20,000 | 561.2 | 154.0 | 912.3 | 115.0 | 87.7 | 87.7 | 64.4 | 75.9 | 23.9 | 1.3985 | 0.0000 | 0.0000 | 0.0000 | 1.7813 | 1.4976 | 0.2604 | 42.3 | 0.2486 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | desc | 20,000 | 580.9 | 159.3 | 940.2 | 119.4 | 89.6 | 89.6 | 71.3 | 77.1 | 24.8 | 1.3591 | 0.0000 | 0.0000 | 0.0000 | 1.7492 | 1.4866 | 0.2497 | 38.6 | 0.2273 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-capture_mode=mandatory-dreimal_wuerfeln=True` | desc | 20,000 | 556.1 | 152.8 | 885.1 | 113.7 | 87.2 | 87.2 | 58.9 | 66.4 | 25.0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7613 | 1.4783 | 0.2538 | 42.2 | 0.2485 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-capture_mode=mandatory-dreimal_wuerfeln=True-goal_no_jump=True` | desc | 20,000 | 578.7 | 158.8 | 918.1 | 118.8 | 89.8 | 89.8 | 66.2 | 68.0 | 25.8 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7443 | 1.4859 | 0.2481 | 38.9 | 0.2291 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True` | desc | 20,000 | 654.9 | 179.4 | 1,066 | 134.4 | 104.6 | 104.6 | 72.3 | 89.4 | 27.4 | 1.3564 | 0.0000 | 0.0000 | 2.4954 | 1.7975 | 1.5346 | 0.2658 | 42.0 | 0.2470 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | desc | 20,000 | 676.7 | 185.6 | 1,097 | 138.9 | 106.9 | 106.9 | 78.2 | 91.1 | 28.2 | 1.3644 | 0.0000 | 0.0000 | 2.7197 | 1.7721 | 1.5235 | 0.2574 | 39.3 | 0.2314 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-capture_mode=mandatory_extended-dreimal_wuerfeln=True` | desc | 20,000 | 651.8 | 178.9 | 1,042 | 133.2 | 104.6 | 104.6 | 66.9 | 79.9 | 28.5 | 0.0000 | 0.0000 | 0.0000 | 2.4901 | 1.7871 | 1.5177 | 0.2624 | 42.3 | 0.2490 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-capture_mode=mandatory_extended-dreimal_wuerfeln=True-goal_no_jump=True` | desc | 20,000 | 676.2 | 185.5 | 1,078 | 138.5 | 107.5 | 107.5 | 73.2 | 82.4 | 29.5 | 0.0000 | 0.0000 | 0.0000 | 2.7319 | 1.7711 | 1.5117 | 0.2570 | 39.7 | 0.2336 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-cold_start=strict-dreimal_wuerfeln=True` | desc | 20,000 | 402.9 | 111.3 | 620.3 | 82.1 | 49.4 | 49.4 | 40.4 | 39.5 | 18.1 | 1.3889 | 0.0000 | 0.0000 | 0.0000 | 1.7619 | 1.4756 | 0.2540 | 36.3 | 0.2135 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | desc | 20,000 | 425.3 | 117.2 | 650.7 | 87.2 | 51.2 | 51.2 | 49.1 | 40.3 | 18.8 | 1.3918 | 0.0000 | 0.0000 | 0.0000 | 1.7546 | 1.4990 | 0.2515 | 31.1 | 0.1827 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-dreimal_wuerfeln=True` | desc | 20,000 | 399.5 | 110.4 | 596.1 | 81.3 | 49.3 | 49.3 | 35.1 | 30.1 | 19.4 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7547 | 1.4758 | 0.2516 | 36.0 | 0.2115 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-dreimal_wuerfeln=True-goal_no_jump=True` | desc | 20,000 | 420.2 | 115.9 | 623.4 | 85.9 | 50.7 | 50.7 | 43.5 | 30.7 | 20.0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7421 | 1.4972 | 0.2473 | 31.2 | 0.1834 |
| `ex4/4s4p/random/bonus_roll_forfeited=True` | desc | 20,000 | 445.5 | 124.3 | 530.9 | 88.6 | 42.0 | 42.0 | 70.1 | 60.3 | 17.4 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7620 | 1.4945 | 0.2540 | 39.3 | 0.2313 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory` | desc | 20,000 | 578.7 | 160.8 | 690.7 | 115.4 | 63.5 | 63.5 | 115.7 | 112.3 | 20.1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7775 | 1.5229 | 0.2592 | 44.0 | 0.2587 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=free_entry` | desc | 20,000 | 1,851 | 501.5 | 2,218 | 381.7 | 512.9 | 512.9 | 10.4 | 73.2 | 77.7 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7594 | 1.4581 | 0.2531 | 69.9 | 0.4110 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=free_entry-goal_no_jump=True` | desc | 20,000 | 1,912 | 518.2 | 2,289 | 395.3 | 526.7 | 526.7 | 16.4 | 75.2 | 79.9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7174 | 1.4423 | 0.2391 | 66.8 | 0.3930 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=strict` | desc | 20,000 | 596.7 | 165.4 | 712.2 | 119.5 | 63.0 | 63.0 | 134.7 | 135.0 | 17.2 | 5.0495 | 0.0000 | 0.0000 | 0.0000 | 1.7894 | 1.5352 | 0.2631 | 44.3 | 0.2608 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True` | desc | 20,000 | 595.5 | 164.3 | 837.3 | 120.6 | 79.9 | 79.9 | 63.1 | 68.9 | 22.1 | 1.3744 | 0.0000 | 0.0000 | 0.0000 | 1.7367 | 1.4766 | 0.2456 | 43.2 | 0.2541 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | desc | 20,000 | 619.9 | 170.8 | 867.7 | 126.2 | 82.2 | 82.2 | 71.5 | 70.3 | 22.8 | 1.3791 | 0.0000 | 0.0000 | 0.0000 | 1.7266 | 1.4664 | 0.2422 | 39.3 | 0.2314 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=strict-goal_no_jump=True` | desc | 20,000 | 628.4 | 173.6 | 748.5 | 127.2 | 65.4 | 65.4 | 147.9 | 139.3 | 18.3 | 4.9806 | 0.0000 | 0.0000 | 0.0000 | 1.7768 | 1.5246 | 0.2589 | 38.5 | 0.2265 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory-dreimal_wuerfeln=True` | desc | 20,000 | 588.9 | 162.5 | 811.7 | 119.2 | 79.8 | 79.8 | 57.7 | 59.2 | 23.2 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7483 | 1.4754 | 0.2494 | 42.7 | 0.2514 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory-dreimal_wuerfeln=True-goal_no_jump=True` | desc | 20,000 | 614.4 | 169.4 | 844.0 | 125.0 | 82.2 | 82.2 | 66.4 | 60.9 | 23.9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7227 | 1.4720 | 0.2409 | 38.9 | 0.2288 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory-goal_no_jump=True` | desc | 20,000 | 610.3 | 169.0 | 727.0 | 122.9 | 66.1 | 66.1 | 128.4 | 116.1 | 21.1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7566 | 1.5149 | 0.2522 | 38.6 | 0.2271 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory_extended` | desc | 20,000 | 670.8 | 185.9 | 801.2 | 134.0 | 75.4 | 75.4 | 134.0 | 134.2 | 22.5 | 0.0000 | 0.0000 | 0.0000 | 2.1557 | 1.7982 | 1.5502 | 0.2661 | 44.3 | 0.2607 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=free_entry` | desc | 20,000 | 2,200 | 594.3 | 2,636 | 456.5 | 610.2 | 610.2 | 10.2 | 88.9 | 91.1 | 0.0000 | 0.0000 | 0.0000 | 3.5753 | 1.7638 | 1.4776 | 0.2546 | 68.0 | 0.3998 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=free_entry-goal_no_jump=True` | desc | 20,000 | 2,283 | 617.2 | 2,734 | 473.2 | 630.7 | 630.7 | 14.6 | 92.0 | 93.7 | 0.0000 | 0.0000 | 0.0000 | 3.9237 | 1.7427 | 1.4472 | 0.2476 | 66.3 | 0.3900 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=strict` | desc | 20,000 | 687.0 | 189.9 | 820.7 | 138.1 | 74.7 | 74.7 | 152.4 | 156.3 | 19.9 | 4.9799 | 0.0000 | 0.0000 | 2.1411 | 1.8236 | 1.5617 | 0.2745 | 44.3 | 0.2608 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True` | desc | 20,000 | 696.8 | 191.9 | 981.6 | 141.3 | 96.0 | 96.0 | 70.7 | 81.4 | 25.3 | 1.3761 | 0.0000 | 0.0000 | 2.4453 | 1.7600 | 1.5029 | 0.2533 | 43.5 | 0.2558 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | desc | 20,000 | 722.4 | 198.9 | 1,015 | 146.8 | 98.6 | 98.6 | 77.8 | 83.4 | 26.1 | 1.3582 | 0.0000 | 0.0000 | 2.7004 | 1.7515 | 1.4937 | 0.2505 | 40.6 | 0.2387 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=strict-goal_no_jump=True` | desc | 20,000 | 723.3 | 199.7 | 863.1 | 146.3 | 77.8 | 77.8 | 165.3 | 162.4 | 20.8 | 5.0038 | 0.0000 | 0.0000 | 2.4719 | 1.7863 | 1.5400 | 0.2621 | 40.1 | 0.2356 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory_extended-dreimal_wuerfeln=True` | desc | 20,000 | 689.6 | 190.2 | 955.2 | 139.3 | 95.8 | 95.8 | 65.0 | 71.6 | 26.1 | 0.0000 | 0.0000 | 0.0000 | 2.4346 | 1.7528 | 1.4980 | 0.2509 | 43.8 | 0.2574 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory_extended-dreimal_wuerfeln=True-goal_no_jump=True` | desc | 20,000 | 715.3 | 197.2 | 988.7 | 145.0 | 98.2 | 98.2 | 72.2 | 73.7 | 27.1 | 0.0000 | 0.0000 | 0.0000 | 2.6879 | 1.7417 | 1.4895 | 0.2472 | 40.3 | 0.2371 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory_extended-goal_no_jump=True` | desc | 20,000 | 706.3 | 195.3 | 842.7 | 142.1 | 78.5 | 78.5 | 146.2 | 139.7 | 23.7 | 0.0000 | 0.0000 | 0.0000 | 2.4624 | 1.7707 | 1.5322 | 0.2569 | 40.1 | 0.2357 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-cold_start=free_entry` | desc | 20,000 | 596.3 | 165.3 | 711.9 | 118.9 | 105.6 | 105.6 | 11.3 | 9.4841 | 25.6 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7242 | 1.3900 | 0.2414 | 51.5 | 0.3030 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-cold_start=free_entry-goal_no_jump=True` | desc | 20,000 | 641.0 | 177.6 | 762.3 | 128.4 | 110.8 | 110.8 | 23.2 | 9.7391 | 26.8 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.6694 | 1.3859 | 0.2231 | 43.9 | 0.2580 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-cold_start=strict` | desc | 20,000 | 463.5 | 128.9 | 552.5 | 92.9 | 41.6 | 41.6 | 88.9 | 83.0 | 14.4 | 4.9556 | 0.0000 | 0.0000 | 0.0000 | 1.7861 | 1.4961 | 0.2620 | 39.9 | 0.2348 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-cold_start=strict-dreimal_wuerfeln=True` | desc | 20,000 | 451.2 | 124.8 | 608.7 | 91.5 | 49.1 | 49.1 | 43.1 | 38.8 | 17.8 | 1.3633 | 0.0000 | 0.0000 | 0.0000 | 1.7430 | 1.4581 | 0.2477 | 37.7 | 0.2215 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | desc | 20,000 | 474.4 | 131.2 | 636.2 | 96.6 | 50.6 | 50.6 | 53.3 | 39.4 | 18.6 | 1.3739 | 0.0000 | 0.0000 | 0.0000 | 1.7367 | 1.4861 | 0.2455 | 32.4 | 0.1907 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-cold_start=strict-goal_no_jump=True` | desc | 20,000 | 493.0 | 136.6 | 585.7 | 99.7 | 43.5 | 43.5 | 101.9 | 85.0 | 15.2 | 4.9233 | 0.0000 | 0.0000 | 0.0000 | 1.7506 | 1.5176 | 0.2502 | 33.1 | 0.1948 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-dreimal_wuerfeln=True` | desc | 20,000 | 443.4 | 122.8 | 581.8 | 89.5 | 48.8 | 48.8 | 37.3 | 29.1 | 18.8 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7409 | 1.4540 | 0.2470 | 38.0 | 0.2237 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-dreimal_wuerfeln=True-goal_no_jump=True` | desc | 20,000 | 468.6 | 129.7 | 611.7 | 95.1 | 50.6 | 50.6 | 47.6 | 29.8 | 19.5 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7259 | 1.4710 | 0.2420 | 32.6 | 0.1916 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-goal_no_jump=True` | desc | 20,000 | 474.5 | 131.9 | 563.5 | 95.4 | 43.9 | 43.9 | 82.9 | 62.3 | 18.2 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7354 | 1.5272 | 0.2451 | 32.7 | 0.1923 |
| `ex4/4s4p/random/capture_mode=mandatory` | desc | 20,000 | 572.0 | 159.0 | 686.5 | 113.9 | 63.3 | 63.3 | 111.6 | 110.8 | 20.1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7759 | 1.5076 | 0.2586 | 46.2 | 0.2719 |
| `ex4/4s4p/random/capture_mode=mandatory-cold_start=free_entry` | desc | 20,000 | 1,842 | 499.5 | 2,210 | 378.4 | 511.7 | 511.7 | 7.8288 | 72.2 | 77.4 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7488 | 1.4546 | 0.2496 | 71.7 | 0.4218 |
| `ex4/4s4p/random/capture_mode=mandatory-cold_start=free_entry-goal_no_jump=True` | desc | 20,000 | 1,891 | 512.9 | 2,269 | 389.1 | 522.2 | 522.2 | 12.8 | 73.8 | 78.8 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7313 | 1.4343 | 0.2438 | 68.9 | 0.4052 |
| `ex4/4s4p/random/capture_mode=mandatory-cold_start=strict` | desc | 20,000 | 588.4 | 163.2 | 706.1 | 117.9 | 62.6 | 62.6 | 130.3 | 133.2 | 17.0 | 4.9928 | 0.0000 | 0.0000 | 0.0000 | 1.7753 | 1.5185 | 0.2584 | 45.9 | 0.2700 |
| `ex4/4s4p/random/capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True` | desc | 20,000 | 588.6 | 162.4 | 831.1 | 119.0 | 79.5 | 79.5 | 59.9 | 68.1 | 21.9 | 1.3852 | 0.0000 | 0.0000 | 0.0000 | 1.7407 | 1.4667 | 0.2469 | 45.3 | 0.2663 |
| `ex4/4s4p/random/capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | desc | 20,000 | 611.3 | 168.5 | 861.1 | 124.3 | 81.6 | 81.6 | 67.5 | 69.6 | 22.6 | 1.3761 | 0.0000 | 0.0000 | 0.0000 | 1.7188 | 1.4500 | 0.2396 | 41.2 | 0.2422 |
| `ex4/4s4p/random/capture_mode=mandatory-cold_start=strict-goal_no_jump=True` | desc | 20,000 | 617.6 | 170.7 | 741.0 | 125.0 | 64.8 | 64.8 | 141.9 | 137.2 | 18.0 | 5.0515 | 0.0000 | 0.0000 | 0.0000 | 1.7608 | 1.5127 | 0.2536 | 40.6 | 0.2388 |
| `ex4/4s4p/random/capture_mode=mandatory-dreimal_wuerfeln=True` | desc | 20,000 | 581.6 | 160.6 | 805.0 | 117.6 | 79.2 | 79.2 | 54.3 | 58.5 | 22.9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7299 | 1.4624 | 0.2433 | 44.9 | 0.2642 |
| `ex4/4s4p/random/capture_mode=mandatory-dreimal_wuerfeln=True-goal_no_jump=True` | desc | 20,000 | 605.9 | 167.1 | 837.2 | 123.1 | 81.7 | 81.7 | 62.0 | 60.1 | 23.7 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7125 | 1.4525 | 0.2375 | 40.9 | 0.2409 |
| `ex4/4s4p/random/capture_mode=mandatory-goal_no_jump=True` | desc | 20,000 | 600.8 | 166.5 | 720.8 | 120.8 | 65.5 | 65.5 | 122.8 | 114.1 | 20.9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7421 | 1.4981 | 0.2473 | 40.6 | 0.2386 |
| `ex4/4s4p/random/capture_mode=mandatory_extended` | desc | 20,000 | 660.2 | 183.1 | 792.1 | 131.7 | 74.6 | 74.6 | 129.1 | 131.6 | 22.3 | 0.0000 | 0.0000 | 0.0000 | 2.1307 | 1.7768 | 1.5291 | 0.2589 | 46.3 | 0.2723 |
| `ex4/4s4p/random/capture_mode=mandatory_extended-cold_start=free_entry` | desc | 20,000 | 2,188 | 591.6 | 2,625 | 453.5 | 608.6 | 608.6 | 7.5067 | 88.0 | 90.6 | 0.0000 | 0.0000 | 0.0000 | 3.5771 | 1.7532 | 1.4695 | 0.2511 | 69.5 | 0.4089 |
| `ex4/4s4p/random/capture_mode=mandatory_extended-cold_start=free_entry-goal_no_jump=True` | desc | 20,000 | 2,252 | 609.5 | 2,702 | 466.3 | 623.2 | 623.2 | 11.3 | 90.2 | 92.6 | 0.0000 | 0.0000 | 0.0000 | 3.9179 | 1.7313 | 1.4500 | 0.2438 | 67.3 | 0.3961 |
| `ex4/4s4p/random/capture_mode=mandatory_extended-cold_start=strict` | desc | 20,000 | 675.9 | 187.1 | 811.1 | 135.5 | 73.8 | 73.8 | 147.5 | 153.8 | 19.5 | 5.0018 | 0.0000 | 0.0000 | 2.1092 | 1.8160 | 1.5581 | 0.2720 | 46.2 | 0.2716 |
| `ex4/4s4p/random/capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True` | desc | 20,000 | 687.3 | 189.6 | 971.6 | 138.8 | 95.2 | 95.2 | 67.2 | 80.1 | 24.9 | 1.3797 | 0.0000 | 0.0000 | 2.4321 | 1.7667 | 1.4891 | 0.2556 | 45.6 | 0.2682 |
| `ex4/4s4p/random/capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | desc | 20,000 | 712.6 | 196.4 | 1,005 | 144.7 | 97.8 | 97.8 | 73.6 | 82.0 | 25.8 | 1.3835 | 0.0000 | 0.0000 | 2.6799 | 1.7496 | 1.4873 | 0.2499 | 41.9 | 0.2464 |
| `ex4/4s4p/random/capture_mode=mandatory_extended-cold_start=strict-goal_no_jump=True` | desc | 20,000 | 712.1 | 196.7 | 854.5 | 143.9 | 77.2 | 77.2 | 159.3 | 159.8 | 20.6 | 5.1119 | 0.0000 | 0.0000 | 2.4464 | 1.7826 | 1.5360 | 0.2609 | 41.7 | 0.2453 |
| `ex4/4s4p/random/capture_mode=mandatory_extended-dreimal_wuerfeln=True` | desc | 20,000 | 678.7 | 187.4 | 943.2 | 136.7 | 94.5 | 94.5 | 61.4 | 70.3 | 25.9 | 0.0000 | 0.0000 | 0.0000 | 2.4288 | 1.7656 | 1.4870 | 0.2552 | 45.6 | 0.2685 |
| `ex4/4s4p/random/capture_mode=mandatory_extended-dreimal_wuerfeln=True-goal_no_jump=True` | desc | 20,000 | 707.4 | 195.1 | 981.9 | 143.3 | 97.8 | 97.8 | 68.2 | 72.6 | 26.9 | 0.0000 | 0.0000 | 0.0000 | 2.6856 | 1.7366 | 1.4834 | 0.2455 | 42.1 | 0.2476 |
| `ex4/4s4p/random/capture_mode=mandatory_extended-goal_no_jump=True` | desc | 20,000 | 695.1 | 192.4 | 834.0 | 139.8 | 77.7 | 77.7 | 140.6 | 137.4 | 23.3 | 0.0000 | 0.0000 | 0.0000 | 2.4468 | 1.7621 | 1.5282 | 0.2540 | 41.6 | 0.2449 |
| `ex4/4s4p/random/cold_start=free_entry` | desc | 20,000 | 588.8 | 163.2 | 706.6 | 117.5 | 104.9 | 104.9 | 8.4340 | 9.2257 | 25.6 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7106 | 1.3836 | 0.2369 | 53.2 | 0.3129 |
| `ex4/4s4p/random/cold_start=free_entry-goal_no_jump=True` | desc | 20,000 | 630.7 | 174.8 | 756.8 | 126.2 | 110.1 | 110.1 | 18.1 | 9.4724 | 26.7 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.6726 | 1.3771 | 0.2242 | 46.5 | 0.2735 |
| `ex4/4s4p/random/cold_start=strict` | desc | 20,000 | 456.5 | 126.8 | 547.9 | 91.7 | 41.3 | 41.3 | 85.0 | 81.8 | 14.4 | 4.9136 | 0.0000 | 0.0000 | 0.0000 | 1.7792 | 1.4850 | 0.2597 | 41.4 | 0.2437 |
| `ex4/4s4p/random/cold_start=strict-dreimal_wuerfeln=True` | desc | 20,000 | 442.9 | 122.6 | 601.3 | 89.7 | 48.5 | 48.5 | 39.8 | 38.1 | 17.6 | 1.3752 | 0.0000 | 0.0000 | 0.0000 | 1.7321 | 1.4415 | 0.2440 | 39.9 | 0.2349 |
| `ex4/4s4p/random/cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | desc | 20,000 | 466.2 | 128.8 | 630.3 | 95.1 | 50.1 | 50.1 | 48.6 | 38.6 | 18.5 | 1.3739 | 0.0000 | 0.0000 | 0.0000 | 1.7351 | 1.4790 | 0.2450 | 34.0 | 0.1998 |
| `ex4/4s4p/random/cold_start=strict-goal_no_jump=True` | desc | 20,000 | 483.3 | 134.0 | 580.1 | 97.7 | 43.0 | 43.0 | 96.2 | 83.5 | 15.0 | 5.0274 | 0.0000 | 0.0000 | 0.0000 | 1.7578 | 1.5058 | 0.2526 | 35.4 | 0.2080 |
| `ex4/4s4p/random/dreimal_wuerfeln=True` | desc | 20,000 | 437.2 | 121.1 | 577.1 | 88.3 | 48.6 | 48.6 | 34.2 | 28.6 | 18.7 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7303 | 1.4373 | 0.2434 | 40.0 | 0.2354 |
| `ex4/4s4p/random/dreimal_wuerfeln=True-goal_no_jump=True` | desc | 20,000 | 460.9 | 127.5 | 606.6 | 93.5 | 50.2 | 50.2 | 43.1 | 29.3 | 19.4 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7169 | 1.4511 | 0.2390 | 34.6 | 0.2033 |
| `ex4/4s4p/random/goal_no_jump=True` | desc | 20,000 | 464.6 | 129.2 | 557.7 | 93.4 | 43.4 | 43.4 | 77.5 | 60.9 | 18.0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7347 | 1.4914 | 0.2449 | 34.6 | 0.2038 |
| `ex5/2p/adjacent/random` | desc | 20,000 | 117.7 | 59.1 | 141.3 | 59.1 | 5.7062 | 5.7062 | 9.2327 | 5.6785 | 6.9374 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3126 | 1.2163 | 0.3125 | 42.1 | 0.2479 |
| `ex5/2p/adjacent/spread` | desc | 20,000 | 120.5 | 60.5 | 144.6 | 60.5 | 5.2938 | 5.2938 | 8.9152 | 5.2847 | 6.7642 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.2945 | 1.1880 | 0.2945 | 39.5 | 0.2322 |
| `ex5/2p/opposite/random` | desc | 20,000 | 117.9 | 59.2 | 141.5 | 59.2 | 5.5080 | 5.5080 | 8.4794 | 4.8580 | 7.3328 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3259 | 1.2205 | 0.3259 | 40.2 | 0.2367 |
| `ex5/2p/opposite/spread` | desc | 20,000 | 120.1 | 60.3 | 144.0 | 60.3 | 4.5168 | 4.5168 | 7.9077 | 4.2428 | 8.0298 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3606 | 1.2497 | 0.3607 | 29.7 | 0.1749 |
| `ex5/3p/4s-adjacent/random` | conf | 250,002 | 250.1 | 89.1 | 300.1 | 72.4 | 19.1 | 19.1 | 29.0 | 22.6 | 12.4 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5593 | 1.3627 | 0.2796 | 40.1 | 0.2358 |
| `ex5/3p/4s-adjacent/spread` | conf | 250,002 | 316.5 | 113.4 | 379.9 | 90.3 | 26.4 | 26.4 | 33.2 | 25.6 | 14.8 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.6653 | 1.3731 | 0.3326 | 50.2 | 0.2951 |
| `ex5/3p/6s-adjacent/random` | conf | 250,002 | 289.8 | 103.1 | 347.8 | 84.1 | 21.4 | 21.4 | 26.1 | 20.2 | 12.9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5538 | 1.3469 | 0.2769 | 48.5 | 0.2399 |
| `ex5/3p/6s-adjacent/spread` | conf | 250,002 | 349.7 | 125.5 | 419.6 | 99.3 | 26.7 | 26.7 | 28.0 | 21.1 | 13.6 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.6606 | 1.3509 | 0.3303 | 60.7 | 0.3007 |
| `ex5/3p/6s-spread/random` | conf | 250,002 | 296.3 | 105.3 | 355.6 | 86.2 | 21.5 | 21.5 | 23.8 | 17.6 | 13.7 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5554 | 1.3478 | 0.2777 | 48.5 | 0.2401 |
| `ex5/3p/6s-spread/spread` | conf | 250,002 | 375.9 | 134.3 | 451.0 | 107.8 | 28.4 | 28.4 | 26.3 | 19.1 | 17.1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7020 | 1.3830 | 0.3510 | 59.3 | 0.2935 |
| `ex6a/4s4p/focus_front/mandatory` | desc | 20,000 | 411.0 | 114.8 | 493.2 | 81.5 | 39.0 | 39.0 | 78.2 | 70.5 | 14.6 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7523 | 1.5154 | 0.2507 | 38.5 | 0.2262 |
| `ex6a/4s4p/focus_front/mandatory_extended` | desc | 20,000 | 449.1 | 125.4 | 538.8 | 88.8 | 43.4 | 43.4 | 86.4 | 79.7 | 15.8 | 0.0000 | 0.0000 | 0.0000 | 1.1199 | 1.7839 | 1.5458 | 0.2613 | 39.1 | 0.2297 |
| `ex6a/4s4p/focus_front/optional` | desc | 20,000 | 314.9 | 88.4 | 377.9 | 62.4 | 24.3 | 24.3 | 51.1 | 41.0 | 13.1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7419 | 1.4956 | 0.2473 | 32.0 | 0.1881 |
| `ex6a/4s4p/focus_rear/mandatory` | desc | 20,000 | 725.9 | 201.9 | 871.0 | 143.2 | 84.7 | 84.7 | 136.5 | 133.9 | 24.9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.8169 | 1.5264 | 0.2723 | 53.0 | 0.3115 |
| `ex6a/4s4p/focus_rear/mandatory_extended` | desc | 20,000 | 887.8 | 246.2 | 1,065 | 176.1 | 106.2 | 106.2 | 166.6 | 168.6 | 29.2 | 0.0000 | 0.0000 | 0.0000 | 3.0222 | 1.8415 | 1.5733 | 0.2805 | 53.1 | 0.3123 |
| `ex6a/4s4p/focus_rear/optional` | desc | 20,000 | 589.8 | 164.5 | 708.0 | 116.2 | 61.8 | 61.8 | 82.9 | 73.5 | 22.3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.8340 | 1.5014 | 0.2780 | 50.4 | 0.2966 |
| `ex6a/4s4p/greedy_capture/mandatory` | desc | 20,000 | 570.1 | 158.5 | 684.2 | 113.5 | 63.1 | 63.1 | 111.0 | 110.2 | 19.9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7685 | 1.5052 | 0.2562 | 46.3 | 0.2722 |
| `ex6a/4s4p/greedy_capture/mandatory_extended` | desc | 20,000 | 660.4 | 183.2 | 792.4 | 131.6 | 74.6 | 74.6 | 129.0 | 131.5 | 22.3 | 0.0000 | 0.0000 | 0.0000 | 2.1232 | 1.7812 | 1.5257 | 0.2604 | 46.4 | 0.2729 |
| `ex6a/4s4p/greedy_capture/optional` | desc | 20,000 | 570.0 | 158.5 | 684.0 | 113.4 | 63.1 | 63.1 | 111.2 | 110.3 | 20.0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7691 | 1.5081 | 0.2563 | 46.0 | 0.2706 |
| `ex6a/4s4p/random/mandatory` | desc | 20,000 | 571.0 | 158.8 | 685.2 | 113.4 | 63.1 | 63.1 | 111.5 | 110.6 | 19.9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7717 | 1.5094 | 0.2572 | 46.2 | 0.2718 |
| `ex6a/4s4p/random/mandatory_extended` | desc | 20,000 | 662.4 | 183.7 | 795.0 | 132.1 | 75.0 | 75.0 | 129.4 | 132.0 | 22.4 | 0.0000 | 0.0000 | 0.0000 | 2.1521 | 1.7855 | 1.5425 | 0.2618 | 46.1 | 0.2714 |
| `ex6a/4s4p/random/optional` | desc | 20,000 | 438.6 | 122.4 | 526.3 | 87.2 | 41.7 | 41.7 | 66.3 | 59.2 | 17.3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7597 | 1.4716 | 0.2532 | 41.4 | 0.2432 |
| `ex6a/4s4p/spread/mandatory` | desc | 20,000 | 772.9 | 215.6 | 927.6 | 151.4 | 91.4 | 91.4 | 144.2 | 142.9 | 26.1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.8300 | 1.5210 | 0.2767 | 55.6 | 0.3270 |
| `ex6a/4s4p/spread/mandatory_extended` | desc | 20,000 | 935.9 | 260.3 | 1,123 | 184.0 | 113.0 | 113.0 | 174.3 | 177.7 | 30.2 | 0.0000 | 0.0000 | 0.0000 | 3.0406 | 1.8581 | 1.5565 | 0.2860 | 56.0 | 0.3292 |
| `ex6a/4s4p/spread/optional` | desc | 20,000 | 624.1 | 174.5 | 748.7 | 122.2 | 65.9 | 65.9 | 86.1 | 77.0 | 23.3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.8731 | 1.4968 | 0.2910 | 52.8 | 0.3105 |
| `ex6b/4s4p/focus_front-vs-random/mandatory` | conf | 400,000 | 528.2 | 148.1 | 633.8 | 102.8 | 56.7 | 56.7 | 102.8 | 100.1 | 17.8 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7306 | 1.4690 | 0.2435 | 47.0 | 0.2763 |
| `ex6b/4s4p/focus_front-vs-random/mandatory_extended` | conf | 400,000 | 603.9 | 169.1 | 724.7 | 117.6 | 66.3 | 66.3 | 117.9 | 117.7 | 19.6 | 0.0000 | 0.0000 | 0.0000 | 1.9302 | 1.7490 | 1.5009 | 0.2497 | 46.8 | 0.2756 |
| `ex6b/4s4p/focus_front-vs-random/optional` | conf | 400,000 | 402.4 | 113.5 | 482.9 | 77.8 | 36.7 | 36.7 | 61.7 | 53.7 | 15.1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7000 | 1.4265 | 0.2333 | 42.4 | 0.2495 |
| `ex6b/4s4p/focus_rear-vs-random/mandatory` | desc | 20,000 | 604.4 | 168.7 | 725.2 | 119.1 | 68.0 | 68.0 | 116.9 | 115.8 | 20.7 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7757 | 1.5090 | 0.2586 | 47.9 | 0.2819 |
| `ex6b/4s4p/focus_rear-vs-random/mandatory_extended` | desc | 20,000 | 707.9 | 197.2 | 849.5 | 139.8 | 81.4 | 81.4 | 137.0 | 139.6 | 23.4 | 0.0000 | 0.0000 | 0.0000 | 2.4187 | 1.7900 | 1.5280 | 0.2633 | 48.6 | 0.2857 |
| `ex6b/4s4p/focus_rear-vs-random/optional` | desc | 20,000 | 466.6 | 130.7 | 560.0 | 91.8 | 45.6 | 45.6 | 68.5 | 61.2 | 17.9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7603 | 1.4652 | 0.2534 | 43.7 | 0.2572 |
| `ex6b/4s4p/greedy_capture-vs-random/mandatory` | desc | 20,000 | 570.9 | 158.8 | 685.0 | 113.4 | 63.1 | 63.1 | 111.3 | 110.6 | 19.9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7658 | 1.5022 | 0.2553 | 46.3 | 0.2723 |
| `ex6b/4s4p/greedy_capture-vs-random/mandatory_extended` | desc | 20,000 | 661.2 | 183.3 | 793.5 | 132.0 | 74.8 | 74.8 | 129.1 | 131.5 | 22.4 | 0.0000 | 0.0000 | 0.0000 | 2.1519 | 1.7888 | 1.5488 | 0.2629 | 45.8 | 0.2692 |
| `ex6b/4s4p/greedy_capture-vs-random/optional` | desc | 20,000 | 472.9 | 131.7 | 567.5 | 94.2 | 47.5 | 47.5 | 77.4 | 71.9 | 18.0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7506 | 1.4828 | 0.2502 | 42.8 | 0.2519 |
| `ex6b/4s4p/spread-vs-random/mandatory` | conf | 400,000 | 610.3 | 170.9 | 732.3 | 119.3 | 68.8 | 68.8 | 118.0 | 117.2 | 20.6 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7561 | 1.4790 | 0.2520 | 49.2 | 0.2896 |
| `ex6b/4s4p/spread-vs-random/mandatory_extended` | conf | 400,000 | 718.5 | 200.9 | 862.2 | 140.6 | 82.9 | 82.9 | 138.8 | 141.8 | 23.4 | 0.0000 | 0.0000 | 0.0000 | 2.4587 | 1.7734 | 1.5088 | 0.2578 | 49.2 | 0.2894 |
| `ex6b/4s4p/spread-vs-random/optional` | conf | 400,000 | 471.0 | 132.3 | 565.2 | 92.2 | 46.1 | 46.1 | 69.2 | 61.8 | 18.0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7605 | 1.4523 | 0.2535 | 44.6 | 0.2625 |
| `ex6c/4s4p/focus_front/barriers=False` | desc | 20,000 | 315.4 | 88.5 | 378.4 | 62.5 | 24.4 | 24.4 | 51.1 | 41.0 | 13.3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7329 | 1.4935 | 0.2443 | 32.1 | 0.1887 |
| `ex6c/4s4p/focus_front/barriers=True` | desc | 20,000 | 321.0 | 89.9 | 385.2 | 63.9 | 25.0 | 25.0 | 52.7 | 41.4 | 13.2 | 0.0000 | 2.1738 | 24.3 | 0.0000 | 1.7423 | 1.4917 | 0.2474 | 32.2 | 0.1895 |
| `ex6c/4s4p/focus_rear/barriers=False` | desc | 20,000 | 590.9 | 164.7 | 709.1 | 116.6 | 61.9 | 61.9 | 83.0 | 73.8 | 22.4 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.8473 | 1.5132 | 0.2824 | 50.2 | 0.2951 |
| `ex6c/4s4p/focus_rear/barriers=True` | desc | 20,000 | 457.4 | 127.1 | 548.7 | 91.3 | 38.3 | 38.3 | 80.5 | 54.8 | 16.6 | 0.0000 | 27.8 | 243.5 | 0.0000 | 1.8661 | 1.5785 | 0.2887 | 37.9 | 0.2228 |
| `ex6c/4s4p/greedy_capture/barriers=False` | desc | 20,000 | 571.4 | 158.9 | 685.7 | 113.5 | 63.3 | 63.3 | 111.4 | 110.6 | 20.0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7674 | 1.5044 | 0.2558 | 46.8 | 0.2754 |
| `ex6c/4s4p/greedy_capture/barriers=True` | desc | 20,000 | 567.4 | 157.8 | 680.6 | 112.8 | 61.9 | 61.9 | 110.5 | 107.6 | 19.8 | 0.0000 | 11.5 | 62.4 | 0.0000 | 1.7892 | 1.5186 | 0.2630 | 45.9 | 0.2702 |
| `ex6c/4s4p/random/barriers=False` | desc | 20,000 | 438.6 | 122.3 | 526.4 | 87.4 | 41.7 | 41.7 | 65.9 | 58.8 | 17.3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7549 | 1.4701 | 0.2516 | 41.1 | 0.2415 |
| `ex6c/4s4p/random/barriers=True` | desc | 20,000 | 431.6 | 120.4 | 517.8 | 85.9 | 40.0 | 40.0 | 64.8 | 56.0 | 17.0 | 0.0000 | 10.8 | 59.2 | 0.0000 | 1.7641 | 1.4837 | 0.2547 | 40.4 | 0.2378 |
| `ex6c/4s4p/spread/barriers=False` | desc | 20,000 | 620.8 | 173.6 | 744.7 | 121.3 | 65.3 | 65.3 | 85.7 | 76.6 | 23.2 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.8887 | 1.5055 | 0.2962 | 52.9 | 0.3112 |
| `ex6c/4s4p/spread/barriers=True` | desc | 20,000 | 557.1 | 155.8 | 668.5 | 109.2 | 53.2 | 53.2 | 83.6 | 64.6 | 20.6 | 0.0000 | 54.9 | 233.8 | 0.0000 | 1.8839 | 1.5120 | 0.2946 | 47.1 | 0.2769 |
| `ex6d/4s4p/focus_front-vs-random/barriers=False` | conf | 400,000 | 402.6 | 113.5 | 483.0 | 77.9 | 36.7 | 36.7 | 61.7 | 53.7 | 15.1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.6973 | 1.4268 | 0.2324 | 42.5 | 0.2500 |
| `ex6d/4s4p/focus_front-vs-random/barriers=True` | conf | 400,000 | 400.4 | 112.8 | 480.4 | 77.6 | 35.8 | 35.8 | 61.4 | 51.8 | 15.0 | 0.0000 | 8.4144 | 49.3 | 0.0000 | 1.7030 | 1.4292 | 0.2343 | 41.8 | 0.2462 |
| `ex6d/4s4p/focus_rear-vs-random/barriers=False` | desc | 20,000 | 467.1 | 130.9 | 560.4 | 91.9 | 45.5 | 45.5 | 69.2 | 61.8 | 18.0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7539 | 1.4652 | 0.2513 | 43.6 | 0.2562 |
| `ex6d/4s4p/focus_rear-vs-random/barriers=True` | desc | 20,000 | 439.2 | 122.5 | 527.1 | 87.2 | 39.8 | 39.8 | 68.5 | 55.2 | 16.7 | 0.0000 | 15.1 | 113.1 | 0.0000 | 1.7862 | 1.5043 | 0.2621 | 40.6 | 0.2389 |
| `ex6d/4s4p/greedy_capture-vs-random/barriers=False` | desc | 20,000 | 472.7 | 131.7 | 567.3 | 94.1 | 47.5 | 47.5 | 77.4 | 71.9 | 17.9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7545 | 1.4795 | 0.2515 | 43.2 | 0.2539 |
| `ex6d/4s4p/greedy_capture-vs-random/barriers=True` | desc | 20,000 | 466.7 | 130.0 | 560.0 | 92.9 | 45.9 | 45.9 | 76.0 | 68.6 | 17.7 | 0.0000 | 10.9 | 59.9 | 0.0000 | 1.7674 | 1.4844 | 0.2558 | 42.5 | 0.2500 |
| `ex6d/4s4p/spread-vs-random/barriers=False` | conf | 400,000 | 470.4 | 132.1 | 564.5 | 92.1 | 46.0 | 46.0 | 69.2 | 61.8 | 18.0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7601 | 1.4532 | 0.2534 | 44.5 | 0.2617 |
| `ex6d/4s4p/spread-vs-random/barriers=True` | conf | 400,000 | 459.7 | 128.9 | 551.6 | 90.2 | 42.9 | 42.9 | 69.2 | 57.8 | 17.6 | 0.0000 | 20.9 | 103.9 | 0.0000 | 1.7850 | 1.4712 | 0.2617 | 42.8 | 0.2518 |
| `ex6e/6s2p/random/mandatory` | conf | 400,000 | 161.0 | 80.7 | 193.2 | 80.7 | 10.9 | 10.9 | 13.7 | 10.6 | 7.4650 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3176 | 1.2169 | 0.3176 | 62.2 | 0.3079 |
| `ex6e/6s2p/random/mandatory_extended` | desc | 20,000 | 174.7 | 87.6 | 209.6 | 87.6 | 12.2 | 12.2 | 14.7 | 11.8 | 7.8446 | 0.0000 | 0.0000 | 0.0000 | 0.4802 | 1.3241 | 1.2282 | 0.3241 | 63.3 | 0.3134 |
| `ex6e/6s2p/random/optional` | conf | 400,000 | 136.7 | 68.6 | 164.0 | 68.6 | 6.3461 | 6.3461 | 8.3367 | 5.0857 | 7.3691 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3050 | 1.2019 | 0.3050 | 50.9 | 0.2518 |
| `ex6e/6s3p/random/mandatory` | desc | 20,001 | 373.4 | 132.9 | 448.1 | 108.0 | 35.2 | 35.2 | 48.2 | 44.6 | 14.2 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5624 | 1.3757 | 0.2812 | 56.6 | 0.2802 |
| `ex6e/6s3p/random/mandatory_extended` | desc | 20,001 | 420.0 | 149.4 | 503.9 | 121.7 | 40.5 | 40.5 | 54.4 | 51.8 | 15.5 | 0.0000 | 0.0000 | 0.0000 | 1.1932 | 1.5798 | 1.3944 | 0.2899 | 57.1 | 0.2826 |
| `ex6e/6s3p/random/optional` | desc | 20,001 | 289.8 | 103.1 | 347.8 | 84.1 | 21.5 | 21.5 | 26.2 | 20.3 | 13.0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5458 | 1.3429 | 0.2729 | 48.8 | 0.2417 |
| `ex6e/6s4p/random/mandatory` | desc | 20,000 | 696.4 | 193.3 | 835.6 | 138.9 | 76.8 | 76.8 | 113.8 | 114.8 | 21.3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7591 | 1.4946 | 0.2530 | 57.0 | 0.2820 |
| `ex6e/6s4p/random/mandatory_extended` | desc | 20,000 | 798.2 | 220.8 | 957.7 | 159.9 | 89.5 | 89.5 | 130.7 | 134.7 | 23.9 | 0.0000 | 0.0000 | 0.0000 | 2.0027 | 1.7778 | 1.5220 | 0.2593 | 56.7 | 0.2806 |
| `ex6e/6s4p/random/optional` | desc | 20,000 | 516.3 | 143.9 | 619.5 | 103.0 | 47.9 | 47.9 | 60.5 | 53.9 | 18.3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7591 | 1.4627 | 0.2530 | 50.1 | 0.2481 |
| `ex6e/6s6p/random/mandatory` | conf | 400,002 | 1,739 | 335.5 | 2,087 | 205.6 | 224.7 | 224.7 | 383.7 | 419.7 | 36.0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.0887 | 1.6500 | 0.2177 | 60.1 | 0.2976 |
| `ex6e/6s6p/random/mandatory_extended` | desc | 20,004 | 2,039 | 391.4 | 2,446 | 242.1 | 265.6 | 265.6 | 451.0 | 500.4 | 41.1 | 0.0000 | 0.0000 | 0.0000 | 3.9757 | 2.1308 | 1.6913 | 0.2262 | 59.0 | 0.2922 |
| `ex6e/6s6p/random/optional` | conf | 400,002 | 1,241 | 241.4 | 1,489 | 147.0 | 145.3 | 145.3 | 211.3 | 217.5 | 29.1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.0656 | 1.6153 | 0.2131 | 54.7 | 0.2709 |
| `ex6f/6s2p/focus_front-vs-random/mandatory` | desc | 20,000 | 150.2 | 75.3 | 180.2 | 75.3 | 9.6636 | 9.6636 | 13.8 | 10.4 | 6.8235 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.2980 | 1.2030 | 0.2980 | 63.4 | 0.3138 |
| `ex6f/6s2p/focus_front-vs-random/mandatory_extended` | desc | 20,000 | 160.1 | 80.3 | 192.3 | 80.3 | 10.6 | 10.6 | 14.6 | 11.3 | 7.0986 | 0.0000 | 0.0000 | 0.0000 | 0.3588 | 1.3024 | 1.2066 | 0.3024 | 64.3 | 0.3185 |
| `ex6f/6s2p/focus_front-vs-random/optional` | desc | 20,000 | 128.6 | 64.5 | 154.3 | 64.5 | 5.7638 | 5.7638 | 8.3917 | 5.1828 | 6.7183 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.2746 | 1.1765 | 0.2746 | 56.3 | 0.2789 |
| `ex6f/6s2p/focus_rear-vs-random/mandatory` | desc | 20,000 | 168.5 | 84.5 | 202.2 | 84.5 | 11.5 | 11.5 | 13.8 | 10.5 | 7.6521 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3101 | 1.1946 | 0.3101 | 69.8 | 0.3455 |
| `ex6f/6s2p/focus_rear-vs-random/mandatory_extended` | desc | 20,000 | 186.3 | 93.4 | 223.6 | 93.4 | 13.3 | 13.3 | 15.2 | 12.2 | 8.1186 | 0.0000 | 0.0000 | 0.0000 | 0.5292 | 1.3265 | 1.2048 | 0.3266 | 71.9 | 0.3558 |
| `ex6f/6s2p/focus_rear-vs-random/optional` | desc | 20,000 | 140.7 | 70.6 | 168.8 | 70.6 | 6.7018 | 6.7018 | 8.4461 | 5.0142 | 7.3675 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3013 | 1.1835 | 0.3013 | 55.1 | 0.2728 |
| `ex6f/6s2p/greedy_capture-vs-random/mandatory` | desc | 20,000 | 161.1 | 80.8 | 193.3 | 80.8 | 10.9 | 10.9 | 13.8 | 10.7 | 7.4718 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3185 | 1.2171 | 0.3185 | 62.7 | 0.3104 |
| `ex6f/6s2p/greedy_capture-vs-random/mandatory_extended` | desc | 20,000 | 174.2 | 87.4 | 209.1 | 87.4 | 12.2 | 12.2 | 14.7 | 11.9 | 7.8351 | 0.0000 | 0.0000 | 0.0000 | 0.4810 | 1.3236 | 1.2225 | 0.3236 | 63.4 | 0.3140 |
| `ex6f/6s2p/greedy_capture-vs-random/optional` | desc | 20,000 | 147.0 | 73.8 | 176.4 | 73.8 | 8.7149 | 8.7149 | 10.7 | 7.5560 | 7.0770 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.2706 | 1.1761 | 0.2706 | 63.0 | 0.3117 |
| `ex6f/6s2p/spread-vs-random/mandatory` | desc | 20,000 | 170.7 | 85.6 | 204.8 | 85.6 | 11.8 | 11.8 | 13.9 | 10.8 | 7.6858 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3056 | 1.1842 | 0.3056 | 72.7 | 0.3601 |
| `ex6f/6s2p/spread-vs-random/mandatory_extended` | desc | 20,000 | 189.5 | 95.0 | 227.4 | 95.0 | 13.6 | 13.6 | 15.4 | 12.6 | 8.0566 | 0.0000 | 0.0000 | 0.0000 | 0.5607 | 1.3124 | 1.1851 | 0.3124 | 76.5 | 0.3787 |
| `ex6f/6s2p/spread-vs-random/optional` | desc | 20,000 | 139.6 | 70.0 | 167.5 | 70.0 | 6.5037 | 6.5037 | 8.3195 | 5.0248 | 7.2796 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3015 | 1.1807 | 0.3015 | 56.5 | 0.2795 |
| `ex6f/6s3p/focus_front-vs-random/mandatory` | desc | 20,007 | 343.6 | 123.1 | 412.5 | 97.8 | 31.2 | 31.2 | 45.6 | 40.9 | 12.7 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5293 | 1.3416 | 0.2646 | 57.7 | 0.2855 |
| `ex6f/6s3p/focus_front-vs-random/mandatory_extended` | desc | 20,007 | 380.1 | 136.2 | 456.1 | 108.2 | 35.2 | 35.2 | 50.3 | 46.4 | 13.5 | 0.0000 | 0.0000 | 0.0000 | 1.0071 | 1.5402 | 1.3619 | 0.2701 | 58.4 | 0.2889 |
| `ex6f/6s3p/focus_front-vs-random/optional` | desc | 20,007 | 266.8 | 95.7 | 320.2 | 75.8 | 18.8 | 18.8 | 25.4 | 19.2 | 11.3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.4891 | 1.2950 | 0.2446 | 51.3 | 0.2538 |
| `ex6f/6s3p/focus_rear-vs-random/mandatory` | desc | 20,007 | 399.8 | 143.0 | 479.8 | 114.2 | 38.3 | 38.3 | 50.5 | 46.6 | 14.7 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5643 | 1.3571 | 0.2821 | 61.7 | 0.3056 |
| `ex6f/6s3p/focus_rear-vs-random/mandatory_extended` | desc | 20,007 | 457.8 | 163.6 | 549.4 | 131.0 | 45.2 | 45.2 | 57.6 | 55.0 | 16.3 | 0.0000 | 0.0000 | 0.0000 | 1.3526 | 1.5876 | 1.3832 | 0.2938 | 62.6 | 0.3099 |
| `ex6f/6s3p/focus_rear-vs-random/optional` | desc | 20,007 | 307.9 | 110.1 | 369.5 | 88.3 | 23.4 | 23.4 | 26.9 | 20.6 | 13.2 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5786 | 1.3425 | 0.2893 | 53.8 | 0.2663 |
| `ex6f/6s3p/greedy_capture-vs-random/mandatory` | desc | 20,007 | 374.7 | 133.4 | 449.7 | 108.4 | 35.3 | 35.3 | 48.5 | 44.9 | 14.4 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5653 | 1.3743 | 0.2827 | 56.5 | 0.2798 |
| `ex6f/6s3p/greedy_capture-vs-random/mandatory_extended` | desc | 20,007 | 419.1 | 149.1 | 502.7 | 121.5 | 40.3 | 40.3 | 54.2 | 51.6 | 15.5 | 0.0000 | 0.0000 | 0.0000 | 1.1838 | 1.5820 | 1.4018 | 0.2910 | 56.6 | 0.2800 |
| `ex6f/6s3p/greedy_capture-vs-random/optional` | desc | 20,007 | 319.4 | 113.8 | 383.3 | 92.3 | 26.5 | 26.5 | 33.4 | 28.0 | 13.2 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5357 | 1.3366 | 0.2678 | 53.9 | 0.2671 |
| `ex6f/6s3p/spread-vs-random/mandatory` | desc | 20,007 | 405.6 | 145.5 | 486.8 | 115.2 | 39.1 | 39.1 | 51.0 | 47.4 | 14.7 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5631 | 1.3474 | 0.2815 | 63.6 | 0.3147 |
| `ex6f/6s3p/spread-vs-random/mandatory_extended` | desc | 20,007 | 465.4 | 167.0 | 558.6 | 131.9 | 46.1 | 46.1 | 58.5 | 56.2 | 16.2 | 0.0000 | 0.0000 | 0.0000 | 1.3829 | 1.5782 | 1.3580 | 0.2891 | 64.6 | 0.3199 |
| `ex6f/6s3p/spread-vs-random/optional` | desc | 20,007 | 309.1 | 110.6 | 370.9 | 88.4 | 23.5 | 23.5 | 26.8 | 20.8 | 13.1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5904 | 1.3286 | 0.2952 | 54.7 | 0.2707 |
| `ex6f/6s4p/focus_front-vs-random/mandatory` | desc | 20,000 | 637.0 | 178.5 | 764.5 | 123.7 | 68.2 | 68.2 | 104.9 | 103.4 | 18.8 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7286 | 1.4557 | 0.2429 | 58.5 | 0.2895 |
| `ex6f/6s4p/focus_front-vs-random/mandatory_extended` | desc | 20,000 | 722.9 | 202.3 | 867.4 | 140.5 | 78.7 | 78.7 | 119.5 | 120.6 | 20.5 | 0.0000 | 0.0000 | 0.0000 | 1.8129 | 1.7322 | 1.4746 | 0.2441 | 58.2 | 0.2879 |
| `ex6f/6s4p/focus_front-vs-random/optional` | desc | 20,000 | 469.3 | 132.5 | 563.2 | 90.3 | 41.8 | 41.8 | 56.1 | 48.6 | 15.6 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.6701 | 1.3867 | 0.2234 | 53.2 | 0.2631 |
| `ex6f/6s4p/focus_rear-vs-random/mandatory` | desc | 20,000 | 743.2 | 207.5 | 891.9 | 146.3 | 83.2 | 83.2 | 119.6 | 120.3 | 22.2 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7616 | 1.4831 | 0.2539 | 60.0 | 0.2969 |
| `ex6f/6s4p/focus_rear-vs-random/mandatory_extended` | desc | 20,000 | 863.5 | 240.9 | 1,036 | 169.4 | 98.1 | 98.1 | 138.8 | 143.1 | 24.8 | 0.0000 | 0.0000 | 0.0000 | 2.2500 | 1.7920 | 1.5071 | 0.2640 | 60.7 | 0.3007 |
| `ex6f/6s4p/focus_rear-vs-random/optional` | desc | 20,000 | 552.8 | 155.0 | 663.4 | 108.5 | 52.6 | 52.6 | 62.6 | 55.8 | 19.0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7595 | 1.4334 | 0.2532 | 54.5 | 0.2696 |
| `ex6f/6s4p/greedy_capture-vs-random/mandatory` | desc | 20,000 | 698.2 | 193.7 | 837.8 | 139.4 | 77.1 | 77.1 | 114.3 | 115.2 | 21.4 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7671 | 1.4955 | 0.2557 | 56.9 | 0.2816 |
| `ex6f/6s4p/greedy_capture-vs-random/mandatory_extended` | desc | 20,000 | 797.4 | 220.8 | 956.7 | 159.2 | 89.3 | 89.3 | 130.2 | 134.3 | 23.7 | 0.0000 | 0.0000 | 0.0000 | 2.0051 | 1.7914 | 1.5226 | 0.2638 | 57.0 | 0.2819 |
| `ex6f/6s4p/greedy_capture-vs-random/optional` | desc | 20,000 | 563.3 | 156.6 | 676.1 | 112.4 | 55.9 | 55.9 | 73.3 | 68.5 | 19.0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7368 | 1.4571 | 0.2456 | 53.2 | 0.2635 |
| `ex6f/6s4p/spread-vs-random/mandatory` | desc | 20,000 | 754.2 | 211.2 | 904.9 | 147.4 | 84.6 | 84.6 | 120.9 | 122.4 | 22.3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7485 | 1.4665 | 0.2495 | 61.6 | 0.3047 |
| `ex6f/6s4p/spread-vs-random/mandatory_extended` | desc | 20,000 | 875.5 | 245.1 | 1,051 | 170.8 | 99.8 | 99.8 | 140.4 | 145.4 | 24.9 | 0.0000 | 0.0000 | 0.0000 | 2.2897 | 1.7764 | 1.4963 | 0.2588 | 61.3 | 0.3035 |
| `ex6f/6s4p/spread-vs-random/optional` | desc | 20,000 | 555.7 | 156.1 | 666.8 | 108.7 | 52.7 | 52.7 | 62.7 | 55.8 | 18.8 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7724 | 1.4336 | 0.2574 | 54.6 | 0.2703 |
| `ex6f/6s6p/focus_front-vs-random/mandatory` | desc | 20,016 | 1,601 | 312.7 | 1,921 | 182.5 | 203.4 | 203.4 | 351.9 | 380.5 | 31.7 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.0457 | 1.6008 | 0.2091 | 60.6 | 0.2999 |
| `ex6f/6s6p/focus_front-vs-random/mandatory_extended` | desc | 20,016 | 1,869 | 363.6 | 2,243 | 213.7 | 239.8 | 239.8 | 412.0 | 452.5 | 35.6 | 0.0000 | 0.0000 | 0.0000 | 3.7780 | 2.0547 | 1.6433 | 0.2109 | 59.4 | 0.2942 |
| `ex6f/6s6p/focus_front-vs-random/optional` | desc | 20,016 | 1,129 | 223.3 | 1,355 | 126.9 | 128.8 | 128.8 | 192.6 | 194.7 | 24.6 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.9734 | 1.5378 | 0.1947 | 56.6 | 0.2803 |
| `ex6f/6s6p/focus_rear-vs-random/mandatory` | desc | 20,016 | 1,823 | 353.9 | 2,188 | 212.7 | 237.0 | 237.0 | 399.0 | 436.4 | 37.1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.0890 | 1.6390 | 0.2178 | 61.9 | 0.3065 |
| `ex6f/6s6p/focus_rear-vs-random/mandatory_extended` | desc | 20,016 | 2,150 | 415.5 | 2,580 | 252.3 | 281.7 | 281.7 | 472.8 | 524.5 | 42.8 | 0.0000 | 0.0000 | 0.0000 | 4.2250 | 2.1027 | 1.6759 | 0.2205 | 60.4 | 0.2992 |
| `ex6f/6s6p/focus_rear-vs-random/optional` | desc | 20,016 | 1,317 | 257.7 | 1,580 | 153.4 | 155.9 | 155.9 | 220.9 | 227.4 | 30.1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.0398 | 1.6045 | 0.2080 | 57.4 | 0.2840 |
| `ex6f/6s6p/greedy_capture-vs-random/mandatory` | desc | 20,016 | 1,737 | 335.1 | 2,084 | 205.3 | 224.5 | 224.5 | 382.9 | 418.9 | 36.0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.0819 | 1.6495 | 0.2164 | 60.3 | 0.2985 |
| `ex6f/6s6p/greedy_capture-vs-random/mandatory_extended` | desc | 20,016 | 2,046 | 392.4 | 2,455 | 243.5 | 266.7 | 266.7 | 452.7 | 502.3 | 41.4 | 0.0000 | 0.0000 | 0.0000 | 4.0053 | 2.1308 | 1.7006 | 0.2262 | 59.0 | 0.2920 |
| `ex6f/6s6p/greedy_capture-vs-random/optional` | desc | 20,016 | 1,326 | 257.3 | 1,592 | 157.0 | 159.1 | 159.1 | 239.9 | 250.8 | 30.2 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.0602 | 1.6160 | 0.2120 | 56.4 | 0.2790 |
| `ex6f/6s6p/spread-vs-random/mandatory` | desc | 20,016 | 1,833 | 356.6 | 2,199 | 213.3 | 238.4 | 238.4 | 400.5 | 438.3 | 37.1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.0754 | 1.6287 | 0.2151 | 61.5 | 0.3047 |
| `ex6f/6s6p/spread-vs-random/mandatory_extended` | desc | 20,016 | 2,171 | 420.4 | 2,605 | 253.8 | 284.7 | 284.7 | 476.0 | 528.4 | 42.8 | 0.0000 | 0.0000 | 0.0000 | 4.2969 | 2.1232 | 1.6820 | 0.2246 | 60.4 | 0.2990 |
| `ex6f/6s6p/spread-vs-random/optional` | desc | 20,016 | 1,317 | 258.2 | 1,580 | 153.2 | 155.7 | 155.7 | 220.1 | 226.8 | 30.0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.0521 | 1.5925 | 0.2104 | 57.2 | 0.2830 |

---

Generated by `madnlab report`. Every number is reproducible from the master seeds in `campaigns/*.json` and the analysis seed above (NF-6, NF-7).

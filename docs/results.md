# MadnLab results

Measured effects of the optional rules and movement strategies of *Mensch ärgere Dich nicht*, against the pre-registration frozen at `prereg-v1`.

| | |
|---|---|
| Pre-registration | `prereg-v1` |
| Engine | `0.1.0` |
| Campaigns | s0, s0, s0, s0, s0, s0, s0, s0, s0, s0, s0, s0, s0, s0, s1, s1, s1, s1, s1, s1, s1, s1, s1, s2, s2, s2, s2, s2, s2, s3, s3, s3, s3, s3, s3, s4, s4, s5, s5, s6, s6, s7, s7 |
| Cells | 533 |
| Games | 99,690,710 |
| Analysis seed | `20260801` |
| Bootstrap resamples | 1,000 |

## 1. Reading this document

Sections 2 and 3 are **confirmatory**: 40 hypotheses fixed in §6.4 before any campaign ran, Holm-corrected within each family. Sections 4 to 6 are **descriptive** — computed, published, and explicitly not error-controlled. §14.4 requires every §6.2 metric of every cell to appear whether or not anything depends on it, which is why section 6 is long and unselective.

Game outcomes: **0 abandoned**, **0 stalemated** out of 99,690,710. Both are measured outcomes of the rule set (D-69, D-70), not errors; no estimand is published from a cell with a non-negligible rate without saying so.

## 2. Confirmatory results

### RQ-1

8 tests, Holm-corrected within the family at alpha = 0.05.

| Contrast | Estimate | 95% CI | p | Holm alpha | Verdict |
|---|---:|---|---:|---:|---|
| CV ratio rounds_to_first_win :: mandatory-optional | 1.1641 | [1.1595, 1.1690] | &lt;1e-300 | 0.00625 | **rejected** |
| lead changes per turn :: mandatory-optional | -0.0057 | [-0.0059, -0.0056] | &lt;1e-300 | 0.00714 | **rejected** |
| comeback rate :: mandatory-optional | 0.0057 | [0.0035, 0.0080] | 6.96e-07 | 0.02500 | **rejected** |
| leader-at-50% wins :: mandatory-optional | -0.0018 | [-0.0046, 0.0010] | 0.2070 | 0.05000 | not rejected |
| CV ratio rounds_to_first_win :: mandatory_extended-optional | 1.2313 | [1.2261, 1.2362] | &lt;1e-300 | 0.00833 | **rejected** |
| lead changes per turn :: mandatory_extended-optional | -0.0072 | [-0.0073, -0.0071] | &lt;1e-300 | 0.01000 | **rejected** |
| comeback rate :: mandatory_extended-optional | 0.0157 | [0.0134, 0.0180] | &lt;1e-300 | 0.01250 | **rejected** |
| leader-at-50% wins :: mandatory_extended-optional | -0.0095 | [-0.0122, -0.0067] | 2.06e-11 | 0.01667 | **rejected** |

**7 of 8 rejected** after Holm correction.

### RQ-2

18 tests, Holm-corrected within the family at alpha = 0.05.

| Contrast | Estimate | 95% CI | p | Holm alpha | Verdict |
|---|---:|---|---:|---:|---|
| win rate by starting seat :: cold_start:strict-one_piece_out | -0.0003 | [-0.0011, 0.0004] | 0.3380 | 0.01000 | not rejected |
| rounds to first win :: cold_start:strict-one_piece_out | 2.1319 | [2.0735, 2.2038] | &lt;1e-300 | 0.00278 | **rejected** |
| win rate by starting seat :: cold_start:free_entry-one_piece_out | -0.0025 | [-0.0035, -0.0015] | 1.05e-06 | 0.00500 | **rejected** |
| rounds to first win :: cold_start:free_entry-one_piece_out | 207.6 | [207.2, 208.0] | &lt;1e-300 | 0.00294 | **rejected** |
| win rate by starting seat :: capture_mode:mandatory-optional | -0.0006 | [-0.0014, 0.0002] | 0.1754 | 0.00714 | not rejected |
| rounds to first win :: capture_mode:mandatory-optional | 64.3 | [64.1, 64.4] | &lt;1e-300 | 0.00313 | **rejected** |
| win rate by starting seat :: capture_mode:mandatory_extended-optional | -0.0010 | [-0.0018, -0.0002] | 0.0122 | 0.00625 | not rejected |
| rounds to first win :: capture_mode:mandatory_extended-optional | 92.2 | [92.1, 92.4] | &lt;1e-300 | 0.00333 | **rejected** |
| win rate by starting seat :: dreimal_wuerfeln:on-off | 0.0002 | [-0.0005, 0.0008] | 0.6138 | 0.01250 | not rejected |
| rounds to first win :: dreimal_wuerfeln:on-off | -69.9 | [-70.1, -69.7] | &lt;1e-300 | 0.00357 | **rejected** |
| win rate by starting seat :: bonus_roll_after_quick_entry:true-false | 0.0004 | [-0.0003, 0.0012] | 0.2349 | 0.00833 | not rejected |
| rounds to first win :: bonus_roll_after_quick_entry:true-false | -45.8 | [-45.9, -45.7] | &lt;1e-300 | 0.00385 | **rejected** |
| win rate by starting seat :: goal_no_jump:true-false | -0.0001 | [-0.0007, 0.0006] | 0.8619 | 0.02500 | not rejected |
| rounds to first win :: goal_no_jump:true-false | 6.9826 | [6.8299, 7.1481] | &lt;1e-300 | 0.00417 | **rejected** |
| win rate by starting seat :: barriers:true-false | 0.0001 | [-0.0006, 0.0007] | 0.8661 | 0.05000 | not rejected |
| rounds to first win :: barriers:true-false | -0.3966 | [-0.5712, -0.2274] | 4.16e-06 | 0.00556 | **rejected** |
| win rate by starting seat :: bonus_roll_forfeited:true-false | 0.0001 | [-0.0005, 0.0008] | 0.6637 | 0.01667 | not rejected |
| rounds to first win :: bonus_roll_forfeited:true-false | 2.1440 | [1.9702, 2.3062] | &lt;1e-300 | 0.00455 | **rejected** |

**10 of 18 rejected** after Holm correction.

### RQ-3

4 tests, Holm-corrected within the family at alpha = 0.05.

| Contrast | Estimate | 95% CI | p | Holm alpha | Verdict |
|---|---:|---|---:|---:|---|
| deviant win rate vs 1/k :: SPREAD | -0.0005 | [-0.0023, 0.0014] | 0.6384 | 0.02500 | not rejected |
| deviant win rate vs 1/k :: FOCUS_FRONT | 0.0013 | [-0.0006, 0.0032] | 0.1664 | 0.01250 | not rejected |
| deviant win rate vs 1/k :: FOCUS_REAR | 0.0002 | [-0.0017, 0.0021] | 0.8203 | 0.05000 | not rejected |
| deviant win rate :: FOCUS_FRONT - FOCUS_REAR | 0.0011 | [-0.0016, 0.0038] | 0.4139 | 0.01667 | not rejected |

**0 of 4 rejected** after Holm correction.

### RQ-4

10 tests, Holm-corrected within the family at alpha = 0.05.

| Contrast | Estimate | 95% CI | p | Holm alpha | Verdict |
|---|---:|---|---:|---:|---|
| deviant edge shift :: capture_mode:mandatory x strategy | 0.0016 | [-0.0003, 0.0035] | 0.1013 | 0.00833 | not rejected |
| deviant edge shift :: capture_mode:mandatory_extended x strategy | 0.0008 | [-0.0011, 0.0027] | 0.4250 | 0.01667 | not rejected |
| deviant edge shift :: barriers x strategy | 0.0012 | [-0.0007, 0.0031] | 0.2117 | 0.01000 | not rejected |
| deviant edge shift :: capture_mode:mandatory x strategy x players | -0.0005 | [-0.0024, 0.0014] | 0.6404 | 0.02500 | not rejected |
| deviant edge shift :: capture_mode:mandatory_extended x strategy x players | -0.0010 | [-0.0029, 0.0009] | 0.3018 | 0.01250 | not rejected |
| deviant edge shift :: barriers x strategy x players | 0.0001 | [-0.0018, 0.0020] | 0.8870 | 0.05000 | not rejected |
| rounds to first win, interaction :: capture_mode x players | -46.5 | [-46.7, -46.2] | &lt;1e-300 | 0.00500 | **rejected** |
| rounds to first win, interaction :: capture_mode x players x board | 9.6372 | [8.9584, 10.3] | &lt;1e-300 | 0.00556 | **rejected** |
| rounds to first win :: EX-5 pattern effect | -2.0068 | [-2.1143, -1.8920] | &lt;1e-300 | 0.00625 | **rejected** |
| rounds to first win :: EX-5 geometry effect | -11.7 | [-11.8, -11.6] | &lt;1e-300 | 0.00714 | **rejected** |

**4 of 10 rejected** after Holm correction.

### RQ-5

8 tests, Holm-corrected within the family at alpha = 0.05.

| Contrast | Estimate | 95% CI | p | Holm alpha | Verdict |
|---|---:|---|---:|---:|---|
| seat asymmetry :: 4s2p-adjacent-spread | 0.2920 | [0.2878, 0.2962] | &lt;1e-300 | 0.00625 | **rejected** |
| seat asymmetry :: 4s2p-adjacent-random | 0.0401 | [0.0358, 0.0445] | &lt;1e-300 | 0.00714 | **rejected** |
| seat asymmetry :: 4s2p-opposite-spread | 0.0062 | [0.0018, 0.0106] | 0.0057 | 0.02500 | **rejected** |
| seat asymmetry :: 4s2p-opposite-random | 0.0004 | [-0.0040, 0.0048] | 0.8686 | 0.05000 | not rejected |
| asymmetry shift :: spread-minus-random x adjacent | 0.2519 | [0.2458, 0.2579] | &lt;1e-300 | 0.00833 | **rejected** |
| asymmetry shift :: adjacent-minus-opposite x spread | 0.2858 | [0.2798, 0.2919] | &lt;1e-300 | 0.01000 | **rejected** |
| asymmetry shift :: 6s3p adjacent-minus-spread x spread | 0.1381 | [0.1331, 0.1431] | &lt;1e-300 | 0.01250 | **rejected** |
| asymmetry shift :: 6s3p adjacent-minus-spread x random | 0.0145 | [0.0095, 0.0196] | 2.08e-08 | 0.01667 | **rejected** |

**7 of 8 rejected** after Holm correction.

### RQ-6

9 tests, Holm-corrected within the family at alpha = 0.05.

| Contrast | Estimate | 95% CI | p | Holm alpha | Verdict |
|---|---:|---|---:|---:|---|
| starter advantage :: starter advantage, 4 players | 0.0052 | [0.0038, 0.0065] | 4.20e-14 | 0.00714 | **rejected** |
| starter advantage :: starter advantage, 6 players | 0.0025 | [0.0013, 0.0037] | 2.29e-05 | 0.01000 | **rejected** |
| starter advantage :: starter advantage, 2p minus 6p | 0.0053 | [0.0028, 0.0077] | 2.36e-05 | 0.01250 | **rejected** |
| GREEDY edge :: GREEDY_CAPTURE vs 1/k, optional | -0.0000 | [-0.0017, 0.0017] | 0.9926 | 0.05000 | not rejected |
| GREEDY edge :: GREEDY_CAPTURE vs 1/k, mandatory | -0.0002 | [-0.0019, 0.0015] | 0.8390 | 0.01667 | not rejected |
| GREEDY edge shift :: GREEDY_CAPTURE edge, optional minus mandatory | 0.0002 | [-0.0022, 0.0026] | 0.8909 | 0.02500 | not rejected |
| middle seat :: middle seat, 3p on 4 seats, RANDOM | 0.0082 | [0.0054, 0.0109] | 8.86e-09 | 0.00833 | **rejected** |
| middle seat :: middle seat, 3p on 4 seats, SPREAD | 0.0573 | [0.0545, 0.0602] | &lt;1e-300 | 0.00556 | **rejected** |
| captures per game :: manipulation check: captures under mandatory | 21.5 | [21.4, 21.6] | &lt;1e-300 | 0.00625 | **rejected** |

**6 of 9 rejected** after Holm correction.

### RQ-7

100 tests, Holm-corrected within the family at alpha = 0.05.

| Contrast | Estimate | 95% CI | p | Holm alpha | Verdict |
|---|---:|---|---:|---:|---|
| win_rate_by_starting_seat :: cold_start x capture_mode | 0.0004 | [-0.0013, 0.0021] | 0.6498 | 0.00250 | not rejected |
| rounds_to_first_win :: cold_start x capture_mode | -0.0704 | [-0.1816, 0.0409] | 0.2150 | 0.00135 | not rejected |
| captures_total :: cold_start x capture_mode | -0.0719 | [-0.1554, 0.0117] | 0.0920 | 0.00111 | not rejected |
| lead_changes_per_turn :: cold_start x capture_mode | 0.0018 | [0.0017, 0.0018] | &lt;1e-300 | 0.00050 | **rejected** |
| comeback_rate :: cold_start x capture_mode | -0.0013 | [-0.0029, 0.0004] | 0.1313 | 0.00125 | not rejected |
| win_rate_by_starting_seat :: cold_start x dreimal | 0.0006 | [-0.0009, 0.0021] | 0.4686 | 0.00179 | not rejected |
| rounds_to_first_win :: cold_start x dreimal | -2.8712 | [-2.9850, -2.7573] | &lt;1e-300 | 0.00051 | **rejected** |
| captures_total :: cold_start x dreimal | 0.6666 | [0.5884, 0.7448] | &lt;1e-300 | 0.00051 | **rejected** |
| lead_changes_per_turn :: cold_start x dreimal | 0.0053 | [0.0053, 0.0054] | &lt;1e-300 | 0.00052 | **rejected** |
| comeback_rate :: cold_start x dreimal | -0.0027 | [-0.0041, -0.0012] | 0.0002 | 0.00083 | **rejected** |
| win_rate_by_starting_seat :: cold_start x bonus_quick | 0.0002 | [-0.0013, 0.0017] | 0.8131 | 0.00625 | not rejected |
| rounds_to_first_win :: cold_start x bonus_quick | -1.7512 | [-1.8641, -1.6384] | &lt;1e-300 | 0.00052 | **rejected** |
| captures_total :: cold_start x bonus_quick | 0.4434 | [0.3525, 0.5343] | &lt;1e-300 | 0.00053 | **rejected** |
| lead_changes_per_turn :: cold_start x bonus_quick | 0.0025 | [0.0024, 0.0025] | &lt;1e-300 | 0.00053 | **rejected** |
| comeback_rate :: cold_start x bonus_quick | -0.0020 | [-0.0035, -0.0006] | 0.0050 | 0.00093 | not rejected |
| win_rate_by_starting_seat :: cold_start x goal_no_jump | 0.0006 | [-0.0008, 0.0021] | 0.3770 | 0.00152 | not rejected |
| rounds_to_first_win :: cold_start x goal_no_jump | -0.0541 | [-0.1614, 0.0532] | 0.3232 | 0.00143 | not rejected |
| captures_total :: cold_start x goal_no_jump | -0.0646 | [-0.1450, 0.0158] | 0.1152 | 0.00122 | not rejected |
| lead_changes_per_turn :: cold_start x goal_no_jump | 0.0004 | [0.0003, 0.0005] | &lt;1e-300 | 0.00054 | **rejected** |
| comeback_rate :: cold_start x goal_no_jump | -0.0003 | [-0.0016, 0.0011] | 0.6889 | 0.00294 | not rejected |
| win_rate_by_starting_seat :: cold_start x barriers | -0.0005 | [-0.0019, 0.0009] | 0.4939 | 0.00185 | not rejected |
| rounds_to_first_win :: cold_start x barriers | 0.0102 | [-0.0971, 0.1175] | 0.8520 | 0.01000 | not rejected |
| captures_total :: cold_start x barriers | 0.0003 | [-0.0801, 0.0806] | 0.9950 | 0.05000 | not rejected |
| lead_changes_per_turn :: cold_start x barriers | -0.0001 | [-0.0002, -0.0001] | 0.0002 | 0.00082 | **rejected** |
| comeback_rate :: cold_start x barriers | -0.0003 | [-0.0016, 0.0010] | 0.6665 | 0.00278 | not rejected |
| win_rate_by_starting_seat :: cold_start x bonus_forfeited | 0.0010 | [-0.0004, 0.0024] | 0.1683 | 0.00132 | not rejected |
| rounds_to_first_win :: cold_start x bonus_forfeited | 0.0215 | [-0.0858, 0.1289] | 0.6940 | 0.00333 | not rejected |
| captures_total :: cold_start x bonus_forfeited | -0.0241 | [-0.1045, 0.0562] | 0.5564 | 0.00227 | not rejected |
| lead_changes_per_turn :: cold_start x bonus_forfeited | 0.0001 | [-0.0000, 0.0001] | 0.0748 | 0.00109 | not rejected |
| comeback_rate :: cold_start x bonus_forfeited | -0.0002 | [-0.0015, 0.0012] | 0.8171 | 0.00714 | not rejected |
| win_rate_by_starting_seat :: capture_mode x dreimal | -0.0017 | [-0.0033, -0.0001] | 0.0421 | 0.00102 | not rejected |
| rounds_to_first_win :: capture_mode x dreimal | -75.7 | [-75.9, -75.5] | &lt;1e-300 | 0.00054 | **rejected** |
| captures_total :: capture_mode x dreimal | -116.2 | [-116.4, -115.9] | &lt;1e-300 | 0.00055 | **rejected** |
| lead_changes_per_turn :: capture_mode x dreimal | 0.0004 | [0.0003, 0.0005] | &lt;1e-300 | 0.00056 | **rejected** |
| comeback_rate :: capture_mode x dreimal | -0.0065 | [-0.0080, -0.0049] | &lt;1e-300 | 0.00056 | **rejected** |
| win_rate_by_starting_seat :: capture_mode x bonus_quick | -0.0007 | [-0.0024, 0.0011] | 0.4682 | 0.00172 | not rejected |
| rounds_to_first_win :: capture_mode x bonus_quick | -43.2 | [-43.4, -43.1] | &lt;1e-300 | 0.00057 | **rejected** |
| captures_total :: capture_mode x bonus_quick | -64.7 | [-64.9, -64.6] | &lt;1e-300 | 0.00057 | **rejected** |
| lead_changes_per_turn :: capture_mode x bonus_quick | 0.0004 | [0.0003, 0.0005] | 8.88e-16 | 0.00068 | **rejected** |
| comeback_rate :: capture_mode x bonus_quick | -0.0043 | [-0.0060, -0.0026] | 4.46e-07 | 0.00075 | **rejected** |
| win_rate_by_starting_seat :: capture_mode x goal_no_jump | 0.0016 | [-0.0000, 0.0032] | 0.0568 | 0.00106 | not rejected |
| rounds_to_first_win :: capture_mode x goal_no_jump | 0.4834 | [0.3003, 0.6666] | 2.30e-07 | 0.00072 | **rejected** |
| captures_total :: capture_mode x goal_no_jump | 1.5319 | [1.3337, 1.7301] | &lt;1e-300 | 0.00058 | **rejected** |
| lead_changes_per_turn :: capture_mode x goal_no_jump | 0.0007 | [0.0006, 0.0008] | &lt;1e-300 | 0.00059 | **rejected** |
| comeback_rate :: capture_mode x goal_no_jump | -0.0015 | [-0.0030, -0.0000] | 0.0478 | 0.00104 | not rejected |
| win_rate_by_starting_seat :: capture_mode x barriers | -0.0007 | [-0.0023, 0.0009] | 0.3877 | 0.00156 | not rejected |
| rounds_to_first_win :: capture_mode x barriers | 2.3499 | [2.1667, 2.5330] | &lt;1e-300 | 0.00060 | **rejected** |
| captures_total :: capture_mode x barriers | 0.8713 | [0.6731, 1.0695] | &lt;1e-300 | 0.00060 | **rejected** |
| lead_changes_per_turn :: capture_mode x barriers | 0.0000 | [-0.0001, 0.0001] | 0.8077 | 0.00556 | not rejected |
| comeback_rate :: capture_mode x barriers | 0.0003 | [-0.0012, 0.0018] | 0.7286 | 0.00357 | not rejected |
| win_rate_by_starting_seat :: capture_mode x bonus_forfeited | 0.0002 | [-0.0014, 0.0019] | 0.7701 | 0.00417 | not rejected |
| rounds_to_first_win :: capture_mode x bonus_forfeited | 0.6083 | [0.4251, 0.7914] | 7.56e-11 | 0.00069 | **rejected** |
| captures_total :: capture_mode x bonus_forfeited | 0.4507 | [0.2525, 0.6490] | 8.30e-06 | 0.00078 | **rejected** |
| lead_changes_per_turn :: capture_mode x bonus_forfeited | 0.0002 | [0.0001, 0.0003] | 4.09e-07 | 0.00074 | **rejected** |
| comeback_rate :: capture_mode x bonus_forfeited | -0.0002 | [-0.0017, 0.0013] | 0.8050 | 0.00500 | not rejected |
| win_rate_by_starting_seat :: dreimal x goal_no_jump | 0.0010 | [-0.0004, 0.0023] | 0.1576 | 0.00128 | not rejected |
| rounds_to_first_win :: dreimal x goal_no_jump | -3.4612 | [-3.6690, -3.2533] | &lt;1e-300 | 0.00061 | **rejected** |
| captures_total :: dreimal x goal_no_jump | -3.0641 | [-3.2950, -2.8332] | &lt;1e-300 | 0.00062 | **rejected** |
| lead_changes_per_turn :: dreimal x goal_no_jump | 0.0001 | [0.0000, 0.0002] | 0.0028 | 0.00089 | not rejected |
| comeback_rate :: dreimal x goal_no_jump | 0.0038 | [0.0026, 0.0051] | 1.61e-09 | 0.00071 | **rejected** |
| win_rate_by_starting_seat :: dreimal x barriers | -0.0004 | [-0.0018, 0.0009] | 0.5272 | 0.00217 | not rejected |
| rounds_to_first_win :: dreimal x barriers | 0.3392 | [0.1314, 0.5470] | 0.0014 | 0.00088 | not rejected |
| captures_total :: dreimal x barriers | 3.6581 | [3.4272, 3.8890] | &lt;1e-300 | 0.00063 | **rejected** |
| lead_changes_per_turn :: dreimal x barriers | -0.0003 | [-0.0004, -0.0002] | &lt;1e-300 | 0.00063 | **rejected** |
| comeback_rate :: dreimal x barriers | -0.0010 | [-0.0023, 0.0002] | 0.1000 | 0.00114 | not rejected |
| win_rate_by_starting_seat :: dreimal x bonus_forfeited | 0.0011 | [-0.0002, 0.0024] | 0.1042 | 0.00116 | not rejected |
| rounds_to_first_win :: dreimal x bonus_forfeited | -0.7867 | [-0.9945, -0.5788] | 1.18e-13 | 0.00068 | **rejected** |
| captures_total :: dreimal x bonus_forfeited | -0.5451 | [-0.7760, -0.3142] | 3.70e-06 | 0.00076 | **rejected** |
| lead_changes_per_turn :: dreimal x bonus_forfeited | 0.0000 | [-0.0000, 0.0001] | 0.5058 | 0.00200 | not rejected |
| comeback_rate :: dreimal x bonus_forfeited | 0.0004 | [-0.0009, 0.0016] | 0.5641 | 0.00238 | not rejected |
| win_rate_by_starting_seat :: bonus_quick x goal_no_jump | 0.0003 | [-0.0012, 0.0018] | 0.6901 | 0.00313 | not rejected |
| rounds_to_first_win :: bonus_quick x goal_no_jump | -2.4956 | [-2.6498, -2.3415] | &lt;1e-300 | 0.00064 | **rejected** |
| captures_total :: bonus_quick x goal_no_jump | -1.8408 | [-1.9994, -1.6822] | &lt;1e-300 | 0.00065 | **rejected** |
| lead_changes_per_turn :: bonus_quick x goal_no_jump | 0.0001 | [0.0001, 0.0002] | 5.49e-05 | 0.00081 | **rejected** |
| comeback_rate :: bonus_quick x goal_no_jump | 0.0023 | [0.0009, 0.0036] | 0.0012 | 0.00085 | not rejected |
| win_rate_by_starting_seat :: bonus_quick x barriers | -0.0003 | [-0.0017, 0.0012] | 0.7307 | 0.00385 | not rejected |
| rounds_to_first_win :: bonus_quick x barriers | 0.2524 | [0.0982, 0.4065] | 0.0013 | 0.00086 | not rejected |
| captures_total :: bonus_quick x barriers | 1.9854 | [1.8268, 2.1440] | &lt;1e-300 | 0.00066 | **rejected** |
| lead_changes_per_turn :: bonus_quick x barriers | -0.0003 | [-0.0004, -0.0002] | &lt;1e-300 | 0.00067 | **rejected** |
| comeback_rate :: bonus_quick x barriers | -0.0011 | [-0.0025, 0.0002] | 0.1067 | 0.00119 | not rejected |
| win_rate_by_starting_seat :: bonus_quick x bonus_forfeited | 0.0006 | [-0.0008, 0.0021] | 0.4128 | 0.00167 | not rejected |
| rounds_to_first_win :: bonus_quick x bonus_forfeited | -0.4959 | [-0.6500, -0.3417] | 2.88e-10 | 0.00070 | **rejected** |
| captures_total :: bonus_quick x bonus_forfeited | -0.3414 | [-0.5000, -0.1828] | 2.46e-05 | 0.00079 | **rejected** |
| lead_changes_per_turn :: bonus_quick x bonus_forfeited | -0.0000 | [-0.0001, 0.0001] | 0.7831 | 0.00455 | not rejected |
| comeback_rate :: bonus_quick x bonus_forfeited | 0.0020 | [0.0007, 0.0034] | 0.0035 | 0.00091 | not rejected |
| win_rate_by_starting_seat :: goal_no_jump x barriers | 0.0006 | [-0.0007, 0.0020] | 0.3405 | 0.00147 | not rejected |
| rounds_to_first_win :: goal_no_jump x barriers | 0.2156 | [0.0307, 0.4005] | 0.0223 | 0.00096 | not rejected |
| captures_total :: goal_no_jump x barriers | -0.1159 | [-0.3178, 0.0860] | 0.2607 | 0.00139 | not rejected |
| lead_changes_per_turn :: goal_no_jump x barriers | -0.0001 | [-0.0001, -0.0000] | 0.0120 | 0.00094 | not rejected |
| comeback_rate :: goal_no_jump x barriers | -0.0004 | [-0.0017, 0.0008] | 0.5006 | 0.00192 | not rejected |
| win_rate_by_starting_seat :: goal_no_jump x bonus_forfeited | 0.0001 | [-0.0012, 0.0014] | 0.8717 | 0.01250 | not rejected |
| rounds_to_first_win :: goal_no_jump x bonus_forfeited | 0.4245 | [0.2396, 0.6094] | 6.82e-06 | 0.00077 | **rejected** |
| captures_total :: goal_no_jump x bonus_forfeited | 0.2347 | [0.0328, 0.4366] | 0.0227 | 0.00098 | not rejected |
| lead_changes_per_turn :: goal_no_jump x bonus_forfeited | 0.0001 | [0.0000, 0.0001] | 0.0261 | 0.00100 | not rejected |
| comeback_rate :: goal_no_jump x bonus_forfeited | 0.0004 | [-0.0008, 0.0016] | 0.5188 | 0.00208 | not rejected |
| win_rate_by_starting_seat :: barriers x bonus_forfeited | 0.0006 | [-0.0007, 0.0019] | 0.3982 | 0.00161 | not rejected |
| rounds_to_first_win :: barriers x bonus_forfeited | 0.0192 | [-0.1657, 0.2042] | 0.8384 | 0.00833 | not rejected |
| captures_total :: barriers x bonus_forfeited | 0.0128 | [-0.1891, 0.2147] | 0.9011 | 0.02500 | not rejected |
| lead_changes_per_turn :: barriers x bonus_forfeited | -0.0000 | [-0.0001, 0.0001] | 0.8799 | 0.01667 | not rejected |
| comeback_rate :: barriers x bonus_forfeited | -0.0003 | [-0.0015, 0.0009] | 0.6509 | 0.00263 | not rejected |

**Not evaluated.** These contrasts are declared in §6.4 and no cell in the dataset answers them. Listed rather than dropped, because a family reported as complete when it is not is a different claim:

- `win_rate_by_starting_seat @ dreimal x bonus_quick`
- `rounds_to_first_win @ dreimal x bonus_quick`
- `captures_total @ dreimal x bonus_quick`
- `lead_changes_per_turn @ dreimal x bonus_quick`
- `comeback_rate @ dreimal x bonus_quick`

**41 of 100 rejected** after Holm correction.

### RQ-8

180 tests, Holm-corrected within the family at alpha = 0.05.

| Contrast | Estimate | 95% CI | p | Holm alpha | Verdict |
|---|---:|---|---:|---:|---|
| win_rate_by_starting_seat :: cold_start:strict x spread | 0.0007 | [-0.0015, 0.0029] | 0.5454 | 0.00200 | not rejected |
| rounds_to_first_win :: cold_start:strict x spread | 0.0497 | [-0.0680, 0.1674] | 0.4075 | 0.00128 | not rejected |
| captures_total :: cold_start:strict x spread | 0.0269 | [-0.0463, 0.1001] | 0.4715 | 0.00161 | not rejected |
| lead_changes_per_turn :: cold_start:strict x spread | 0.0006 | [0.0005, 0.0008] | &lt;1e-300 | 0.00028 | **rejected** |
| comeback_rate :: cold_start:strict x spread | 0.0020 | [-0.0001, 0.0040] | 0.0654 | 0.00070 | not rejected |
| win_rate_by_starting_seat :: cold_start:strict x focus_front | -0.0002 | [-0.0024, 0.0020] | 0.8693 | 0.00833 | not rejected |
| rounds_to_first_win :: cold_start:strict x focus_front | -0.0826 | [-0.1869, 0.0217] | 0.1206 | 0.00077 | not rejected |
| captures_total :: cold_start:strict x focus_front | -0.0134 | [-0.0772, 0.0504] | 0.6799 | 0.00294 | not rejected |
| lead_changes_per_turn :: cold_start:strict x focus_front | -0.0015 | [-0.0016, -0.0014] | &lt;1e-300 | 0.00028 | **rejected** |
| comeback_rate :: cold_start:strict x focus_front | 0.0007 | [-0.0014, 0.0027] | 0.5238 | 0.00185 | not rejected |
| win_rate_by_starting_seat :: cold_start:strict x focus_rear | 0.0011 | [-0.0011, 0.0033] | 0.3389 | 0.00111 | not rejected |
| rounds_to_first_win :: cold_start:strict x focus_rear | 0.0440 | [-0.0730, 0.1609] | 0.4614 | 0.00143 | not rejected |
| captures_total :: cold_start:strict x focus_rear | 0.0292 | [-0.0434, 0.1017] | 0.4307 | 0.00139 | not rejected |
| lead_changes_per_turn :: cold_start:strict x focus_rear | 0.0005 | [0.0004, 0.0007] | &lt;1e-300 | 0.00028 | **rejected** |
| comeback_rate :: cold_start:strict x focus_rear | 0.0007 | [-0.0013, 0.0028] | 0.4881 | 0.00167 | not rejected |
| win_rate_by_starting_seat :: cold_start:strict x greedy_capture | 0.0020 | [-0.0002, 0.0042] | 0.0817 | 0.00072 | not rejected |
| rounds_to_first_win :: cold_start:strict x greedy_capture | 0.0331 | [-0.0860, 0.1522] | 0.5857 | 0.00217 | not rejected |
| captures_total :: cold_start:strict x greedy_capture | -0.0033 | [-0.0775, 0.0710] | 0.9313 | 0.01250 | not rejected |
| lead_changes_per_turn :: cold_start:strict x greedy_capture | 0.0009 | [0.0008, 0.0010] | &lt;1e-300 | 0.00028 | **rejected** |
| comeback_rate :: cold_start:strict x greedy_capture | -0.0004 | [-0.0025, 0.0017] | 0.7164 | 0.00333 | not rejected |
| win_rate_by_starting_seat :: cold_start:free_entry x spread | -0.0001 | [-0.0023, 0.0021] | 0.9338 | 0.01667 | not rejected |
| rounds_to_first_win :: cold_start:free_entry x spread | 6.1903 | [6.0264, 6.3542] | &lt;1e-300 | 0.00028 | **rejected** |
| captures_total :: cold_start:free_entry x spread | 15.2 | [15.1, 15.4] | &lt;1e-300 | 0.00029 | **rejected** |
| lead_changes_per_turn :: cold_start:free_entry x spread | 0.0011 | [0.0010, 0.0012] | &lt;1e-300 | 0.00029 | **rejected** |
| comeback_rate :: cold_start:free_entry x spread | 0.0074 | [0.0053, 0.0094] | 1.81e-12 | 0.00043 | **rejected** |
| win_rate_by_starting_seat :: cold_start:free_entry x focus_front | -0.0002 | [-0.0024, 0.0020] | 0.8355 | 0.00625 | not rejected |
| rounds_to_first_win :: cold_start:free_entry x focus_front | -29.5 | [-29.6, -29.3] | &lt;1e-300 | 0.00029 | **rejected** |
| captures_total :: cold_start:free_entry x focus_front | -30.7 | [-30.8, -30.6] | &lt;1e-300 | 0.00029 | **rejected** |
| lead_changes_per_turn :: cold_start:free_entry x focus_front | -0.0083 | [-0.0084, -0.0082] | &lt;1e-300 | 0.00029 | **rejected** |
| comeback_rate :: cold_start:free_entry x focus_front | -0.0812 | [-0.0831, -0.0793] | &lt;1e-300 | 0.00029 | **rejected** |
| win_rate_by_starting_seat :: cold_start:free_entry x focus_rear | 0.0013 | [-0.0009, 0.0035] | 0.2612 | 0.00098 | not rejected |
| rounds_to_first_win :: cold_start:free_entry x focus_rear | -34.8 | [-35.0, -34.7] | &lt;1e-300 | 0.00030 | **rejected** |
| captures_total :: cold_start:free_entry x focus_rear | -34.5 | [-34.6, -34.4] | &lt;1e-300 | 0.00030 | **rejected** |
| lead_changes_per_turn :: cold_start:free_entry x focus_rear | -0.0080 | [-0.0081, -0.0079] | &lt;1e-300 | 0.00030 | **rejected** |
| comeback_rate :: cold_start:free_entry x focus_rear | -0.0850 | [-0.0870, -0.0831] | &lt;1e-300 | 0.00030 | **rejected** |
| win_rate_by_starting_seat :: cold_start:free_entry x greedy_capture | 0.0017 | [-0.0005, 0.0039] | 0.1384 | 0.00081 | not rejected |
| rounds_to_first_win :: cold_start:free_entry x greedy_capture | 34.6 | [34.4, 34.8] | &lt;1e-300 | 0.00030 | **rejected** |
| captures_total :: cold_start:free_entry x greedy_capture | 54.0 | [53.8, 54.1] | &lt;1e-300 | 0.00030 | **rejected** |
| lead_changes_per_turn :: cold_start:free_entry x greedy_capture | -0.0009 | [-0.0010, -0.0008] | &lt;1e-300 | 0.00031 | **rejected** |
| comeback_rate :: cold_start:free_entry x greedy_capture | -0.0024 | [-0.0044, -0.0004] | 0.0202 | 0.00063 | not rejected |
| win_rate_by_starting_seat :: capture:mandatory x spread | -0.0014 | [-0.0036, 0.0008] | 0.2147 | 0.00089 | not rejected |
| rounds_to_first_win :: capture:mandatory x spread | 0.7180 | [0.5693, 0.8668] | &lt;1e-300 | 0.00031 | **rejected** |
| captures_total :: capture:mandatory x spread | 1.2974 | [1.2025, 1.3924] | &lt;1e-300 | 0.00031 | **rejected** |
| lead_changes_per_turn :: capture:mandatory x spread | 0.0001 | [0.0000, 0.0003] | 0.0051 | 0.00059 | not rejected |
| comeback_rate :: capture:mandatory x spread | -0.0071 | [-0.0092, -0.0051] | 1.55e-11 | 0.00044 | **rejected** |
| win_rate_by_starting_seat :: capture:mandatory x focus_front | 0.0004 | [-0.0018, 0.0026] | 0.7502 | 0.00385 | not rejected |
| rounds_to_first_win :: capture:mandatory x focus_front | -1.4947 | [-1.6282, -1.3612] | &lt;1e-300 | 0.00031 | **rejected** |
| captures_total :: capture:mandatory x focus_front | -1.4636 | [-1.5477, -1.3794] | &lt;1e-300 | 0.00031 | **rejected** |
| lead_changes_per_turn :: capture:mandatory x focus_front | 0.0003 | [0.0001, 0.0004] | 3.40e-06 | 0.00051 | **rejected** |
| comeback_rate :: capture:mandatory x focus_front | 0.0069 | [0.0049, 0.0090] | 2.69e-11 | 0.00044 | **rejected** |
| win_rate_by_starting_seat :: capture:mandatory x focus_rear | 0.0011 | [-0.0011, 0.0033] | 0.3229 | 0.00106 | not rejected |
| rounds_to_first_win :: capture:mandatory x focus_rear | 0.3707 | [0.2229, 0.5184] | 8.77e-07 | 0.00050 | **rejected** |
| captures_total :: capture:mandatory x focus_rear | 0.7722 | [0.6783, 0.8661] | &lt;1e-300 | 0.00032 | **rejected** |
| lead_changes_per_turn :: capture:mandatory x focus_rear | 0.0002 | [0.0001, 0.0003] | 4.30e-05 | 0.00053 | **rejected** |
| comeback_rate :: capture:mandatory x focus_rear | -0.0046 | [-0.0067, -0.0025] | 1.30e-05 | 0.00053 | **rejected** |
| win_rate_by_starting_seat :: capture:mandatory x greedy_capture | 0.0008 | [-0.0014, 0.0030] | 0.4932 | 0.00172 | not rejected |
| rounds_to_first_win :: capture:mandatory x greedy_capture | -7.0324 | [-7.1770, -6.8879] | &lt;1e-300 | 0.00032 | **rejected** |
| captures_total :: capture:mandatory x greedy_capture | -5.7992 | [-5.8911, -5.7073] | &lt;1e-300 | 0.00032 | **rejected** |
| lead_changes_per_turn :: capture:mandatory x greedy_capture | 0.0021 | [0.0020, 0.0022] | &lt;1e-300 | 0.00032 | **rejected** |
| comeback_rate :: capture:mandatory x greedy_capture | 0.0021 | [-0.0000, 0.0041] | 0.0516 | 0.00068 | not rejected |
| win_rate_by_starting_seat :: capture:mandatory_extended x spread | -0.0006 | [-0.0028, 0.0016] | 0.6089 | 0.00227 | not rejected |
| rounds_to_first_win :: capture:mandatory_extended x spread | 3.6920 | [3.5181, 3.8659] | &lt;1e-300 | 0.00032 | **rejected** |
| captures_total :: capture:mandatory_extended x spread | 3.7780 | [3.6697, 3.8864] | &lt;1e-300 | 0.00033 | **rejected** |
| lead_changes_per_turn :: capture:mandatory_extended x spread | -0.0001 | [-0.0002, 0.0001] | 0.3283 | 0.00109 | not rejected |
| comeback_rate :: capture:mandatory_extended x spread | -0.0084 | [-0.0105, -0.0063] | 2.44e-15 | 0.00041 | **rejected** |
| win_rate_by_starting_seat :: capture:mandatory_extended x focus_front | 0.0000 | [-0.0022, 0.0023] | 0.9657 | 0.02500 | not rejected |
| rounds_to_first_win :: capture:mandatory_extended x focus_front | -5.0155 | [-5.1705, -4.8605] | &lt;1e-300 | 0.00033 | **rejected** |
| captures_total :: capture:mandatory_extended x focus_front | -3.4793 | [-3.5745, -3.3840] | &lt;1e-300 | 0.00033 | **rejected** |
| lead_changes_per_turn :: capture:mandatory_extended x focus_front | 0.0003 | [0.0002, 0.0004] | 1.36e-06 | 0.00050 | **rejected** |
| comeback_rate :: capture:mandatory_extended x focus_front | 0.0057 | [0.0037, 0.0078] | 4.38e-08 | 0.00048 | **rejected** |
| win_rate_by_starting_seat :: capture:mandatory_extended x focus_rear | 0.0008 | [-0.0014, 0.0030] | 0.4656 | 0.00147 | not rejected |
| rounds_to_first_win :: capture:mandatory_extended x focus_rear | 3.1154 | [2.9426, 3.2882] | &lt;1e-300 | 0.00033 | **rejected** |
| captures_total :: capture:mandatory_extended x focus_rear | 2.9692 | [2.8619, 3.0764] | &lt;1e-300 | 0.00034 | **rejected** |
| lead_changes_per_turn :: capture:mandatory_extended x focus_rear | 0.0000 | [-0.0001, 0.0001] | 0.6786 | 0.00278 | not rejected |
| comeback_rate :: capture:mandatory_extended x focus_rear | -0.0051 | [-0.0072, -0.0030] | 1.61e-06 | 0.00051 | **rejected** |
| win_rate_by_starting_seat :: capture:mandatory_extended x greedy_capture | 0.0020 | [-0.0002, 0.0042] | 0.0715 | 0.00071 | not rejected |
| rounds_to_first_win :: capture:mandatory_extended x greedy_capture | -6.9545 | [-7.1218, -6.7871] | &lt;1e-300 | 0.00034 | **rejected** |
| captures_total :: capture:mandatory_extended x greedy_capture | -5.7908 | [-5.8945, -5.6870] | &lt;1e-300 | 0.00034 | **rejected** |
| lead_changes_per_turn :: capture:mandatory_extended x greedy_capture | 0.0021 | [0.0020, 0.0022] | &lt;1e-300 | 0.00034 | **rejected** |
| comeback_rate :: capture:mandatory_extended x greedy_capture | 0.0028 | [0.0007, 0.0049] | 0.0085 | 0.00060 | not rejected |
| win_rate_by_starting_seat :: dreimal x spread | -0.0018 | [-0.0040, 0.0004] | 0.1052 | 0.00076 | not rejected |
| rounds_to_first_win :: dreimal x spread | -0.2288 | [-0.3447, -0.1128] | 0.0001 | 0.00054 | **rejected** |
| captures_total :: dreimal x spread | 0.2631 | [0.1851, 0.3411] | 3.79e-11 | 0.00045 | **rejected** |
| lead_changes_per_turn :: dreimal x spread | -0.0002 | [-0.0003, -0.0000] | 0.0076 | 0.00060 | not rejected |
| comeback_rate :: dreimal x spread | -0.0021 | [-0.0042, -0.0001] | 0.0405 | 0.00066 | not rejected |
| win_rate_by_starting_seat :: dreimal x focus_front | -0.0011 | [-0.0033, 0.0011] | 0.3174 | 0.00104 | not rejected |
| rounds_to_first_win :: dreimal x focus_front | -0.8749 | [-0.9772, -0.7725] | &lt;1e-300 | 0.00034 | **rejected** |
| captures_total :: dreimal x focus_front | -1.1815 | [-1.2497, -1.1134] | &lt;1e-300 | 0.00035 | **rejected** |
| lead_changes_per_turn :: dreimal x focus_front | -0.0003 | [-0.0004, -0.0002] | 2.16e-07 | 0.00048 | **rejected** |
| comeback_rate :: dreimal x focus_front | -0.0010 | [-0.0030, 0.0010] | 0.3415 | 0.00116 | not rejected |
| win_rate_by_starting_seat :: dreimal x focus_rear | -0.0007 | [-0.0029, 0.0015] | 0.5592 | 0.00208 | not rejected |
| rounds_to_first_win :: dreimal x focus_rear | -0.0753 | [-0.1906, 0.0401] | 0.2011 | 0.00088 | not rejected |
| captures_total :: dreimal x focus_rear | 0.3999 | [0.3225, 0.4774] | &lt;1e-300 | 0.00035 | **rejected** |
| lead_changes_per_turn :: dreimal x focus_rear | -0.0001 | [-0.0003, -0.0000] | 0.0174 | 0.00063 | not rejected |
| comeback_rate :: dreimal x focus_rear | -0.0012 | [-0.0032, 0.0009] | 0.2585 | 0.00096 | not rejected |
| win_rate_by_starting_seat :: dreimal x greedy_capture | 0.0009 | [-0.0013, 0.0031] | 0.4124 | 0.00132 | not rejected |
| rounds_to_first_win :: dreimal x greedy_capture | 0.7446 | [0.6266, 0.8625] | &lt;1e-300 | 0.00035 | **rejected** |
| captures_total :: dreimal x greedy_capture | 2.2692 | [2.1888, 2.3495] | &lt;1e-300 | 0.00035 | **rejected** |
| lead_changes_per_turn :: dreimal x greedy_capture | 0.0004 | [0.0003, 0.0005] | 2.28e-12 | 0.00043 | **rejected** |
| comeback_rate :: dreimal x greedy_capture | 0.0005 | [-0.0015, 0.0025] | 0.6304 | 0.00250 | not rejected |
| win_rate_by_starting_seat :: bonus_quick x spread | 0.0021 | [-0.0001, 0.0043] | 0.0596 | 0.00069 | not rejected |
| rounds_to_first_win :: bonus_quick x spread | 0.4327 | [0.3225, 0.5429] | 1.40e-14 | 0.00042 | **rejected** |
| captures_total :: bonus_quick x spread | 0.9626 | [0.8788, 1.0463] | &lt;1e-300 | 0.00036 | **rejected** |
| lead_changes_per_turn :: bonus_quick x spread | -0.0003 | [-0.0005, -0.0002] | 1.24e-08 | 0.00047 | **rejected** |
| comeback_rate :: bonus_quick x spread | -0.0047 | [-0.0068, -0.0027] | 5.49e-06 | 0.00052 | **rejected** |
| win_rate_by_starting_seat :: bonus_quick x focus_front | 0.0011 | [-0.0011, 0.0033] | 0.3390 | 0.00114 | not rejected |
| rounds_to_first_win :: bonus_quick x focus_front | 0.2885 | [0.1918, 0.3853] | 5.01e-09 | 0.00046 | **rejected** |
| captures_total :: bonus_quick x focus_front | -0.4416 | [-0.5144, -0.3688] | &lt;1e-300 | 0.00036 | **rejected** |
| lead_changes_per_turn :: bonus_quick x focus_front | -0.0011 | [-0.0012, -0.0010] | &lt;1e-300 | 0.00036 | **rejected** |
| comeback_rate :: bonus_quick x focus_front | -0.0060 | [-0.0080, -0.0041] | 2.69e-09 | 0.00045 | **rejected** |
| win_rate_by_starting_seat :: bonus_quick x focus_rear | 0.0017 | [-0.0005, 0.0039] | 0.1346 | 0.00079 | not rejected |
| rounds_to_first_win :: bonus_quick x focus_rear | 0.3254 | [0.2157, 0.4351] | 6.13e-09 | 0.00046 | **rejected** |
| captures_total :: bonus_quick x focus_rear | 0.7874 | [0.7042, 0.8706] | &lt;1e-300 | 0.00036 | **rejected** |
| lead_changes_per_turn :: bonus_quick x focus_rear | -0.0002 | [-0.0003, -0.0001] | 0.0036 | 0.00058 | not rejected |
| comeback_rate :: bonus_quick x focus_rear | -0.0038 | [-0.0059, -0.0018] | 0.0002 | 0.00054 | **rejected** |
| win_rate_by_starting_seat :: bonus_quick x greedy_capture | 0.0005 | [-0.0017, 0.0027] | 0.6299 | 0.00238 | not rejected |
| rounds_to_first_win :: bonus_quick x greedy_capture | 0.2887 | [0.1760, 0.4014] | 5.20e-07 | 0.00049 | **rejected** |
| captures_total :: bonus_quick x greedy_capture | 1.2503 | [1.1627, 1.3379] | &lt;1e-300 | 0.00037 | **rejected** |
| lead_changes_per_turn :: bonus_quick x greedy_capture | -0.0001 | [-0.0002, -0.0000] | 0.0366 | 0.00065 | not rejected |
| comeback_rate :: bonus_quick x greedy_capture | -0.0013 | [-0.0034, 0.0007] | 0.2000 | 0.00086 | not rejected |
| win_rate_by_starting_seat :: goal_no_jump x spread | -0.0019 | [-0.0041, 0.0003] | 0.0896 | 0.00074 | not rejected |
| rounds_to_first_win :: goal_no_jump x spread | 1.1273 | [1.0098, 1.2449] | &lt;1e-300 | 0.00037 | **rejected** |
| captures_total :: goal_no_jump x spread | 0.7265 | [0.6530, 0.8001] | &lt;1e-300 | 0.00037 | **rejected** |
| lead_changes_per_turn :: goal_no_jump x spread | -0.0002 | [-0.0003, -0.0001] | 0.0022 | 0.00057 | not rejected |
| comeback_rate :: goal_no_jump x spread | -0.0013 | [-0.0033, 0.0008] | 0.2285 | 0.00091 | not rejected |
| win_rate_by_starting_seat :: goal_no_jump x focus_front | 0.0002 | [-0.0020, 0.0025] | 0.8255 | 0.00556 | not rejected |
| rounds_to_first_win :: goal_no_jump x focus_front | 8.1289 | [8.0226, 8.2352] | &lt;1e-300 | 0.00038 | **rejected** |
| captures_total :: goal_no_jump x focus_front | 2.8769 | [2.8115, 2.9423] | &lt;1e-300 | 0.00038 | **rejected** |
| lead_changes_per_turn :: goal_no_jump x focus_front | -0.0006 | [-0.0007, -0.0005] | &lt;1e-300 | 0.00038 | **rejected** |
| comeback_rate :: goal_no_jump x focus_front | 0.0406 | [0.0385, 0.0426] | &lt;1e-300 | 0.00038 | **rejected** |
| win_rate_by_starting_seat :: goal_no_jump x focus_rear | -0.0003 | [-0.0025, 0.0019] | 0.7989 | 0.00500 | not rejected |
| rounds_to_first_win :: goal_no_jump x focus_rear | 1.4081 | [1.2911, 1.5252] | &lt;1e-300 | 0.00039 | **rejected** |
| captures_total :: goal_no_jump x focus_rear | 0.8548 | [0.7817, 0.9278] | &lt;1e-300 | 0.00039 | **rejected** |
| lead_changes_per_turn :: goal_no_jump x focus_rear | -0.0002 | [-0.0003, -0.0001] | 0.0003 | 0.00056 | **rejected** |
| comeback_rate :: goal_no_jump x focus_rear | 0.0010 | [-0.0011, 0.0030] | 0.3504 | 0.00119 | not rejected |
| win_rate_by_starting_seat :: goal_no_jump x greedy_capture | 0.0007 | [-0.0015, 0.0029] | 0.5154 | 0.00179 | not rejected |
| rounds_to_first_win :: goal_no_jump x greedy_capture | 0.2728 | [0.1542, 0.3913] | 6.49e-06 | 0.00052 | **rejected** |
| captures_total :: goal_no_jump x greedy_capture | 0.2150 | [0.1404, 0.2896] | 1.64e-08 | 0.00047 | **rejected** |
| lead_changes_per_turn :: goal_no_jump x greedy_capture | 0.0002 | [0.0001, 0.0003] | 0.0002 | 0.00055 | **rejected** |
| comeback_rate :: goal_no_jump x greedy_capture | -0.0009 | [-0.0029, 0.0011] | 0.3906 | 0.00125 | not rejected |
| win_rate_by_starting_seat :: barriers x spread | 0.0002 | [-0.0020, 0.0024] | 0.8392 | 0.00714 | not rejected |
| rounds_to_first_win :: barriers x spread | -0.3906 | [-0.5063, -0.2749] | 3.68e-11 | 0.00045 | **rejected** |
| captures_total :: barriers x spread | -1.3522 | [-1.4234, -1.2811] | &lt;1e-300 | 0.00039 | **rejected** |
| lead_changes_per_turn :: barriers x spread | -0.0001 | [-0.0002, 0.0000] | 0.0589 | 0.00068 | not rejected |
| comeback_rate :: barriers x spread | 0.0073 | [0.0053, 0.0094] | 3.98e-12 | 0.00043 | **rejected** |
| win_rate_by_starting_seat :: barriers x focus_front | -0.0005 | [-0.0027, 0.0017] | 0.6850 | 0.00313 | not rejected |
| rounds_to_first_win :: barriers x focus_front | 1.3104 | [1.2078, 1.4130] | &lt;1e-300 | 0.00040 | **rejected** |
| captures_total :: barriers x focus_front | 0.9713 | [0.9086, 1.0339] | &lt;1e-300 | 0.00040 | **rejected** |
| lead_changes_per_turn :: barriers x focus_front | -0.0002 | [-0.0003, -0.0001] | 0.0005 | 0.00056 | **rejected** |
| comeback_rate :: barriers x focus_front | 0.0023 | [0.0003, 0.0043] | 0.0265 | 0.00064 | not rejected |
| win_rate_by_starting_seat :: barriers x focus_rear | 0.0009 | [-0.0013, 0.0031] | 0.4178 | 0.00135 | not rejected |
| rounds_to_first_win :: barriers x focus_rear | -2.9404 | [-3.0540, -2.8267] | &lt;1e-300 | 0.00040 | **rejected** |
| captures_total :: barriers x focus_rear | -3.9048 | [-3.9740, -3.8356] | &lt;1e-300 | 0.00041 | **rejected** |
| lead_changes_per_turn :: barriers x focus_rear | -0.0010 | [-0.0011, -0.0009] | &lt;1e-300 | 0.00041 | **rejected** |
| comeback_rate :: barriers x focus_rear | 0.0077 | [0.0056, 0.0097] | 4.52e-13 | 0.00042 | **rejected** |
| win_rate_by_starting_seat :: barriers x greedy_capture | 0.0015 | [-0.0007, 0.0037] | 0.1858 | 0.00085 | not rejected |
| rounds_to_first_win :: barriers x greedy_capture | 0.2977 | [0.1805, 0.4149] | 6.44e-07 | 0.00049 | **rejected** |
| captures_total :: barriers x greedy_capture | 0.2646 | [0.1917, 0.3374] | 1.13e-12 | 0.00042 | **rejected** |
| lead_changes_per_turn :: barriers x greedy_capture | -0.0001 | [-0.0002, -0.0000] | 0.0162 | 0.00062 | not rejected |
| comeback_rate :: barriers x greedy_capture | 0.0003 | [-0.0018, 0.0024] | 0.7692 | 0.00455 | not rejected |
| win_rate_by_starting_seat :: bonus_forfeited x spread | -0.0012 | [-0.0034, 0.0011] | 0.3054 | 0.00102 | not rejected |
| rounds_to_first_win :: bonus_forfeited x spread | 0.0697 | [-0.0482, 0.1876] | 0.2468 | 0.00094 | not rejected |
| captures_total :: bonus_forfeited x spread | 0.0272 | [-0.0462, 0.1005] | 0.4682 | 0.00152 | not rejected |
| lead_changes_per_turn :: bonus_forfeited x spread | -0.0001 | [-0.0002, 0.0000] | 0.0968 | 0.00075 | not rejected |
| comeback_rate :: bonus_forfeited x spread | 0.0000 | [-0.0020, 0.0021] | 0.9824 | 0.05000 | not rejected |
| win_rate_by_starting_seat :: bonus_forfeited x focus_front | -0.0010 | [-0.0032, 0.0012] | 0.3865 | 0.00122 | not rejected |
| rounds_to_first_win :: bonus_forfeited x focus_front | 0.0067 | [-0.0978, 0.1113] | 0.8993 | 0.01000 | not rejected |
| captures_total :: bonus_forfeited x focus_front | -0.0151 | [-0.0791, 0.0489] | 0.6446 | 0.00263 | not rejected |
| lead_changes_per_turn :: bonus_forfeited x focus_front | -0.0002 | [-0.0003, -0.0001] | 0.0018 | 0.00057 | not rejected |
| comeback_rate :: bonus_forfeited x focus_front | 0.0011 | [-0.0009, 0.0031] | 0.2855 | 0.00100 | not rejected |
| win_rate_by_starting_seat :: bonus_forfeited x focus_rear | -0.0008 | [-0.0030, 0.0014] | 0.4705 | 0.00156 | not rejected |
| rounds_to_first_win :: bonus_forfeited x focus_rear | 0.1190 | [0.0017, 0.2362] | 0.0467 | 0.00067 | not rejected |
| captures_total :: bonus_forfeited x focus_rear | 0.0557 | [-0.0171, 0.1284] | 0.1338 | 0.00078 | not rejected |
| lead_changes_per_turn :: bonus_forfeited x focus_rear | -0.0000 | [-0.0001, 0.0001] | 0.5290 | 0.00192 | not rejected |
| comeback_rate :: bonus_forfeited x focus_rear | 0.0003 | [-0.0018, 0.0024] | 0.7668 | 0.00417 | not rejected |
| win_rate_by_starting_seat :: bonus_forfeited x greedy_capture | 0.0013 | [-0.0009, 0.0035] | 0.2437 | 0.00093 | not rejected |
| rounds_to_first_win :: bonus_forfeited x greedy_capture | 0.1503 | [0.0310, 0.2696] | 0.0135 | 0.00061 | not rejected |
| captures_total :: bonus_forfeited x greedy_capture | 0.0511 | [-0.0233, 0.1256] | 0.1783 | 0.00083 | not rejected |
| lead_changes_per_turn :: bonus_forfeited x greedy_capture | -0.0000 | [-0.0001, 0.0001] | 0.7244 | 0.00357 | not rejected |
| comeback_rate :: bonus_forfeited x greedy_capture | 0.0014 | [-0.0006, 0.0035] | 0.1749 | 0.00082 | not rejected |

**92 of 180 rejected** after Holm correction.

### RQ-9

135 tests, Holm-corrected within the family at alpha = 0.05.

| Contrast | Estimate | 95% CI | p | Holm alpha | Verdict |
|---|---:|---|---:|---:|---|
| win_rate_by_starting_seat :: cold_start:strict x 2 | -0.0011 | [-0.0035, 0.0013] | 0.3731 | 0.00200 | not rejected |
| rounds_to_first_win :: cold_start:strict x 2 | -0.0187 | [-0.1213, 0.0838] | 0.7203 | 0.00417 | not rejected |
| captures_total :: cold_start:strict x 2 | 0.3388 | [0.2844, 0.3933] | &lt;1e-300 | 0.00037 | **rejected** |
| lead_changes_per_turn :: cold_start:strict x 2 | -0.0112 | [-0.0114, -0.0111] | &lt;1e-300 | 0.00037 | **rejected** |
| comeback_rate :: cold_start:strict x 2 | -0.0149 | [-0.0171, -0.0127] | &lt;1e-300 | 0.00038 | **rejected** |
| win_rate_by_starting_seat :: cold_start:strict x 3 | -0.0020 | [-0.0043, 0.0003] | 0.0849 | 0.00119 | not rejected |
| rounds_to_first_win :: cold_start:strict x 3 | -0.0317 | [-0.1445, 0.0812] | 0.5825 | 0.00278 | not rejected |
| captures_total :: cold_start:strict x 3 | 0.1393 | [0.0792, 0.1993] | 5.45e-06 | 0.00083 | **rejected** |
| lead_changes_per_turn :: cold_start:strict x 3 | -0.0050 | [-0.0051, -0.0048] | &lt;1e-300 | 0.00038 | **rejected** |
| comeback_rate :: cold_start:strict x 3 | -0.0045 | [-0.0068, -0.0022] | 0.0001 | 0.00091 | **rejected** |
| win_rate_by_starting_seat :: cold_start:strict x 6 | -0.0007 | [-0.0028, 0.0013] | 0.4953 | 0.00238 | not rejected |
| rounds_to_first_win :: cold_start:strict x 6 | 0.0244 | [-0.1471, 0.1958] | 0.7805 | 0.00556 | not rejected |
| captures_total :: cold_start:strict x 6 | -0.3399 | [-0.4843, -0.1955] | 3.98e-06 | 0.00082 | **rejected** |
| lead_changes_per_turn :: cold_start:strict x 6 | 0.0053 | [0.0052, 0.0054] | &lt;1e-300 | 0.00038 | **rejected** |
| comeback_rate :: cold_start:strict x 6 | -0.0017 | [-0.0039, 0.0005] | 0.1299 | 0.00139 | not rejected |
| win_rate_by_starting_seat :: cold_start:free_entry x 2 | 0.0007 | [-0.0017, 0.0030] | 0.5853 | 0.00294 | not rejected |
| rounds_to_first_win :: cold_start:free_entry x 2 | -28.3 | [-28.5, -28.2] | &lt;1e-300 | 0.00038 | **rejected** |
| captures_total :: cold_start:free_entry x 2 | -55.0 | [-55.1, -54.9] | &lt;1e-300 | 0.00039 | **rejected** |
| lead_changes_per_turn :: cold_start:free_entry x 2 | -0.0013 | [-0.0014, -0.0011] | &lt;1e-300 | 0.00039 | **rejected** |
| comeback_rate :: cold_start:free_entry x 2 | -0.0059 | [-0.0081, -0.0037] | 1.13e-07 | 0.00077 | **rejected** |
| win_rate_by_starting_seat :: cold_start:free_entry x 3 | 0.0005 | [-0.0018, 0.0028] | 0.7002 | 0.00357 | not rejected |
| rounds_to_first_win :: cold_start:free_entry x 3 | -20.9 | [-21.0, -20.7] | &lt;1e-300 | 0.00039 | **rejected** |
| captures_total :: cold_start:free_entry x 3 | -42.5 | [-42.6, -42.4] | &lt;1e-300 | 0.00040 | **rejected** |
| lead_changes_per_turn :: cold_start:free_entry x 3 | -0.0011 | [-0.0012, -0.0010] | &lt;1e-300 | 0.00040 | **rejected** |
| comeback_rate :: cold_start:free_entry x 3 | -0.0056 | [-0.0078, -0.0033] | 1.80e-06 | 0.00081 | **rejected** |
| win_rate_by_starting_seat :: cold_start:free_entry x 6 | 0.0016 | [-0.0004, 0.0037] | 0.1173 | 0.00132 | not rejected |
| rounds_to_first_win :: cold_start:free_entry x 6 | 130.3 | [130.0, 130.6] | &lt;1e-300 | 0.00040 | **rejected** |
| captures_total :: cold_start:free_entry x 6 | 394.7 | [394.2, 395.2] | &lt;1e-300 | 0.00041 | **rejected** |
| lead_changes_per_turn :: cold_start:free_entry x 6 | 0.0025 | [0.0024, 0.0026] | &lt;1e-300 | 0.00041 | **rejected** |
| comeback_rate :: cold_start:free_entry x 6 | -0.0089 | [-0.0111, -0.0067] | 8.88e-16 | 0.00069 | **rejected** |
| win_rate_by_starting_seat :: capture:mandatory x 2 | -0.0004 | [-0.0028, 0.0020] | 0.7296 | 0.00455 | not rejected |
| rounds_to_first_win :: capture:mandatory x 2 | -23.9 | [-24.1, -23.8] | &lt;1e-300 | 0.00041 | **rejected** |
| captures_total :: capture:mandatory x 2 | -24.4 | [-24.5, -24.4] | &lt;1e-300 | 0.00042 | **rejected** |
| lead_changes_per_turn :: capture:mandatory x 2 | -0.0014 | [-0.0016, -0.0013] | &lt;1e-300 | 0.00042 | **rejected** |
| comeback_rate :: capture:mandatory x 2 | 0.0033 | [0.0011, 0.0055] | 0.0037 | 0.00098 | not rejected |
| win_rate_by_starting_seat :: capture:mandatory x 3 | 0.0006 | [-0.0017, 0.0029] | 0.6173 | 0.00313 | not rejected |
| rounds_to_first_win :: capture:mandatory x 3 | -12.1 | [-12.3, -12.0] | &lt;1e-300 | 0.00042 | **rejected** |
| captures_total :: capture:mandatory x 3 | -15.2 | [-15.3, -15.1] | &lt;1e-300 | 0.00043 | **rejected** |
| lead_changes_per_turn :: capture:mandatory x 3 | -0.0011 | [-0.0012, -0.0010] | &lt;1e-300 | 0.00043 | **rejected** |
| comeback_rate :: capture:mandatory x 3 | -0.0026 | [-0.0049, -0.0004] | 0.0237 | 0.00109 | not rejected |
| win_rate_by_starting_seat :: capture:mandatory x 6 | 0.0012 | [-0.0009, 0.0032] | 0.2624 | 0.00185 | not rejected |
| rounds_to_first_win :: capture:mandatory x 6 | 22.4 | [22.2, 22.6] | &lt;1e-300 | 0.00043 | **rejected** |
| captures_total :: capture:mandatory x 6 | 50.5 | [50.3, 50.6] | &lt;1e-300 | 0.00044 | **rejected** |
| lead_changes_per_turn :: capture:mandatory x 6 | 0.0020 | [0.0020, 0.0021] | &lt;1e-300 | 0.00044 | **rejected** |
| comeback_rate :: capture:mandatory x 6 | -0.0055 | [-0.0077, -0.0033] | 8.37e-07 | 0.00079 | **rejected** |
| win_rate_by_starting_seat :: capture:mandatory_extended x 2 | 0.0002 | [-0.0022, 0.0025] | 0.8828 | 0.01250 | not rejected |
| rounds_to_first_win :: capture:mandatory_extended x 2 | -37.4 | [-37.6, -37.3] | &lt;1e-300 | 0.00045 | **rejected** |
| captures_total :: capture:mandatory_extended x 2 | -35.6 | [-35.7, -35.5] | &lt;1e-300 | 0.00045 | **rejected** |
| lead_changes_per_turn :: capture:mandatory_extended x 2 | -0.0014 | [-0.0016, -0.0013] | &lt;1e-300 | 0.00045 | **rejected** |
| comeback_rate :: capture:mandatory_extended x 2 | 0.0028 | [0.0005, 0.0050] | 0.0147 | 0.00102 | not rejected |
| win_rate_by_starting_seat :: capture:mandatory_extended x 3 | -0.0010 | [-0.0033, 0.0013] | 0.4060 | 0.00217 | not rejected |
| rounds_to_first_win :: capture:mandatory_extended x 3 | -19.1 | [-19.3, -18.9] | &lt;1e-300 | 0.00046 | **rejected** |
| captures_total :: capture:mandatory_extended x 3 | -22.5 | [-22.6, -22.4] | &lt;1e-300 | 0.00046 | **rejected** |
| lead_changes_per_turn :: capture:mandatory_extended x 3 | -0.0012 | [-0.0013, -0.0011] | &lt;1e-300 | 0.00047 | **rejected** |
| comeback_rate :: capture:mandatory_extended x 3 | -0.0018 | [-0.0041, 0.0005] | 0.1259 | 0.00135 | not rejected |
| win_rate_by_starting_seat :: capture:mandatory_extended x 6 | 0.0004 | [-0.0016, 0.0025] | 0.6838 | 0.00333 | not rejected |
| rounds_to_first_win :: capture:mandatory_extended x 6 | 39.2 | [38.9, 39.4] | &lt;1e-300 | 0.00047 | **rejected** |
| captures_total :: capture:mandatory_extended x 6 | 79.1 | [78.9, 79.3] | &lt;1e-300 | 0.00048 | **rejected** |
| lead_changes_per_turn :: capture:mandatory_extended x 6 | 0.0024 | [0.0023, 0.0024] | &lt;1e-300 | 0.00048 | **rejected** |
| comeback_rate :: capture:mandatory_extended x 6 | -0.0027 | [-0.0049, -0.0005] | 0.0171 | 0.00104 | not rejected |
| win_rate_by_starting_seat :: dreimal x 2 | -0.0016 | [-0.0039, 0.0008] | 0.1995 | 0.00167 | not rejected |
| rounds_to_first_win :: dreimal x 2 | -0.8319 | [-0.9323, -0.7315] | &lt;1e-300 | 0.00049 | **rejected** |
| captures_total :: dreimal x 2 | -5.4855 | [-5.5427, -5.4284] | &lt;1e-300 | 0.00049 | **rejected** |
| lead_changes_per_turn :: dreimal x 2 | 0.0009 | [0.0007, 0.0010] | &lt;1e-300 | 0.00050 | **rejected** |
| comeback_rate :: dreimal x 2 | 0.0102 | [0.0080, 0.0124] | &lt;1e-300 | 0.00050 | **rejected** |
| win_rate_by_starting_seat :: dreimal x 3 | -0.0021 | [-0.0044, 0.0002] | 0.0749 | 0.00116 | not rejected |
| rounds_to_first_win :: dreimal x 3 | -0.7694 | [-0.8800, -0.6587] | &lt;1e-300 | 0.00051 | **rejected** |
| captures_total :: dreimal x 3 | -4.1587 | [-4.2214, -4.0960] | &lt;1e-300 | 0.00051 | **rejected** |
| lead_changes_per_turn :: dreimal x 3 | 0.0003 | [0.0001, 0.0004] | 3.07e-05 | 0.00086 | **rejected** |
| comeback_rate :: dreimal x 3 | 0.0004 | [-0.0018, 0.0027] | 0.7012 | 0.00385 | not rejected |
| win_rate_by_starting_seat :: dreimal x 6 | -0.0015 | [-0.0035, 0.0006] | 0.1549 | 0.00147 | not rejected |
| rounds_to_first_win :: dreimal x 6 | 6.7326 | [6.5583, 6.9068] | &lt;1e-300 | 0.00052 | **rejected** |
| captures_total :: dreimal x 6 | 31.2 | [31.0, 31.4] | &lt;1e-300 | 0.00052 | **rejected** |
| lead_changes_per_turn :: dreimal x 6 | 0.0001 | [0.0000, 0.0002] | 0.0033 | 0.00096 | not rejected |
| comeback_rate :: dreimal x 6 | -0.0038 | [-0.0059, -0.0016] | 0.0007 | 0.00094 | **rejected** |
| win_rate_by_starting_seat :: bonus_quick x 2 | 0.0011 | [-0.0013, 0.0034] | 0.3739 | 0.00208 | not rejected |
| rounds_to_first_win :: bonus_quick x 2 | 3.2701 | [3.1753, 3.3649] | &lt;1e-300 | 0.00053 | **rejected** |
| captures_total :: bonus_quick x 2 | -0.6874 | [-0.7474, -0.6274] | &lt;1e-300 | 0.00053 | **rejected** |
| lead_changes_per_turn :: bonus_quick x 2 | -0.0021 | [-0.0023, -0.0019] | &lt;1e-300 | 0.00054 | **rejected** |
| comeback_rate :: bonus_quick x 2 | -0.0089 | [-0.0111, -0.0067] | 1.33e-15 | 0.00070 | **rejected** |
| win_rate_by_starting_seat :: bonus_quick x 3 | 0.0008 | [-0.0015, 0.0031] | 0.5038 | 0.00263 | not rejected |
| rounds_to_first_win :: bonus_quick x 3 | 1.5592 | [1.4549, 1.6635] | &lt;1e-300 | 0.00054 | **rejected** |
| captures_total :: bonus_quick x 3 | -0.6293 | [-0.6949, -0.5637] | &lt;1e-300 | 0.00055 | **rejected** |
| lead_changes_per_turn :: bonus_quick x 3 | -0.0004 | [-0.0005, -0.0003] | 3.93e-09 | 0.00075 | **rejected** |
| comeback_rate :: bonus_quick x 3 | -0.0019 | [-0.0042, 0.0004] | 0.0998 | 0.00122 | not rejected |
| win_rate_by_starting_seat :: bonus_quick x 6 | 0.0015 | [-0.0005, 0.0036] | 0.1459 | 0.00143 | not rejected |
| rounds_to_first_win :: bonus_quick x 6 | 0.1239 | [-0.0485, 0.2963] | 0.1590 | 0.00152 | not rejected |
| captures_total :: bonus_quick x 6 | 11.2 | [11.0, 11.4] | &lt;1e-300 | 0.00056 | **rejected** |
| lead_changes_per_turn :: bonus_quick x 6 | -0.0002 | [-0.0003, -0.0001] | 3.83e-07 | 0.00078 | **rejected** |
| comeback_rate :: bonus_quick x 6 | -0.0004 | [-0.0025, 0.0018] | 0.7342 | 0.00500 | not rejected |
| win_rate_by_starting_seat :: goal_no_jump x 2 | -0.0016 | [-0.0040, 0.0008] | 0.1900 | 0.00156 | not rejected |
| rounds_to_first_win :: goal_no_jump x 2 | 1.7053 | [1.6028, 1.8078] | &lt;1e-300 | 0.00056 | **rejected** |
| captures_total :: goal_no_jump x 2 | -1.2694 | [-1.3241, -1.2148] | &lt;1e-300 | 0.00057 | **rejected** |
| lead_changes_per_turn :: goal_no_jump x 2 | -0.0019 | [-0.0020, -0.0017] | &lt;1e-300 | 0.00057 | **rejected** |
| comeback_rate :: goal_no_jump x 2 | 0.0234 | [0.0212, 0.0256] | &lt;1e-300 | 0.00058 | **rejected** |
| win_rate_by_starting_seat :: goal_no_jump x 3 | 0.0003 | [-0.0020, 0.0026] | 0.8182 | 0.00625 | not rejected |
| rounds_to_first_win :: goal_no_jump x 3 | 0.8753 | [0.7628, 0.9879] | &lt;1e-300 | 0.00059 | **rejected** |
| captures_total :: goal_no_jump x 3 | -0.6618 | [-0.7221, -0.6016] | &lt;1e-300 | 0.00060 | **rejected** |
| lead_changes_per_turn :: goal_no_jump x 3 | -0.0007 | [-0.0008, -0.0006] | &lt;1e-300 | 0.00060 | **rejected** |
| comeback_rate :: goal_no_jump x 3 | 0.0067 | [0.0044, 0.0089] | 1.06e-08 | 0.00076 | **rejected** |
| win_rate_by_starting_seat :: goal_no_jump x 6 | 0.0001 | [-0.0020, 0.0022] | 0.9253 | 0.01667 | not rejected |
| rounds_to_first_win :: goal_no_jump x 6 | -1.3809 | [-1.5517, -1.2100] | &lt;1e-300 | 0.00061 | **rejected** |
| captures_total :: goal_no_jump x 6 | 1.1829 | [1.0382, 1.3275] | &lt;1e-300 | 0.00062 | **rejected** |
| lead_changes_per_turn :: goal_no_jump x 6 | 0.0007 | [0.0006, 0.0008] | &lt;1e-300 | 0.00063 | **rejected** |
| comeback_rate :: goal_no_jump x 6 | -0.0026 | [-0.0048, -0.0004] | 0.0195 | 0.00106 | not rejected |
| win_rate_by_starting_seat :: barriers x 2 | 0.0025 | [0.0002, 0.0049] | 0.0363 | 0.00114 | not rejected |
| rounds_to_first_win :: barriers x 2 | 1.2686 | [1.1684, 1.3688] | &lt;1e-300 | 0.00063 | **rejected** |
| captures_total :: barriers x 2 | 1.9164 | [1.8633, 1.9695] | &lt;1e-300 | 0.00064 | **rejected** |
| lead_changes_per_turn :: barriers x 2 | 0.0004 | [0.0002, 0.0005] | 1.20e-05 | 0.00085 | **rejected** |
| comeback_rate :: barriers x 2 | -0.0018 | [-0.0040, 0.0004] | 0.1114 | 0.00128 | not rejected |
| win_rate_by_starting_seat :: barriers x 3 | 0.0015 | [-0.0008, 0.0038] | 0.1990 | 0.00161 | not rejected |
| rounds_to_first_win :: barriers x 3 | 0.4091 | [0.2986, 0.5195] | 3.95e-13 | 0.00072 | **rejected** |
| captures_total :: barriers x 3 | 1.0659 | [1.0075, 1.1244] | &lt;1e-300 | 0.00065 | **rejected** |
| lead_changes_per_turn :: barriers x 3 | 0.0003 | [0.0001, 0.0004] | 3.56e-05 | 0.00088 | **rejected** |
| comeback_rate :: barriers x 3 | -0.0010 | [-0.0033, 0.0013] | 0.4092 | 0.00227 | not rejected |
| win_rate_by_starting_seat :: barriers x 6 | 0.0012 | [-0.0009, 0.0032] | 0.2543 | 0.00179 | not rejected |
| rounds_to_first_win :: barriers x 6 | 0.7647 | [0.5953, 0.9340] | &lt;1e-300 | 0.00066 | **rejected** |
| captures_total :: barriers x 6 | -1.4598 | [-1.6018, -1.3179] | &lt;1e-300 | 0.00067 | **rejected** |
| lead_changes_per_turn :: barriers x 6 | -0.0001 | [-0.0002, 0.0000] | 0.1053 | 0.00125 | not rejected |
| comeback_rate :: barriers x 6 | 0.0000 | [-0.0022, 0.0022] | 0.9833 | 0.05000 | not rejected |
| win_rate_by_starting_seat :: bonus_forfeited x 2 | 0.0015 | [-0.0008, 0.0039] | 0.2008 | 0.00172 | not rejected |
| rounds_to_first_win :: bonus_forfeited x 2 | -0.3432 | [-0.4457, -0.2408] | 5.07e-11 | 0.00074 | **rejected** |
| captures_total :: bonus_forfeited x 2 | -0.2114 | [-0.2659, -0.1568] | 3.11e-14 | 0.00071 | **rejected** |
| lead_changes_per_turn :: bonus_forfeited x 2 | -0.0000 | [-0.0002, 0.0001] | 0.8390 | 0.00833 | not rejected |
| comeback_rate :: bonus_forfeited x 2 | 0.0008 | [-0.0014, 0.0030] | 0.5010 | 0.00250 | not rejected |
| win_rate_by_starting_seat :: bonus_forfeited x 3 | 0.0011 | [-0.0012, 0.0034] | 0.3318 | 0.00192 | not rejected |
| rounds_to_first_win :: bonus_forfeited x 3 | -0.1260 | [-0.2390, -0.0131] | 0.0288 | 0.00111 | not rejected |
| captures_total :: bonus_forfeited x 3 | -0.1171 | [-0.1772, -0.0570] | 0.0001 | 0.00093 | **rejected** |
| lead_changes_per_turn :: bonus_forfeited x 3 | -0.0000 | [-0.0001, 0.0001] | 0.8264 | 0.00714 | not rejected |
| comeback_rate :: bonus_forfeited x 3 | -0.0000 | [-0.0023, 0.0023] | 0.9784 | 0.02500 | not rejected |
| win_rate_by_starting_seat :: bonus_forfeited x 6 | 0.0002 | [-0.0019, 0.0022] | 0.8712 | 0.01000 | not rejected |
| rounds_to_first_win :: bonus_forfeited x 6 | 0.8184 | [0.6462, 0.9906] | &lt;1e-300 | 0.00068 | **rejected** |
| captures_total :: bonus_forfeited x 6 | 0.8820 | [0.7372, 1.0269] | &lt;1e-300 | 0.00068 | **rejected** |
| lead_changes_per_turn :: bonus_forfeited x 6 | 0.0002 | [0.0001, 0.0003] | 7.71e-05 | 0.00089 | **rejected** |
| comeback_rate :: bonus_forfeited x 6 | -0.0028 | [-0.0050, -0.0006] | 0.0115 | 0.00100 | not rejected |

**83 of 135 rejected** after Holm correction.

### RQ-10

60 tests, Holm-corrected within the family at alpha = 0.05.

| Contrast | Estimate | 95% CI | p | Holm alpha | Verdict |
|---|---:|---|---:|---:|---|
| win_rate_by_starting_seat :: spread x 2p | -0.0006 | [-0.0030, 0.0017] | 0.6066 | 0.00833 | not rejected |
| rounds_to_first_win :: spread x 2p | -4.5505 | [-4.6596, -4.4414] | &lt;1e-300 | 0.00083 | **rejected** |
| captures_total :: spread x 2p | -4.7554 | [-4.8137, -4.6971] | &lt;1e-300 | 0.00085 | **rejected** |
| lead_changes_per_turn :: spread x 2p | -0.0006 | [-0.0007, -0.0004] | 1.15e-11 | 0.00227 | **rejected** |
| comeback_rate :: spread x 2p | -0.0093 | [-0.0115, -0.0071] | &lt;1e-300 | 0.00086 | **rejected** |
| win_rate_by_starting_seat :: spread x 3p | 0.0005 | [-0.0018, 0.0028] | 0.6859 | 0.01250 | not rejected |
| rounds_to_first_win :: spread x 3p | -1.6844 | [-1.8049, -1.5639] | &lt;1e-300 | 0.00088 | **rejected** |
| captures_total :: spread x 3p | -2.9338 | [-2.9983, -2.8693] | &lt;1e-300 | 0.00089 | **rejected** |
| lead_changes_per_turn :: spread x 3p | -0.0003 | [-0.0004, -0.0001] | 1.26e-05 | 0.00250 | **rejected** |
| comeback_rate :: spread x 3p | 0.0186 | [0.0163, 0.0209] | &lt;1e-300 | 0.00091 | **rejected** |
| win_rate_by_starting_seat :: spread x 6p | 0.0003 | [-0.0018, 0.0023] | 0.7956 | 0.01667 | not rejected |
| rounds_to_first_win :: spread x 6p | 0.8346 | [0.6555, 1.0136] | &lt;1e-300 | 0.00093 | **rejected** |
| captures_total :: spread x 6p | 6.1726 | [6.0214, 6.3239] | &lt;1e-300 | 0.00094 | **rejected** |
| lead_changes_per_turn :: spread x 6p | 0.0006 | [0.0006, 0.0007] | &lt;1e-300 | 0.00096 | **rejected** |
| comeback_rate :: spread x 6p | -0.0124 | [-0.0146, -0.0102] | &lt;1e-300 | 0.00098 | **rejected** |
| win_rate_by_starting_seat :: focus_front x 2p | -0.0002 | [-0.0026, 0.0022] | 0.8590 | 0.02500 | not rejected |
| rounds_to_first_win :: focus_front x 2p | 8.6076 | [8.5123, 8.7028] | &lt;1e-300 | 0.00100 | **rejected** |
| captures_total :: focus_front x 2p | 5.5469 | [5.4964, 5.5975] | &lt;1e-300 | 0.00102 | **rejected** |
| lead_changes_per_turn :: focus_front x 2p | -0.0004 | [-0.0006, -0.0003] | 4.43e-07 | 0.00238 | **rejected** |
| comeback_rate :: focus_front x 2p | -0.0035 | [-0.0057, -0.0014] | 0.0013 | 0.00313 | **rejected** |
| win_rate_by_starting_seat :: focus_front x 3p | 0.0012 | [-0.0011, 0.0035] | 0.3151 | 0.00556 | not rejected |
| rounds_to_first_win :: focus_front x 3p | 4.5619 | [4.4570, 4.6668] | &lt;1e-300 | 0.00104 | **rejected** |
| captures_total :: focus_front x 3p | 3.5836 | [3.5279, 3.6394] | &lt;1e-300 | 0.00106 | **rejected** |
| lead_changes_per_turn :: focus_front x 3p | -0.0001 | [-0.0003, -0.0000] | 0.0488 | 0.00417 | not rejected |
| comeback_rate :: focus_front x 3p | -0.0160 | [-0.0183, -0.0138] | &lt;1e-300 | 0.00109 | **rejected** |
| win_rate_by_starting_seat :: focus_front x 6p | 0.0021 | [0.0001, 0.0042] | 0.0432 | 0.00357 | not rejected |
| rounds_to_first_win :: focus_front x 6p | -7.6604 | [-7.8204, -7.5004] | &lt;1e-300 | 0.00111 | **rejected** |
| captures_total :: focus_front x 6p | -10.6 | [-10.7, -10.5] | &lt;1e-300 | 0.00114 | **rejected** |
| lead_changes_per_turn :: focus_front x 6p | 0.0005 | [0.0004, 0.0006] | &lt;1e-300 | 0.00116 | **rejected** |
| comeback_rate :: focus_front x 6p | -0.0044 | [-0.0065, -0.0023] | 5.64e-05 | 0.00294 | **rejected** |
| win_rate_by_starting_seat :: focus_rear x 2p | -0.0008 | [-0.0032, 0.0016] | 0.5193 | 0.00625 | not rejected |
| rounds_to_first_win :: focus_rear x 2p | -3.7726 | [-3.8811, -3.6642] | &lt;1e-300 | 0.00119 | **rejected** |
| captures_total :: focus_rear x 2p | -4.2386 | [-4.2966, -4.1806] | &lt;1e-300 | 0.00122 | **rejected** |
| lead_changes_per_turn :: focus_rear x 2p | -0.0003 | [-0.0005, -0.0002] | 4.70e-05 | 0.00263 | **rejected** |
| comeback_rate :: focus_rear x 2p | -0.0046 | [-0.0067, -0.0024] | 4.95e-05 | 0.00278 | **rejected** |
| win_rate_by_starting_seat :: focus_rear x 3p | -0.0001 | [-0.0024, 0.0022] | 0.9468 | 0.05000 | not rejected |
| rounds_to_first_win :: focus_rear x 3p | -1.4752 | [-1.5949, -1.3554] | &lt;1e-300 | 0.00125 | **rejected** |
| captures_total :: focus_rear x 3p | -2.5928 | [-2.6569, -2.5288] | &lt;1e-300 | 0.00128 | **rejected** |
| lead_changes_per_turn :: focus_rear x 3p | -0.0002 | [-0.0003, -0.0001] | 0.0018 | 0.00333 | **rejected** |
| comeback_rate :: focus_rear x 3p | 0.0094 | [0.0071, 0.0117] | 8.88e-16 | 0.00217 | **rejected** |
| win_rate_by_starting_seat :: focus_rear x 6p | 0.0015 | [-0.0006, 0.0035] | 0.1649 | 0.00500 | not rejected |
| rounds_to_first_win :: focus_rear x 6p | 0.7822 | [0.6036, 0.9609] | &lt;1e-300 | 0.00132 | **rejected** |
| captures_total :: focus_rear x 6p | 5.8124 | [5.6615, 5.9634] | &lt;1e-300 | 0.00135 | **rejected** |
| lead_changes_per_turn :: focus_rear x 6p | 0.0006 | [0.0005, 0.0006] | &lt;1e-300 | 0.00139 | **rejected** |
| comeback_rate :: focus_rear x 6p | -0.0096 | [-0.0118, -0.0074] | &lt;1e-300 | 0.00143 | **rejected** |
| win_rate_by_starting_seat :: greedy_capture x 2p | -0.0020 | [-0.0043, 0.0004] | 0.1072 | 0.00455 | not rejected |
| rounds_to_first_win :: greedy_capture x 2p | -4.5050 | [-4.6162, -4.3937] | &lt;1e-300 | 0.00147 | **rejected** |
| captures_total :: greedy_capture x 2p | -5.5896 | [-5.6499, -5.5292] | &lt;1e-300 | 0.00152 | **rejected** |
| lead_changes_per_turn :: greedy_capture x 2p | -0.0034 | [-0.0036, -0.0033] | &lt;1e-300 | 0.00156 | **rejected** |
| comeback_rate :: greedy_capture x 2p | -0.0293 | [-0.0315, -0.0272] | &lt;1e-300 | 0.00161 | **rejected** |
| win_rate_by_starting_seat :: greedy_capture x 3p | -0.0023 | [-0.0046, -0.0000] | 0.0467 | 0.00385 | not rejected |
| rounds_to_first_win :: greedy_capture x 3p | -1.4413 | [-1.5643, -1.3182] | &lt;1e-300 | 0.00167 | **rejected** |
| captures_total :: greedy_capture x 3p | -2.8286 | [-2.8954, -2.7619] | &lt;1e-300 | 0.00172 | **rejected** |
| lead_changes_per_turn :: greedy_capture x 3p | -0.0014 | [-0.0015, -0.0013] | &lt;1e-300 | 0.00179 | **rejected** |
| comeback_rate :: greedy_capture x 3p | -0.0136 | [-0.0158, -0.0113] | &lt;1e-300 | 0.00185 | **rejected** |
| win_rate_by_starting_seat :: greedy_capture x 6p | 0.0004 | [-0.0016, 0.0025] | 0.6692 | 0.01000 | not rejected |
| rounds_to_first_win :: greedy_capture x 6p | 0.7645 | [0.5823, 0.9467] | 2.22e-16 | 0.00208 | **rejected** |
| captures_total :: greedy_capture x 6p | 6.0252 | [5.8712, 6.1792] | &lt;1e-300 | 0.00192 | **rejected** |
| lead_changes_per_turn :: greedy_capture x 6p | 0.0013 | [0.0012, 0.0014] | &lt;1e-300 | 0.00200 | **rejected** |
| comeback_rate :: greedy_capture x 6p | 0.0006 | [-0.0016, 0.0028] | 0.5962 | 0.00714 | not rejected |

**46 of 60 rejected** after Holm correction.

### RQ-11

45 tests, Holm-corrected within the family at alpha = 0.05.

| Contrast | Estimate | 95% CI | p | Holm alpha | Verdict |
|---|---:|---|---:|---:|---|
| win_rate_by_starting_seat :: cold_start:strict x opposite | 0.0016 | [-0.0010, 0.0041] | 0.2249 | 0.00238 | not rejected |
| rounds_to_first_win :: cold_start:strict x opposite | 0.2716 | [0.2088, 0.3344] | &lt;1e-300 | 0.00111 | **rejected** |
| captures_total :: cold_start:strict x opposite | 0.1105 | [0.0946, 0.1264] | &lt;1e-300 | 0.00114 | **rejected** |
| lead_changes_per_turn :: cold_start:strict x opposite | -0.0013 | [-0.0015, -0.0011] | &lt;1e-300 | 0.00116 | **rejected** |
| comeback_rate :: cold_start:strict x opposite | -0.0012 | [-0.0036, 0.0011] | 0.3077 | 0.00263 | not rejected |
| win_rate_by_starting_seat :: cold_start:free_entry x opposite | 0.0009 | [-0.0016, 0.0035] | 0.4673 | 0.00357 | not rejected |
| rounds_to_first_win :: cold_start:free_entry x opposite | -1.0884 | [-1.1505, -1.0263] | &lt;1e-300 | 0.00119 | **rejected** |
| captures_total :: cold_start:free_entry x opposite | -1.0817 | [-1.1004, -1.0629] | &lt;1e-300 | 0.00122 | **rejected** |
| lead_changes_per_turn :: cold_start:free_entry x opposite | 0.0022 | [0.0020, 0.0024] | &lt;1e-300 | 0.00125 | **rejected** |
| comeback_rate :: cold_start:free_entry x opposite | 0.0092 | [0.0069, 0.0116] | 1.64e-14 | 0.00167 | **rejected** |
| win_rate_by_starting_seat :: capture:mandatory x opposite | 0.0005 | [-0.0020, 0.0030] | 0.6975 | 0.00714 | not rejected |
| rounds_to_first_win :: capture:mandatory x opposite | 1.9655 | [1.8893, 2.0417] | &lt;1e-300 | 0.00128 | **rejected** |
| captures_total :: capture:mandatory x opposite | 0.5845 | [0.5628, 0.6061] | &lt;1e-300 | 0.00132 | **rejected** |
| lead_changes_per_turn :: capture:mandatory x opposite | -0.0002 | [-0.0004, 0.0000] | 0.1235 | 0.00217 | not rejected |
| comeback_rate :: capture:mandatory x opposite | -0.0097 | [-0.0121, -0.0074] | 4.44e-16 | 0.00156 | **rejected** |
| win_rate_by_starting_seat :: capture:mandatory_extended x opposite | -0.0012 | [-0.0037, 0.0014] | 0.3682 | 0.00294 | not rejected |
| rounds_to_first_win :: capture:mandatory_extended x opposite | 2.0097 | [1.9226, 2.0968] | &lt;1e-300 | 0.00135 | **rejected** |
| captures_total :: capture:mandatory_extended x opposite | 0.5582 | [0.5343, 0.5820] | &lt;1e-300 | 0.00139 | **rejected** |
| lead_changes_per_turn :: capture:mandatory_extended x opposite | -0.0001 | [-0.0003, 0.0001] | 0.5046 | 0.00417 | not rejected |
| comeback_rate :: capture:mandatory_extended x opposite | -0.0100 | [-0.0124, -0.0077] | &lt;1e-300 | 0.00143 | **rejected** |
| win_rate_by_starting_seat :: dreimal x opposite | 0.0002 | [-0.0023, 0.0027] | 0.8667 | 0.01250 | not rejected |
| rounds_to_first_win :: dreimal x opposite | 0.0261 | [-0.0337, 0.0859] | 0.3924 | 0.00333 | not rejected |
| captures_total :: dreimal x opposite | -0.0780 | [-0.0941, -0.0620] | &lt;1e-300 | 0.00147 | **rejected** |
| lead_changes_per_turn :: dreimal x opposite | -0.0009 | [-0.0011, -0.0007] | 4.95e-14 | 0.00172 | **rejected** |
| comeback_rate :: dreimal x opposite | -0.0045 | [-0.0068, -0.0021] | 0.0002 | 0.00185 | **rejected** |
| win_rate_by_starting_seat :: bonus_quick x opposite | 0.0013 | [-0.0013, 0.0038] | 0.3233 | 0.00278 | not rejected |
| rounds_to_first_win :: bonus_quick x opposite | 0.1519 | [0.0959, 0.2079] | 1.05e-07 | 0.00179 | **rejected** |
| captures_total :: bonus_quick x opposite | 0.0041 | [-0.0121, 0.0203] | 0.6198 | 0.00500 | not rejected |
| lead_changes_per_turn :: bonus_quick x opposite | 0.0001 | [-0.0002, 0.0003] | 0.5025 | 0.00385 | not rejected |
| comeback_rate :: bonus_quick x opposite | 0.0035 | [0.0011, 0.0058] | 0.0037 | 0.00200 | not rejected |
| win_rate_by_starting_seat :: goal_no_jump x opposite | -0.0006 | [-0.0031, 0.0020] | 0.6541 | 0.00625 | not rejected |
| rounds_to_first_win :: goal_no_jump x opposite | 0.1020 | [0.0383, 0.1658] | 0.0017 | 0.00192 | **rejected** |
| captures_total :: goal_no_jump x opposite | 0.0219 | [0.0058, 0.0381] | 0.0078 | 0.00208 | not rejected |
| lead_changes_per_turn :: goal_no_jump x opposite | -0.0002 | [-0.0004, 0.0001] | 0.1538 | 0.00227 | not rejected |
| comeback_rate :: goal_no_jump x opposite | 0.0003 | [-0.0021, 0.0027] | 0.8024 | 0.00833 | not rejected |
| win_rate_by_starting_seat :: barriers x opposite | -0.0001 | [-0.0027, 0.0024] | 0.9075 | 0.01667 | not rejected |
| rounds_to_first_win :: barriers x opposite | -0.2515 | [-0.3117, -0.1913] | 2.22e-16 | 0.00152 | **rejected** |
| captures_total :: barriers x opposite | -0.0613 | [-0.0768, -0.0458] | 7.99e-15 | 0.00161 | **rejected** |
| lead_changes_per_turn :: barriers x opposite | 0.0001 | [-0.0001, 0.0003] | 0.3857 | 0.00313 | not rejected |
| comeback_rate :: barriers x opposite | -0.0012 | [-0.0036, 0.0011] | 0.3040 | 0.00250 | not rejected |
| win_rate_by_starting_seat :: bonus_forfeited x opposite | -0.0007 | [-0.0032, 0.0019] | 0.5992 | 0.00455 | not rejected |
| rounds_to_first_win :: bonus_forfeited x opposite | -0.0005 | [-0.0623, 0.0613] | 0.9871 | 0.05000 | not rejected |
| captures_total :: bonus_forfeited x opposite | -0.0037 | [-0.0196, 0.0122] | 0.6457 | 0.00556 | not rejected |
| lead_changes_per_turn :: bonus_forfeited x opposite | 0.0000 | [-0.0002, 0.0002] | 0.9405 | 0.02500 | not rejected |
| comeback_rate :: bonus_forfeited x opposite | -0.0002 | [-0.0026, 0.0021] | 0.8452 | 0.01000 | not rejected |

**20 of 45 rejected** after Holm correction.

### RQ-1 support criterion

§6.4 states the criterion as a decidable biconditional: RQ-1 is supported **iff** (i) the lower bound of the 95% BCa CI on the CV ratio of `rounds_to_first_win` (mandatory ÷ optional) exceeds 1, **and** (ii) at least 2 of 3 dynamism conjuncts have Holm-adjusted CIs excluding zero in the dynamism direction.

- (i) CV ratio 1.1641, 95% CI lower bound 1.1595 > 1
- (ii) lead_changes_per_turn: -0.005738 (dynamism direction no), Holm rejected at alpha=0.00714 -> does not count
- (ii) comeback_rate: +0.005744 (dynamism direction yes), Holm rejected at alpha=0.02500 -> counts
- (ii) predictability_skill: -0.001784 (dynamism direction yes), Holm not rejected at alpha=0.05000 -> does not count

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
| `ex10/6s2p/random/barriers` | FAIL | no | 0.1659 | — | — |
| `ex10/6s2p/random/baseline` | FAIL | no | 0.1660 | — | — |
| `ex10/6s2p/random/bonus_forfeited` | FAIL | no | 0.1660 | — | — |
| `ex10/6s2p/random/bonus_quick` | FAIL | no | 0.1657 | — | — |
| `ex10/6s2p/random/capture=mandatory` | FAIL | no | 0.1663 | 5,698,130 / 0 | 0 / 0 |
| `ex10/6s2p/random/capture=mandatory_extended` | FAIL | no | 0.1657 | 6,454,287 / 0 | 287,099 / 0 |
| `ex10/6s2p/random/cold_start=free_entry` | FAIL | no | 0.1648 | — | — |
| `ex10/6s2p/random/cold_start=strict` | FAIL | no | 0.1659 | — | — |
| `ex10/6s2p/random/dreimal` | FAIL | no | 0.1659 | — | — |
| `ex10/6s2p/random/goal_no_jump` | FAIL | no | 0.1659 | — | — |
| `ex10/6s3p/random/barriers` | FAIL | no | 0.1558 | — | — |
| `ex10/6s3p/random/baseline` | FAIL | no | 0.1563 | — | — |
| `ex10/6s3p/random/bonus_forfeited` | FAIL | no | 0.1563 | — | — |
| `ex10/6s3p/random/bonus_quick` | FAIL | no | 0.1550 | — | — |
| `ex10/6s3p/random/capture=mandatory` | FAIL | no | 0.1580 | 17,777,969 / 0 | 0 / 0 |
| `ex10/6s3p/random/capture=mandatory_extended` | FAIL | no | 0.1616 | 20,554,885 / 0 | 700,799 / 0 |
| `ex10/6s3p/random/cold_start=free_entry` | FAIL | no | 0.1556 | — | — |
| `ex10/6s3p/random/cold_start=strict` | FAIL | no | 0.1560 | — | — |
| `ex10/6s3p/random/dreimal` | FAIL | no | 0.1558 | — | — |
| `ex10/6s3p/random/goal_no_jump` | FAIL | no | 0.1566 | — | — |
| `ex10/6s4p/random/barriers` | FAIL | no | 0.1443 | — | — |
| `ex10/6s4p/random/baseline` | FAIL | no | 0.1449 | — | — |
| `ex10/6s4p/random/bonus_forfeited` | FAIL | no | 0.1449 | — | — |
| `ex10/6s4p/random/bonus_quick` | FAIL | no | 0.1432 | — | — |
| `ex10/6s4p/random/capture=mandatory` | FAIL | no | 0.1451 | 37,848,455 / 0 | 0 / 0 |
| `ex10/6s4p/random/capture=mandatory_extended` | FAIL | no | 0.1501 | 44,254,116 / 0 | 1,179,955 / 0 |
| `ex10/6s4p/random/cold_start=free_entry` | FAIL | no | 0.1466 | — | — |
| `ex10/6s4p/random/cold_start=strict` | FAIL | no | 0.1444 | — | — |
| `ex10/6s4p/random/dreimal` | FAIL | no | 0.1440 | — | — |
| `ex10/6s4p/random/goal_no_jump` | FAIL | no | 0.1454 | — | — |
| `ex10/6s6p/random/barriers` | PASS | yes | 0.1241 | — | — |
| `ex10/6s6p/random/baseline` | PASS | yes | 0.1237 | — | — |
| `ex10/6s6p/random/bonus_forfeited` | PASS | yes | 0.1238 | — | — |
| `ex10/6s6p/random/bonus_quick` | PASS | yes | 0.1240 | — | — |
| `ex10/6s6p/random/capture=mandatory` | PASS | yes | 0.1239 | 105,411,208 / 0 | 0 / 0 |
| `ex10/6s6p/random/capture=mandatory_extended` | PASS | yes | 0.1241 | 125,286,131 / 0 | 2,344,729 / 0 |
| `ex10/6s6p/random/cold_start=free_entry` | PASS | yes | 0.1240 | — | — |
| `ex10/6s6p/random/cold_start=strict` | PASS | yes | 0.1241 | — | — |
| `ex10/6s6p/random/dreimal` | PASS | yes | 0.1240 | — | — |
| `ex10/6s6p/random/goal_no_jump` | PASS | yes | 0.1241 | — | — |
| `ex11/6s2p/focus_front-vs-random/baseline` | FAIL | no | 0.1661 | — | — |
| `ex11/6s2p/focus_rear-vs-random/baseline` | FAIL | no | 0.1648 | — | — |
| `ex11/6s2p/greedy_capture-vs-random/baseline` | FAIL | no | 0.1662 | — | — |
| `ex11/6s2p/spread-vs-random/baseline` | FAIL | no | 0.1641 | — | — |
| `ex11/6s3p/focus_front-vs-random/baseline` | FAIL | no | 0.1592 | — | — |
| `ex11/6s3p/focus_rear-vs-random/baseline` | FAIL | no | 0.1548 | — | — |
| `ex11/6s3p/greedy_capture-vs-random/baseline` | FAIL | no | 0.1569 | — | — |
| `ex11/6s3p/spread-vs-random/baseline` | FAIL | no | 0.1547 | — | — |
| `ex11/6s4p/focus_front-vs-random/baseline` | FAIL | no | 0.1473 | — | — |
| `ex11/6s4p/focus_rear-vs-random/baseline` | FAIL | no | 0.1441 | — | — |
| `ex11/6s4p/greedy_capture-vs-random/baseline` | FAIL | no | 0.1449 | — | — |
| `ex11/6s4p/spread-vs-random/baseline` | FAIL | no | 0.1437 | — | — |
| `ex11/6s6p/focus_front-vs-random/baseline` | PASS | no | 0.1239 | — | — |
| `ex11/6s6p/focus_rear-vs-random/baseline` | PASS | no | 0.1241 | — | — |
| `ex11/6s6p/greedy_capture-vs-random/baseline` | PASS | no | 0.1239 | — | — |
| `ex11/6s6p/spread-vs-random/baseline` | PASS | no | 0.1240 | — | — |
| `ex12/2p/4s-adjacent/random/barriers` | FAIL | no | 0.1661 | — | — |
| `ex12/2p/4s-adjacent/random/baseline` | FAIL | no | 0.1661 | — | — |
| `ex12/2p/4s-adjacent/random/bonus_forfeited` | FAIL | no | 0.1661 | — | — |
| `ex12/2p/4s-adjacent/random/bonus_quick` | FAIL | no | 0.1660 | — | — |
| `ex12/2p/4s-adjacent/random/capture=mandatory` | FAIL | no | 0.1663 | 4,909,625 / 0 | 0 / 0 |
| `ex12/2p/4s-adjacent/random/capture=mandatory_extended` | FAIL | no | 0.1659 | 5,649,538 / 0 | 302,745 / 0 |
| `ex12/2p/4s-adjacent/random/cold_start=free_entry` | FAIL | no | 0.1653 | — | — |
| `ex12/2p/4s-adjacent/random/cold_start=strict` | FAIL | no | 0.1661 | — | — |
| `ex12/2p/4s-adjacent/random/dreimal` | FAIL | no | 0.1661 | — | — |
| `ex12/2p/4s-adjacent/random/goal_no_jump` | FAIL | no | 0.1661 | — | — |
| `ex12/2p/4s-opposite/random/barriers` | PASS | yes | 0.1663 | — | — |
| `ex12/2p/4s-opposite/random/baseline` | PASS | yes | 0.1663 | — | — |
| `ex12/2p/4s-opposite/random/bonus_forfeited` | PASS | yes | 0.1663 | — | — |
| `ex12/2p/4s-opposite/random/bonus_quick` | PASS | yes | 0.1663 | — | — |
| `ex12/2p/4s-opposite/random/capture=mandatory` | PASS | yes | 0.1663 | 5,144,817 / 0 | 0 / 0 |
| `ex12/2p/4s-opposite/random/capture=mandatory_extended` | PASS | yes | 0.1663 | 5,866,657 / 0 | 284,041 / 0 |
| `ex12/2p/4s-opposite/random/cold_start=free_entry` | PASS | yes | 0.1663 | — | — |
| `ex12/2p/4s-opposite/random/cold_start=strict` | PASS | yes | 0.1663 | — | — |
| `ex12/2p/4s-opposite/random/dreimal` | PASS | yes | 0.1663 | — | — |
| `ex12/2p/4s-opposite/random/goal_no_jump` | PASS | yes | 0.1663 | — | — |
| `ex1b/6s6p/random/baseline` | PASS | yes | 0.1521 | — | — |
| `ex2/4s2p/greedy_capture/mandatory` | INCONCLUSIVE | no | 0.9104 | 163,983 / 0 | 0 / 0 |
| `ex2/4s2p/greedy_capture/mandatory_extended` | INCONCLUSIVE | no | 0.9085 | 188,266 / 0 | 10,023 / 0 |
| `ex2/4s2p/greedy_capture/optional` | INCONCLUSIVE | no | 0.9102 | — | — |
| `ex2/4s2p/random/mandatory` | INCONCLUSIVE | no | 0.9105 | 164,188 / 0 | 0 / 0 |
| `ex2/4s2p/random/mandatory_extended` | INCONCLUSIVE | no | 0.9085 | 189,546 / 0 | 10,206 / 0 |
| `ex2/4s2p/random/optional` | INCONCLUSIVE | no | 0.9101 | — | — |
| `ex2/4s2p/spread/mandatory` | INCONCLUSIVE | no | 0.8900 | 164,630 / 0 | 0 / 0 |
| `ex2/4s2p/spread/mandatory_extended` | INCONCLUSIVE | no | 0.8945 | 197,350 / 0 | 11,020 / 0 |
| `ex2/4s2p/spread/optional` | INCONCLUSIVE | no | 0.8734 | — | — |
| `ex2/4s3p/greedy_capture/mandatory` | INCONCLUSIVE | no | 0.8592 | 496,766 / 0 | 0 / 0 |
| `ex2/4s3p/greedy_capture/mandatory_extended` | INCONCLUSIVE | no | 0.8750 | 590,511 / 0 | 24,530 / 0 |
| `ex2/4s3p/greedy_capture/optional` | INCONCLUSIVE | no | 0.8638 | — | — |
| `ex2/4s3p/random/mandatory` | INCONCLUSIVE | no | 0.8615 | 502,530 / 0 | 0 / 0 |
| `ex2/4s3p/random/mandatory_extended` | INCONCLUSIVE | no | 0.8741 | 586,806 / 0 | 24,162 / 0 |
| `ex2/4s3p/random/optional` | INCONCLUSIVE | no | 0.8569 | — | — |
| `ex2/4s3p/spread/mandatory` | INCONCLUSIVE | no | 0.8404 | 655,746 / 0 | 0 / 0 |
| `ex2/4s3p/spread/mandatory_extended` | INCONCLUSIVE | no | 0.8523 | 814,861 / 0 | 34,502 / 0 |
| `ex2/4s3p/spread/optional` | INCONCLUSIVE | no | 0.8338 | — | — |
| `ex2/4s4p/greedy_capture/mandatory` | INCONCLUSIVE | yes | 0.7881 | 1,014,882 / 0 | 0 / 0 |
| `ex2/4s4p/greedy_capture/mandatory_extended` | INCONCLUSIVE | yes | 0.7913 | 1,204,311 / 0 | 41,730 / 0 |
| `ex2/4s4p/greedy_capture/optional` | INCONCLUSIVE | yes | 0.7863 | — | — |
| `ex2/4s4p/random/mandatory` | PASS | yes | 0.2231 | 12,642,085 / 0 | 0 / 0 |
| `ex2/4s4p/random/mandatory_extended` | PASS | yes | 0.2231 | 15,088,714 / 0 | 526,061 / 0 |
| `ex2/4s4p/random/optional` | PASS | yes | 0.2231 | — | — |
| `ex2/4s4p/spread/mandatory` | INCONCLUSIVE | yes | 0.7861 | 1,415,075 / 0 | 0 / 0 |
| `ex2/4s4p/spread/mandatory_extended` | INCONCLUSIVE | yes | 0.7862 | 1,775,395 / 0 | 60,962 / 0 |
| `ex2/4s4p/spread/optional` | INCONCLUSIVE | yes | 0.7915 | — | — |
| `ex2/6s6p/greedy_capture/mandatory` | INCONCLUSIVE | yes | 0.6846 | 3,503,790 / 0 | 0 / 0 |
| `ex2/6s6p/greedy_capture/mandatory_extended` | INCONCLUSIVE | yes | 0.6815 | 4,197,592 / 0 | 78,583 / 0 |
| `ex2/6s6p/greedy_capture/optional` | INCONCLUSIVE | yes | 0.6766 | — | — |
| `ex2/6s6p/random/mandatory` | INCONCLUSIVE | yes | 0.6817 | 3,498,973 / 0 | 0 / 0 |
| `ex2/6s6p/random/mandatory_extended` | INCONCLUSIVE | yes | 0.6834 | 4,187,414 / 0 | 78,105 / 0 |
| `ex2/6s6p/random/optional` | INCONCLUSIVE | yes | 0.6694 | — | — |
| `ex2/6s6p/spread/mandatory` | INCONCLUSIVE | yes | 0.6849 | 5,304,452 / 0 | 0 / 0 |
| `ex2/6s6p/spread/mandatory_extended` | INCONCLUSIVE | yes | 0.6734 | 6,544,149 / 0 | 109,012 / 0 |
| `ex2/6s6p/spread/optional` | INCONCLUSIVE | yes | 0.6780 | — | — |
| `ex3/deviant/4s2p/focus_front-vs-focus_rear` | INCONCLUSIVE | no | 0.9105 | — | — |
| `ex3/deviant/4s2p/focus_front-vs-random` | INCONCLUSIVE | no | 0.9101 | — | — |
| `ex3/deviant/4s2p/focus_front-vs-spread` | INCONCLUSIVE | no | 0.9102 | — | — |
| `ex3/deviant/4s2p/focus_rear-vs-focus_front` | INCONCLUSIVE | no | 0.9102 | — | — |
| `ex3/deviant/4s2p/focus_rear-vs-random` | INCONCLUSIVE | no | 0.9060 | — | — |
| `ex3/deviant/4s2p/focus_rear-vs-spread` | INCONCLUSIVE | no | 0.8780 | — | — |
| `ex3/deviant/4s2p/random-vs-focus_front` | INCONCLUSIVE | no | 0.9102 | — | — |
| `ex3/deviant/4s2p/random-vs-focus_rear` | INCONCLUSIVE | no | 0.9056 | — | — |
| `ex3/deviant/4s2p/random-vs-spread` | INCONCLUSIVE | no | 0.9041 | — | — |
| `ex3/deviant/4s2p/spread-vs-focus_front` | INCONCLUSIVE | no | 0.9101 | — | — |
| `ex3/deviant/4s2p/spread-vs-focus_rear` | INCONCLUSIVE | no | 0.8798 | — | — |
| `ex3/deviant/4s2p/spread-vs-random` | INCONCLUSIVE | no | 0.9045 | — | — |
| `ex3/deviant/4s3p/focus_front-vs-focus_rear` | INCONCLUSIVE | no | 0.8590 | — | — |
| `ex3/deviant/4s3p/focus_front-vs-random` | INCONCLUSIVE | no | 0.8645 | — | — |
| `ex3/deviant/4s3p/focus_front-vs-spread` | INCONCLUSIVE | no | 0.8585 | — | — |
| `ex3/deviant/4s3p/focus_rear-vs-focus_front` | INCONCLUSIVE | no | 0.8693 | — | — |
| `ex3/deviant/4s3p/focus_rear-vs-random` | INCONCLUSIVE | no | 0.8532 | — | — |
| `ex3/deviant/4s3p/focus_rear-vs-spread` | INCONCLUSIVE | no | 0.8346 | — | — |
| `ex3/deviant/4s3p/random-vs-focus_front` | INCONCLUSIVE | no | 0.8726 | — | — |
| `ex3/deviant/4s3p/random-vs-focus_rear` | INCONCLUSIVE | no | 0.8470 | — | — |
| `ex3/deviant/4s3p/random-vs-spread` | INCONCLUSIVE | no | 0.8464 | — | — |
| `ex3/deviant/4s3p/spread-vs-focus_front` | INCONCLUSIVE | no | 0.8694 | — | — |
| `ex3/deviant/4s3p/spread-vs-focus_rear` | INCONCLUSIVE | no | 0.8334 | — | — |
| `ex3/deviant/4s3p/spread-vs-random` | INCONCLUSIVE | no | 0.8483 | — | — |
| `ex3/deviant/4s4p/focus_front-vs-focus_rear` | INCONCLUSIVE | no | 0.7876 | — | — |
| `ex3/deviant/4s4p/focus_front-vs-random` | PASS | no | 0.2498 | — | — |
| `ex3/deviant/4s4p/focus_front-vs-spread` | INCONCLUSIVE | no | 0.7888 | — | — |
| `ex3/deviant/4s4p/focus_rear-vs-focus_front` | INCONCLUSIVE | no | 0.7880 | — | — |
| `ex3/deviant/4s4p/focus_rear-vs-random` | PASS | no | 0.2495 | — | — |
| `ex3/deviant/4s4p/focus_rear-vs-spread` | INCONCLUSIVE | no | 0.7867 | — | — |
| `ex3/deviant/4s4p/random-vs-focus_front` | INCONCLUSIVE | no | 0.7907 | — | — |
| `ex3/deviant/4s4p/random-vs-focus_rear` | INCONCLUSIVE | no | 0.7863 | — | — |
| `ex3/deviant/4s4p/random-vs-spread` | INCONCLUSIVE | no | 0.7870 | — | — |
| `ex3/deviant/4s4p/spread-vs-focus_front` | INCONCLUSIVE | no | 0.7874 | — | — |
| `ex3/deviant/4s4p/spread-vs-focus_rear` | INCONCLUSIVE | no | 0.7894 | — | — |
| `ex3/deviant/4s4p/spread-vs-random` | PASS | no | 0.2492 | — | — |
| `ex3/deviant/6s6p/focus_front-vs-focus_rear` | INCONCLUSIVE | no | 0.6760 | — | — |
| `ex3/deviant/6s6p/focus_front-vs-random` | INCONCLUSIVE | no | 0.6796 | — | — |
| `ex3/deviant/6s6p/focus_front-vs-spread` | INCONCLUSIVE | no | 0.6802 | — | — |
| `ex3/deviant/6s6p/focus_rear-vs-focus_front` | INCONCLUSIVE | no | 0.6742 | — | — |
| `ex3/deviant/6s6p/focus_rear-vs-random` | INCONCLUSIVE | no | 0.6737 | — | — |
| `ex3/deviant/6s6p/focus_rear-vs-spread` | INCONCLUSIVE | no | 0.6792 | — | — |
| `ex3/deviant/6s6p/random-vs-focus_front` | INCONCLUSIVE | no | 0.6729 | — | — |
| `ex3/deviant/6s6p/random-vs-focus_rear` | INCONCLUSIVE | no | 0.6759 | — | — |
| `ex3/deviant/6s6p/random-vs-spread` | INCONCLUSIVE | no | 0.6817 | — | — |
| `ex3/deviant/6s6p/spread-vs-focus_front` | INCONCLUSIVE | no | 0.6778 | — | — |
| `ex3/deviant/6s6p/spread-vs-focus_rear` | INCONCLUSIVE | no | 0.6728 | — | — |
| `ex3/deviant/6s6p/spread-vs-random` | INCONCLUSIVE | no | 0.6838 | — | — |
| `ex3/homogeneous/4s2p/focus_front` | INCONCLUSIVE | no | 0.9096 | — | — |
| `ex3/homogeneous/4s2p/focus_rear` | INCONCLUSIVE | no | 0.8916 | — | — |
| `ex3/homogeneous/4s2p/random` | INCONCLUSIVE | no | 0.9097 | — | — |
| `ex3/homogeneous/4s2p/spread` | INCONCLUSIVE | no | 0.8752 | — | — |
| `ex3/homogeneous/4s3p/focus_front` | INCONCLUSIVE | no | 0.8684 | — | — |
| `ex3/homogeneous/4s3p/focus_rear` | INCONCLUSIVE | no | 0.8425 | — | — |
| `ex3/homogeneous/4s3p/random` | INCONCLUSIVE | no | 0.8558 | — | — |
| `ex3/homogeneous/4s3p/spread` | INCONCLUSIVE | no | 0.8346 | — | — |
| `ex3/homogeneous/4s4p/focus_front` | INCONCLUSIVE | yes | 0.7914 | — | — |
| `ex3/homogeneous/4s4p/focus_rear` | INCONCLUSIVE | yes | 0.7917 | — | — |
| `ex3/homogeneous/4s4p/random` | INCONCLUSIVE | yes | 0.7879 | — | — |
| `ex3/homogeneous/4s4p/spread` | INCONCLUSIVE | yes | 0.7878 | — | — |
| `ex3/homogeneous/6s6p/focus_front` | INCONCLUSIVE | yes | 0.6806 | — | — |
| `ex3/homogeneous/6s6p/focus_rear` | INCONCLUSIVE | yes | 0.6743 | — | — |
| `ex3/homogeneous/6s6p/random` | INCONCLUSIVE | yes | 0.6843 | — | — |
| `ex3/homogeneous/6s6p/spread` | INCONCLUSIVE | yes | 0.6742 | — | — |
| `ex4/4s4p/random/barriers=True` | INCONCLUSIVE | yes | 0.5599 | — | — |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.5610 | 2,780,958 / 0 | 0 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5586 | 2,864,683 / 0 | 0 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.5583 | 2,792,267 / 0 | 0 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5595 | 2,867,299 / 0 | 0 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.5581 | 3,359,835 / 0 | 99,298 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5540 | 3,459,310 / 0 | 108,426 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.5601 | 3,360,276 / 0 | 99,740 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5566 | 3,467,168 / 0 | 109,023 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-cold_start=strict-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.5588 | — | — |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5581 | — | — |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.5564 | — | — |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5571 | — | — |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.5579 | 2,771,042 / 0 | 0 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5582 | 2,831,458 / 0 | 0 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-capture_mode=mandatory-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.5598 | 2,758,852 / 0 | 0 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-capture_mode=mandatory-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5608 | 2,838,031 / 0 | 0 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.5602 | 3,336,577 / 0 | 99,575 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5576 | 3,439,168 / 0 | 109,177 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-capture_mode=mandatory_extended-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.5582 | 3,344,177 / 0 | 99,635 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-capture_mode=mandatory_extended-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5594 | 3,432,902 / 0 | 108,526 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-cold_start=strict-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.5558 | — | — |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5567 | — | — |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.5565 | — | — |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5582 | — | — |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True` | INCONCLUSIVE | yes | 0.5578 | — | — |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory` | INCONCLUSIVE | yes | 0.5584 | 2,020,999 / 0 | 0 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=free_entry` | INCONCLUSIVE | yes | 0.5606 | 18,627,928 / 0 | 0 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=free_entry-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5561 | 19,086,942 / 0 | 0 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=strict` | INCONCLUSIVE | yes | 0.5559 | 1,993,542 / 0 | 0 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.5609 | 2,519,555 / 0 | 0 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5563 | 2,589,706 / 0 | 0 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=strict-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5600 | 2,085,289 / 0 | 0 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.5564 | 2,511,559 / 0 | 0 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5571 | 2,598,083 / 0 | 0 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5601 | 2,105,342 / 0 | 0 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended` | INCONCLUSIVE | yes | 0.5579 | 2,412,376 / 0 | 86,206 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=free_entry` | INCONCLUSIVE | yes | 0.5583 | 22,361,722 / 0 | 130,006 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=free_entry-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5577 | 22,990,916 / 0 | 141,829 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=strict` | INCONCLUSIVE | yes | 0.5582 | 2,391,705 / 0 | 85,625 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.5568 | 3,034,438 / 0 | 97,279 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5570 | 3,130,483 / 0 | 107,032 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=strict-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5586 | 2,506,447 / 0 | 98,241 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.5581 | 3,041,503 / 0 | 96,968 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5575 | 3,145,398 / 0 | 107,481 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5561 | 2,536,554 / 0 | 97,912 / 0 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-cold_start=free_entry` | INCONCLUSIVE | yes | 0.5601 | — | — |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-cold_start=free_entry-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5585 | — | — |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-cold_start=strict` | INCONCLUSIVE | yes | 0.5622 | — | — |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-cold_start=strict-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.5589 | — | — |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5586 | — | — |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-cold_start=strict-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5577 | — | — |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.5544 | — | — |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5589 | — | — |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5549 | — | — |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory` | INCONCLUSIVE | yes | 0.5584 | 2,000,503 / 0 | 0 / 0 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory-cold_start=free_entry` | INCONCLUSIVE | yes | 0.5570 | 18,572,654 / 0 | 0 / 0 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory-cold_start=free_entry-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5579 | 18,955,511 / 0 | 0 / 0 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory-cold_start=strict` | INCONCLUSIVE | yes | 0.5553 | 1,979,970 / 0 | 0 / 0 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.5559 | 2,490,174 / 0 | 0 / 0 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5573 | 2,573,080 / 0 | 0 / 0 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory-cold_start=strict-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5569 | 2,063,011 / 0 | 0 / 0 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.5551 | 2,491,398 / 0 | 0 / 0 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5603 | 2,575,555 / 0 | 0 / 0 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5570 | 2,092,528 / 0 | 0 / 0 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory_extended` | INCONCLUSIVE | yes | 0.5540 | 2,405,618 / 0 | 85,642 / 0 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory_extended-cold_start=free_entry` | INCONCLUSIVE | yes | 0.5602 | 22,271,186 / 0 | 129,230 / 0 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory_extended-cold_start=free_entry-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5567 | 22,774,319 / 0 | 141,245 / 0 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory_extended-cold_start=strict` | INCONCLUSIVE | yes | 0.5587 | 2,371,623 / 0 | 84,592 / 0 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.5567 | 3,016,031 / 0 | 96,359 / 0 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5590 | 3,107,833 / 0 | 106,045 / 0 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory_extended-cold_start=strict-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5566 | 2,482,627 / 0 | 97,739 / 0 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory_extended-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.5548 | 3,019,549 / 0 | 96,698 / 0 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory_extended-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5556 | 3,122,332 / 0 | 106,788 / 0 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory_extended-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5581 | 2,520,296 / 0 | 98,256 / 0 |
| `ex4/4s4p/random/barriers=True-cold_start=free_entry` | INCONCLUSIVE | yes | 0.5562 | — | — |
| `ex4/4s4p/random/barriers=True-cold_start=free_entry-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5592 | — | — |
| `ex4/4s4p/random/barriers=True-cold_start=strict` | INCONCLUSIVE | yes | 0.5583 | — | — |
| `ex4/4s4p/random/barriers=True-cold_start=strict-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.5569 | — | — |
| `ex4/4s4p/random/barriers=True-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5578 | — | — |
| `ex4/4s4p/random/barriers=True-cold_start=strict-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5546 | — | — |
| `ex4/4s4p/random/barriers=True-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.5569 | — | — |
| `ex4/4s4p/random/barriers=True-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5577 | — | — |
| `ex4/4s4p/random/barriers=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5536 | — | — |
| `ex4/4s4p/random/baseline` | INCONCLUSIVE | yes | 0.5587 | — | — |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.5585 | 2,818,005 / 0 | 0 / 0 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5556 | 2,894,982 / 0 | 0 / 0 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.5585 | 2,825,042 / 0 | 0 / 0 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5570 | 2,899,528 / 0 | 0 / 0 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.5554 | 3,389,496 / 0 | 98,522 / 0 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5581 | 3,487,827 / 0 | 106,987 / 0 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.5553 | 3,385,086 / 0 | 98,261 / 0 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5600 | 3,486,129 / 0 | 107,263 / 0 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-cold_start=strict-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.5567 | — | — |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5575 | — | — |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.5574 | — | — |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5560 | — | — |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.5581 | 2,798,605 / 0 | 0 / 0 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5571 | 2,874,695 / 0 | 0 / 0 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-capture_mode=mandatory-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.5581 | 2,802,279 / 0 | 0 / 0 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-capture_mode=mandatory-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5586 | 2,877,331 / 0 | 0 / 0 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.5578 | 3,370,071 / 0 | 97,524 / 0 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5546 | 3,463,812 / 0 | 107,812 / 0 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-capture_mode=mandatory_extended-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.5562 | 3,372,024 / 0 | 97,527 / 0 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-capture_mode=mandatory_extended-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5582 | 3,468,144 / 0 | 106,778 / 0 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-cold_start=strict-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.5553 | — | — |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5549 | — | — |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.5569 | — | — |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5581 | — | — |
| `ex4/4s4p/random/bonus_roll_forfeited=True` | INCONCLUSIVE | yes | 0.5582 | — | — |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory` | INCONCLUSIVE | yes | 0.5553 | 2,041,615 / 0 | 0 / 0 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=free_entry` | INCONCLUSIVE | yes | 0.5554 | 19,071,794 / 0 | 0 / 0 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=free_entry-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5568 | 19,555,309 / 0 | 0 / 0 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=strict` | INCONCLUSIVE | yes | 0.5577 | 2,013,831 / 0 | 0 / 0 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.5563 | 2,538,224 / 0 | 0 / 0 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5568 | 2,615,919 / 0 | 0 / 0 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=strict-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5565 | 2,102,865 / 0 | 0 / 0 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.5610 | 2,539,377 / 0 | 0 / 0 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5577 | 2,624,136 / 0 | 0 / 0 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5603 | 2,122,393 / 0 | 0 / 0 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory_extended` | INCONCLUSIVE | yes | 0.5573 | 2,429,142 / 0 | 84,948 / 0 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=free_entry` | INCONCLUSIVE | yes | 0.5573 | 22,699,489 / 0 | 128,093 / 0 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=free_entry-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5571 | 23,348,889 / 0 | 140,617 / 0 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=strict` | INCONCLUSIVE | yes | 0.5599 | 2,408,611 / 0 | 84,534 / 0 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.5574 | 3,055,536 / 0 | 95,108 / 0 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5565 | 3,142,267 / 0 | 105,284 / 0 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=strict-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5602 | 2,515,096 / 0 | 96,783 / 0 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory_extended-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.5588 | 3,067,309 / 0 | 96,098 / 0 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory_extended-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5612 | 3,163,701 / 0 | 105,902 / 0 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory_extended-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5582 | 2,539,183 / 0 | 96,922 / 0 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-cold_start=free_entry` | INCONCLUSIVE | yes | 0.5575 | — | — |
| `ex4/4s4p/random/bonus_roll_forfeited=True-cold_start=free_entry-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5570 | — | — |
| `ex4/4s4p/random/bonus_roll_forfeited=True-cold_start=strict` | INCONCLUSIVE | yes | 0.5601 | — | — |
| `ex4/4s4p/random/bonus_roll_forfeited=True-cold_start=strict-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.5562 | — | — |
| `ex4/4s4p/random/bonus_roll_forfeited=True-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5556 | — | — |
| `ex4/4s4p/random/bonus_roll_forfeited=True-cold_start=strict-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5586 | — | — |
| `ex4/4s4p/random/bonus_roll_forfeited=True-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.5608 | — | — |
| `ex4/4s4p/random/bonus_roll_forfeited=True-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5596 | — | — |
| `ex4/4s4p/random/bonus_roll_forfeited=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5577 | — | — |
| `ex4/4s4p/random/capture_mode=mandatory` | INCONCLUSIVE | yes | 0.5573 | 2,019,911 / 0 | 0 / 0 |
| `ex4/4s4p/random/capture_mode=mandatory-cold_start=free_entry` | INCONCLUSIVE | yes | 0.5563 | 18,924,773 / 0 | 0 / 0 |
| `ex4/4s4p/random/capture_mode=mandatory-cold_start=free_entry-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5578 | 19,475,243 / 0 | 0 / 0 |
| `ex4/4s4p/random/capture_mode=mandatory-cold_start=strict` | INCONCLUSIVE | yes | 0.5569 | 2,000,240 / 0 | 0 / 0 |
| `ex4/4s4p/random/capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.5573 | 2,517,463 / 0 | 0 / 0 |
| `ex4/4s4p/random/capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5601 | 2,590,954 / 0 | 0 / 0 |
| `ex4/4s4p/random/capture_mode=mandatory-cold_start=strict-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5573 | 2,079,831 / 0 | 0 / 0 |
| `ex4/4s4p/random/capture_mode=mandatory-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.5556 | 2,519,202 / 0 | 0 / 0 |
| `ex4/4s4p/random/capture_mode=mandatory-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5585 | 2,595,879 / 0 | 0 / 0 |
| `ex4/4s4p/random/capture_mode=mandatory-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5564 | 2,105,501 / 0 | 0 / 0 |
| `ex4/4s4p/random/capture_mode=mandatory_extended` | INCONCLUSIVE | yes | 0.5575 | 2,418,955 / 0 | 84,424 / 0 |
| `ex4/4s4p/random/capture_mode=mandatory_extended-cold_start=free_entry` | INCONCLUSIVE | yes | 0.5588 | 22,608,231 / 0 | 127,409 / 0 |
| `ex4/4s4p/random/capture_mode=mandatory_extended-cold_start=free_entry-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5587 | 23,195,935 / 0 | 139,494 / 0 |
| `ex4/4s4p/random/capture_mode=mandatory_extended-cold_start=strict` | INCONCLUSIVE | yes | 0.5572 | 2,384,880 / 0 | 83,804 / 0 |
| `ex4/4s4p/random/capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.5578 | 3,032,686 / 0 | 95,398 / 0 |
| `ex4/4s4p/random/capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5567 | 3,126,606 / 0 | 105,328 / 0 |
| `ex4/4s4p/random/capture_mode=mandatory_extended-cold_start=strict-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5562 | 2,490,412 / 0 | 96,727 / 0 |
| `ex4/4s4p/random/capture_mode=mandatory_extended-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.5589 | 3,032,037 / 0 | 95,262 / 0 |
| `ex4/4s4p/random/capture_mode=mandatory_extended-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5603 | 3,125,088 / 0 | 105,591 / 0 |
| `ex4/4s4p/random/capture_mode=mandatory_extended-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5574 | 2,519,046 / 0 | 96,195 / 0 |
| `ex4/4s4p/random/cold_start=free_entry` | INCONCLUSIVE | yes | 0.5591 | — | — |
| `ex4/4s4p/random/cold_start=free_entry-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5572 | — | — |
| `ex4/4s4p/random/cold_start=strict` | INCONCLUSIVE | yes | 0.5581 | — | — |
| `ex4/4s4p/random/cold_start=strict-dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.5577 | — | — |
| `ex4/4s4p/random/cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5553 | — | — |
| `ex4/4s4p/random/cold_start=strict-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5588 | — | — |
| `ex4/4s4p/random/dreimal_wuerfeln=True` | INCONCLUSIVE | yes | 0.5578 | — | — |
| `ex4/4s4p/random/dreimal_wuerfeln=True-goal_no_jump=True` | INCONCLUSIVE | yes | 0.5591 | — | — |
| `ex4/4s4p/random/goal_no_jump=True` | INCONCLUSIVE | yes | 0.5584 | — | — |
| `ex5/2p/adjacent/random` | INCONCLUSIVE | no | 0.9094 | — | — |
| `ex5/2p/adjacent/spread` | INCONCLUSIVE | no | 0.8734 | — | — |
| `ex5/2p/opposite/random` | INCONCLUSIVE | yes | 0.9105 | — | — |
| `ex5/2p/opposite/spread` | INCONCLUSIVE | yes | 0.9105 | — | — |
| `ex5/3p/4s-adjacent/random` | FAIL | no | 0.2427 | — | — |
| `ex5/3p/4s-adjacent/spread` | FAIL | no | 0.2359 | — | — |
| `ex5/3p/6s-adjacent/random` | FAIL | no | 0.2423 | — | — |
| `ex5/3p/6s-adjacent/spread` | FAIL | no | 0.2227 | — | — |
| `ex5/3p/6s-spread/random` | PASS | yes | 0.2427 | — | — |
| `ex5/3p/6s-spread/spread` | PASS | yes | 0.2429 | — | — |
| `ex6a/4s4p/focus_front/mandatory` | INCONCLUSIVE | yes | 0.7907 | 646,887 / 0 | 0 / 0 |
| `ex6a/4s4p/focus_front/mandatory_extended` | INCONCLUSIVE | yes | 0.7863 | 724,498 / 0 | 21,457 / 0 |
| `ex6a/4s4p/focus_front/optional` | INCONCLUSIVE | yes | 0.7892 | — | — |
| `ex6a/4s4p/focus_rear/mandatory` | INCONCLUSIVE | yes | 0.7883 | 1,329,031 / 0 | 0 / 0 |
| `ex6a/4s4p/focus_rear/mandatory_extended` | INCONCLUSIVE | yes | 0.7858 | 1,675,203 / 0 | 59,581 / 0 |
| `ex6a/4s4p/focus_rear/optional` | INCONCLUSIVE | yes | 0.7881 | — | — |
| `ex6a/4s4p/greedy_capture/mandatory` | INCONCLUSIVE | yes | 0.7846 | 1,012,973 / 0 | 0 / 0 |
| `ex6a/4s4p/greedy_capture/mandatory_extended` | INCONCLUSIVE | yes | 0.7900 | 1,202,995 / 0 | 41,833 / 0 |
| `ex6a/4s4p/greedy_capture/optional` | INCONCLUSIVE | yes | 0.7862 | — | — |
| `ex6a/4s4p/random/mandatory` | INCONCLUSIVE | yes | 0.7836 | 1,010,041 / 0 | 0 / 0 |
| `ex6a/4s4p/random/mandatory_extended` | INCONCLUSIVE | yes | 0.7861 | 1,210,845 / 0 | 42,533 / 0 |
| `ex6a/4s4p/random/optional` | INCONCLUSIVE | yes | 0.7872 | — | — |
| `ex6a/4s4p/spread/mandatory` | INCONCLUSIVE | yes | 0.7902 | 1,415,720 / 0 | 0 / 0 |
| `ex6a/4s4p/spread/mandatory_extended` | INCONCLUSIVE | yes | 0.7901 | 1,778,367 / 0 | 61,147 / 0 |
| `ex6a/4s4p/spread/optional` | INCONCLUSIVE | yes | 0.7896 | — | — |
| `ex6b/4s4p/focus_front-vs-random/mandatory` | PASS | no | 0.1764 | 18,319,012 / 0 | 0 / 0 |
| `ex6b/4s4p/focus_front-vs-random/mandatory_extended` | PASS | no | 0.1763 | 21,566,282 / 0 | 757,436 / 0 |
| `ex6b/4s4p/focus_front-vs-random/optional` | PASS | no | 0.1765 | — | — |
| `ex6b/4s4p/focus_rear-vs-random/mandatory` | INCONCLUSIVE | no | 0.7911 | 1,080,907 / 0 | 0 / 0 |
| `ex6b/4s4p/focus_rear-vs-random/mandatory_extended` | INCONCLUSIVE | no | 0.7905 | 1,308,005 / 0 | 47,369 / 0 |
| `ex6b/4s4p/focus_rear-vs-random/optional` | INCONCLUSIVE | no | 0.7960 | — | — |
| `ex6b/4s4p/greedy_capture-vs-random/mandatory` | INCONCLUSIVE | no | 0.7902 | 1,011,337 / 0 | 0 / 0 |
| `ex6b/4s4p/greedy_capture-vs-random/mandatory_extended` | INCONCLUSIVE | no | 0.7949 | 1,198,448 / 0 | 41,596 / 0 |
| `ex6b/4s4p/greedy_capture-vs-random/optional` | INCONCLUSIVE | no | 0.7848 | — | — |
| `ex6b/4s4p/spread-vs-random/mandatory` | PASS | no | 0.1767 | 21,882,285 / 0 | 0 / 0 |
| `ex6b/4s4p/spread-vs-random/mandatory_extended` | PASS | no | 0.1765 | 26,587,466 / 0 | 967,016 / 0 |
| `ex6b/4s4p/spread-vs-random/optional` | PASS | no | 0.1763 | — | — |
| `ex6c/4s4p/focus_front/barriers=False` | INCONCLUSIVE | yes | 0.7835 | — | — |
| `ex6c/4s4p/focus_front/barriers=True` | INCONCLUSIVE | yes | 0.7896 | — | — |
| `ex6c/4s4p/focus_rear/barriers=False` | INCONCLUSIVE | yes | 0.7879 | — | — |
| `ex6c/4s4p/focus_rear/barriers=True` | INCONCLUSIVE | yes | 0.7891 | — | — |
| `ex6c/4s4p/greedy_capture/barriers=False` | INCONCLUSIVE | yes | 0.7905 | — | — |
| `ex6c/4s4p/greedy_capture/barriers=True` | INCONCLUSIVE | yes | 0.7871 | — | — |
| `ex6c/4s4p/random/barriers=False` | INCONCLUSIVE | yes | 0.7899 | — | — |
| `ex6c/4s4p/random/barriers=True` | INCONCLUSIVE | yes | 0.7891 | — | — |
| `ex6c/4s4p/spread/barriers=False` | INCONCLUSIVE | yes | 0.7879 | — | — |
| `ex6c/4s4p/spread/barriers=True` | INCONCLUSIVE | yes | 0.7846 | — | — |
| `ex6d/4s4p/focus_front-vs-random/barriers=False` | PASS | no | 0.1763 | — | — |
| `ex6d/4s4p/focus_front-vs-random/barriers=True` | PASS | no | 0.1763 | — | — |
| `ex6d/4s4p/focus_rear-vs-random/barriers=False` | INCONCLUSIVE | no | 0.7891 | — | — |
| `ex6d/4s4p/focus_rear-vs-random/barriers=True` | INCONCLUSIVE | no | 0.7887 | — | — |
| `ex6d/4s4p/greedy_capture-vs-random/barriers=False` | INCONCLUSIVE | no | 0.7883 | — | — |
| `ex6d/4s4p/greedy_capture-vs-random/barriers=True` | INCONCLUSIVE | no | 0.7911 | — | — |
| `ex6d/4s4p/spread-vs-random/barriers=False` | PASS | no | 0.1763 | — | — |
| `ex6d/4s4p/spread-vs-random/barriers=True` | PASS | no | 0.1766 | — | — |
| `ex6e/6s2p/random/mandatory` | FAIL | no | 0.2036 | 3,799,916 / 0 | 0 / 0 |
| `ex6e/6s2p/random/mandatory_extended` | INCONCLUSIVE | no | 0.9077 | 212,684 / 0 | 9,308 / 0 |
| `ex6e/6s2p/random/optional` | FAIL | no | 0.2033 | — | — |
| `ex6e/6s3p/random/mandatory` | INCONCLUSIVE | no | 0.8631 | 591,958 / 0 | 0 / 0 |
| `ex6e/6s3p/random/mandatory_extended` | INCONCLUSIVE | no | 0.8855 | 684,566 / 0 | 23,480 / 0 |
| `ex6e/6s3p/random/optional` | INCONCLUSIVE | no | 0.8518 | — | — |
| `ex6e/6s4p/random/mandatory` | INCONCLUSIVE | no | 0.7902 | 1,262,547 / 0 | 0 / 0 |
| `ex6e/6s4p/random/mandatory_extended` | INCONCLUSIVE | no | 0.8200 | 1,477,199 / 0 | 39,269 / 0 |
| `ex6e/6s4p/random/optional` | INCONCLUSIVE | no | 0.7957 | — | — |
| `ex6e/6s6p/random/mandatory` | PASS | yes | 0.1517 | 70,348,742 / 0 | 0 / 0 |
| `ex6e/6s6p/random/mandatory_extended` | INCONCLUSIVE | yes | 0.6834 | 4,177,516 / 0 | 78,048 / 0 |
| `ex6e/6s6p/random/optional` | PASS | yes | 0.1521 | — | — |
| `ex6f/6s2p/focus_front-vs-random/mandatory` | INCONCLUSIVE | no | 0.9068 | 170,769 / 0 | 0 / 0 |
| `ex6f/6s2p/focus_front-vs-random/mandatory_extended` | INCONCLUSIVE | no | 0.9007 | 187,519 / 0 | 7,010 / 0 |
| `ex6f/6s2p/focus_front-vs-random/optional` | INCONCLUSIVE | no | 0.9095 | — | — |
| `ex6f/6s2p/focus_rear-vs-random/mandatory` | INCONCLUSIVE | no | 0.9087 | 202,062 / 0 | 0 / 0 |
| `ex6f/6s2p/focus_rear-vs-random/mandatory_extended` | INCONCLUSIVE | no | 0.9105 | 234,459 / 0 | 10,488 / 0 |
| `ex6f/6s2p/focus_rear-vs-random/optional` | INCONCLUSIVE | no | 0.9011 | — | — |
| `ex6f/6s2p/greedy_capture-vs-random/mandatory` | INCONCLUSIVE | no | 0.9105 | 190,542 / 0 | 0 / 0 |
| `ex6f/6s2p/greedy_capture-vs-random/mandatory_extended` | INCONCLUSIVE | no | 0.9084 | 217,077 / 0 | 9,618 / 0 |
| `ex6f/6s2p/greedy_capture-vs-random/optional` | INCONCLUSIVE | no | 0.9103 | — | — |
| `ex6f/6s2p/spread-vs-random/mandatory` | INCONCLUSIVE | no | 0.9077 | 204,806 / 0 | 0 / 0 |
| `ex6f/6s2p/spread-vs-random/mandatory_extended` | INCONCLUSIVE | no | 0.9105 | 243,130 / 0 | 11,134 / 0 |
| `ex6f/6s2p/spread-vs-random/optional` | INCONCLUSIVE | no | 0.8983 | — | — |
| `ex6f/6s3p/focus_front-vs-random/mandatory` | INCONCLUSIVE | no | 0.8794 | 527,359 / 0 | 0 / 0 |
| `ex6f/6s3p/focus_front-vs-random/mandatory_extended` | INCONCLUSIVE | no | 0.8921 | 599,918 / 0 | 19,921 / 0 |
| `ex6f/6s3p/focus_front-vs-random/optional` | INCONCLUSIVE | no | 0.8722 | — | — |
| `ex6f/6s3p/focus_rear-vs-random/mandatory` | INCONCLUSIVE | no | 0.8567 | 644,911 / 0 | 0 / 0 |
| `ex6f/6s3p/focus_rear-vs-random/mandatory_extended` | INCONCLUSIVE | no | 0.8791 | 762,439 / 0 | 26,584 / 0 |
| `ex6f/6s3p/focus_rear-vs-random/optional` | INCONCLUSIVE | no | 0.8526 | — | — |
| `ex6f/6s3p/greedy_capture-vs-random/mandatory` | INCONCLUSIVE | no | 0.8623 | 590,731 / 0 | 0 / 0 |
| `ex6f/6s3p/greedy_capture-vs-random/mandatory_extended` | INCONCLUSIVE | no | 0.8844 | 684,483 / 0 | 23,263 / 0 |
| `ex6f/6s3p/greedy_capture-vs-random/optional` | INCONCLUSIVE | no | 0.8610 | — | — |
| `ex6f/6s3p/spread-vs-random/mandatory` | INCONCLUSIVE | no | 0.8600 | 657,716 / 0 | 0 / 0 |
| `ex6f/6s3p/spread-vs-random/mandatory_extended` | INCONCLUSIVE | no | 0.8744 | 778,436 / 0 | 27,417 / 0 |
| `ex6f/6s3p/spread-vs-random/optional` | INCONCLUSIVE | no | 0.8468 | — | — |
| `ex6f/6s4p/focus_front-vs-random/mandatory` | INCONCLUSIVE | no | 0.8186 | 1,129,933 / 0 | 0 / 0 |
| `ex6f/6s4p/focus_front-vs-random/mandatory_extended` | INCONCLUSIVE | no | 0.8315 | 1,301,642 / 0 | 35,461 / 0 |
| `ex6f/6s4p/focus_front-vs-random/optional` | INCONCLUSIVE | no | 0.8087 | — | — |
| `ex6f/6s4p/focus_rear-vs-random/mandatory` | INCONCLUSIVE | no | 0.7952 | 1,356,064 / 0 | 0 / 0 |
| `ex6f/6s4p/focus_rear-vs-random/mandatory_extended` | INCONCLUSIVE | no | 0.8172 | 1,621,919 / 0 | 44,397 / 0 |
| `ex6f/6s4p/focus_rear-vs-random/optional` | INCONCLUSIVE | no | 0.7855 | — | — |
| `ex6f/6s4p/greedy_capture-vs-random/mandatory` | INCONCLUSIVE | no | 0.7978 | 1,261,612 / 0 | 0 / 0 |
| `ex6f/6s4p/greedy_capture-vs-random/mandatory_extended` | INCONCLUSIVE | no | 0.8249 | 1,476,668 / 0 | 39,811 / 0 |
| `ex6f/6s4p/greedy_capture-vs-random/optional` | INCONCLUSIVE | no | 0.7891 | — | — |
| `ex6f/6s4p/spread-vs-random/mandatory` | INCONCLUSIVE | no | 0.7944 | 1,382,944 / 0 | 0 / 0 |
| `ex6f/6s4p/spread-vs-random/mandatory_extended` | INCONCLUSIVE | no | 0.8154 | 1,632,828 / 0 | 44,325 / 0 |
| `ex6f/6s4p/spread-vs-random/optional` | INCONCLUSIVE | no | 0.7834 | — | — |
| `ex6f/6s6p/focus_front-vs-random/mandatory` | INCONCLUSIVE | no | 0.6810 | 3,212,582 / 0 | 0 / 0 |
| `ex6f/6s6p/focus_front-vs-random/mandatory_extended` | INCONCLUSIVE | no | 0.6835 | 3,789,254 / 0 | 73,610 / 0 |
| `ex6f/6s6p/focus_front-vs-random/optional` | INCONCLUSIVE | no | 0.6737 | — | — |
| `ex6f/6s6p/focus_rear-vs-random/mandatory` | INCONCLUSIVE | no | 0.6796 | 3,702,203 / 0 | 0 / 0 |
| `ex6f/6s6p/focus_rear-vs-random/mandatory_extended` | INCONCLUSIVE | no | 0.6814 | 4,436,107 / 0 | 84,465 / 0 |
| `ex6f/6s6p/focus_rear-vs-random/optional` | INCONCLUSIVE | no | 0.6801 | — | — |
| `ex6f/6s6p/greedy_capture-vs-random/mandatory` | INCONCLUSIVE | no | 0.6825 | 3,510,828 / 0 | 0 / 0 |
| `ex6f/6s6p/greedy_capture-vs-random/mandatory_extended` | INCONCLUSIVE | no | 0.6797 | 4,169,150 / 0 | 77,439 / 0 |
| `ex6f/6s6p/greedy_capture-vs-random/optional` | INCONCLUSIVE | no | 0.6766 | — | — |
| `ex6f/6s6p/spread-vs-random/mandatory` | INCONCLUSIVE | no | 0.6794 | 3,717,575 / 0 | 0 / 0 |
| `ex6f/6s6p/spread-vs-random/mandatory_extended` | INCONCLUSIVE | no | 0.6794 | 4,457,593 / 0 | 84,398 / 0 |
| `ex6f/6s6p/spread-vs-random/optional` | INCONCLUSIVE | no | 0.6778 | — | — |
| `ex7/2p/4s-adjacent/focus_front` | FAIL | no | 0.2878 | — | — |
| `ex7/2p/4s-adjacent/focus_rear` | FAIL | no | 0.2811 | — | — |
| `ex7/2p/4s-adjacent/greedy_capture` | FAIL | no | 0.2879 | — | — |
| `ex7/2p/4s-adjacent/random` | FAIL | no | 0.2877 | — | — |
| `ex7/2p/4s-adjacent/spread` | FAIL | no | 0.2754 | — | — |
| `ex7/2p/4s-opposite/focus_front` | PASS | yes | 0.2880 | — | — |
| `ex7/2p/4s-opposite/focus_rear` | PASS | yes | 0.2880 | — | — |
| `ex7/2p/4s-opposite/greedy_capture` | PASS | yes | 0.2880 | — | — |
| `ex7/2p/4s-opposite/random` | PASS | yes | 0.2880 | — | — |
| `ex7/2p/4s-opposite/spread` | FAIL | yes | 0.2880 | — | — |
| `ex7/3p/6s-adjacent/random` | FAIL | no | 0.2711 | — | — |
| `ex7/3p/6s-adjacent/spread` | FAIL | no | 0.2499 | — | — |
| `ex7/3p/6s-spread/random` | PASS | yes | 0.2712 | — | — |
| `ex7/3p/6s-spread/spread` | PASS | yes | 0.2716 | — | — |
| `ex8/4s4p/greedy_capture-vs-random/mandatory` | PASS | no | 0.2230 | 12,634,973 / 0 | 0 / 0 |
| `ex8/4s4p/greedy_capture-vs-random/optional` | PASS | no | 0.2231 | — | — |
| `ex8/6s2p/random/baseline` | FAIL | no | 0.2571 | — | — |
| `ex8/6s3p/random/baseline` | FAIL | no | 0.2423 | — | — |
| `ex8/6s4p/random/baseline` | FAIL | no | 0.2244 | — | — |
| `ex8/6s6p/random/baseline` | PASS | yes | 0.1919 | — | — |
| `ex9/4s4p/focus_front/barriers` | PASS | no | 0.1441 | — | — |
| `ex9/4s4p/focus_front/baseline` | PASS | no | 0.1441 | — | — |
| `ex9/4s4p/focus_front/bonus_forfeited` | PASS | no | 0.1441 | — | — |
| `ex9/4s4p/focus_front/bonus_quick` | PASS | no | 0.1439 | — | — |
| `ex9/4s4p/focus_front/capture=mandatory` | PASS | no | 0.1441 | 27,474,009 / 0 | 0 / 0 |
| `ex9/4s4p/focus_front/capture=mandatory_extended` | PASS | no | 0.1440 | 32,346,685 / 0 | 1,132,495 / 0 |
| `ex9/4s4p/focus_front/cold_start=free_entry` | PASS | no | 0.1440 | — | — |
| `ex9/4s4p/focus_front/cold_start=strict` | PASS | no | 0.1441 | — | — |
| `ex9/4s4p/focus_front/dreimal` | PASS | no | 0.1439 | — | — |
| `ex9/4s4p/focus_front/goal_no_jump` | PASS | no | 0.1442 | — | — |
| `ex9/4s4p/focus_rear/barriers` | PASS | no | 0.1442 | — | — |
| `ex9/4s4p/focus_rear/baseline` | PASS | no | 0.1439 | — | — |
| `ex9/4s4p/focus_rear/bonus_forfeited` | PASS | no | 0.1439 | — | — |
| `ex9/4s4p/focus_rear/bonus_quick` | PASS | no | 0.1439 | — | — |
| `ex9/4s4p/focus_rear/capture=mandatory` | PASS | no | 0.1441 | 32,408,223 / 0 | 0 / 0 |
| `ex9/4s4p/focus_rear/capture=mandatory_extended` | PASS | no | 0.1441 | 39,320,048 / 0 | 1,419,527 / 0 |
| `ex9/4s4p/focus_rear/cold_start=free_entry` | PASS | no | 0.1440 | — | — |
| `ex9/4s4p/focus_rear/cold_start=strict` | PASS | no | 0.1440 | — | — |
| `ex9/4s4p/focus_rear/dreimal` | PASS | no | 0.1440 | — | — |
| `ex9/4s4p/focus_rear/goal_no_jump` | PASS | no | 0.1439 | — | — |
| `ex9/4s4p/greedy_capture/barriers` | PASS | no | 0.1442 | — | — |
| `ex9/4s4p/greedy_capture/baseline` | PASS | no | 0.1441 | — | — |
| `ex9/4s4p/greedy_capture/bonus_forfeited` | PASS | no | 0.1440 | — | — |
| `ex9/4s4p/greedy_capture/bonus_quick` | PASS | no | 0.1440 | — | — |
| `ex9/4s4p/greedy_capture/capture=mandatory` | PASS | no | 0.1439 | 30,343,895 / 0 | 0 / 0 |
| `ex9/4s4p/greedy_capture/capture=mandatory_extended` | PASS | no | 0.1441 | 36,180,892 / 0 | 1,257,365 / 0 |
| `ex9/4s4p/greedy_capture/cold_start=free_entry` | PASS | no | 0.1440 | — | — |
| `ex9/4s4p/greedy_capture/cold_start=strict` | PASS | no | 0.1438 | — | — |
| `ex9/4s4p/greedy_capture/dreimal` | PASS | no | 0.1439 | — | — |
| `ex9/4s4p/greedy_capture/goal_no_jump` | PASS | no | 0.1440 | — | — |
| `ex9/4s4p/random/barriers` | PASS | yes | 0.1441 | — | — |
| `ex9/4s4p/random/baseline` | PASS | yes | 0.1440 | — | — |
| `ex9/4s4p/random/bonus_forfeited` | PASS | yes | 0.1438 | — | — |
| `ex9/4s4p/random/bonus_quick` | PASS | yes | 0.1440 | — | — |
| `ex9/4s4p/random/capture=mandatory` | PASS | yes | 0.1442 | 30,348,831 / 0 | 0 / 0 |
| `ex9/4s4p/random/capture=mandatory_extended` | PASS | yes | 0.1439 | 36,176,564 / 0 | 1,259,623 / 0 |
| `ex9/4s4p/random/cold_start=free_entry` | PASS | yes | 0.1440 | — | — |
| `ex9/4s4p/random/cold_start=strict` | PASS | yes | 0.1441 | — | — |
| `ex9/4s4p/random/dreimal` | PASS | yes | 0.1438 | — | — |
| `ex9/4s4p/random/goal_no_jump` | PASS | yes | 0.1439 | — | — |
| `ex9/4s4p/spread/barriers` | PASS | no | 0.1441 | — | — |
| `ex9/4s4p/spread/baseline` | PASS | no | 0.1441 | — | — |
| `ex9/4s4p/spread/bonus_forfeited` | PASS | no | 0.1441 | — | — |
| `ex9/4s4p/spread/bonus_quick` | PASS | no | 0.1440 | — | — |
| `ex9/4s4p/spread/capture=mandatory` | PASS | no | 0.1439 | 32,843,441 / 0 | 0 / 0 |
| `ex9/4s4p/spread/capture=mandatory_extended` | PASS | no | 0.1439 | 39,877,409 / 0 | 1,451,270 / 0 |
| `ex9/4s4p/spread/cold_start=free_entry` | PASS | no | 0.1441 | — | — |
| `ex9/4s4p/spread/cold_start=strict` | PASS | no | 0.1440 | — | — |
| `ex9/4s4p/spread/dreimal` | PASS | no | 0.1440 | — | — |
| `ex9/4s4p/spread/goal_no_jump` | PASS | no | 0.1439 | — | — |
### RQ-5 support criterion

§15.2: supported **iff** hypotheses 1, 5 and 6 are Holm-rejected in the predicted direction **and** hypothesis 3 — the `opposite` negative control, where the entry-field gaps are equal — is equivalent to zero within ±1 pp.

- H1 (4s2p-adjacent-spread): +29.201 pp, Holm rejected, needs > 0 and > 5 pp -> holds
- H5 (spread-minus-random x adjacent): +25.187 pp, Holm rejected, needs > 0 -> holds
- H6 (adjacent-minus-opposite x spread): +28.583 pp, Holm rejected, needs > 0 -> holds
- H3 (4s2p-opposite-spread): +0.618 pp, CI [+0.180, +1.056] vs margin +/-1.0 pp -> not equivalent

## RQ-5 is **NOT SUPPORTED**


## 4. Seat profiles where seats are not exchangeable

Where the field is homogeneous and the seats are exchangeable, §6.3's symmetry identity fixes every seat at 1/k for any rule set, so a per-seat rate there states arithmetic rather than a measurement. These are the cells where that does not hold — an uneven seating gap, or one seat playing a different policy — and the profile is the finding. AK-4 reports these as failures and deliberately does not gate on them (D-74): the asymmetry is what EX-5 set out to measure.

**The largest asymmetries, of 265 such cells.** These are **not pre-registered**: no §6.4 hypothesis asks about them, they carry no multiplicity correction, and they are reported because §14.4 requires every result to appear — not as a claim the study set out to test. Anything here worth believing needs its own pre-registered replication.

- `ex7/2p/4s-adjacent/spread` — 35.40% / 64.60% (**29.20 pp**, n = 200,000)
- `ex5/2p/adjacent/spread` — 35.86% / 64.14% (**28.28 pp**, n = 20,000)
- `ex2/4s2p/spread/optional` — 35.87% / 64.13% (**28.27 pp**, n = 20,000)
- `ex3/homogeneous/4s2p/spread` — 36.20% / 63.80% (**27.60 pp**, n = 20,000)
- `ex3/deviant/4s2p/focus_rear-vs-spread` — 36.74% / 63.25% (**26.51 pp**, n = 20,000)

| Cell | n | per-seat win rates | spread |
|---|---:|---|---:|
| `ex10/6s2p/random/barriers` | 600,000 | 46.70% / 53.30% | 6.60 pp |
| `ex10/6s2p/random/baseline` | 600,000 | 47.04% / 52.96% | 5.92 pp |
| `ex10/6s2p/random/bonus_forfeited` | 600,000 | 46.94% / 53.06% | 6.12 pp |
| `ex10/6s2p/random/bonus_quick` | 600,000 | 46.02% / 53.98% | 7.97 pp |
| `ex10/6s2p/random/capture=mandatory` | 600,000 | 50.47% / 49.53% | 0.94 pp |
| `ex10/6s2p/random/capture=mandatory_extended` | 600,000 | 54.04% / 45.96% | 8.08 pp |
| `ex10/6s2p/random/cold_start=free_entry` | 600,000 | 43.43% / 56.57% | 13.14 pp |
| `ex10/6s2p/random/cold_start=strict` | 600,000 | 46.77% / 53.23% | 6.47 pp |
| `ex10/6s2p/random/dreimal` | 600,000 | 46.72% / 53.28% | 6.57 pp |
| `ex10/6s2p/random/goal_no_jump` | 600,000 | 46.71% / 53.29% | 6.58 pp |
| `ex10/6s3p/random/barriers` | 600,000 | 32.54% / 34.68% / 32.78% | 2.15 pp |
| `ex10/6s3p/random/baseline` | 600,000 | 32.92% / 34.69% / 32.40% | 2.29 pp |
| `ex10/6s3p/random/bonus_forfeited` | 600,000 | 32.95% / 34.78% / 32.28% | 2.50 pp |
| `ex10/6s3p/random/bonus_quick` | 600,000 | 31.91% / 36.21% / 31.88% | 4.33 pp |
| `ex10/6s3p/random/capture=mandatory` | 600,000 | 34.44% / 34.43% / 31.13% | 3.31 pp |
| `ex10/6s3p/random/capture=mandatory_extended` | 600,000 | 38.21% / 33.39% / 28.40% | 9.81 pp |
| `ex10/6s3p/random/cold_start=free_entry` | 600,000 | 32.37% / 35.00% / 32.64% | 2.63 pp |
| `ex10/6s3p/random/cold_start=strict` | 600,000 | 32.71% / 35.13% / 32.16% | 2.96 pp |
| `ex10/6s3p/random/dreimal` | 600,000 | 32.56% / 35.65% / 31.79% | 3.86 pp |
| `ex10/6s3p/random/goal_no_jump` | 600,000 | 33.24% / 34.82% / 31.94% | 2.88 pp |
| `ex10/6s4p/random/barriers` | 600,000 | 25.14% / 26.74% / 25.84% / 22.28% | 4.46 pp |
| `ex10/6s4p/random/baseline` | 600,000 | 25.46% / 26.83% / 25.67% / 22.04% | 4.78 pp |
| `ex10/6s4p/random/bonus_forfeited` | 600,000 | 25.48% / 26.75% / 25.63% / 22.15% | 4.60 pp |
| `ex10/6s4p/random/bonus_quick` | 600,000 | 24.60% / 28.38% / 26.57% / 20.45% | 7.93 pp |
| `ex10/6s4p/random/capture=mandatory` | 600,000 | 25.59% / 26.30% / 25.32% / 22.78% | 3.52 pp |
| `ex10/6s4p/random/capture=mandatory_extended` | 600,000 | 28.47% / 26.34% / 24.11% / 21.07% | 7.40 pp |
| `ex10/6s4p/random/cold_start=free_entry` | 600,000 | 26.40% / 27.54% / 25.26% / 20.80% | 6.74 pp |
| `ex10/6s4p/random/cold_start=strict` | 600,000 | 25.22% / 27.14% / 25.74% / 21.90% | 5.24 pp |
| `ex10/6s4p/random/dreimal` | 600,000 | 25.01% / 27.90% / 26.10% / 20.99% | 6.90 pp |
| `ex10/6s4p/random/goal_no_jump` | 600,000 | 25.72% / 26.88% / 25.55% / 21.84% | 5.04 pp |
| `ex11/6s2p/focus_front-vs-random/baseline` | 600,000 | 51.96% / 48.04% | 3.92 pp |
| `ex11/6s2p/focus_rear-vs-random/baseline` | 600,000 | 43.39% / 56.61% | 13.21 pp |
| `ex11/6s2p/greedy_capture-vs-random/baseline` | 600,000 | 48.79% / 51.21% | 2.42 pp |
| `ex11/6s2p/spread-vs-random/baseline` | 600,000 | 41.96% / 58.04% | 16.09 pp |
| `ex11/6s3p/focus_front-vs-random/baseline` | 600,003 | 35.55% / 33.63% / 30.82% | 4.74 pp |
| `ex11/6s3p/focus_rear-vs-random/baseline` | 600,003 | 31.76% / 35.58% / 32.66% | 3.82 pp |
| `ex11/6s3p/greedy_capture-vs-random/baseline` | 600,003 | 33.47% / 34.67% / 31.86% | 2.81 pp |
| `ex11/6s3p/spread-vs-random/baseline` | 600,003 | 31.64% / 35.64% / 32.72% | 4.00 pp |
| `ex11/6s4p/focus_front-vs-random/baseline` | 600,000 | 26.84% / 26.15% / 24.63% / 22.38% | 4.45 pp |
| `ex11/6s4p/focus_rear-vs-random/baseline` | 600,000 | 25.04% / 27.08% / 25.91% / 21.97% | 5.11 pp |
| `ex11/6s4p/greedy_capture-vs-random/baseline` | 600,000 | 25.46% / 26.65% / 25.53% / 22.35% | 4.31 pp |
| `ex11/6s4p/spread-vs-random/baseline` | 600,000 | 24.87% / 27.07% / 26.15% / 21.91% | 5.16 pp |
| `ex11/6s6p/focus_front-vs-random/baseline` | 600,012 | 16.66% / 16.72% / 16.68% / 16.63% / 16.68% / 16.63% | 0.09 pp |
| `ex11/6s6p/focus_rear-vs-random/baseline` | 600,012 | 16.72% / 16.68% / 16.56% / 16.70% / 16.68% / 16.66% | 0.16 pp |
| `ex11/6s6p/greedy_capture-vs-random/baseline` | 600,012 | 16.65% / 16.67% / 16.68% / 16.69% / 16.63% / 16.68% | 0.05 pp |
| `ex11/6s6p/spread-vs-random/baseline` | 600,012 | 16.70% / 16.64% / 16.63% / 16.69% / 16.73% / 16.61% | 0.12 pp |
| `ex12/2p/4s-adjacent/random/barriers` | 600,000 | 47.71% / 52.29% | 4.58 pp |
| `ex12/2p/4s-adjacent/random/baseline` | 600,000 | 47.89% / 52.11% | 4.22 pp |
| `ex12/2p/4s-adjacent/random/bonus_forfeited` | 600,000 | 47.80% / 52.20% | 4.40 pp |
| `ex12/2p/4s-adjacent/random/bonus_quick` | 600,000 | 46.99% / 53.01% | 6.01 pp |
| `ex12/2p/4s-adjacent/random/capture=mandatory` | 600,000 | 50.65% / 49.35% | 1.30 pp |
| `ex12/2p/4s-adjacent/random/capture=mandatory_extended` | 600,000 | 53.10% / 46.90% | 6.19 pp |
| `ex12/2p/4s-adjacent/random/cold_start=free_entry` | 600,000 | 44.48% / 55.52% | 11.05 pp |
| `ex12/2p/4s-adjacent/random/cold_start=strict` | 600,000 | 47.80% / 52.20% | 4.39 pp |
| `ex12/2p/4s-adjacent/random/dreimal` | 600,000 | 47.61% / 52.39% | 4.78 pp |
| `ex12/2p/4s-adjacent/random/goal_no_jump` | 600,000 | 47.80% / 52.20% | 4.40 pp |
| `ex2/4s2p/greedy_capture/mandatory` | 20,000 | 51.00% / 49.00% | 2.00 pp |
| `ex2/4s2p/greedy_capture/mandatory_extended` | 20,000 | 53.36% / 46.64% | 6.72 pp |
| `ex2/4s2p/greedy_capture/optional` | 20,000 | 51.28% / 48.73% | 2.55 pp |
| `ex2/4s2p/random/mandatory` | 20,000 | 50.28% / 49.72% | 0.56 pp |
| `ex2/4s2p/random/mandatory_extended` | 20,000 | 53.37% / 46.63% | 6.74 pp |
| `ex2/4s2p/random/optional` | 20,000 | 48.49% / 51.51% | 3.01 pp |
| `ex2/4s2p/spread/mandatory` | 20,000 | 39.42% / 60.58% | 21.15 pp |
| `ex2/4s2p/spread/mandatory_extended` | 20,000 | 40.65% / 59.35% | 18.70 pp |
| `ex2/4s2p/spread/optional` | 20,000 | 35.87% / 64.13% | 28.27 pp |
| `ex2/4s3p/greedy_capture/mandatory` | 20,001 | 33.45% / 34.02% / 32.52% | 1.50 pp |
| `ex2/4s3p/greedy_capture/mandatory_extended` | 20,001 | 36.16% / 32.73% / 31.10% | 5.06 pp |
| `ex2/4s3p/greedy_capture/optional` | 20,001 | 34.19% / 33.37% / 32.43% | 1.76 pp |
| `ex2/4s3p/random/mandatory` | 20,001 | 33.81% / 33.93% / 32.25% | 1.68 pp |
| `ex2/4s3p/random/mandatory_extended` | 20,001 | 36.00% / 33.30% / 30.70% | 5.30 pp |
| `ex2/4s3p/random/optional` | 20,001 | 33.10% / 34.56% / 32.34% | 2.22 pp |
| `ex2/4s3p/spread/mandatory` | 20,001 | 30.76% / 36.80% / 32.44% | 6.04 pp |
| `ex2/4s3p/spread/mandatory_extended` | 20,001 | 32.40% / 36.09% / 31.51% | 4.58 pp |
| `ex2/4s3p/spread/optional` | 20,001 | 29.91% / 36.91% / 33.18% | 7.00 pp |
| `ex3/deviant/4s2p/focus_front-vs-focus_rear` | 20,000 | 50.69% / 49.31% | 1.37 pp |
| `ex3/deviant/4s2p/focus_front-vs-random` | 20,000 | 51.58% / 48.43% | 3.15 pp |
| `ex3/deviant/4s2p/focus_front-vs-spread` | 20,000 | 51.33% / 48.67% | 2.67 pp |
| `ex3/deviant/4s2p/focus_rear-vs-focus_front` | 20,000 | 51.30% / 48.70% | 2.60 pp |
| `ex3/deviant/4s2p/focus_rear-vs-random` | 20,000 | 45.03% / 54.97% | 9.94 pp |
| `ex3/deviant/4s2p/focus_rear-vs-spread` | 20,000 | 36.74% / 63.25% | 26.51 pp |
| `ex3/deviant/4s2p/random-vs-focus_front` | 20,000 | 51.46% / 48.54% | 2.92 pp |
| `ex3/deviant/4s2p/random-vs-focus_rear` | 20,000 | 44.79% / 55.21% | 10.42 pp |
| `ex3/deviant/4s2p/random-vs-spread` | 20,000 | 44.05% / 55.95% | 11.90 pp |
| `ex3/deviant/4s2p/spread-vs-focus_front` | 20,000 | 51.48% / 48.52% | 2.96 pp |
| `ex3/deviant/4s2p/spread-vs-focus_rear` | 20,000 | 37.12% / 62.88% | 25.76 pp |
| `ex3/deviant/4s2p/spread-vs-random` | 20,000 | 44.25% / 55.75% | 11.50 pp |
| `ex3/deviant/4s3p/focus_front-vs-focus_rear` | 20,007 | 33.44% / 34.21% / 32.35% | 1.86 pp |
| `ex3/deviant/4s3p/focus_front-vs-random` | 20,007 | 34.32% / 33.09% / 32.58% | 1.74 pp |
| `ex3/deviant/4s3p/focus_front-vs-spread` | 20,007 | 33.35% / 34.47% / 32.18% | 2.29 pp |
| `ex3/deviant/4s3p/focus_rear-vs-focus_front` | 20,007 | 35.15% / 32.48% / 32.37% | 2.78 pp |
| `ex3/deviant/4s3p/focus_rear-vs-random` | 20,007 | 32.55% / 34.43% / 33.01% | 1.88 pp |
| `ex3/deviant/4s3p/focus_rear-vs-spread` | 20,007 | 30.03% / 37.46% / 32.51% | 7.43 pp |
| `ex3/deviant/4s3p/random-vs-focus_front` | 20,007 | 35.74% / 32.59% / 31.67% | 4.07 pp |
| `ex3/deviant/4s3p/random-vs-focus_rear` | 20,007 | 31.67% / 35.42% / 32.91% | 3.75 pp |
| `ex3/deviant/4s3p/random-vs-spread` | 20,007 | 31.59% / 36.12% / 32.29% | 4.53 pp |
| `ex3/deviant/4s3p/spread-vs-focus_front` | 20,007 | 35.16% / 33.89% / 30.94% | 4.22 pp |
| `ex3/deviant/4s3p/spread-vs-focus_rear` | 20,007 | 29.87% / 36.67% / 33.46% | 6.79 pp |
| `ex3/deviant/4s3p/spread-vs-random` | 20,007 | 31.85% / 34.78% / 33.37% | 2.93 pp |
| `ex3/deviant/4s4p/focus_front-vs-focus_rear` | 20,000 | 24.91% / 24.99% / 25.11% / 24.99% | 0.21 pp |
| `ex3/deviant/4s4p/focus_front-vs-random` | 200,000 | 25.13% / 24.90% / 24.91% / 25.06% | 0.23 pp |
| `ex3/deviant/4s4p/focus_front-vs-spread` | 20,000 | 25.01% / 25.34% / 24.82% / 24.82% | 0.52 pp |
| `ex3/deviant/4s4p/focus_rear-vs-focus_front` | 20,000 | 24.94% / 24.76% / 25.36% / 24.94% | 0.60 pp |
| `ex3/deviant/4s4p/focus_rear-vs-random` | 200,000 | 25.02% / 24.93% / 25.08% / 24.97% | 0.15 pp |
| `ex3/deviant/4s4p/focus_rear-vs-spread` | 20,000 | 24.82% / 25.42% / 24.70% / 25.06% | 0.73 pp |
| `ex3/deviant/4s4p/random-vs-focus_front` | 20,000 | 25.20% / 25.04% / 24.98% / 24.79% | 0.41 pp |
| `ex3/deviant/4s4p/random-vs-focus_rear` | 20,000 | 24.78% / 24.95% / 25.52% / 24.75% | 0.77 pp |
| `ex3/deviant/4s4p/random-vs-spread` | 20,000 | 24.85% / 24.93% / 25.16% / 25.06% | 0.31 pp |
| `ex3/deviant/4s4p/spread-vs-focus_front` | 20,000 | 24.88% / 25.31% / 24.64% / 25.16% | 0.67 pp |
| `ex3/deviant/4s4p/spread-vs-focus_rear` | 20,000 | 25.08% / 24.82% / 24.99% / 25.11% | 0.29 pp |
| `ex3/deviant/4s4p/spread-vs-random` | 200,000 | 24.95% / 24.95% / 25.09% / 25.00% | 0.14 pp |
| `ex3/deviant/6s6p/focus_front-vs-focus_rear` | 20,016 | 16.52% / 16.79% / 16.95% / 16.54% / 16.66% / 16.55% | 0.43 pp |
| `ex3/deviant/6s6p/focus_front-vs-random` | 20,016 | 16.74% / 16.94% / 16.16% / 16.93% / 16.73% / 16.51% | 0.78 pp |
| `ex3/deviant/6s6p/focus_front-vs-spread` | 20,016 | 16.77% / 16.62% / 16.44% / 16.66% / 16.73% / 16.78% | 0.34 pp |
| `ex3/deviant/6s6p/focus_rear-vs-focus_front` | 20,016 | 16.40% / 16.58% / 16.84% / 17.10% / 16.25% / 16.83% | 0.85 pp |
| `ex3/deviant/6s6p/focus_rear-vs-random` | 20,016 | 16.37% / 16.94% / 16.84% / 16.98% / 16.21% / 16.67% | 0.76 pp |
| `ex3/deviant/6s6p/focus_rear-vs-spread` | 20,016 | 16.71% / 16.82% / 16.83% / 16.55% / 16.45% / 16.64% | 0.37 pp |
| `ex3/deviant/6s6p/random-vs-focus_front` | 20,016 | 16.33% / 17.06% / 16.45% / 16.43% / 16.83% / 16.90% | 0.73 pp |
| `ex3/deviant/6s6p/random-vs-focus_rear` | 20,016 | 16.51% / 16.80% / 16.47% / 16.77% / 16.64% / 16.81% | 0.34 pp |
| `ex3/deviant/6s6p/random-vs-spread` | 20,016 | 16.87% / 16.54% / 16.43% / 16.35% / 16.88% / 16.93% | 0.58 pp |
| `ex3/deviant/6s6p/spread-vs-focus_front` | 20,016 | 16.63% / 16.61% / 16.79% / 16.62% / 16.65% / 16.71% | 0.18 pp |
| `ex3/deviant/6s6p/spread-vs-focus_rear` | 20,016 | 16.32% / 16.82% / 16.92% / 16.47% / 16.85% / 16.64% | 0.60 pp |
| `ex3/deviant/6s6p/spread-vs-random` | 20,016 | 17.00% / 16.73% / 17.04% / 16.58% / 16.45% / 16.21% | 0.83 pp |
| `ex3/homogeneous/4s2p/focus_front` | 20,000 | 52.26% / 47.73% | 4.53 pp |
| `ex3/homogeneous/4s2p/focus_rear` | 20,000 | 39.86% / 60.14% | 20.28 pp |
| `ex3/homogeneous/4s2p/random` | 20,000 | 47.88% / 52.12% | 4.24 pp |
| `ex3/homogeneous/4s2p/spread` | 20,000 | 36.20% / 63.80% | 27.60 pp |
| `ex3/homogeneous/4s3p/focus_front` | 20,001 | 34.96% / 33.23% / 31.81% | 3.15 pp |
| `ex3/homogeneous/4s3p/focus_rear` | 20,001 | 31.04% / 36.00% / 32.96% | 4.96 pp |
| `ex3/homogeneous/4s3p/random` | 20,001 | 32.93% / 33.72% / 33.35% | 0.79 pp |
| `ex3/homogeneous/4s3p/spread` | 20,001 | 30.00% / 37.06% / 32.94% | 7.05 pp |
| `ex5/2p/adjacent/random` | 20,000 | 47.54% / 52.46% | 4.92 pp |
| `ex5/2p/adjacent/spread` | 20,000 | 35.86% / 64.14% | 28.28 pp |
| `ex5/3p/4s-adjacent/random` | 250,002 | 33.25% / 33.88% / 32.87% | 1.01 pp |
| `ex5/3p/4s-adjacent/spread` | 250,002 | 29.93% / 37.15% / 32.92% | 7.22 pp |
| `ex5/3p/6s-adjacent/random` | 250,002 | 33.01% / 34.82% / 32.17% | 2.65 pp |
| `ex5/3p/6s-adjacent/spread` | 250,002 | 24.89% / 38.97% / 36.15% | 14.08 pp |
| `ex6b/4s4p/focus_front-vs-random/mandatory` | 400,000 | 25.02% / 25.05% / 24.99% / 24.94% | 0.11 pp |
| `ex6b/4s4p/focus_front-vs-random/mandatory_extended` | 400,000 | 24.96% / 25.10% / 25.01% / 24.93% | 0.17 pp |
| `ex6b/4s4p/focus_front-vs-random/optional` | 400,000 | 25.06% / 25.01% / 24.96% / 24.97% | 0.10 pp |
| `ex6b/4s4p/focus_rear-vs-random/mandatory` | 20,000 | 25.24% / 25.26% / 24.43% / 25.07% | 0.84 pp |
| `ex6b/4s4p/focus_rear-vs-random/mandatory_extended` | 20,000 | 25.19% / 24.44% / 25.28% / 25.10% | 0.85 pp |
| `ex6b/4s4p/focus_rear-vs-random/optional` | 20,000 | 25.72% / 24.91% / 24.59% / 24.79% | 1.13 pp |
| `ex6b/4s4p/greedy_capture-vs-random/mandatory` | 20,000 | 25.16% / 25.44% / 25.01% / 24.39% | 1.05 pp |
| `ex6b/4s4p/greedy_capture-vs-random/mandatory_extended` | 20,000 | 25.61% / 25.02% / 24.88% / 24.49% | 1.12 pp |
| `ex6b/4s4p/greedy_capture-vs-random/optional` | 20,000 | 24.64% / 24.86% / 25.05% / 25.45% | 0.81 pp |
| `ex6b/4s4p/spread-vs-random/mandatory` | 400,000 | 25.13% / 24.91% / 25.00% / 24.96% | 0.22 pp |
| `ex6b/4s4p/spread-vs-random/mandatory_extended` | 400,000 | 25.05% / 24.90% / 25.06% / 24.99% | 0.16 pp |
| `ex6b/4s4p/spread-vs-random/optional` | 400,000 | 24.97% / 25.06% / 25.05% / 24.93% | 0.13 pp |
| `ex6d/4s4p/focus_front-vs-random/barriers=False` | 400,000 | 24.96% / 24.95% / 25.10% / 24.98% | 0.15 pp |
| `ex6d/4s4p/focus_front-vs-random/barriers=True` | 400,000 | 24.97% / 25.02% / 24.99% / 25.01% | 0.05 pp |
| `ex6d/4s4p/focus_rear-vs-random/barriers=False` | 20,000 | 25.05% / 24.79% / 25.02% / 25.14% | 0.36 pp |
| `ex6d/4s4p/focus_rear-vs-random/barriers=True` | 20,000 | 25.01% / 24.62% / 25.24% / 25.13% | 0.62 pp |
| `ex6d/4s4p/greedy_capture-vs-random/barriers=False` | 20,000 | 24.98% / 24.81% / 25.31% / 24.91% | 0.50 pp |
| `ex6d/4s4p/greedy_capture-vs-random/barriers=True` | 20,000 | 25.24% / 24.70% / 25.18% / 24.88% | 0.55 pp |
| `ex6d/4s4p/spread-vs-random/barriers=False` | 400,000 | 24.99% / 24.97% / 24.98% / 25.06% | 0.09 pp |
| `ex6d/4s4p/spread-vs-random/barriers=True` | 400,000 | 25.11% / 25.07% / 24.99% / 24.83% | 0.28 pp |
| `ex6e/6s2p/random/mandatory` | 400,000 | 50.35% / 49.65% | 0.71 pp |
| `ex6e/6s2p/random/mandatory_extended` | 20,000 | 53.95% / 46.05% | 7.91 pp |
| `ex6e/6s2p/random/optional` | 400,000 | 47.01% / 53.00% | 5.99 pp |
| `ex6e/6s3p/random/mandatory` | 20,001 | 34.08% / 34.49% / 31.43% | 3.05 pp |
| `ex6e/6s3p/random/mandatory_extended` | 20,001 | 38.36% / 33.73% / 27.91% | 10.44 pp |
| `ex6e/6s3p/random/optional` | 20,001 | 32.33% / 35.21% / 32.46% | 2.87 pp |
| `ex6e/6s4p/random/mandatory` | 20,000 | 25.16% / 26.21% / 25.41% / 23.21% | 3.00 pp |
| `ex6e/6s4p/random/mandatory_extended` | 20,000 | 28.26% / 26.63% / 24.23% / 20.88% | 7.39 pp |
| `ex6e/6s4p/random/optional` | 20,000 | 25.69% / 26.79% / 25.79% / 21.73% | 5.06 pp |
| `ex6f/6s2p/focus_front-vs-random/mandatory` | 20,000 | 54.52% / 45.48% | 9.04 pp |
| `ex6f/6s2p/focus_front-vs-random/mandatory_extended` | 20,000 | 57.32% / 42.68% | 14.64 pp |
| `ex6f/6s2p/focus_front-vs-random/optional` | 20,000 | 52.43% / 47.57% | 4.87 pp |
| `ex6f/6s2p/focus_rear-vs-random/mandatory` | 20,000 | 46.86% / 53.14% | 6.29 pp |
| `ex6f/6s2p/focus_rear-vs-random/mandatory_extended` | 20,000 | 49.72% / 50.28% | 0.56 pp |
| `ex6f/6s2p/focus_rear-vs-random/optional` | 20,000 | 42.80% / 57.20% | 14.40 pp |
| `ex6f/6s2p/greedy_capture-vs-random/mandatory` | 20,000 | 50.17% / 49.83% | 0.34 pp |
| `ex6f/6s2p/greedy_capture-vs-random/mandatory_extended` | 20,000 | 53.42% / 46.58% | 6.85 pp |
| `ex6f/6s2p/greedy_capture-vs-random/optional` | 20,000 | 48.87% / 51.13% | 2.26 pp |
| `ex6f/6s2p/spread-vs-random/mandatory` | 20,000 | 46.05% / 53.95% | 7.90 pp |
| `ex6f/6s2p/spread-vs-random/mandatory_extended` | 20,000 | 49.50% / 50.50% | 1.00 pp |
| `ex6f/6s2p/spread-vs-random/optional` | 20,000 | 41.84% / 58.16% | 16.32 pp |
| `ex6f/6s3p/focus_front-vs-random/mandatory` | 20,007 | 37.06% / 33.20% / 29.74% | 7.32 pp |
| `ex6f/6s3p/focus_front-vs-random/mandatory_extended` | 20,007 | 40.04% / 32.28% / 27.68% | 12.36 pp |
| `ex6f/6s3p/focus_front-vs-random/optional` | 20,007 | 35.67% / 33.68% / 30.65% | 5.02 pp |
| `ex6f/6s3p/focus_rear-vs-random/mandatory` | 20,007 | 33.08% / 34.78% / 32.13% | 2.65 pp |
| `ex6f/6s3p/focus_rear-vs-random/mandatory_extended` | 20,007 | 37.00% / 34.17% / 28.82% | 8.18 pp |
| `ex6f/6s3p/focus_rear-vs-random/optional` | 20,007 | 32.47% / 35.45% / 32.08% | 3.37 pp |
| `ex6f/6s3p/greedy_capture-vs-random/mandatory` | 20,007 | 33.96% / 34.45% / 31.59% | 2.86 pp |
| `ex6f/6s3p/greedy_capture-vs-random/mandatory_extended` | 20,007 | 38.15% / 33.91% / 27.95% | 10.20 pp |
| `ex6f/6s3p/greedy_capture-vs-random/optional` | 20,007 | 33.75% / 34.72% / 31.53% | 3.19 pp |
| `ex6f/6s3p/spread-vs-random/mandatory` | 20,007 | 33.59% / 34.93% / 31.48% | 3.45 pp |
| `ex6f/6s3p/spread-vs-random/mandatory_extended` | 20,007 | 36.08% / 34.99% / 28.93% | 7.15 pp |
| `ex6f/6s3p/spread-vs-random/optional` | 20,007 | 31.64% / 35.73% / 32.63% | 4.09 pp |
| `ex6f/6s4p/focus_front-vs-random/mandatory` | 20,000 | 28.11% / 25.34% / 24.50% / 22.06% | 6.05 pp |
| `ex6f/6s4p/focus_front-vs-random/mandatory_extended` | 20,000 | 29.62% / 25.84% / 23.24% / 21.30% | 8.32 pp |
| `ex6f/6s4p/focus_front-vs-random/optional` | 20,000 | 27.02% / 26.21% / 24.69% / 22.08% | 4.94 pp |
| `ex6f/6s4p/focus_rear-vs-random/mandatory` | 20,000 | 25.64% / 26.34% / 24.87% / 23.16% | 3.18 pp |
| `ex6f/6s4p/focus_rear-vs-random/mandatory_extended` | 20,000 | 27.94% / 26.50% / 24.07% / 21.49% | 6.45 pp |
| `ex6f/6s4p/focus_rear-vs-random/optional` | 20,000 | 24.70% / 27.32% / 26.21% / 21.77% | 5.55 pp |
| `ex6f/6s4p/greedy_capture-vs-random/mandatory` | 20,000 | 25.90% / 26.30% / 25.36% / 22.43% | 3.87 pp |
| `ex6f/6s4p/greedy_capture-vs-random/mandatory_extended` | 20,000 | 28.83% / 26.58% / 23.73% / 20.86% | 7.97 pp |
| `ex6f/6s4p/greedy_capture-vs-random/optional` | 20,000 | 25.05% / 27.03% / 25.65% / 22.27% | 4.76 pp |
| `ex6f/6s4p/spread-vs-random/mandatory` | 20,000 | 25.56% / 27.05% / 24.86% / 22.54% | 4.51 pp |
| `ex6f/6s4p/spread-vs-random/mandatory_extended` | 20,000 | 27.74% / 26.62% / 24.67% / 20.97% | 6.77 pp |
| `ex6f/6s4p/spread-vs-random/optional` | 20,000 | 24.51% / 27.38% / 26.40% / 21.72% | 5.65 pp |
| `ex6f/6s6p/focus_front-vs-random/mandatory` | 20,016 | 16.82% / 16.82% / 16.30% / 16.66% / 16.86% / 16.55% | 0.56 pp |
| `ex6f/6s6p/focus_front-vs-random/mandatory_extended` | 20,016 | 16.98% / 16.47% / 16.99% / 16.77% / 16.21% / 16.59% | 0.77 pp |
| `ex6f/6s6p/focus_front-vs-random/optional` | 20,016 | 16.38% / 16.68% / 16.48% / 16.69% / 16.78% / 17.00% | 0.62 pp |
| `ex6f/6s6p/focus_rear-vs-random/mandatory` | 20,016 | 16.73% / 16.50% / 16.97% / 16.99% / 16.11% / 16.70% | 0.88 pp |
| `ex6f/6s6p/focus_rear-vs-random/mandatory_extended` | 20,016 | 16.85% / 16.81% / 16.53% / 16.71% / 16.64% / 16.48% | 0.37 pp |
| `ex6f/6s6p/focus_rear-vs-random/optional` | 20,016 | 16.77% / 16.55% / 16.78% / 16.71% / 16.86% / 16.34% | 0.51 pp |
| `ex6f/6s6p/greedy_capture-vs-random/mandatory` | 20,016 | 16.92% / 16.32% / 16.61% / 16.40% / 16.94% / 16.82% | 0.61 pp |
| `ex6f/6s6p/greedy_capture-vs-random/mandatory_extended` | 20,016 | 16.74% / 16.73% / 17.20% / 16.16% / 16.65% / 16.52% | 1.04 pp |
| `ex6f/6s6p/greedy_capture-vs-random/optional` | 20,016 | 16.55% / 16.77% / 16.42% / 16.78% / 16.49% / 16.99% | 0.57 pp |
| `ex6f/6s6p/spread-vs-random/mandatory` | 20,016 | 16.72% / 16.95% / 16.52% / 16.97% / 16.29% / 16.56% | 0.68 pp |
| `ex6f/6s6p/spread-vs-random/mandatory_extended` | 20,016 | 16.72% / 16.50% / 16.84% / 16.48% / 16.75% / 16.71% | 0.35 pp |
| `ex6f/6s6p/spread-vs-random/optional` | 20,016 | 16.62% / 16.79% / 16.49% / 16.59% / 16.98% / 16.54% | 0.49 pp |
| `ex7/2p/4s-adjacent/focus_front` | 200,000 | 51.51% / 48.49% | 3.03 pp |
| `ex7/2p/4s-adjacent/focus_rear` | 200,000 | 39.10% / 60.90% | 21.80 pp |
| `ex7/2p/4s-adjacent/greedy_capture` | 200,000 | 50.80% / 49.20% | 1.60 pp |
| `ex7/2p/4s-adjacent/random` | 200,000 | 47.99% / 52.01% | 4.01 pp |
| `ex7/2p/4s-adjacent/spread` | 200,000 | 35.40% / 64.60% | 29.20 pp |
| `ex7/3p/6s-adjacent/random` | 200,001 | 33.14% / 34.91% / 31.95% | 2.96 pp |
| `ex7/3p/6s-adjacent/spread` | 200,001 | 25.16% / 38.90% / 35.95% | 13.74 pp |
| `ex8/4s4p/greedy_capture-vs-random/mandatory` | 250,000 | 24.98% / 25.01% / 25.18% / 24.83% | 0.35 pp |
| `ex8/4s4p/greedy_capture-vs-random/optional` | 250,000 | 25.00% / 25.06% / 24.93% / 25.02% | 0.13 pp |
| `ex8/6s2p/random/baseline` | 250,000 | 47.01% / 52.99% | 5.98 pp |
| `ex8/6s3p/random/baseline` | 250,002 | 33.04% / 34.78% / 32.18% | 2.60 pp |
| `ex8/6s4p/random/baseline` | 250,000 | 25.45% / 26.71% / 25.62% / 22.22% | 4.49 pp |
| `ex9/4s4p/focus_front/barriers` | 600,000 | 25.04% / 24.96% / 25.03% / 24.97% | 0.09 pp |
| `ex9/4s4p/focus_front/baseline` | 600,000 | 25.04% / 24.92% / 25.03% / 25.01% | 0.12 pp |
| `ex9/4s4p/focus_front/bonus_forfeited` | 600,000 | 25.08% / 24.90% / 25.02% / 25.01% | 0.18 pp |
| `ex9/4s4p/focus_front/bonus_quick` | 600,000 | 24.97% / 24.93% / 25.05% / 25.06% | 0.13 pp |
| `ex9/4s4p/focus_front/capture=mandatory` | 600,000 | 25.05% / 24.97% / 25.01% / 24.96% | 0.09 pp |
| `ex9/4s4p/focus_front/capture=mandatory_extended` | 600,000 | 25.00% / 24.99% / 25.03% / 24.98% | 0.05 pp |
| `ex9/4s4p/focus_front/cold_start=free_entry` | 600,000 | 25.00% / 25.00% / 25.00% / 25.00% | 0.00 pp |
| `ex9/4s4p/focus_front/cold_start=strict` | 600,000 | 25.04% / 24.90% / 24.99% / 25.07% | 0.17 pp |
| `ex9/4s4p/focus_front/dreimal` | 600,000 | 24.96% / 25.01% / 25.04% / 24.99% | 0.08 pp |
| `ex9/4s4p/focus_front/goal_no_jump` | 600,000 | 25.08% / 24.99% / 24.95% / 24.97% | 0.13 pp |
| `ex9/4s4p/focus_rear/barriers` | 600,000 | 25.10% / 24.88% / 25.02% / 24.99% | 0.22 pp |
| `ex9/4s4p/focus_rear/baseline` | 600,000 | 24.96% / 24.89% / 25.03% / 25.11% | 0.22 pp |
| `ex9/4s4p/focus_rear/bonus_forfeited` | 600,000 | 24.93% / 25.05% / 25.03% / 24.98% | 0.12 pp |
| `ex9/4s4p/focus_rear/bonus_quick` | 600,000 | 24.93% / 25.02% / 25.07% / 24.97% | 0.14 pp |
| `ex9/4s4p/focus_rear/capture=mandatory` | 600,000 | 25.04% / 25.04% / 24.94% / 24.99% | 0.10 pp |
| `ex9/4s4p/focus_rear/capture=mandatory_extended` | 600,000 | 25.08% / 24.94% / 24.96% / 25.02% | 0.14 pp |
| `ex9/4s4p/focus_rear/cold_start=free_entry` | 600,000 | 25.03% / 25.02% / 25.00% / 24.96% | 0.07 pp |
| `ex9/4s4p/focus_rear/cold_start=strict` | 600,000 | 24.98% / 25.00% / 24.98% / 25.03% | 0.05 pp |
| `ex9/4s4p/focus_rear/dreimal` | 600,000 | 24.98% / 24.92% / 25.17% / 24.94% | 0.25 pp |
| `ex9/4s4p/focus_rear/goal_no_jump` | 600,000 | 24.96% / 25.02% / 24.99% / 25.02% | 0.07 pp |
| `ex9/4s4p/greedy_capture/barriers` | 600,000 | 25.09% / 25.02% / 24.96% / 24.93% | 0.15 pp |
| `ex9/4s4p/greedy_capture/baseline` | 600,000 | 25.03% / 24.97% / 25.02% / 24.98% | 0.07 pp |
| `ex9/4s4p/greedy_capture/bonus_forfeited` | 600,000 | 25.00% / 25.06% / 24.96% / 24.99% | 0.10 pp |
| `ex9/4s4p/greedy_capture/bonus_quick` | 600,000 | 24.99% / 25.02% / 24.96% / 25.03% | 0.07 pp |
| `ex9/4s4p/greedy_capture/capture=mandatory` | 600,000 | 24.96% / 24.96% / 24.99% / 25.09% | 0.13 pp |
| `ex9/4s4p/greedy_capture/capture=mandatory_extended` | 600,000 | 25.04% / 24.93% / 25.02% / 25.02% | 0.11 pp |
| `ex9/4s4p/greedy_capture/cold_start=free_entry` | 600,000 | 25.00% / 25.04% / 24.92% / 25.03% | 0.12 pp |
| `ex9/4s4p/greedy_capture/cold_start=strict` | 600,000 | 24.92% / 25.01% / 24.97% / 25.10% | 0.18 pp |
| `ex9/4s4p/greedy_capture/dreimal` | 600,000 | 24.96% / 25.00% / 25.07% / 24.96% | 0.11 pp |
| `ex9/4s4p/greedy_capture/goal_no_jump` | 600,000 | 25.00% / 25.05% / 24.93% / 25.03% | 0.11 pp |
| `ex9/4s4p/spread/barriers` | 600,000 | 25.04% / 24.99% / 24.98% / 24.99% | 0.07 pp |
| `ex9/4s4p/spread/baseline` | 600,000 | 25.04% / 25.06% / 24.95% / 24.95% | 0.11 pp |
| `ex9/4s4p/spread/bonus_forfeited` | 600,000 | 25.07% / 24.84% / 25.04% / 25.05% | 0.23 pp |
| `ex9/4s4p/spread/bonus_quick` | 600,000 | 25.02% / 24.96% / 25.00% / 25.01% | 0.06 pp |
| `ex9/4s4p/spread/capture=mandatory` | 600,000 | 24.95% / 24.97% / 24.99% / 25.08% | 0.13 pp |
| `ex9/4s4p/spread/capture=mandatory_extended` | 600,000 | 24.94% / 25.04% / 24.97% / 25.06% | 0.11 pp |
| `ex9/4s4p/spread/cold_start=free_entry` | 600,000 | 25.03% / 25.00% / 25.02% / 24.95% | 0.08 pp |
| `ex9/4s4p/spread/cold_start=strict` | 600,000 | 24.98% / 25.01% / 24.96% / 25.05% | 0.08 pp |
| `ex9/4s4p/spread/dreimal` | 600,000 | 24.98% / 24.97% / 25.02% / 25.03% | 0.06 pp |
| `ex9/4s4p/spread/goal_no_jump` | 600,000 | 24.96% / 25.09% / 24.90% / 25.05% | 0.19 pp |

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
| `ex10/6s2p/random/barriers` | conf | 600,000 | 135.0 | 67.8 | 162.0 | 67.8 | 5.9175 | 5.9175 | 8.3091 | 4.8137 | 7.3134 | 0.0000 | 4.6680 | 15.9 | 0.0000 | 1.3058 | 1.2030 | 0.3058 | 49.6 | 0.2454 |
| `ex10/6s2p/random/baseline` | conf | 600,000 | 136.6 | 68.6 | 164.0 | 68.6 | 6.3381 | 6.3381 | 8.2953 | 5.0515 | 7.3493 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3055 | 1.2027 | 0.3055 | 50.6 | 0.2505 |
| `ex10/6s2p/random/bonus_forfeited` | conf | 600,000 | 138.8 | 69.7 | 165.3 | 69.7 | 6.3721 | 6.3721 | 9.4435 | 5.1706 | 7.3992 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3099 | 1.2125 | 0.3099 | 47.6 | 0.2358 |
| `ex10/6s2p/random/bonus_quick` | conf | 600,000 | 126.9 | 63.7 | 169.7 | 63.7 | 6.6144 | 6.6144 | 5.4487 | 2.3163 | 7.6508 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3047 | 1.2019 | 0.3047 | 43.0 | 0.2131 |
| `ex10/6s2p/random/capture=mandatory` | conf | 600,000 | 161.1 | 80.8 | 193.3 | 80.8 | 10.9 | 10.9 | 13.6 | 10.6 | 7.4725 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3173 | 1.2171 | 0.3173 | 62.1 | 0.3076 |
| `ex10/6s2p/random/capture=mandatory_extended` | conf | 600,000 | 174.9 | 87.7 | 209.9 | 87.7 | 12.2 | 12.2 | 14.8 | 11.9 | 7.8659 | 0.0000 | 0.0000 | 0.0000 | 0.4841 | 1.3263 | 1.2286 | 0.3263 | 63.3 | 0.3133 |
| `ex10/6s2p/random/cold_start=free_entry` | conf | 600,000 | 138.1 | 69.3 | 165.7 | 69.3 | 9.2262 | 9.2262 | 2.9401 | 2.2945 | 7.4916 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.2953 | 1.1822 | 0.2953 | 48.8 | 0.2416 |
| `ex10/6s2p/random/cold_start=strict` | conf | 600,000 | 144.8 | 72.6 | 173.7 | 72.6 | 6.0932 | 6.0932 | 18.0 | 16.7 | 4.8213 | 5.0055 | 0.0000 | 0.0000 | 0.0000 | 1.2985 | 1.1999 | 0.2985 | 53.0 | 0.2624 |
| `ex10/6s2p/random/dreimal` | conf | 600,000 | 136.0 | 68.2 | 167.2 | 68.2 | 6.6090 | 6.6090 | 5.3771 | 2.2094 | 7.7272 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3037 | 1.1949 | 0.3037 | 47.4 | 0.2345 |
| `ex10/6s2p/random/goal_no_jump` | conf | 600,000 | 152.4 | 76.4 | 182.9 | 76.4 | 6.6529 | 6.6529 | 15.3 | 5.1129 | 7.7027 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3212 | 1.2657 | 0.3212 | 33.9 | 0.1679 |
| `ex10/6s3p/random/barriers` | conf | 600,000 | 284.1 | 101.1 | 341.0 | 82.4 | 20.2 | 20.2 | 25.7 | 19.0 | 12.7 | 0.0000 | 8.0517 | 37.3 | 0.0000 | 1.5530 | 1.3451 | 0.2765 | 47.6 | 0.2355 |
| `ex10/6s3p/random/baseline` | conf | 600,000 | 289.8 | 103.1 | 347.7 | 84.1 | 21.4 | 21.4 | 26.2 | 20.2 | 12.9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5523 | 1.3458 | 0.2761 | 48.4 | 0.2397 |
| `ex10/6s3p/random/bonus_forfeited` | conf | 600,000 | 294.2 | 104.6 | 350.5 | 85.4 | 21.6 | 21.6 | 28.6 | 20.7 | 13.0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5594 | 1.3588 | 0.2797 | 46.0 | 0.2277 |
| `ex10/6s3p/random/bonus_quick` | conf | 600,000 | 264.3 | 93.6 | 367.7 | 77.6 | 23.1 | 23.1 | 15.0 | 9.4350 | 13.6 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5492 | 1.3394 | 0.2746 | 42.0 | 0.2081 |
| `ex10/6s3p/random/capture=mandatory` | conf | 600,000 | 373.9 | 133.1 | 448.7 | 108.1 | 35.2 | 35.2 | 48.4 | 44.7 | 14.3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5652 | 1.3763 | 0.2826 | 56.4 | 0.2792 |
| `ex10/6s3p/random/capture=mandatory_extended` | conf | 600,000 | 419.7 | 149.3 | 503.7 | 121.6 | 40.5 | 40.5 | 54.2 | 51.6 | 15.5 | 0.0000 | 0.0000 | 0.0000 | 1.1882 | 1.5842 | 1.4002 | 0.2921 | 56.8 | 0.2813 |
| `ex10/6s3p/random/cold_start=free_entry` | conf | 600,000 | 317.5 | 112.9 | 381.1 | 92.3 | 36.8 | 36.8 | 5.7578 | 4.2829 | 14.2 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5437 | 1.3003 | 0.2718 | 53.7 | 0.2657 |
| `ex10/6s3p/random/cold_start=strict` | conf | 600,000 | 302.6 | 107.5 | 363.1 | 88.2 | 21.0 | 21.0 | 40.3 | 37.3 | 9.7659 | 4.9962 | 0.0000 | 0.0000 | 0.0000 | 1.5594 | 1.3498 | 0.2797 | 49.3 | 0.2442 |
| `ex10/6s3p/random/dreimal` | conf | 600,000 | 286.9 | 101.8 | 360.7 | 83.8 | 23.0 | 23.0 | 14.6 | 8.9559 | 13.4 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5358 | 1.3228 | 0.2679 | 46.6 | 0.2308 |
| `ex10/6s3p/random/goal_no_jump` | conf | 600,000 | 311.4 | 110.4 | 373.7 | 91.1 | 22.4 | 22.4 | 35.1 | 20.8 | 13.5 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5498 | 1.3885 | 0.2749 | 38.2 | 0.1890 |
| `ex10/6s4p/random/barriers` | conf | 600,000 | 506.5 | 141.1 | 607.8 | 100.9 | 45.7 | 45.7 | 59.0 | 50.6 | 18.0 | 0.0000 | 12.9 | 74.0 | 0.0000 | 1.7526 | 1.4551 | 0.2509 | 49.6 | 0.2455 |
| `ex10/6s4p/random/baseline` | conf | 600,000 | 516.4 | 143.8 | 619.7 | 103.0 | 48.0 | 48.0 | 60.2 | 53.6 | 18.3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7488 | 1.4547 | 0.2496 | 50.4 | 0.2493 |
| `ex10/6s4p/random/bonus_forfeited` | conf | 600,000 | 523.2 | 145.6 | 624.1 | 104.5 | 48.3 | 48.3 | 64.0 | 54.7 | 18.4 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7568 | 1.4690 | 0.2523 | 48.1 | 0.2383 |
| `ex10/6s4p/random/bonus_quick` | conf | 600,000 | 471.7 | 130.5 | 682.2 | 95.7 | 54.5 | 54.5 | 31.4 | 26.4 | 20.0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7404 | 1.4391 | 0.2468 | 44.8 | 0.2220 |
| `ex10/6s4p/random/capture=mandatory` | conf | 600,000 | 697.6 | 193.6 | 837.1 | 139.2 | 77.0 | 77.0 | 113.9 | 114.9 | 21.5 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7665 | 1.4928 | 0.2555 | 57.0 | 0.2823 |
| `ex10/6s4p/random/capture=mandatory_extended` | conf | 600,000 | 798.3 | 221.1 | 958.0 | 159.6 | 89.5 | 89.5 | 130.4 | 134.5 | 23.8 | 0.0000 | 0.0000 | 0.0000 | 2.0042 | 1.7900 | 1.5246 | 0.2633 | 56.8 | 0.2813 |
| `ex10/6s4p/random/cold_start=free_entry` | conf | 600,000 | 663.4 | 184.2 | 796.1 | 132.1 | 106.0 | 106.0 | 8.4670 | 8.2855 | 24.3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7310 | 1.3801 | 0.2437 | 63.6 | 0.3146 |
| `ex10/6s4p/random/cold_start=strict` | conf | 600,000 | 533.6 | 148.2 | 640.3 | 107.1 | 47.4 | 47.4 | 78.9 | 76.0 | 15.1 | 5.0082 | 0.0000 | 0.0000 | 0.0000 | 1.7679 | 1.4623 | 0.2560 | 50.8 | 0.2517 |
| `ex10/6s4p/random/dreimal` | conf | 600,000 | 514.2 | 142.7 | 662.7 | 103.5 | 53.8 | 53.8 | 30.5 | 24.9 | 19.3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7141 | 1.4128 | 0.2380 | 49.4 | 0.2446 |
| `ex10/6s4p/random/goal_no_jump` | conf | 600,000 | 542.6 | 150.7 | 651.1 | 109.2 | 49.6 | 49.6 | 70.4 | 55.2 | 18.9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7290 | 1.4672 | 0.2430 | 43.6 | 0.2160 |
| `ex10/6s6p/random/barriers` | conf | 600,000 | 1,228 | 238.7 | 1,474 | 145.6 | 141.4 | 141.4 | 207.7 | 207.7 | 28.8 | 0.0000 | 27.5 | 210.4 | 0.0000 | 2.0787 | 1.6216 | 0.2157 | 54.0 | 0.2673 |
| `ex10/6s6p/random/baseline` | conf | 600,000 | 1,241 | 241.3 | 1,489 | 146.9 | 145.2 | 145.2 | 211.2 | 217.4 | 29.1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.0712 | 1.6172 | 0.2142 | 54.7 | 0.2707 |
| `ex10/6s6p/random/bonus_forfeited` | conf | 600,000 | 1,257 | 244.2 | 1,502 | 149.2 | 146.4 | 146.4 | 219.1 | 221.2 | 29.3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.0745 | 1.6314 | 0.2149 | 52.7 | 0.2608 |
| `ex10/6s6p/random/bonus_quick` | conf | 600,000 | 1,207 | 231.9 | 1,894 | 146.5 | 194.1 | 194.1 | 106.5 | 129.8 | 35.7 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.0560 | 1.5905 | 0.2112 | 51.9 | 0.2570 |
| `ex10/6s6p/random/capture=mandatory` | conf | 600,000 | 1,739 | 335.4 | 2,087 | 205.5 | 224.7 | 224.7 | 383.5 | 419.6 | 36.0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.0886 | 1.6493 | 0.2177 | 60.1 | 0.2976 |
| `ex10/6s6p/random/capture=mandatory_extended` | conf | 600,000 | 2,041 | 391.8 | 2,449 | 242.7 | 265.9 | 265.9 | 451.7 | 501.2 | 41.3 | 0.0000 | 0.0000 | 0.0000 | 3.9874 | 2.1326 | 1.6994 | 0.2265 | 58.7 | 0.2907 |
| `ex10/6s6p/random/cold_start=free_entry` | conf | 600,000 | 2,557 | 483.5 | 3,068 | 306.3 | 597.9 | 597.9 | 13.7 | 44.1 | 68.8 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.0935 | 1.5392 | 0.2187 | 83.4 | 0.4127 |
| `ex10/6s6p/random/cold_start=strict` | conf | 600,000 | 1,266 | 245.6 | 1,519 | 151.1 | 144.3 | 144.3 | 238.3 | 249.8 | 26.2 | 5.0026 | 0.0000 | 0.0000 | 0.0000 | 2.0943 | 1.6257 | 0.2189 | 54.8 | 0.2714 |
| `ex10/6s6p/random/dreimal` | conf | 600,000 | 1,287 | 248.9 | 1,760 | 154.2 | 182.2 | 182.2 | 99.9 | 118.0 | 32.8 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.0231 | 1.5548 | 0.2046 | 55.5 | 0.2749 |
| `ex10/6s6p/random/goal_no_jump` | conf | 600,000 | 1,276 | 248.2 | 1,531 | 151.7 | 148.0 | 148.0 | 224.5 | 222.2 | 29.7 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.0364 | 1.5951 | 0.2073 | 51.4 | 0.2544 |
| `ex11/6s2p/focus_front-vs-random/baseline` | conf | 600,000 | 128.8 | 64.6 | 154.5 | 64.6 | 5.7656 | 5.7656 | 8.4147 | 5.1437 | 6.6950 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.2735 | 1.1762 | 0.2735 | 56.1 | 0.2778 |
| `ex11/6s2p/focus_rear-vs-random/baseline` | conf | 600,000 | 140.6 | 70.5 | 168.7 | 70.5 | 6.7079 | 6.7079 | 8.4075 | 5.0453 | 7.4092 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3061 | 1.1842 | 0.3061 | 55.7 | 0.2757 |
| `ex11/6s2p/greedy_capture-vs-random/baseline` | conf | 600,000 | 147.2 | 73.8 | 176.6 | 73.8 | 8.7136 | 8.7136 | 10.8 | 7.6079 | 7.0851 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.2746 | 1.1778 | 0.2746 | 62.7 | 0.3105 |
| `ex11/6s2p/spread-vs-random/baseline` | conf | 600,000 | 139.1 | 69.8 | 167.0 | 69.8 | 6.4633 | 6.4633 | 8.2701 | 4.9555 | 7.2806 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3025 | 1.1779 | 0.3025 | 56.7 | 0.2806 |
| `ex11/6s3p/focus_front-vs-random/baseline` | conf | 600,003 | 267.7 | 96.0 | 321.2 | 76.1 | 18.9 | 18.9 | 25.4 | 19.2 | 11.3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.4878 | 1.2965 | 0.2439 | 51.6 | 0.2552 |
| `ex11/6s3p/focus_rear-vs-random/baseline` | conf | 600,003 | 308.1 | 110.1 | 369.7 | 88.4 | 23.5 | 23.5 | 27.0 | 20.8 | 13.2 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5765 | 1.3348 | 0.2883 | 53.6 | 0.2653 |
| `ex11/6s3p/greedy_capture-vs-random/baseline` | conf | 600,003 | 319.5 | 113.8 | 383.5 | 92.4 | 26.6 | 26.6 | 33.4 | 28.2 | 13.2 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5312 | 1.3386 | 0.2656 | 53.7 | 0.2658 |
| `ex11/6s3p/spread-vs-random/baseline` | conf | 600,003 | 308.6 | 110.4 | 370.3 | 88.2 | 23.4 | 23.4 | 26.8 | 20.7 | 13.1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5898 | 1.3282 | 0.2949 | 54.5 | 0.2700 |
| `ex11/6s4p/focus_front-vs-random/baseline` | conf | 600,000 | 470.0 | 132.7 | 564.1 | 90.5 | 41.9 | 41.9 | 56.4 | 48.8 | 15.6 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.6638 | 1.3876 | 0.2213 | 53.0 | 0.2625 |
| `ex11/6s4p/focus_rear-vs-random/baseline` | conf | 600,000 | 553.6 | 155.1 | 664.3 | 108.8 | 52.6 | 52.6 | 62.8 | 55.9 | 18.9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7609 | 1.4388 | 0.2536 | 54.3 | 0.2690 |
| `ex11/6s4p/greedy_capture-vs-random/baseline` | conf | 600,000 | 564.7 | 157.0 | 677.7 | 112.8 | 56.0 | 56.0 | 73.7 | 68.8 | 19.1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7403 | 1.4580 | 0.2468 | 53.1 | 0.2630 |
| `ex11/6s4p/spread-vs-random/baseline` | conf | 600,000 | 556.6 | 156.3 | 667.9 | 108.8 | 52.9 | 52.9 | 62.7 | 55.9 | 18.9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7639 | 1.4297 | 0.2546 | 55.1 | 0.2728 |
| `ex11/6s6p/focus_front-vs-random/baseline` | conf | 600,012 | 1,128 | 223.2 | 1,354 | 126.7 | 128.5 | 128.5 | 192.7 | 194.7 | 24.5 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.9629 | 1.5310 | 0.1926 | 56.9 | 0.2816 |
| `ex11/6s6p/focus_rear-vs-random/baseline` | conf | 600,012 | 1,315 | 257.3 | 1,578 | 153.5 | 155.7 | 155.7 | 220.6 | 227.1 | 30.1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.0602 | 1.5997 | 0.2120 | 56.9 | 0.2819 |
| `ex11/6s6p/greedy_capture-vs-random/baseline` | conf | 600,012 | 1,327 | 257.4 | 1,593 | 157.5 | 159.2 | 159.2 | 239.8 | 250.7 | 30.3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.0693 | 1.6193 | 0.2139 | 56.0 | 0.2771 |
| `ex11/6s6p/spread-vs-random/baseline` | conf | 600,012 | 1,320 | 258.8 | 1,584 | 153.6 | 156.3 | 156.3 | 220.6 | 227.4 | 30.1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.0549 | 1.5927 | 0.2110 | 57.1 | 0.2828 |
| `ex12/2p/4s-adjacent/random/barriers` | conf | 600,000 | 116.3 | 58.4 | 139.6 | 58.4 | 5.3161 | 5.3161 | 9.2156 | 5.4074 | 6.9452 | 0.0000 | 4.0663 | 13.4 | 0.0000 | 1.3133 | 1.2161 | 0.3133 | 41.0 | 0.2410 |
| `ex12/2p/4s-adjacent/random/baseline` | conf | 600,000 | 117.8 | 59.2 | 141.4 | 59.2 | 5.7267 | 5.7267 | 9.2378 | 5.7075 | 7.0002 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3119 | 1.2135 | 0.3119 | 42.3 | 0.2487 |
| `ex12/2p/4s-adjacent/random/bonus_forfeited` | conf | 600,000 | 120.0 | 60.3 | 142.6 | 60.3 | 5.7623 | 5.7623 | 10.4 | 5.8660 | 7.0390 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3175 | 1.2253 | 0.3175 | 39.6 | 0.2331 |
| `ex12/2p/4s-adjacent/random/bonus_quick` | conf | 600,000 | 108.2 | 54.3 | 146.8 | 54.3 | 5.9557 | 5.9557 | 5.9900 | 2.5845 | 7.1937 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3130 | 1.2171 | 0.3130 | 34.4 | 0.2021 |
| `ex12/2p/4s-adjacent/random/capture=mandatory` | conf | 600,000 | 137.8 | 69.1 | 165.3 | 69.1 | 9.5459 | 9.5459 | 14.6 | 11.2 | 7.0686 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3196 | 1.2206 | 0.3196 | 54.1 | 0.3183 |
| `ex12/2p/4s-adjacent/random/capture=mandatory_extended` | conf | 600,000 | 150.2 | 75.4 | 180.3 | 75.4 | 10.9 | 10.9 | 15.9 | 12.7 | 7.4270 | 0.0000 | 0.0000 | 0.0000 | 0.5111 | 1.3235 | 1.2283 | 0.3235 | 55.8 | 0.3280 |
| `ex12/2p/4s-adjacent/random/cold_start=free_entry` | conf | 600,000 | 118.8 | 59.7 | 142.6 | 59.7 | 8.4846 | 8.4846 | 2.9360 | 2.2750 | 7.2969 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3030 | 1.1976 | 0.3029 | 38.0 | 0.2238 |
| `ex12/2p/4s-adjacent/random/cold_start=strict` | conf | 600,000 | 126.3 | 63.4 | 151.5 | 63.4 | 5.5298 | 5.5298 | 19.1 | 17.5 | 4.5033 | 5.0022 | 0.0000 | 0.0000 | 0.0000 | 1.3028 | 1.2107 | 0.3028 | 44.7 | 0.2631 |
| `ex12/2p/4s-adjacent/random/dreimal` | conf | 600,000 | 117.1 | 58.8 | 145.2 | 58.8 | 6.0190 | 6.0190 | 5.9719 | 2.5338 | 7.3391 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3094 | 1.2089 | 0.3094 | 37.9 | 0.2230 |
| `ex12/2p/4s-adjacent/random/goal_no_jump` | conf | 600,000 | 133.7 | 67.1 | 160.5 | 67.1 | 6.0781 | 6.0781 | 16.7 | 5.7700 | 7.3887 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3357 | 1.2867 | 0.3357 | 27.0 | 0.1588 |
| `ex12/2p/4s-opposite/random/barriers` | conf | 600,000 | 115.8 | 58.2 | 139.0 | 58.2 | 5.0010 | 5.0010 | 8.4429 | 4.6057 | 7.2522 | 0.0000 | 4.2324 | 14.0 | 0.0000 | 1.3218 | 1.2237 | 0.3218 | 38.5 | 0.2267 |
| `ex12/2p/4s-opposite/random/baseline` | conf | 600,000 | 117.8 | 59.2 | 141.4 | 59.2 | 5.4729 | 5.4729 | 8.5025 | 4.9237 | 7.3373 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3216 | 1.2218 | 0.3216 | 40.1 | 0.2359 |
| `ex12/2p/4s-opposite/random/bonus_forfeited` | conf | 600,000 | 120.0 | 60.3 | 142.7 | 60.3 | 5.5047 | 5.5047 | 9.7118 | 5.0867 | 7.3821 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3269 | 1.2343 | 0.3269 | 37.5 | 0.2208 |
| `ex12/2p/4s-opposite/random/bonus_quick` | conf | 600,000 | 108.5 | 54.5 | 146.3 | 54.5 | 5.6280 | 5.6280 | 5.6847 | 2.2060 | 7.4399 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3217 | 1.2257 | 0.3217 | 32.3 | 0.1903 |
| `ex12/2p/4s-opposite/random/capture=mandatory` | conf | 600,000 | 141.7 | 71.1 | 170.0 | 71.1 | 9.8766 | 9.8766 | 13.9 | 10.6 | 7.6848 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3195 | 1.2224 | 0.3195 | 54.2 | 0.3190 |
| `ex12/2p/4s-opposite/random/capture=mandatory_extended` | conf | 600,000 | 154.3 | 77.4 | 185.1 | 77.4 | 11.2 | 11.2 | 15.2 | 12.0 | 8.0913 | 0.0000 | 0.0000 | 0.0000 | 0.4796 | 1.3232 | 1.2295 | 0.3232 | 55.9 | 0.3287 |
| `ex12/2p/4s-opposite/random/cold_start=free_entry` | conf | 600,000 | 116.6 | 58.6 | 140.0 | 58.6 | 7.1490 | 7.1490 | 2.9198 | 2.1932 | 7.7126 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3218 | 1.2150 | 0.3218 | 33.8 | 0.1987 |
| `ex12/2p/4s-opposite/random/cold_start=strict` | conf | 600,000 | 126.8 | 63.7 | 152.2 | 63.7 | 5.3865 | 5.3865 | 18.5 | 17.0 | 4.7246 | 4.9971 | 0.0000 | 0.0000 | 0.0000 | 1.3112 | 1.2173 | 0.3112 | 42.9 | 0.2524 |
| `ex12/2p/4s-opposite/random/dreimal` | conf | 600,000 | 117.2 | 58.8 | 144.6 | 58.8 | 5.6872 | 5.6872 | 5.6810 | 2.1811 | 7.5753 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3146 | 1.2158 | 0.3146 | 36.1 | 0.2123 |
| `ex12/2p/4s-opposite/random/goal_no_jump` | conf | 600,000 | 133.9 | 67.2 | 160.7 | 67.2 | 5.8462 | 5.8462 | 16.2 | 5.0496 | 7.7662 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3457 | 1.2954 | 0.3457 | 25.8 | 0.1518 |
| `ex1b/6s6p/random/baseline` | conf | 400,002 | 1,241 | 241.3 | 1,489 | 146.9 | 145.2 | 145.2 | 211.2 | 217.4 | 29.1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.0658 | 1.6146 | 0.2132 | 54.9 | 0.2716 |
| `ex2/4s2p/greedy_capture/mandatory` | desc | 20,000 | 137.8 | 69.2 | 165.4 | 69.2 | 9.5614 | 9.5614 | 14.6 | 11.2 | 7.0777 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3209 | 1.2216 | 0.3209 | 53.9 | 0.3172 |
| `ex2/4s2p/greedy_capture/mandatory_extended` | desc | 20,000 | 150.6 | 75.5 | 180.6 | 75.5 | 10.9 | 10.9 | 16.0 | 12.8 | 7.4631 | 0.0000 | 0.0000 | 0.0000 | 0.5078 | 1.3229 | 1.2307 | 0.3229 | 55.5 | 0.3267 |
| `ex2/4s2p/greedy_capture/optional` | desc | 20,000 | 137.6 | 69.0 | 165.1 | 69.0 | 9.5129 | 9.5129 | 14.6 | 11.2 | 7.0701 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3161 | 1.2196 | 0.3161 | 54.0 | 0.3178 |
| `ex2/4s2p/random/mandatory` | desc | 20,000 | 137.9 | 69.2 | 165.5 | 69.2 | 9.5602 | 9.5602 | 14.6 | 11.2 | 7.0458 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3158 | 1.2170 | 0.3159 | 53.8 | 0.3166 |
| `ex2/4s2p/random/mandatory_extended` | desc | 20,000 | 150.8 | 75.6 | 180.9 | 75.6 | 10.9 | 10.9 | 15.9 | 12.7 | 7.4619 | 0.0000 | 0.0000 | 0.0000 | 0.5160 | 1.3236 | 1.2284 | 0.3236 | 55.7 | 0.3276 |
| `ex2/4s2p/random/optional` | desc | 20,000 | 118.0 | 59.3 | 141.6 | 59.3 | 5.7413 | 5.7413 | 9.3445 | 5.7936 | 7.0004 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3147 | 1.2166 | 0.3146 | 42.1 | 0.2476 |
| `ex2/4s2p/spread/mandatory` | desc | 20,000 | 146.5 | 73.5 | 175.8 | 73.5 | 9.7968 | 9.7968 | 14.1 | 10.3 | 7.5555 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3193 | 1.1948 | 0.3193 | 53.2 | 0.3128 |
| `ex2/4s2p/spread/mandatory_extended` | desc | 20,000 | 163.1 | 81.8 | 195.7 | 81.8 | 11.6 | 11.6 | 15.5 | 11.8 | 7.9658 | 0.0000 | 0.0000 | 0.0000 | 0.5510 | 1.3179 | 1.2024 | 0.3180 | 54.4 | 0.3201 |
| `ex2/4s2p/spread/optional` | desc | 20,000 | 120.3 | 60.4 | 144.3 | 60.4 | 5.2542 | 5.2542 | 8.7981 | 5.1176 | 6.8106 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3044 | 1.1932 | 0.3044 | 39.1 | 0.2298 |
| `ex2/4s3p/greedy_capture/mandatory` | desc | 20,001 | 315.9 | 112.7 | 379.1 | 91.0 | 30.0 | 30.0 | 48.9 | 44.6 | 13.8 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5750 | 1.3864 | 0.2875 | 46.8 | 0.2754 |
| `ex2/4s3p/greedy_capture/mandatory_extended` | desc | 20,001 | 360.3 | 128.2 | 432.4 | 104.4 | 35.4 | 35.4 | 56.1 | 52.9 | 15.2 | 0.0000 | 0.0000 | 0.0000 | 1.2476 | 1.5854 | 1.4181 | 0.2927 | 46.8 | 0.2752 |
| `ex2/4s3p/greedy_capture/optional` | desc | 20,001 | 317.2 | 113.1 | 380.5 | 91.4 | 30.1 | 30.1 | 49.2 | 44.9 | 13.8 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5709 | 1.3876 | 0.2855 | 46.9 | 0.2757 |
| `ex2/4s3p/random/mandatory` | desc | 20,001 | 318.0 | 113.4 | 381.7 | 91.8 | 30.4 | 30.4 | 49.2 | 45.0 | 13.9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5674 | 1.3851 | 0.2837 | 46.8 | 0.2754 |
| `ex2/4s3p/random/mandatory_extended` | desc | 20,001 | 359.1 | 127.9 | 430.9 | 103.8 | 35.2 | 35.2 | 55.9 | 52.8 | 15.0 | 0.0000 | 0.0000 | 0.0000 | 1.2286 | 1.5795 | 1.4034 | 0.2898 | 47.5 | 0.2792 |
| `ex2/4s3p/random/optional` | desc | 20,001 | 250.7 | 89.3 | 300.9 | 72.6 | 19.2 | 19.2 | 28.9 | 22.6 | 12.4 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5581 | 1.3564 | 0.2791 | 40.1 | 0.2361 |
| `ex2/4s3p/spread/mandatory` | desc | 20,001 | 401.6 | 143.8 | 481.9 | 114.5 | 40.7 | 40.7 | 58.9 | 53.2 | 16.8 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.6408 | 1.4008 | 0.3204 | 55.8 | 0.3283 |
| `ex2/4s3p/spread/mandatory_extended` | desc | 20,001 | 476.8 | 170.5 | 572.1 | 136.2 | 50.0 | 50.0 | 69.4 | 65.2 | 19.0 | 0.0000 | 0.0000 | 0.0000 | 1.7250 | 1.6479 | 1.4183 | 0.3240 | 57.5 | 0.3383 |
| `ex2/4s3p/spread/optional` | desc | 20,001 | 316.3 | 113.4 | 379.7 | 90.1 | 26.4 | 26.4 | 33.1 | 25.5 | 14.8 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.6795 | 1.3709 | 0.3397 | 50.1 | 0.2948 |
| `ex2/4s4p/greedy_capture/mandatory` | desc | 20,000 | 572.4 | 159.2 | 686.9 | 113.8 | 63.3 | 63.3 | 111.7 | 110.9 | 20.0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7548 | 1.5028 | 0.2516 | 46.5 | 0.2738 |
| `ex2/4s4p/greedy_capture/mandatory_extended` | desc | 20,000 | 660.8 | 183.5 | 792.8 | 131.3 | 74.6 | 74.6 | 129.1 | 131.5 | 22.3 | 0.0000 | 0.0000 | 0.0000 | 2.1257 | 1.7911 | 1.5240 | 0.2637 | 46.9 | 0.2757 |
| `ex2/4s4p/greedy_capture/optional` | desc | 20,000 | 571.9 | 159.0 | 686.4 | 113.8 | 63.4 | 63.4 | 111.5 | 110.8 | 20.1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7773 | 1.5068 | 0.2591 | 46.3 | 0.2724 |
| `ex2/4s4p/random/mandatory` | conf | 250,000 | 570.9 | 158.7 | 685.0 | 113.6 | 63.1 | 63.1 | 111.4 | 110.6 | 20.0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7699 | 1.5073 | 0.2566 | 46.1 | 0.2714 |
| `ex2/4s4p/random/mandatory_extended` | conf | 250,000 | 661.4 | 183.4 | 793.6 | 131.9 | 74.8 | 74.8 | 129.2 | 131.7 | 22.4 | 0.0000 | 0.0000 | 0.0000 | 2.1441 | 1.7933 | 1.5405 | 0.2644 | 46.1 | 0.2714 |
| `ex2/4s4p/random/optional` | conf | 250,000 | 438.2 | 122.2 | 525.8 | 87.2 | 41.7 | 41.7 | 66.1 | 59.0 | 17.3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7587 | 1.4776 | 0.2529 | 41.1 | 0.2416 |
| `ex2/4s4p/spread/mandatory` | desc | 20,000 | 769.3 | 214.6 | 923.3 | 150.6 | 90.9 | 90.9 | 143.7 | 142.1 | 26.1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.8304 | 1.5166 | 0.2768 | 55.7 | 0.3274 |
| `ex2/4s4p/spread/mandatory_extended` | desc | 20,000 | 935.1 | 260.2 | 1,122 | 183.7 | 112.9 | 112.9 | 174.2 | 177.6 | 30.3 | 0.0000 | 0.0000 | 0.0000 | 3.0481 | 1.8357 | 1.5446 | 0.2786 | 55.9 | 0.3289 |
| `ex2/4s4p/spread/optional` | desc | 20,000 | 623.4 | 174.2 | 748.1 | 122.0 | 65.9 | 65.9 | 85.8 | 76.9 | 23.3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.8762 | 1.5013 | 0.2921 | 52.4 | 0.3085 |
| `ex2/6s6p/greedy_capture/mandatory` | desc | 20,004 | 1,734 | 334.5 | 2,081 | 205.2 | 224.0 | 224.0 | 382.8 | 418.6 | 36.0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.0824 | 1.6514 | 0.2165 | 59.5 | 0.2946 |
| `ex2/6s6p/greedy_capture/mandatory_extended` | desc | 20,004 | 2,048 | 393.0 | 2,458 | 243.8 | 267.2 | 267.2 | 453.2 | 503.0 | 41.3 | 0.0000 | 0.0000 | 0.0000 | 4.0080 | 2.1456 | 1.6953 | 0.2291 | 58.7 | 0.2907 |
| `ex2/6s6p/greedy_capture/optional` | desc | 20,004 | 1,738 | 335.3 | 2,086 | 205.4 | 224.7 | 224.7 | 382.8 | 418.8 | 36.0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.0943 | 1.6572 | 0.2189 | 59.9 | 0.2965 |
| `ex2/6s6p/random/mandatory` | desc | 20,004 | 1,734 | 334.4 | 2,080 | 204.8 | 223.6 | 223.6 | 382.8 | 418.6 | 35.9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.0989 | 1.6467 | 0.2198 | 60.1 | 0.2976 |
| `ex2/6s6p/random/mandatory_extended` | desc | 20,004 | 2,045 | 392.6 | 2,454 | 243.6 | 266.6 | 266.6 | 452.2 | 501.9 | 41.4 | 0.0000 | 0.0000 | 0.0000 | 3.9822 | 2.1262 | 1.7043 | 0.2252 | 58.4 | 0.2891 |
| `ex2/6s6p/random/optional` | desc | 20,004 | 1,238 | 240.9 | 1,486 | 146.5 | 144.9 | 144.9 | 210.7 | 216.9 | 29.1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.0543 | 1.6117 | 0.2109 | 54.7 | 0.2710 |
| `ex2/6s6p/spread/mandatory` | desc | 20,004 | 2,585 | 500.4 | 3,102 | 298.0 | 348.1 | 348.1 | 547.7 | 600.9 | 51.6 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.1672 | 1.6764 | 0.2334 | 70.6 | 0.3497 |
| `ex2/6s6p/spread/mandatory_extended` | desc | 20,004 | 3,150 | 606.8 | 3,780 | 366.0 | 427.3 | 427.3 | 668.7 | 744.8 | 61.3 | 0.0000 | 0.0000 | 0.0000 | 5.4495 | 2.1747 | 1.6985 | 0.2349 | 69.1 | 0.3423 |
| `ex2/6s6p/spread/optional` | desc | 20,004 | 2,027 | 393.4 | 2,432 | 233.3 | 255.3 | 255.3 | 317.7 | 331.1 | 44.5 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.1494 | 1.6472 | 0.2299 | 69.3 | 0.3429 |
| `ex3/deviant/4s2p/focus_front-vs-focus_rear` | desc | 20,000 | 116.4 | 58.4 | 139.7 | 58.4 | 6.0429 | 6.0429 | 9.8941 | 6.1596 | 6.5148 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.2778 | 1.1681 | 0.2778 | 54.2 | 0.3189 |
| `ex3/deviant/4s2p/focus_front-vs-random` | desc | 20,000 | 110.8 | 55.7 | 133.1 | 55.7 | 5.1860 | 5.1860 | 9.1680 | 5.6390 | 6.4165 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.2885 | 1.1924 | 0.2884 | 45.9 | 0.2701 |
| `ex3/deviant/4s2p/focus_front-vs-spread` | desc | 20,000 | 117.6 | 59.1 | 141.1 | 59.1 | 6.2054 | 6.2054 | 10.1 | 6.3925 | 6.4759 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.2844 | 1.1645 | 0.2843 | 57.0 | 0.3351 |
| `ex3/deviant/4s2p/focus_rear-vs-focus_front` | desc | 20,000 | 116.6 | 58.5 | 139.9 | 58.5 | 6.0823 | 6.0823 | 9.9008 | 6.1985 | 6.4958 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.2891 | 1.1695 | 0.2890 | 54.2 | 0.3191 |
| `ex3/deviant/4s2p/focus_rear-vs-random` | desc | 20,000 | 122.1 | 61.3 | 146.5 | 61.3 | 6.1005 | 6.1005 | 9.4461 | 5.7127 | 7.1391 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3175 | 1.2083 | 0.3175 | 44.1 | 0.2594 |
| `ex3/deviant/4s2p/focus_rear-vs-spread` | desc | 20,000 | 121.6 | 61.0 | 145.9 | 61.0 | 5.5786 | 5.5786 | 8.9563 | 5.2773 | 6.8894 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.2988 | 1.1880 | 0.2988 | 41.0 | 0.2411 |
| `ex3/deviant/4s2p/random-vs-focus_front` | desc | 20,000 | 111.2 | 55.9 | 133.5 | 55.9 | 5.2057 | 5.2057 | 9.2865 | 5.7233 | 6.4479 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.2851 | 1.1915 | 0.2851 | 45.7 | 0.2691 |
| `ex3/deviant/4s2p/random-vs-focus_rear` | desc | 20,000 | 122.3 | 61.4 | 146.7 | 61.4 | 6.2065 | 6.2065 | 9.2577 | 5.6543 | 7.1569 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3199 | 1.2027 | 0.3200 | 44.9 | 0.2640 |
| `ex3/deviant/4s2p/random-vs-spread` | desc | 20,000 | 121.0 | 60.7 | 145.2 | 60.7 | 5.9577 | 5.9577 | 9.1895 | 5.5839 | 7.0869 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3128 | 1.1965 | 0.3127 | 45.4 | 0.2669 |
| `ex3/deviant/4s2p/spread-vs-focus_front` | desc | 20,000 | 117.6 | 59.1 | 141.1 | 59.1 | 6.2223 | 6.2223 | 10.0 | 6.2370 | 6.4775 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.2939 | 1.1579 | 0.2939 | 56.9 | 0.3346 |
| `ex3/deviant/4s2p/spread-vs-focus_rear` | desc | 20,000 | 121.7 | 61.1 | 146.1 | 61.1 | 5.5702 | 5.5702 | 9.0424 | 5.3172 | 6.9186 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.2986 | 1.1882 | 0.2986 | 41.0 | 0.2409 |
| `ex3/deviant/4s2p/spread-vs-random` | desc | 20,000 | 121.2 | 60.9 | 145.4 | 60.9 | 5.9249 | 5.9249 | 9.3181 | 5.6653 | 7.0663 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3189 | 1.2045 | 0.3189 | 44.7 | 0.2632 |
| `ex3/deviant/4s3p/focus_front-vs-focus_rear` | desc | 20,007 | 262.2 | 95.4 | 314.6 | 71.9 | 20.5 | 20.5 | 30.1 | 22.8 | 11.3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5109 | 1.2741 | 0.2554 | 53.8 | 0.3165 |
| `ex3/deviant/4s3p/focus_front-vs-random` | desc | 20,007 | 230.6 | 82.7 | 276.7 | 65.7 | 16.8 | 16.8 | 27.6 | 20.9 | 11.0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5030 | 1.3172 | 0.2515 | 41.7 | 0.2450 |
| `ex3/deviant/4s3p/focus_front-vs-spread` | desc | 20,007 | 270.4 | 98.9 | 324.7 | 73.1 | 21.5 | 21.5 | 30.7 | 23.3 | 11.4 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5046 | 1.2528 | 0.2523 | 57.5 | 0.3382 |
| `ex3/deviant/4s3p/focus_rear-vs-focus_front` | desc | 20,007 | 222.7 | 80.3 | 267.2 | 62.5 | 16.0 | 16.0 | 27.5 | 20.3 | 10.3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.4827 | 1.2935 | 0.2413 | 42.0 | 0.2472 |
| `ex3/deviant/4s3p/focus_rear-vs-random` | desc | 20,007 | 266.5 | 95.3 | 319.7 | 76.4 | 21.1 | 21.1 | 30.1 | 23.3 | 12.8 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5688 | 1.3426 | 0.2844 | 43.9 | 0.2583 |
| `ex3/deviant/4s3p/focus_rear-vs-spread` | desc | 20,007 | 312.8 | 111.9 | 375.4 | 89.5 | 26.0 | 26.0 | 33.1 | 25.3 | 14.8 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.6631 | 1.3816 | 0.3315 | 49.0 | 0.2884 |
| `ex3/deviant/4s3p/random-vs-focus_front` | desc | 20,007 | 211.5 | 75.8 | 253.8 | 60.5 | 14.3 | 14.3 | 26.2 | 19.3 | 10.4 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5074 | 1.3256 | 0.2537 | 37.4 | 0.2199 |
| `ex3/deviant/4s3p/random-vs-focus_rear` | desc | 20,007 | 285.4 | 102.2 | 342.4 | 81.5 | 23.2 | 23.2 | 31.5 | 24.2 | 13.5 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.6020 | 1.3513 | 0.3010 | 46.7 | 0.2750 |
| `ex3/deviant/4s3p/random-vs-spread` | desc | 20,007 | 291.2 | 104.7 | 349.5 | 82.2 | 23.7 | 23.7 | 31.6 | 24.5 | 13.5 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.6118 | 1.3397 | 0.3059 | 50.0 | 0.2943 |
| `ex3/deviant/4s3p/spread-vs-focus_front` | desc | 20,007 | 224.9 | 81.3 | 269.9 | 62.8 | 16.4 | 16.4 | 27.7 | 20.7 | 10.3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.4836 | 1.2846 | 0.2418 | 43.0 | 0.2528 |
| `ex3/deviant/4s3p/spread-vs-focus_rear` | desc | 20,007 | 310.4 | 111.0 | 372.6 | 88.9 | 25.9 | 25.9 | 33.2 | 25.5 | 14.7 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.6459 | 1.3759 | 0.3229 | 48.6 | 0.2857 |
| `ex3/deviant/4s3p/spread-vs-random` | desc | 20,007 | 268.4 | 96.1 | 321.9 | 76.7 | 21.2 | 21.2 | 30.1 | 23.4 | 12.8 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5871 | 1.3495 | 0.2935 | 44.7 | 0.2631 |
| `ex3/deviant/4s4p/focus_front-vs-focus_rear` | desc | 20,000 | 492.0 | 141.3 | 590.4 | 88.9 | 48.3 | 48.3 | 71.1 | 61.5 | 16.0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.6582 | 1.3398 | 0.2194 | 56.4 | 0.3320 |
| `ex3/deviant/4s4p/focus_front-vs-random` | conf | 200,000 | 402.2 | 113.4 | 482.6 | 77.8 | 36.7 | 36.7 | 61.6 | 53.6 | 15.1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.6966 | 1.4255 | 0.2322 | 42.5 | 0.2500 |
| `ex3/deviant/4s4p/focus_front-vs-spread` | desc | 20,000 | 510.2 | 147.4 | 612.2 | 90.3 | 50.6 | 50.6 | 72.4 | 63.0 | 16.3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.6631 | 1.3175 | 0.2211 | 59.5 | 0.3498 |
| `ex3/deviant/4s4p/focus_rear-vs-focus_front` | desc | 20,000 | 356.5 | 101.8 | 427.8 | 67.8 | 30.5 | 30.5 | 56.4 | 46.6 | 13.4 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.6662 | 1.4210 | 0.2221 | 38.0 | 0.2234 |
| `ex3/deviant/4s4p/focus_rear-vs-random` | conf | 200,000 | 467.3 | 130.9 | 560.7 | 91.9 | 45.6 | 45.6 | 69.1 | 61.7 | 18.0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7599 | 1.4624 | 0.2533 | 43.9 | 0.2581 |
| `ex3/deviant/4s4p/focus_rear-vs-spread` | desc | 20,000 | 614.4 | 171.7 | 737.2 | 120.3 | 64.8 | 64.8 | 85.0 | 76.0 | 22.9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.8734 | 1.5056 | 0.2911 | 52.3 | 0.3078 |
| `ex3/deviant/4s4p/random-vs-focus_front` | desc | 20,000 | 340.4 | 96.2 | 408.6 | 66.1 | 28.1 | 28.1 | 54.4 | 44.9 | 13.4 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.6997 | 1.4482 | 0.2332 | 35.8 | 0.2104 |
| `ex3/deviant/4s4p/random-vs-focus_rear` | desc | 20,000 | 541.4 | 151.9 | 649.5 | 105.4 | 55.2 | 55.2 | 77.5 | 68.7 | 20.2 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.8047 | 1.4720 | 0.2682 | 49.4 | 0.2906 |
| `ex3/deviant/4s4p/random-vs-spread` | desc | 20,000 | 561.0 | 158.3 | 673.3 | 107.4 | 57.7 | 57.7 | 78.4 | 70.1 | 20.4 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.8022 | 1.4433 | 0.2674 | 52.0 | 0.3062 |
| `ex3/deviant/4s4p/spread-vs-focus_front` | desc | 20,000 | 358.3 | 102.7 | 430.1 | 67.7 | 30.9 | 30.9 | 56.3 | 46.7 | 13.4 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.6688 | 1.4106 | 0.2229 | 38.1 | 0.2242 |
| `ex3/deviant/4s4p/spread-vs-focus_rear` | desc | 20,000 | 596.9 | 166.4 | 716.3 | 117.7 | 62.5 | 62.5 | 83.7 | 74.5 | 22.5 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.8387 | 1.5023 | 0.2796 | 50.7 | 0.2983 |
| `ex3/deviant/4s4p/spread-vs-random` | conf | 200,000 | 470.6 | 132.1 | 564.7 | 92.1 | 46.0 | 46.0 | 69.2 | 61.9 | 18.0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7639 | 1.4551 | 0.2546 | 44.5 | 0.2616 |
| `ex3/deviant/6s6p/focus_front-vs-focus_rear` | desc | 20,016 | 1,582 | 319.9 | 1,898 | 152.2 | 191.0 | 191.0 | 249.1 | 252.4 | 27.1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.8358 | 1.3682 | 0.1672 | 78.5 | 0.3886 |
| `ex3/deviant/6s6p/focus_front-vs-random` | desc | 20,016 | 1,128 | 223.1 | 1,353 | 126.9 | 128.3 | 128.3 | 192.7 | 194.6 | 24.4 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.9565 | 1.5290 | 0.1913 | 56.2 | 0.2783 |
| `ex3/deviant/6s6p/focus_front-vs-spread` | desc | 20,016 | 1,656 | 337.7 | 1,987 | 153.5 | 200.5 | 200.5 | 254.7 | 259.3 | 27.3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.8297 | 1.3391 | 0.1659 | 82.1 | 0.4063 |
| `ex3/deviant/6s6p/focus_rear-vs-focus_front` | desc | 20,016 | 828.7 | 167.8 | 994.6 | 93.7 | 85.2 | 85.2 | 148.4 | 139.5 | 19.2 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.9959 | 1.6086 | 0.1992 | 43.2 | 0.2137 |
| `ex3/deviant/6s6p/focus_rear-vs-random` | desc | 20,016 | 1,318 | 257.7 | 1,581 | 153.9 | 156.2 | 156.2 | 220.7 | 227.4 | 30.3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.0645 | 1.6044 | 0.2129 | 57.0 | 0.2820 |
| `ex3/deviant/6s6p/focus_rear-vs-spread` | desc | 20,016 | 2,007 | 389.1 | 2,408 | 232.2 | 252.4 | 252.4 | 316.9 | 329.8 | 44.4 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.1862 | 1.6644 | 0.2372 | 68.8 | 0.3406 |
| `ex3/deviant/6s6p/random-vs-focus_front` | desc | 20,016 | 801.0 | 159.7 | 961.0 | 92.6 | 80.9 | 80.9 | 145.4 | 136.3 | 19.3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.0291 | 1.6331 | 0.2058 | 42.2 | 0.2090 |
| `ex3/deviant/6s6p/random-vs-focus_rear` | desc | 20,016 | 1,756 | 343.2 | 2,107 | 199.5 | 217.4 | 217.4 | 281.3 | 290.4 | 38.0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.1128 | 1.6038 | 0.2226 | 66.5 | 0.3290 |
| `ex3/deviant/6s6p/random-vs-spread` | desc | 20,016 | 1,830 | 359.9 | 2,196 | 204.0 | 227.0 | 227.0 | 288.0 | 298.8 | 38.9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.1093 | 1.5794 | 0.2219 | 68.8 | 0.3408 |
| `ex3/deviant/6s6p/spread-vs-focus_front` | desc | 20,016 | 828.3 | 168.1 | 993.8 | 93.4 | 85.1 | 85.1 | 148.4 | 139.5 | 19.3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.9861 | 1.6051 | 0.1972 | 43.4 | 0.2150 |
| `ex3/deviant/6s6p/spread-vs-focus_rear` | desc | 20,016 | 1,931 | 373.7 | 2,317 | 224.2 | 242.3 | 242.3 | 307.8 | 319.1 | 43.1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.1472 | 1.6490 | 0.2294 | 67.5 | 0.3341 |
| `ex3/deviant/6s6p/spread-vs-random` | desc | 20,016 | 1,322 | 259.3 | 1,587 | 153.8 | 156.7 | 156.7 | 220.4 | 227.2 | 30.3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.0694 | 1.5965 | 0.2139 | 57.4 | 0.2842 |
| `ex3/homogeneous/4s2p/focus_front` | desc | 20,000 | 102.9 | 51.7 | 123.4 | 51.7 | 3.9338 | 3.9338 | 8.5586 | 5.0273 | 6.3773 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.2942 | 1.2146 | 0.2943 | 37.6 | 0.2214 |
| `ex3/homogeneous/4s2p/focus_rear` | desc | 20,000 | 123.9 | 62.2 | 148.6 | 62.2 | 5.9812 | 5.9812 | 9.1693 | 5.3716 | 7.1357 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3108 | 1.1950 | 0.3108 | 41.9 | 0.2464 |
| `ex3/homogeneous/4s2p/random` | desc | 20,000 | 117.9 | 59.2 | 141.5 | 59.2 | 5.7294 | 5.7294 | 9.2806 | 5.7582 | 6.9896 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3048 | 1.2126 | 0.3048 | 42.2 | 0.2483 |
| `ex3/homogeneous/4s2p/spread` | desc | 20,000 | 120.3 | 60.4 | 144.3 | 60.4 | 5.2759 | 5.2759 | 8.8048 | 5.1737 | 6.8133 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.2976 | 1.1907 | 0.2976 | 39.7 | 0.2336 |
| `ex3/homogeneous/4s3p/focus_front` | desc | 20,001 | 194.5 | 69.3 | 233.2 | 56.5 | 11.8 | 11.8 | 24.6 | 17.4 | 10.4 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5404 | 1.3735 | 0.2702 | 31.7 | 0.1863 |
| `ex3/homogeneous/4s3p/focus_rear` | desc | 20,001 | 307.2 | 109.7 | 368.8 | 88.3 | 25.7 | 25.7 | 32.9 | 25.1 | 14.7 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.6346 | 1.3841 | 0.3173 | 47.4 | 0.2787 |
| `ex3/homogeneous/4s3p/random` | desc | 20,001 | 250.9 | 89.4 | 301.1 | 72.7 | 19.2 | 19.2 | 29.1 | 22.8 | 12.5 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5634 | 1.3605 | 0.2817 | 39.9 | 0.2344 |
| `ex3/homogeneous/4s3p/spread` | desc | 20,001 | 316.8 | 113.5 | 380.3 | 90.4 | 26.4 | 26.4 | 33.2 | 25.6 | 14.8 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.6677 | 1.3754 | 0.3339 | 50.5 | 0.2969 |
| `ex3/homogeneous/4s4p/focus_front` | desc | 20,000 | 315.1 | 88.5 | 378.1 | 62.3 | 24.3 | 24.3 | 51.1 | 41.0 | 13.2 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7342 | 1.4870 | 0.2447 | 32.2 | 0.1894 |
| `ex3/homogeneous/4s4p/focus_rear` | desc | 20,000 | 591.4 | 164.7 | 709.7 | 116.9 | 61.9 | 61.9 | 83.1 | 73.6 | 22.4 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.8509 | 1.5099 | 0.2836 | 49.9 | 0.2935 |
| `ex3/homogeneous/4s4p/random` | desc | 20,000 | 437.5 | 122.0 | 525.0 | 87.0 | 41.6 | 41.6 | 66.0 | 58.9 | 17.3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7571 | 1.4760 | 0.2523 | 41.1 | 0.2416 |
| `ex3/homogeneous/4s4p/spread` | desc | 20,000 | 622.6 | 174.1 | 747.1 | 121.6 | 65.8 | 65.8 | 85.5 | 76.7 | 23.3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.8780 | 1.4969 | 0.2926 | 53.3 | 0.3135 |
| `ex3/homogeneous/6s6p/focus_front` | desc | 20,004 | 746.2 | 147.0 | 895.4 | 88.2 | 72.8 | 72.8 | 137.6 | 126.8 | 19.0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.1040 | 1.6774 | 0.2208 | 39.5 | 0.1954 |
| `ex3/homogeneous/6s6p/focus_rear` | desc | 20,004 | 1,919 | 371.0 | 2,302 | 223.8 | 240.7 | 240.7 | 306.7 | 317.6 | 42.8 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.1706 | 1.6689 | 0.2341 | 66.4 | 0.3289 |
| `ex3/homogeneous/6s6p/random` | desc | 20,004 | 1,240 | 241.0 | 1,488 | 147.0 | 145.4 | 145.4 | 210.5 | 216.5 | 29.2 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.0683 | 1.6202 | 0.2137 | 54.8 | 0.2713 |
| `ex3/homogeneous/6s6p/spread` | desc | 20,004 | 2,021 | 392.7 | 2,426 | 232.5 | 254.5 | 254.5 | 316.9 | 330.2 | 44.5 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.1595 | 1.6421 | 0.2319 | 69.2 | 0.3427 |
| `ex4/4s4p/random/barriers=True` | conf | 40,000 | 430.5 | 120.1 | 516.6 | 85.6 | 39.9 | 39.9 | 64.7 | 55.8 | 17.0 | 0.0000 | 10.7 | 59.0 | 0.0000 | 1.7655 | 1.4750 | 0.2552 | 40.4 | 0.2377 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True` | conf | 40,000 | 566.8 | 155.5 | 911.6 | 116.3 | 86.5 | 86.5 | 68.5 | 74.7 | 23.8 | 1.3715 | 14.6 | 66.9 | 0.0000 | 1.7685 | 1.5087 | 0.2562 | 39.9 | 0.2345 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | conf | 40,000 | 590.3 | 161.8 | 944.0 | 121.7 | 88.9 | 88.9 | 77.2 | 76.3 | 24.7 | 1.3834 | 14.9 | 69.1 | 0.0000 | 1.7583 | 1.5068 | 0.2528 | 36.1 | 0.2122 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory-dreimal_wuerfeln=True` | conf | 40,000 | 564.0 | 154.7 | 888.5 | 115.7 | 86.6 | 86.6 | 63.1 | 65.4 | 25.0 | 0.0000 | 14.6 | 66.7 | 0.0000 | 1.7831 | 1.5111 | 0.2610 | 39.8 | 0.2342 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory-dreimal_wuerfeln=True-goal_no_jump=True` | conf | 40,000 | 586.5 | 160.7 | 919.1 | 120.9 | 88.8 | 88.8 | 71.5 | 66.8 | 26.0 | 0.0000 | 14.8 | 68.6 | 0.0000 | 1.7555 | 1.5013 | 0.2518 | 36.0 | 0.2117 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True` | conf | 40,000 | 664.2 | 181.9 | 1,071 | 136.5 | 103.8 | 103.8 | 77.0 | 88.6 | 27.5 | 1.3596 | 17.1 | 78.1 | 2.5345 | 1.8014 | 1.5450 | 0.2671 | 40.0 | 0.2351 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | conf | 40,000 | 689.1 | 188.5 | 1,107 | 142.0 | 106.7 | 106.7 | 84.2 | 90.8 | 28.6 | 1.3723 | 17.4 | 80.1 | 2.7643 | 1.7936 | 1.5433 | 0.2645 | 37.1 | 0.2183 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-dreimal_wuerfeln=True` | conf | 40,000 | 660.5 | 181.0 | 1,046 | 135.5 | 103.6 | 103.6 | 71.7 | 79.0 | 28.6 | 0.0000 | 17.0 | 77.5 | 2.5444 | 1.8058 | 1.5412 | 0.2686 | 39.9 | 0.2348 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-dreimal_wuerfeln=True-goal_no_jump=True` | conf | 40,000 | 686.0 | 187.8 | 1,083 | 141.2 | 106.7 | 106.7 | 78.7 | 81.4 | 29.8 | 0.0000 | 17.4 | 79.6 | 2.7812 | 1.7876 | 1.5285 | 0.2625 | 37.1 | 0.2183 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-cold_start=strict-dreimal_wuerfeln=True` | conf | 40,000 | 403.5 | 111.4 | 612.8 | 82.1 | 47.3 | 47.3 | 44.1 | 38.4 | 17.6 | 1.3860 | 11.9 | 56.6 | 0.0000 | 1.7792 | 1.4898 | 0.2597 | 34.0 | 0.2002 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | conf | 40,000 | 428.7 | 118.2 | 644.5 | 87.8 | 49.2 | 49.2 | 55.0 | 39.1 | 18.6 | 1.3731 | 12.2 | 59.9 | 0.0000 | 1.7660 | 1.5135 | 0.2553 | 28.4 | 0.1673 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-dreimal_wuerfeln=True` | conf | 40,000 | 399.0 | 110.3 | 586.9 | 81.1 | 47.1 | 47.1 | 38.5 | 28.8 | 18.9 | 0.0000 | 11.8 | 55.9 | 0.0000 | 1.7655 | 1.4822 | 0.2552 | 33.6 | 0.1975 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-dreimal_wuerfeln=True-goal_no_jump=True` | conf | 40,000 | 424.7 | 117.2 | 619.4 | 86.9 | 49.0 | 49.0 | 49.4 | 29.7 | 19.9 | 0.0000 | 12.1 | 59.4 | 0.0000 | 1.7626 | 1.5232 | 0.2542 | 28.3 | 0.1664 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True` | conf | 40,000 | 560.7 | 153.8 | 906.6 | 115.0 | 86.2 | 86.2 | 65.1 | 73.9 | 23.6 | 1.3797 | 14.6 | 66.8 | 0.0000 | 1.7738 | 1.4998 | 0.2579 | 41.7 | 0.2451 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | conf | 40,000 | 580.1 | 159.0 | 933.6 | 119.4 | 87.9 | 87.9 | 72.5 | 75.0 | 24.3 | 1.3690 | 14.8 | 68.5 | 0.0000 | 1.7457 | 1.4902 | 0.2486 | 37.9 | 0.2232 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-capture_mode=mandatory-dreimal_wuerfeln=True` | conf | 40,000 | 554.6 | 152.3 | 877.7 | 113.5 | 85.6 | 85.6 | 59.5 | 64.1 | 24.7 | 0.0000 | 14.5 | 66.1 | 0.0000 | 1.7652 | 1.4952 | 0.2551 | 41.8 | 0.2461 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-capture_mode=mandatory-dreimal_wuerfeln=True-goal_no_jump=True` | conf | 40,000 | 576.5 | 158.1 | 908.9 | 118.6 | 87.9 | 87.9 | 66.9 | 65.5 | 25.6 | 0.0000 | 14.8 | 68.1 | 0.0000 | 1.7416 | 1.4881 | 0.2472 | 38.2 | 0.2245 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True` | conf | 40,000 | 656.2 | 179.8 | 1,062 | 134.6 | 103.1 | 103.1 | 73.6 | 87.5 | 27.2 | 1.3726 | 17.1 | 77.5 | 2.5408 | 1.8012 | 1.5380 | 0.2671 | 41.8 | 0.2458 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | conf | 40,000 | 681.0 | 186.5 | 1,099 | 140.1 | 106.1 | 106.1 | 80.1 | 89.6 | 28.2 | 1.3854 | 17.4 | 79.5 | 2.7838 | 1.7835 | 1.5217 | 0.2612 | 38.9 | 0.2287 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-capture_mode=mandatory_extended-dreimal_wuerfeln=True` | conf | 40,000 | 653.5 | 179.1 | 1,039 | 133.9 | 103.2 | 103.2 | 68.2 | 78.1 | 28.4 | 0.0000 | 17.1 | 77.4 | 2.5419 | 1.7943 | 1.5264 | 0.2648 | 41.7 | 0.2456 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-capture_mode=mandatory_extended-dreimal_wuerfeln=True-goal_no_jump=True` | conf | 40,000 | 676.4 | 185.5 | 1,072 | 138.6 | 105.8 | 105.8 | 74.4 | 79.9 | 29.2 | 0.0000 | 17.3 | 79.2 | 2.7685 | 1.7685 | 1.5116 | 0.2562 | 39.2 | 0.2307 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-cold_start=strict-dreimal_wuerfeln=True` | conf | 40,000 | 397.1 | 109.7 | 607.7 | 80.8 | 46.9 | 46.9 | 40.7 | 37.8 | 17.6 | 1.3974 | 11.9 | 56.1 | 0.0000 | 1.7763 | 1.4778 | 0.2588 | 35.9 | 0.2112 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | conf | 40,000 | 420.1 | 115.8 | 638.6 | 86.1 | 48.8 | 48.8 | 50.0 | 38.5 | 18.3 | 1.3753 | 12.2 | 59.4 | 0.0000 | 1.7460 | 1.4981 | 0.2487 | 30.4 | 0.1789 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-dreimal_wuerfeln=True` | conf | 40,000 | 392.9 | 108.7 | 581.9 | 79.7 | 46.8 | 46.8 | 35.2 | 28.2 | 18.7 | 0.0000 | 11.8 | 55.5 | 0.0000 | 1.7602 | 1.4705 | 0.2534 | 35.9 | 0.2111 |
| `ex4/4s4p/random/barriers=True-bonus_roll_after_quick_entry=True-dreimal_wuerfeln=True-goal_no_jump=True` | conf | 40,000 | 416.1 | 114.8 | 613.2 | 85.2 | 48.6 | 48.6 | 44.5 | 28.9 | 19.6 | 0.0000 | 12.1 | 58.8 | 0.0000 | 1.7473 | 1.5014 | 0.2491 | 30.2 | 0.1775 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True` | conf | 40,000 | 437.9 | 122.1 | 521.5 | 87.2 | 40.2 | 40.2 | 68.7 | 57.1 | 17.2 | 0.0000 | 10.8 | 59.6 | 0.0000 | 1.7672 | 1.4947 | 0.2557 | 38.5 | 0.2267 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory` | conf | 40,000 | 577.0 | 160.3 | 688.5 | 114.9 | 62.7 | 62.7 | 115.4 | 110.0 | 19.9 | 0.0000 | 11.6 | 63.7 | 0.0000 | 1.7938 | 1.5209 | 0.2646 | 44.0 | 0.2586 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=free_entry` | conf | 40,000 | 1,836 | 495.4 | 2,198 | 382.9 | 499.0 | 499.0 | 15.1 | 66.8 | 77.0 | 0.0000 | 77.0 | 494.1 | 0.0000 | 1.7725 | 1.4735 | 0.2575 | 67.5 | 0.3972 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=free_entry-goal_no_jump=True` | conf | 40,000 | 1,893 | 511.0 | 2,264 | 394.8 | 511.1 | 511.1 | 21.9 | 68.3 | 78.6 | 0.0000 | 78.6 | 505.0 | 0.0000 | 1.7436 | 1.4420 | 0.2479 | 64.7 | 0.3808 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=strict` | conf | 40,000 | 593.7 | 164.5 | 708.5 | 119.1 | 62.0 | 62.0 | 134.0 | 132.5 | 17.0 | 5.0034 | 11.6 | 63.8 | 0.0000 | 1.8073 | 1.5354 | 0.2691 | 44.0 | 0.2589 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True` | conf | 40,000 | 596.3 | 164.4 | 835.6 | 121.0 | 79.0 | 79.0 | 64.6 | 67.6 | 21.8 | 1.3700 | 12.8 | 68.6 | 0.0000 | 1.7577 | 1.4785 | 0.2526 | 42.6 | 0.2508 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | conf | 40,000 | 620.5 | 170.9 | 865.5 | 126.4 | 81.1 | 81.1 | 73.5 | 69.0 | 22.6 | 1.3798 | 13.0 | 70.7 | 0.0000 | 1.7344 | 1.4811 | 0.2448 | 38.6 | 0.2271 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=strict-goal_no_jump=True` | conf | 40,000 | 626.9 | 173.1 | 746.6 | 127.1 | 64.6 | 64.6 | 147.8 | 136.3 | 18.1 | 4.9985 | 11.9 | 67.5 | 0.0000 | 1.7652 | 1.5227 | 0.2551 | 38.0 | 0.2233 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory-dreimal_wuerfeln=True` | conf | 40,000 | 588.6 | 162.4 | 808.5 | 119.2 | 78.7 | 78.7 | 58.9 | 57.9 | 22.9 | 0.0000 | 12.7 | 67.7 | 0.0000 | 1.7466 | 1.4785 | 0.2489 | 42.6 | 0.2504 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory-dreimal_wuerfeln=True-goal_no_jump=True` | conf | 40,000 | 615.5 | 169.7 | 842.3 | 125.2 | 81.2 | 81.2 | 68.2 | 59.6 | 23.8 | 0.0000 | 12.9 | 70.2 | 0.0000 | 1.7289 | 1.4748 | 0.2430 | 38.5 | 0.2268 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory-goal_no_jump=True` | conf | 40,000 | 609.1 | 168.6 | 725.1 | 122.8 | 65.1 | 65.1 | 128.6 | 113.6 | 21.0 | 0.0000 | 11.8 | 66.8 | 0.0000 | 1.7560 | 1.5144 | 0.2520 | 38.0 | 0.2234 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended` | conf | 40,000 | 668.2 | 185.1 | 798.0 | 133.7 | 74.3 | 74.3 | 133.3 | 131.0 | 22.6 | 0.0000 | 13.3 | 73.3 | 2.1959 | 1.8160 | 1.5586 | 0.2720 | 43.7 | 0.2571 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=free_entry` | conf | 40,000 | 2,198 | 591.5 | 2,632 | 460.7 | 598.5 | 598.5 | 15.8 | 81.8 | 90.6 | 0.0000 | 91.9 | 589.2 | 3.6463 | 1.7717 | 1.4872 | 0.2573 | 65.8 | 0.3868 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=free_entry-goal_no_jump=True` | conf | 40,000 | 2,270 | 611.1 | 2,717 | 476.2 | 615.1 | 615.1 | 20.8 | 84.4 | 93.1 | 0.0000 | 94.0 | 603.5 | 3.9657 | 1.7438 | 1.4664 | 0.2479 | 63.4 | 0.3729 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=strict` | conf | 40,000 | 685.9 | 189.6 | 819.1 | 137.9 | 73.7 | 73.7 | 152.1 | 153.6 | 19.5 | 5.0320 | 13.4 | 73.7 | 2.1820 | 1.8182 | 1.5560 | 0.2727 | 44.1 | 0.2592 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True` | conf | 40,000 | 695.4 | 191.6 | 976.2 | 141.0 | 94.5 | 94.5 | 71.9 | 79.4 | 24.9 | 1.3719 | 14.9 | 79.9 | 2.4811 | 1.7784 | 1.5099 | 0.2595 | 43.2 | 0.2542 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | conf | 40,000 | 723.2 | 199.1 | 1,012 | 147.1 | 97.3 | 97.3 | 79.7 | 81.6 | 26.0 | 1.3693 | 15.1 | 81.4 | 2.7266 | 1.7519 | 1.5050 | 0.2506 | 39.8 | 0.2343 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=strict-goal_no_jump=True` | conf | 40,000 | 723.8 | 199.7 | 863.1 | 146.5 | 77.1 | 77.1 | 165.6 | 159.8 | 20.8 | 5.0045 | 13.8 | 76.8 | 2.5026 | 1.7882 | 1.5482 | 0.2628 | 39.6 | 0.2328 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-dreimal_wuerfeln=True` | conf | 40,000 | 690.2 | 190.3 | 952.6 | 139.5 | 94.6 | 94.6 | 66.4 | 70.0 | 26.0 | 0.0000 | 14.9 | 79.2 | 2.4729 | 1.7630 | 1.5057 | 0.2543 | 43.4 | 0.2551 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-dreimal_wuerfeln=True-goal_no_jump=True` | conf | 40,000 | 719.1 | 198.1 | 990.8 | 146.1 | 97.6 | 97.6 | 74.3 | 72.5 | 27.1 | 0.0000 | 15.2 | 81.5 | 2.7399 | 1.7526 | 1.4977 | 0.2509 | 39.7 | 0.2337 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-goal_no_jump=True` | conf | 40,000 | 707.5 | 195.5 | 843.6 | 142.7 | 77.9 | 77.9 | 146.7 | 137.1 | 23.7 | 0.0000 | 13.8 | 76.7 | 2.4928 | 1.7902 | 1.5504 | 0.2634 | 39.3 | 0.2312 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-cold_start=free_entry` | conf | 40,000 | 553.6 | 153.4 | 659.7 | 110.8 | 90.9 | 90.9 | 13.2 | 8.7333 | 23.8 | 0.0000 | 27.2 | 167.7 | 0.0000 | 1.7344 | 1.4106 | 0.2448 | 47.2 | 0.2776 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-cold_start=free_entry-goal_no_jump=True` | conf | 40,000 | 600.8 | 166.4 | 712.9 | 120.8 | 96.2 | 96.2 | 26.4 | 8.9803 | 25.1 | 0.0000 | 28.3 | 178.6 | 0.0000 | 1.6984 | 1.4140 | 0.2328 | 39.5 | 0.2323 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-cold_start=strict` | conf | 40,000 | 455.0 | 126.5 | 542.0 | 91.2 | 39.6 | 39.6 | 87.5 | 79.8 | 14.0 | 4.9596 | 10.8 | 59.7 | 0.0000 | 1.7867 | 1.5014 | 0.2622 | 39.0 | 0.2296 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-cold_start=strict-dreimal_wuerfeln=True` | conf | 40,000 | 443.0 | 122.6 | 595.6 | 89.7 | 46.7 | 46.7 | 43.4 | 37.0 | 17.3 | 1.3673 | 11.4 | 61.8 | 0.0000 | 1.7517 | 1.4638 | 0.2506 | 37.3 | 0.2194 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | conf | 40,000 | 469.5 | 129.7 | 626.6 | 95.8 | 48.4 | 48.4 | 54.8 | 37.7 | 18.1 | 1.3649 | 11.6 | 65.1 | 0.0000 | 1.7352 | 1.4919 | 0.2451 | 31.5 | 0.1852 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-cold_start=strict-goal_no_jump=True` | conf | 40,000 | 487.0 | 134.9 | 578.0 | 98.5 | 41.6 | 41.6 | 101.8 | 81.8 | 14.9 | 4.9744 | 11.2 | 64.7 | 0.0000 | 1.7684 | 1.5236 | 0.2561 | 32.2 | 0.1894 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-dreimal_wuerfeln=True` | conf | 40,000 | 436.1 | 120.9 | 569.7 | 87.9 | 46.5 | 46.5 | 37.9 | 27.4 | 18.3 | 0.0000 | 11.2 | 60.9 | 0.0000 | 1.7422 | 1.4569 | 0.2474 | 37.5 | 0.2206 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-dreimal_wuerfeln=True-goal_no_jump=True` | conf | 40,000 | 463.8 | 128.3 | 602.2 | 94.3 | 48.4 | 48.4 | 49.4 | 28.3 | 19.2 | 0.0000 | 11.6 | 65.1 | 0.0000 | 1.7254 | 1.4841 | 0.2418 | 31.2 | 0.1835 |
| `ex4/4s4p/random/barriers=True-bonus_roll_forfeited=True-goal_no_jump=True` | conf | 40,000 | 468.2 | 130.1 | 555.6 | 94.2 | 42.0 | 42.0 | 82.6 | 58.8 | 17.9 | 0.0000 | 11.1 | 64.1 | 0.0000 | 1.7626 | 1.5298 | 0.2542 | 31.6 | 0.1857 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory` | conf | 40,000 | 567.7 | 157.8 | 681.2 | 113.0 | 62.1 | 62.1 | 110.7 | 107.8 | 19.8 | 0.0000 | 11.5 | 62.8 | 0.0000 | 1.7766 | 1.5107 | 0.2589 | 45.8 | 0.2697 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory-cold_start=free_entry` | conf | 40,000 | 1,825 | 492.6 | 2,190 | 379.9 | 497.6 | 497.6 | 11.9 | 65.8 | 77.1 | 0.0000 | 77.2 | 493.3 | 0.0000 | 1.7738 | 1.4727 | 0.2579 | 69.4 | 0.4084 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory-cold_start=free_entry-goal_no_jump=True` | conf | 40,000 | 1,874 | 506.3 | 2,249 | 390.1 | 507.6 | 507.6 | 17.4 | 67.2 | 78.2 | 0.0000 | 78.3 | 501.8 | 0.0000 | 1.7490 | 1.4489 | 0.2497 | 66.7 | 0.3922 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory-cold_start=strict` | conf | 40,000 | 585.6 | 162.4 | 702.7 | 117.1 | 61.6 | 61.6 | 129.3 | 130.4 | 16.9 | 4.9501 | 11.6 | 63.4 | 0.0000 | 1.7937 | 1.5164 | 0.2646 | 46.4 | 0.2729 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True` | conf | 40,000 | 587.0 | 162.0 | 826.3 | 118.8 | 78.2 | 78.2 | 61.0 | 66.6 | 21.5 | 1.3753 | 12.7 | 67.4 | 0.0000 | 1.7392 | 1.4617 | 0.2464 | 45.0 | 0.2646 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | conf | 40,000 | 612.0 | 168.6 | 859.1 | 124.8 | 80.6 | 80.6 | 69.1 | 68.0 | 22.4 | 1.3827 | 13.0 | 70.0 | 0.0000 | 1.7310 | 1.4562 | 0.2437 | 40.4 | 0.2374 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory-cold_start=strict-goal_no_jump=True` | conf | 40,000 | 615.9 | 170.2 | 738.9 | 124.6 | 63.9 | 63.9 | 141.6 | 134.3 | 17.8 | 5.0229 | 11.8 | 66.4 | 0.0000 | 1.7617 | 1.5158 | 0.2539 | 40.3 | 0.2369 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory-dreimal_wuerfeln=True` | conf | 40,000 | 580.6 | 160.4 | 801.0 | 117.3 | 78.1 | 78.1 | 55.3 | 56.9 | 22.7 | 0.0000 | 12.6 | 67.2 | 0.0000 | 1.7393 | 1.4641 | 0.2464 | 44.9 | 0.2640 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory-dreimal_wuerfeln=True-goal_no_jump=True` | conf | 40,000 | 606.2 | 167.2 | 834.6 | 123.2 | 80.6 | 80.6 | 63.5 | 58.5 | 23.5 | 0.0000 | 12.9 | 69.6 | 0.0000 | 1.7156 | 1.4571 | 0.2385 | 40.8 | 0.2398 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory-goal_no_jump=True` | conf | 40,000 | 600.1 | 166.1 | 720.2 | 120.8 | 64.7 | 64.7 | 123.3 | 112.0 | 20.7 | 0.0000 | 11.8 | 66.3 | 0.0000 | 1.7434 | 1.5087 | 0.2478 | 40.2 | 0.2365 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory_extended` | conf | 40,000 | 661.6 | 183.4 | 793.9 | 132.0 | 74.1 | 74.1 | 128.9 | 129.2 | 22.3 | 0.0000 | 13.4 | 72.7 | 2.1817 | 1.7899 | 1.5444 | 0.2633 | 46.0 | 0.2703 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory_extended-cold_start=free_entry` | conf | 40,000 | 2,183 | 587.9 | 2,619 | 456.8 | 596.2 | 596.2 | 12.4 | 80.6 | 90.6 | 0.0000 | 91.9 | 588.2 | 3.6311 | 1.7793 | 1.4873 | 0.2598 | 67.4 | 0.3966 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory_extended-cold_start=free_entry-goal_no_jump=True` | conf | 40,000 | 2,243 | 604.3 | 2,691 | 469.7 | 609.4 | 609.4 | 16.6 | 82.7 | 92.9 | 0.0000 | 93.5 | 598.0 | 3.9418 | 1.7574 | 1.4645 | 0.2525 | 65.1 | 0.3832 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory_extended-cold_start=strict` | conf | 40,000 | 676.7 | 187.2 | 812.0 | 135.8 | 73.2 | 73.2 | 147.4 | 151.5 | 19.3 | 4.9742 | 13.4 | 73.4 | 2.1557 | 1.8021 | 1.5519 | 0.2674 | 46.1 | 0.2712 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True` | conf | 40,000 | 687.8 | 189.6 | 969.4 | 139.3 | 94.0 | 94.0 | 68.6 | 78.6 | 24.7 | 1.3827 | 14.9 | 79.0 | 2.4565 | 1.7721 | 1.4955 | 0.2574 | 45.0 | 0.2647 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | conf | 40,000 | 713.9 | 196.6 | 1,004 | 145.2 | 96.7 | 96.7 | 75.3 | 80.6 | 25.7 | 1.3758 | 15.2 | 81.0 | 2.7020 | 1.7546 | 1.4892 | 0.2515 | 41.5 | 0.2444 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory_extended-cold_start=strict-goal_no_jump=True` | conf | 40,000 | 712.1 | 196.7 | 854.6 | 143.8 | 76.4 | 76.4 | 159.5 | 157.2 | 20.5 | 4.9920 | 13.7 | 76.2 | 2.4874 | 1.7812 | 1.5349 | 0.2604 | 41.7 | 0.2451 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory_extended-dreimal_wuerfeln=True` | conf | 40,000 | 682.3 | 188.3 | 945.2 | 137.8 | 94.0 | 94.0 | 63.0 | 69.0 | 25.8 | 0.0000 | 14.9 | 78.8 | 2.4661 | 1.7589 | 1.4881 | 0.2530 | 45.0 | 0.2646 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory_extended-dreimal_wuerfeln=True-goal_no_jump=True` | conf | 40,000 | 709.9 | 195.6 | 982.5 | 144.2 | 97.0 | 97.0 | 69.8 | 71.2 | 26.9 | 0.0000 | 15.2 | 81.0 | 2.7228 | 1.7483 | 1.4946 | 0.2494 | 41.3 | 0.2429 |
| `ex4/4s4p/random/barriers=True-capture_mode=mandatory_extended-goal_no_jump=True` | conf | 40,000 | 698.4 | 193.1 | 837.9 | 140.7 | 77.4 | 77.4 | 141.2 | 135.3 | 23.6 | 0.0000 | 13.7 | 76.0 | 2.5002 | 1.7779 | 1.5338 | 0.2593 | 41.1 | 0.2418 |
| `ex4/4s4p/random/barriers=True-cold_start=free_entry` | conf | 40,000 | 546.2 | 151.5 | 655.5 | 109.2 | 90.4 | 90.4 | 10.0 | 8.5430 | 23.7 | 0.0000 | 27.1 | 166.9 | 0.0000 | 1.7344 | 1.4022 | 0.2448 | 49.5 | 0.2915 |
| `ex4/4s4p/random/barriers=True-cold_start=free_entry-goal_no_jump=True` | conf | 40,000 | 587.0 | 162.6 | 704.4 | 117.8 | 94.9 | 94.9 | 20.6 | 8.7005 | 24.7 | 0.0000 | 28.2 | 175.8 | 0.0000 | 1.6825 | 1.3944 | 0.2275 | 42.5 | 0.2499 |
| `ex4/4s4p/random/barriers=True-cold_start=strict` | conf | 40,000 | 448.8 | 124.9 | 538.6 | 89.8 | 39.4 | 39.4 | 83.8 | 78.8 | 13.9 | 5.0201 | 10.8 | 59.4 | 0.0000 | 1.7753 | 1.4879 | 0.2584 | 41.2 | 0.2424 |
| `ex4/4s4p/random/barriers=True-cold_start=strict-dreimal_wuerfeln=True` | conf | 40,000 | 436.2 | 120.8 | 590.2 | 88.3 | 46.3 | 46.3 | 40.1 | 36.4 | 17.3 | 1.3774 | 11.3 | 61.2 | 0.0000 | 1.7501 | 1.4452 | 0.2500 | 39.2 | 0.2305 |
| `ex4/4s4p/random/barriers=True-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | conf | 40,000 | 460.5 | 127.2 | 620.6 | 93.9 | 47.9 | 47.9 | 49.8 | 37.1 | 17.9 | 1.3718 | 11.6 | 64.3 | 0.0000 | 1.7220 | 1.4626 | 0.2406 | 33.6 | 0.1979 |
| `ex4/4s4p/random/barriers=True-cold_start=strict-goal_no_jump=True` | conf | 40,000 | 476.9 | 132.2 | 572.3 | 96.4 | 41.2 | 41.2 | 95.8 | 80.2 | 14.7 | 5.0086 | 11.1 | 63.7 | 0.0000 | 1.7633 | 1.5044 | 0.2545 | 34.3 | 0.2020 |
| `ex4/4s4p/random/barriers=True-dreimal_wuerfeln=True` | conf | 40,000 | 429.9 | 119.2 | 564.9 | 86.7 | 46.1 | 46.1 | 34.5 | 26.8 | 18.3 | 0.0000 | 11.3 | 60.6 | 0.0000 | 1.7353 | 1.4347 | 0.2451 | 39.3 | 0.2311 |
| `ex4/4s4p/random/barriers=True-dreimal_wuerfeln=True-goal_no_jump=True` | conf | 40,000 | 454.4 | 125.7 | 595.7 | 92.4 | 47.9 | 47.9 | 44.1 | 27.5 | 19.1 | 0.0000 | 11.6 | 64.0 | 0.0000 | 1.7163 | 1.4685 | 0.2388 | 33.5 | 0.1972 |
| `ex4/4s4p/random/barriers=True-goal_no_jump=True` | conf | 40,000 | 458.7 | 127.5 | 550.4 | 92.1 | 41.5 | 41.5 | 76.8 | 57.4 | 17.7 | 0.0000 | 11.1 | 63.1 | 0.0000 | 1.7513 | 1.4939 | 0.2504 | 33.8 | 0.1989 |
| `ex4/4s4p/random/baseline` | conf | 40,000 | 438.4 | 122.3 | 526.1 | 87.1 | 41.8 | 41.8 | 66.0 | 58.9 | 17.3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7612 | 1.4753 | 0.2537 | 41.4 | 0.2433 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True` | conf | 40,000 | 568.1 | 155.8 | 919.2 | 116.6 | 88.1 | 88.1 | 67.7 | 76.8 | 24.0 | 1.3704 | 0.0000 | 0.0000 | 0.0000 | 1.7798 | 1.5104 | 0.2599 | 40.2 | 0.2366 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | conf | 40,000 | 589.9 | 161.8 | 948.7 | 121.5 | 90.4 | 90.4 | 75.6 | 78.1 | 24.9 | 1.3724 | 0.0000 | 0.0000 | 0.0000 | 1.7532 | 1.5066 | 0.2511 | 36.5 | 0.2146 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory-dreimal_wuerfeln=True` | conf | 40,000 | 564.8 | 155.1 | 894.9 | 115.6 | 88.1 | 88.1 | 62.2 | 67.4 | 25.2 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7732 | 1.5056 | 0.2577 | 40.1 | 0.2357 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory-dreimal_wuerfeln=True-goal_no_jump=True` | conf | 40,000 | 586.4 | 160.8 | 924.2 | 120.6 | 90.3 | 90.3 | 70.2 | 68.7 | 26.2 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7548 | 1.5003 | 0.2516 | 36.4 | 0.2144 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True` | conf | 40,000 | 663.1 | 181.7 | 1,075 | 136.0 | 105.3 | 105.3 | 75.7 | 90.5 | 27.6 | 1.3669 | 0.0000 | 0.0000 | 2.5143 | 1.7985 | 1.5427 | 0.2662 | 40.4 | 0.2375 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | conf | 40,000 | 688.0 | 188.5 | 1,111 | 141.5 | 108.2 | 108.2 | 82.7 | 92.8 | 28.7 | 1.3728 | 0.0000 | 0.0000 | 2.7306 | 1.7790 | 1.5345 | 0.2597 | 37.7 | 0.2218 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-dreimal_wuerfeln=True` | conf | 40,000 | 659.3 | 180.7 | 1,050 | 135.1 | 105.0 | 105.0 | 70.4 | 81.1 | 28.8 | 0.0000 | 0.0000 | 0.0000 | 2.5067 | 1.7958 | 1.5486 | 0.2653 | 40.3 | 0.2368 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-capture_mode=mandatory_extended-dreimal_wuerfeln=True-goal_no_jump=True` | conf | 40,000 | 683.7 | 187.3 | 1,085 | 140.5 | 107.9 | 107.9 | 77.2 | 83.3 | 29.9 | 0.0000 | 0.0000 | 0.0000 | 2.7347 | 1.7743 | 1.5284 | 0.2581 | 37.6 | 0.2214 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-cold_start=strict-dreimal_wuerfeln=True` | conf | 40,000 | 409.5 | 113.0 | 626.4 | 83.5 | 49.8 | 49.8 | 43.8 | 40.3 | 18.2 | 1.3613 | 0.0000 | 0.0000 | 0.0000 | 1.7764 | 1.4894 | 0.2588 | 34.4 | 0.2021 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | conf | 40,000 | 432.5 | 119.2 | 655.3 | 88.7 | 51.4 | 51.4 | 53.7 | 41.0 | 19.0 | 1.3682 | 0.0000 | 0.0000 | 0.0000 | 1.7644 | 1.5172 | 0.2548 | 29.1 | 0.1710 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-dreimal_wuerfeln=True` | conf | 40,000 | 405.5 | 112.0 | 600.9 | 82.5 | 49.6 | 49.6 | 38.3 | 30.7 | 19.4 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7634 | 1.4856 | 0.2545 | 34.2 | 0.2013 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-bonus_roll_forfeited=True-dreimal_wuerfeln=True-goal_no_jump=True` | conf | 40,000 | 428.8 | 118.3 | 630.5 | 87.6 | 51.4 | 51.4 | 48.0 | 31.4 | 20.2 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7526 | 1.5158 | 0.2509 | 29.4 | 0.1729 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True` | conf | 40,000 | 560.8 | 154.0 | 911.5 | 114.8 | 87.6 | 87.6 | 64.3 | 75.8 | 23.9 | 1.3778 | 0.0000 | 0.0000 | 0.0000 | 1.7575 | 1.4909 | 0.2525 | 42.4 | 0.2492 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | conf | 40,000 | 581.8 | 159.6 | 941.6 | 119.7 | 89.8 | 89.8 | 71.4 | 77.2 | 24.8 | 1.3884 | 0.0000 | 0.0000 | 0.0000 | 1.7496 | 1.4923 | 0.2499 | 38.2 | 0.2248 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-capture_mode=mandatory-dreimal_wuerfeln=True` | conf | 40,000 | 556.5 | 152.9 | 885.6 | 113.7 | 87.4 | 87.4 | 58.7 | 66.2 | 24.9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7644 | 1.4891 | 0.2548 | 42.5 | 0.2498 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-capture_mode=mandatory-dreimal_wuerfeln=True-goal_no_jump=True` | conf | 40,000 | 577.6 | 158.4 | 916.1 | 118.7 | 89.7 | 89.7 | 65.8 | 67.7 | 25.9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7421 | 1.4870 | 0.2474 | 38.5 | 0.2263 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True` | conf | 40,000 | 655.9 | 179.9 | 1,067 | 134.3 | 104.8 | 104.8 | 72.3 | 89.4 | 27.5 | 1.3604 | 0.0000 | 0.0000 | 2.4897 | 1.7930 | 1.5336 | 0.2643 | 42.2 | 0.2480 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | conf | 40,000 | 679.5 | 186.3 | 1,102 | 139.4 | 107.5 | 107.5 | 78.5 | 91.6 | 28.4 | 1.3822 | 0.0000 | 0.0000 | 2.7495 | 1.7739 | 1.5216 | 0.2580 | 39.6 | 0.2327 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-capture_mode=mandatory_extended-dreimal_wuerfeln=True` | conf | 40,000 | 651.9 | 178.8 | 1,042 | 133.3 | 104.7 | 104.7 | 67.0 | 80.1 | 28.7 | 0.0000 | 0.0000 | 0.0000 | 2.4866 | 1.7922 | 1.5280 | 0.2641 | 42.2 | 0.2480 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-capture_mode=mandatory_extended-dreimal_wuerfeln=True-goal_no_jump=True` | conf | 40,000 | 675.7 | 185.3 | 1,078 | 138.7 | 107.5 | 107.5 | 73.2 | 82.3 | 29.7 | 0.0000 | 0.0000 | 0.0000 | 2.7231 | 1.7677 | 1.5210 | 0.2559 | 39.4 | 0.2317 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-cold_start=strict-dreimal_wuerfeln=True` | conf | 40,000 | 403.0 | 111.3 | 620.6 | 82.1 | 49.4 | 49.4 | 40.5 | 39.6 | 18.0 | 1.3800 | 0.0000 | 0.0000 | 0.0000 | 1.7634 | 1.4707 | 0.2545 | 36.3 | 0.2138 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | conf | 40,000 | 424.5 | 117.0 | 649.5 | 87.0 | 51.0 | 51.0 | 49.0 | 40.3 | 18.8 | 1.3808 | 0.0000 | 0.0000 | 0.0000 | 1.7427 | 1.4920 | 0.2476 | 31.3 | 0.1841 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-dreimal_wuerfeln=True` | conf | 40,000 | 399.3 | 110.3 | 595.5 | 81.2 | 49.3 | 49.3 | 35.0 | 30.1 | 19.3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7534 | 1.4730 | 0.2511 | 36.2 | 0.2127 |
| `ex4/4s4p/random/bonus_roll_after_quick_entry=True-dreimal_wuerfeln=True-goal_no_jump=True` | conf | 40,000 | 420.1 | 115.9 | 623.3 | 85.9 | 50.8 | 50.8 | 43.5 | 30.7 | 20.0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7367 | 1.4880 | 0.2456 | 31.0 | 0.1821 |
| `ex4/4s4p/random/bonus_roll_forfeited=True` | conf | 40,000 | 445.6 | 124.2 | 530.9 | 88.7 | 42.0 | 42.0 | 70.2 | 60.3 | 17.4 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7669 | 1.4953 | 0.2556 | 39.2 | 0.2304 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory` | conf | 40,000 | 580.0 | 161.2 | 692.2 | 115.5 | 63.7 | 63.7 | 116.1 | 112.8 | 20.1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7756 | 1.5223 | 0.2585 | 44.3 | 0.2607 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=free_entry` | conf | 40,000 | 1,852 | 501.8 | 2,219 | 381.9 | 513.0 | 513.0 | 10.5 | 73.4 | 77.4 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7450 | 1.4570 | 0.2483 | 69.8 | 0.4108 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=free_entry-goal_no_jump=True` | conf | 40,000 | 1,910 | 517.7 | 2,286 | 393.7 | 525.8 | 525.8 | 16.5 | 75.1 | 79.2 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7300 | 1.4351 | 0.2433 | 67.2 | 0.3955 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=strict` | conf | 40,000 | 596.0 | 165.1 | 711.5 | 119.5 | 62.9 | 62.9 | 134.6 | 135.1 | 17.2 | 4.9709 | 0.0000 | 0.0000 | 0.0000 | 1.7996 | 1.5355 | 0.2666 | 44.2 | 0.2602 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True` | conf | 40,000 | 596.2 | 164.5 | 838.5 | 120.7 | 80.1 | 80.1 | 63.4 | 69.1 | 22.0 | 1.3668 | 0.0000 | 0.0000 | 0.0000 | 1.7385 | 1.4718 | 0.2462 | 43.4 | 0.2553 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | conf | 40,000 | 621.3 | 171.2 | 869.9 | 126.6 | 82.4 | 82.4 | 72.0 | 70.6 | 22.9 | 1.3626 | 0.0000 | 0.0000 | 0.0000 | 1.7345 | 1.4702 | 0.2448 | 39.0 | 0.2292 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory-cold_start=strict-goal_no_jump=True` | conf | 40,000 | 628.2 | 173.5 | 748.4 | 127.2 | 65.5 | 65.5 | 147.6 | 139.2 | 18.3 | 5.0014 | 0.0000 | 0.0000 | 0.0000 | 1.7665 | 1.5228 | 0.2555 | 38.6 | 0.2272 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory-dreimal_wuerfeln=True` | conf | 40,000 | 590.4 | 163.0 | 813.8 | 119.5 | 80.0 | 80.0 | 57.9 | 59.5 | 23.2 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7473 | 1.4735 | 0.2491 | 43.0 | 0.2532 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory-dreimal_wuerfeln=True-goal_no_jump=True` | conf | 40,000 | 615.9 | 169.8 | 846.3 | 125.2 | 82.5 | 82.5 | 66.4 | 61.1 | 23.9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7177 | 1.4651 | 0.2392 | 39.1 | 0.2299 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory-goal_no_jump=True` | conf | 40,000 | 609.8 | 168.9 | 726.3 | 122.7 | 66.0 | 66.0 | 128.3 | 116.3 | 21.1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7500 | 1.5178 | 0.2500 | 38.8 | 0.2279 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory_extended` | conf | 40,000 | 670.4 | 185.9 | 800.7 | 133.8 | 75.2 | 75.2 | 134.1 | 134.1 | 22.5 | 0.0000 | 0.0000 | 0.0000 | 2.1633 | 1.8006 | 1.5499 | 0.2669 | 44.3 | 0.2606 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=free_entry` | conf | 40,000 | 2,199 | 594.2 | 2,636 | 456.4 | 610.0 | 610.0 | 10.1 | 89.1 | 90.7 | 0.0000 | 0.0000 | 0.0000 | 3.5956 | 1.7629 | 1.4814 | 0.2543 | 67.7 | 0.3981 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=free_entry-goal_no_jump=True` | conf | 40,000 | 2,271 | 614.0 | 2,721 | 471.5 | 627.2 | 627.2 | 14.7 | 91.6 | 93.2 | 0.0000 | 0.0000 | 0.0000 | 3.9263 | 1.7460 | 1.4569 | 0.2487 | 65.6 | 0.3861 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=strict` | conf | 40,000 | 687.3 | 190.1 | 821.1 | 138.0 | 74.7 | 74.7 | 152.6 | 156.4 | 19.6 | 5.0098 | 0.0000 | 0.0000 | 2.1540 | 1.8192 | 1.5555 | 0.2731 | 44.5 | 0.2619 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True` | conf | 40,000 | 695.1 | 191.6 | 979.2 | 140.8 | 95.8 | 95.8 | 70.4 | 81.1 | 25.2 | 1.3740 | 0.0000 | 0.0000 | 2.4242 | 1.7670 | 1.5041 | 0.2557 | 43.4 | 0.2555 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | conf | 40,000 | 720.9 | 198.6 | 1,013 | 146.4 | 98.2 | 98.2 | 77.8 | 83.2 | 26.1 | 1.3630 | 0.0000 | 0.0000 | 2.6830 | 1.7479 | 1.5012 | 0.2493 | 40.1 | 0.2361 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory_extended-cold_start=strict-goal_no_jump=True` | conf | 40,000 | 722.4 | 199.3 | 861.8 | 146.3 | 77.7 | 77.7 | 165.3 | 162.4 | 20.8 | 5.0209 | 0.0000 | 0.0000 | 2.4625 | 1.7870 | 1.5461 | 0.2623 | 39.9 | 0.2348 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory_extended-dreimal_wuerfeln=True` | conf | 40,000 | 691.2 | 190.6 | 957.7 | 139.8 | 96.0 | 96.0 | 65.2 | 71.9 | 26.3 | 0.0000 | 0.0000 | 0.0000 | 2.4500 | 1.7637 | 1.5067 | 0.2546 | 43.4 | 0.2553 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory_extended-dreimal_wuerfeln=True-goal_no_jump=True` | conf | 40,000 | 718.2 | 197.9 | 993.1 | 145.6 | 98.8 | 98.8 | 72.5 | 74.1 | 27.2 | 0.0000 | 0.0000 | 0.0000 | 2.6963 | 1.7414 | 1.4913 | 0.2471 | 40.6 | 0.2386 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-capture_mode=mandatory_extended-goal_no_jump=True` | conf | 40,000 | 705.1 | 195.0 | 841.2 | 141.9 | 78.4 | 78.4 | 145.8 | 139.2 | 23.7 | 0.0000 | 0.0000 | 0.0000 | 2.4689 | 1.7692 | 1.5377 | 0.2564 | 40.1 | 0.2359 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-cold_start=free_entry` | conf | 40,000 | 596.9 | 165.5 | 712.5 | 119.1 | 105.7 | 105.7 | 11.3 | 9.4905 | 25.6 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7194 | 1.3913 | 0.2398 | 51.3 | 0.3020 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-cold_start=free_entry-goal_no_jump=True` | conf | 40,000 | 641.9 | 177.8 | 763.4 | 128.6 | 111.1 | 111.1 | 23.0 | 9.7725 | 26.9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.6859 | 1.3948 | 0.2286 | 43.7 | 0.2568 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-cold_start=strict` | conf | 40,000 | 463.3 | 128.8 | 552.2 | 92.8 | 41.5 | 41.5 | 89.1 | 83.1 | 14.4 | 5.0163 | 0.0000 | 0.0000 | 0.0000 | 1.7901 | 1.4999 | 0.2634 | 40.0 | 0.2350 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-cold_start=strict-dreimal_wuerfeln=True` | conf | 40,000 | 448.9 | 124.3 | 605.6 | 90.8 | 48.8 | 48.8 | 42.9 | 38.5 | 17.7 | 1.3804 | 0.0000 | 0.0000 | 0.0000 | 1.7358 | 1.4518 | 0.2453 | 38.1 | 0.2238 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | conf | 40,000 | 475.2 | 131.2 | 637.2 | 96.9 | 50.7 | 50.7 | 53.2 | 39.5 | 18.5 | 1.3714 | 0.0000 | 0.0000 | 0.0000 | 1.7278 | 1.4827 | 0.2426 | 32.3 | 0.1902 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-cold_start=strict-goal_no_jump=True` | conf | 40,000 | 492.4 | 136.4 | 585.0 | 99.6 | 43.4 | 43.4 | 101.9 | 85.1 | 15.2 | 4.9823 | 0.0000 | 0.0000 | 0.0000 | 1.7564 | 1.5175 | 0.2521 | 33.3 | 0.1956 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-dreimal_wuerfeln=True` | conf | 40,000 | 443.4 | 122.9 | 581.9 | 89.5 | 48.8 | 48.8 | 37.5 | 29.2 | 18.9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7281 | 1.4556 | 0.2427 | 37.8 | 0.2224 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-dreimal_wuerfeln=True-goal_no_jump=True` | conf | 40,000 | 468.4 | 129.6 | 611.2 | 95.2 | 50.5 | 50.5 | 47.8 | 29.8 | 19.6 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7202 | 1.4772 | 0.2401 | 32.3 | 0.1903 |
| `ex4/4s4p/random/bonus_roll_forfeited=True-goal_no_jump=True` | conf | 40,000 | 474.3 | 131.8 | 563.2 | 95.4 | 43.8 | 43.8 | 83.1 | 62.3 | 18.3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7469 | 1.5225 | 0.2490 | 32.4 | 0.1907 |
| `ex4/4s4p/random/capture_mode=mandatory` | conf | 40,000 | 570.2 | 158.5 | 684.2 | 113.5 | 63.0 | 63.0 | 111.3 | 110.5 | 19.9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7754 | 1.5097 | 0.2585 | 46.0 | 0.2707 |
| `ex4/4s4p/random/capture_mode=mandatory-cold_start=free_entry` | conf | 40,000 | 1,834 | 497.5 | 2,200 | 376.8 | 509.1 | 509.1 | 7.8275 | 72.0 | 76.7 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7424 | 1.4426 | 0.2475 | 71.7 | 0.4215 |
| `ex4/4s4p/random/capture_mode=mandatory-cold_start=free_entry-goal_no_jump=True` | conf | 40,000 | 1,895 | 513.9 | 2,274 | 390.4 | 523.7 | 523.7 | 12.8 | 73.9 | 79.3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7271 | 1.4317 | 0.2424 | 69.3 | 0.4078 |
| `ex4/4s4p/random/capture_mode=mandatory-cold_start=strict` | conf | 40,000 | 587.6 | 162.9 | 705.2 | 117.6 | 62.5 | 62.5 | 129.9 | 132.9 | 17.0 | 5.0202 | 0.0000 | 0.0000 | 0.0000 | 1.7822 | 1.5182 | 0.2607 | 46.6 | 0.2740 |
| `ex4/4s4p/random/capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True` | conf | 40,000 | 588.3 | 162.4 | 830.9 | 119.0 | 79.5 | 79.5 | 60.0 | 68.1 | 21.8 | 1.3674 | 0.0000 | 0.0000 | 0.0000 | 1.7372 | 1.4629 | 0.2457 | 45.1 | 0.2650 |
| `ex4/4s4p/random/capture_mode=mandatory-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | conf | 40,000 | 611.6 | 168.7 | 861.0 | 124.2 | 81.6 | 81.6 | 67.5 | 69.4 | 22.5 | 1.3721 | 0.0000 | 0.0000 | 0.0000 | 1.7207 | 1.4521 | 0.2402 | 41.3 | 0.2429 |
| `ex4/4s4p/random/capture_mode=mandatory-cold_start=strict-goal_no_jump=True` | conf | 40,000 | 616.6 | 170.5 | 739.9 | 124.4 | 64.8 | 64.8 | 141.3 | 136.5 | 17.9 | 4.9714 | 0.0000 | 0.0000 | 0.0000 | 1.7534 | 1.5042 | 0.2511 | 41.2 | 0.2424 |
| `ex4/4s4p/random/capture_mode=mandatory-dreimal_wuerfeln=True` | conf | 40,000 | 582.5 | 160.9 | 806.3 | 117.7 | 79.4 | 79.4 | 54.4 | 58.6 | 22.9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7347 | 1.4655 | 0.2449 | 45.2 | 0.2657 |
| `ex4/4s4p/random/capture_mode=mandatory-dreimal_wuerfeln=True-goal_no_jump=True` | conf | 40,000 | 606.1 | 167.2 | 837.1 | 122.9 | 81.7 | 81.7 | 62.0 | 59.9 | 23.6 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7076 | 1.4576 | 0.2359 | 41.1 | 0.2420 |
| `ex4/4s4p/random/capture_mode=mandatory-goal_no_jump=True` | conf | 40,000 | 600.2 | 166.2 | 720.2 | 120.7 | 65.5 | 65.5 | 122.7 | 114.2 | 20.9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7424 | 1.5042 | 0.2475 | 40.6 | 0.2387 |
| `ex4/4s4p/random/capture_mode=mandatory_extended` | conf | 40,000 | 662.1 | 183.6 | 794.6 | 132.1 | 74.9 | 74.9 | 129.3 | 131.9 | 22.5 | 0.0000 | 0.0000 | 0.0000 | 2.1506 | 1.7966 | 1.5365 | 0.2655 | 46.2 | 0.2721 |
| `ex4/4s4p/random/capture_mode=mandatory_extended-cold_start=free_entry` | conf | 40,000 | 2,185 | 591.3 | 2,622 | 451.9 | 607.6 | 607.6 | 7.5572 | 87.7 | 90.5 | 0.0000 | 0.0000 | 0.0000 | 3.5806 | 1.7568 | 1.4691 | 0.2523 | 69.8 | 0.4109 |
| `ex4/4s4p/random/capture_mode=mandatory_extended-cold_start=free_entry-goal_no_jump=True` | conf | 40,000 | 2,251 | 608.9 | 2,701 | 466.3 | 623.2 | 623.2 | 11.2 | 90.2 | 92.8 | 0.0000 | 0.0000 | 0.0000 | 3.8964 | 1.7380 | 1.4490 | 0.2460 | 67.5 | 0.3970 |
| `ex4/4s4p/random/capture_mode=mandatory_extended-cold_start=strict` | conf | 40,000 | 677.2 | 187.4 | 812.6 | 135.9 | 74.0 | 74.0 | 147.8 | 154.1 | 19.5 | 5.0139 | 0.0000 | 0.0000 | 2.1347 | 1.8025 | 1.5401 | 0.2675 | 46.1 | 0.2714 |
| `ex4/4s4p/random/capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True` | conf | 40,000 | 686.8 | 189.4 | 971.0 | 138.9 | 95.1 | 95.1 | 67.1 | 80.0 | 24.9 | 1.3730 | 0.0000 | 0.0000 | 2.4339 | 1.7698 | 1.4973 | 0.2566 | 45.2 | 0.2661 |
| `ex4/4s4p/random/capture_mode=mandatory_extended-cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | conf | 40,000 | 712.5 | 196.3 | 1,005 | 144.7 | 97.8 | 97.8 | 73.5 | 82.1 | 25.9 | 1.3510 | 0.0000 | 0.0000 | 2.6824 | 1.7427 | 1.4867 | 0.2476 | 42.0 | 0.2470 |
| `ex4/4s4p/random/capture_mode=mandatory_extended-cold_start=strict-goal_no_jump=True` | conf | 40,000 | 711.4 | 196.4 | 853.6 | 143.7 | 77.0 | 77.0 | 159.2 | 159.7 | 20.6 | 5.0251 | 0.0000 | 0.0000 | 2.4616 | 1.7730 | 1.5294 | 0.2577 | 42.1 | 0.2477 |
| `ex4/4s4p/random/capture_mode=mandatory_extended-dreimal_wuerfeln=True` | conf | 40,000 | 681.0 | 187.9 | 946.6 | 137.5 | 95.0 | 95.0 | 61.7 | 70.6 | 25.9 | 0.0000 | 0.0000 | 0.0000 | 2.4310 | 1.7635 | 1.4941 | 0.2545 | 45.3 | 0.2664 |
| `ex4/4s4p/random/capture_mode=mandatory_extended-dreimal_wuerfeln=True-goal_no_jump=True` | conf | 40,000 | 706.7 | 194.9 | 981.1 | 143.2 | 97.7 | 97.7 | 68.2 | 72.6 | 26.8 | 0.0000 | 0.0000 | 0.0000 | 2.6902 | 1.7308 | 1.4756 | 0.2436 | 42.0 | 0.2472 |
| `ex4/4s4p/random/capture_mode=mandatory_extended-goal_no_jump=True` | conf | 40,000 | 695.5 | 192.5 | 834.6 | 139.8 | 77.8 | 77.8 | 140.8 | 137.5 | 23.5 | 0.0000 | 0.0000 | 0.0000 | 2.4465 | 1.7639 | 1.5275 | 0.2546 | 41.7 | 0.2455 |
| `ex4/4s4p/random/cold_start=free_entry` | conf | 40,000 | 588.2 | 163.2 | 705.9 | 117.2 | 104.8 | 104.8 | 8.4091 | 9.2067 | 25.4 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7052 | 1.3827 | 0.2351 | 53.7 | 0.3159 |
| `ex4/4s4p/random/cold_start=free_entry-goal_no_jump=True` | conf | 40,000 | 629.5 | 174.4 | 755.3 | 126.1 | 109.9 | 109.9 | 18.0 | 9.4763 | 26.6 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.6758 | 1.3837 | 0.2253 | 46.1 | 0.2711 |
| `ex4/4s4p/random/cold_start=strict` | conf | 40,000 | 455.3 | 126.6 | 546.4 | 91.1 | 41.1 | 41.1 | 84.8 | 81.5 | 14.2 | 4.9446 | 0.0000 | 0.0000 | 0.0000 | 1.7771 | 1.4834 | 0.2590 | 42.0 | 0.2470 |
| `ex4/4s4p/random/cold_start=strict-dreimal_wuerfeln=True` | conf | 40,000 | 443.9 | 122.9 | 602.7 | 89.9 | 48.7 | 48.7 | 39.7 | 38.2 | 17.7 | 1.3763 | 0.0000 | 0.0000 | 0.0000 | 1.7336 | 1.4410 | 0.2445 | 39.9 | 0.2345 |
| `ex4/4s4p/random/cold_start=strict-dreimal_wuerfeln=True-goal_no_jump=True` | conf | 40,000 | 466.4 | 128.9 | 630.8 | 94.9 | 50.2 | 50.2 | 48.7 | 38.8 | 18.3 | 1.3812 | 0.0000 | 0.0000 | 0.0000 | 1.7207 | 1.4598 | 0.2402 | 34.6 | 0.2038 |
| `ex4/4s4p/random/cold_start=strict-goal_no_jump=True` | conf | 40,000 | 483.7 | 134.0 | 580.5 | 97.8 | 43.0 | 43.0 | 96.3 | 83.5 | 15.1 | 4.9817 | 0.0000 | 0.0000 | 0.0000 | 1.7488 | 1.5054 | 0.2496 | 35.1 | 0.2065 |
| `ex4/4s4p/random/dreimal_wuerfeln=True` | conf | 40,000 | 437.2 | 121.2 | 577.1 | 88.2 | 48.5 | 48.5 | 34.2 | 28.6 | 18.8 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7231 | 1.4394 | 0.2410 | 39.8 | 0.2339 |
| `ex4/4s4p/random/dreimal_wuerfeln=True-goal_no_jump=True` | conf | 40,000 | 460.8 | 127.5 | 606.8 | 93.6 | 50.2 | 50.2 | 43.2 | 29.4 | 19.4 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7136 | 1.4566 | 0.2379 | 34.5 | 0.2029 |
| `ex4/4s4p/random/goal_no_jump=True` | conf | 40,000 | 464.9 | 129.2 | 557.8 | 93.5 | 43.4 | 43.4 | 77.4 | 60.9 | 18.0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7475 | 1.5024 | 0.2492 | 34.6 | 0.2037 |
| `ex5/2p/adjacent/random` | desc | 20,000 | 117.8 | 59.2 | 141.3 | 59.2 | 5.7271 | 5.7271 | 9.1720 | 5.6891 | 7.0004 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3067 | 1.2151 | 0.3066 | 42.2 | 0.2483 |
| `ex5/2p/adjacent/spread` | desc | 20,000 | 120.5 | 60.5 | 144.7 | 60.5 | 5.2873 | 5.2873 | 8.9161 | 5.2355 | 6.8756 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.2958 | 1.1934 | 0.2958 | 39.3 | 0.2312 |
| `ex5/2p/opposite/random` | desc | 20,000 | 117.9 | 59.2 | 141.4 | 59.2 | 5.4704 | 5.4704 | 8.5113 | 4.8889 | 7.3055 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3197 | 1.2204 | 0.3197 | 40.2 | 0.2364 |
| `ex5/2p/opposite/spread` | desc | 20,000 | 119.1 | 59.8 | 142.9 | 59.8 | 4.3985 | 4.3985 | 7.6275 | 4.0176 | 8.0255 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3621 | 1.2504 | 0.3621 | 29.2 | 0.1717 |
| `ex5/3p/4s-adjacent/random` | conf | 250,002 | 250.2 | 89.1 | 300.2 | 72.4 | 19.1 | 19.1 | 28.9 | 22.5 | 12.4 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5612 | 1.3637 | 0.2806 | 40.0 | 0.2355 |
| `ex5/3p/4s-adjacent/spread` | conf | 250,002 | 316.0 | 113.2 | 379.2 | 90.1 | 26.3 | 26.3 | 33.2 | 25.5 | 14.8 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.6691 | 1.3729 | 0.3345 | 50.2 | 0.2950 |
| `ex5/3p/6s-adjacent/random` | conf | 250,002 | 289.9 | 103.1 | 347.9 | 84.1 | 21.5 | 21.5 | 26.1 | 20.2 | 12.9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5534 | 1.3442 | 0.2767 | 48.5 | 0.2399 |
| `ex5/3p/6s-adjacent/spread` | conf | 250,002 | 349.1 | 125.2 | 418.9 | 99.1 | 26.6 | 26.6 | 27.9 | 21.1 | 13.6 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.6563 | 1.3477 | 0.3281 | 60.9 | 0.3014 |
| `ex5/3p/6s-spread/random` | conf | 250,002 | 296.3 | 105.3 | 355.6 | 86.1 | 21.5 | 21.5 | 23.8 | 17.7 | 13.7 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5555 | 1.3475 | 0.2778 | 48.5 | 0.2399 |
| `ex5/3p/6s-spread/spread` | conf | 250,002 | 375.2 | 134.1 | 450.2 | 107.6 | 28.3 | 28.3 | 26.2 | 19.0 | 17.1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.6995 | 1.3810 | 0.3498 | 59.2 | 0.2932 |
| `ex6a/4s4p/focus_front/mandatory` | desc | 20,000 | 411.4 | 114.8 | 493.7 | 81.6 | 39.0 | 39.0 | 78.5 | 70.7 | 14.8 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7524 | 1.5076 | 0.2508 | 38.4 | 0.2260 |
| `ex6a/4s4p/focus_front/mandatory_extended` | desc | 20,000 | 448.6 | 125.2 | 538.4 | 89.0 | 43.4 | 43.4 | 86.1 | 79.3 | 15.8 | 0.0000 | 0.0000 | 0.0000 | 1.1036 | 1.7865 | 1.5560 | 0.2621 | 38.7 | 0.2274 |
| `ex6a/4s4p/focus_front/optional` | desc | 20,000 | 315.3 | 88.5 | 378.2 | 62.4 | 24.3 | 24.3 | 51.5 | 41.4 | 13.2 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7386 | 1.4848 | 0.2462 | 32.1 | 0.1886 |
| `ex6a/4s4p/focus_rear/mandatory` | desc | 20,000 | 726.5 | 202.2 | 871.7 | 143.1 | 84.7 | 84.7 | 136.8 | 134.1 | 24.9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.8187 | 1.5394 | 0.2729 | 53.2 | 0.3130 |
| `ex6a/4s4p/focus_rear/mandatory_extended` | desc | 20,000 | 884.9 | 245.3 | 1,062 | 175.5 | 105.9 | 105.9 | 165.9 | 167.7 | 29.3 | 0.0000 | 0.0000 | 0.0000 | 3.0115 | 1.8383 | 1.5662 | 0.2794 | 52.9 | 0.3110 |
| `ex6a/4s4p/focus_rear/optional` | desc | 20,000 | 589.6 | 164.5 | 707.6 | 116.2 | 61.6 | 61.6 | 83.0 | 73.5 | 22.3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.8441 | 1.5131 | 0.2814 | 49.8 | 0.2930 |
| `ex6a/4s4p/greedy_capture/mandatory` | desc | 20,000 | 571.4 | 158.8 | 685.7 | 113.8 | 63.2 | 63.2 | 111.3 | 110.7 | 19.9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7771 | 1.5075 | 0.2590 | 45.9 | 0.2701 |
| `ex6a/4s4p/greedy_capture/mandatory_extended` | desc | 20,000 | 660.5 | 183.1 | 792.4 | 132.0 | 74.6 | 74.6 | 128.9 | 131.4 | 22.5 | 0.0000 | 0.0000 | 0.0000 | 2.1321 | 1.8061 | 1.5562 | 0.2687 | 45.8 | 0.2696 |
| `ex6a/4s4p/greedy_capture/optional` | desc | 20,000 | 569.0 | 158.1 | 682.7 | 113.4 | 62.8 | 62.8 | 111.4 | 110.6 | 20.0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7698 | 1.5083 | 0.2566 | 45.6 | 0.2684 |
| `ex6a/4s4p/random/mandatory` | desc | 20,000 | 570.5 | 158.6 | 684.6 | 113.3 | 63.0 | 63.0 | 111.3 | 110.7 | 20.0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7769 | 1.5107 | 0.2589 | 46.7 | 0.2747 |
| `ex6a/4s4p/random/mandatory_extended` | desc | 20,000 | 662.1 | 183.6 | 794.5 | 132.0 | 75.0 | 75.0 | 128.9 | 131.5 | 22.4 | 0.0000 | 0.0000 | 0.0000 | 2.1679 | 1.7915 | 1.5377 | 0.2638 | 46.4 | 0.2728 |
| `ex6a/4s4p/random/optional` | desc | 20,000 | 437.2 | 122.0 | 524.7 | 86.9 | 41.6 | 41.6 | 65.8 | 58.7 | 17.3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7571 | 1.4788 | 0.2523 | 41.2 | 0.2422 |
| `ex6a/4s4p/spread/mandatory` | desc | 20,000 | 769.8 | 214.8 | 923.8 | 150.7 | 90.8 | 90.8 | 144.1 | 142.6 | 26.1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.8184 | 1.5103 | 0.2728 | 55.2 | 0.3249 |
| `ex6a/4s4p/spread/mandatory_extended` | desc | 20,000 | 937.5 | 260.8 | 1,125 | 184.2 | 113.1 | 113.1 | 174.8 | 178.1 | 30.5 | 0.0000 | 0.0000 | 0.0000 | 3.0574 | 1.8545 | 1.5550 | 0.2848 | 55.5 | 0.3268 |
| `ex6a/4s4p/spread/optional` | desc | 20,000 | 620.3 | 173.5 | 744.5 | 121.2 | 65.5 | 65.5 | 85.1 | 76.1 | 23.2 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.8783 | 1.5016 | 0.2928 | 52.9 | 0.3111 |
| `ex6b/4s4p/focus_front-vs-random/mandatory` | conf | 400,000 | 527.8 | 148.0 | 633.4 | 102.7 | 56.7 | 56.7 | 102.8 | 100.0 | 17.7 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7308 | 1.4691 | 0.2436 | 47.0 | 0.2767 |
| `ex6b/4s4p/focus_front-vs-random/mandatory_extended` | conf | 400,000 | 603.8 | 169.0 | 724.6 | 117.6 | 66.3 | 66.3 | 117.8 | 117.6 | 19.7 | 0.0000 | 0.0000 | 0.0000 | 1.9323 | 1.7488 | 1.4976 | 0.2496 | 46.8 | 0.2751 |
| `ex6b/4s4p/focus_front-vs-random/optional` | conf | 400,000 | 402.6 | 113.5 | 483.1 | 77.9 | 36.7 | 36.7 | 61.7 | 53.7 | 15.1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7004 | 1.4270 | 0.2335 | 42.4 | 0.2495 |
| `ex6b/4s4p/focus_rear-vs-random/mandatory` | desc | 20,000 | 603.3 | 168.5 | 724.0 | 118.6 | 67.8 | 67.8 | 116.6 | 115.5 | 20.6 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7667 | 1.4999 | 0.2556 | 48.5 | 0.2856 |
| `ex6b/4s4p/focus_rear-vs-random/mandatory_extended` | desc | 20,000 | 708.6 | 197.5 | 850.3 | 139.6 | 81.4 | 81.4 | 137.2 | 139.7 | 23.4 | 0.0000 | 0.0000 | 0.0000 | 2.4094 | 1.7788 | 1.5192 | 0.2596 | 48.3 | 0.2842 |
| `ex6b/4s4p/focus_rear-vs-random/optional` | desc | 20,000 | 467.9 | 131.1 | 561.4 | 92.1 | 45.7 | 45.7 | 69.3 | 61.8 | 18.1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7676 | 1.4707 | 0.2559 | 43.9 | 0.2580 |
| `ex6b/4s4p/greedy_capture-vs-random/mandatory` | desc | 20,000 | 570.7 | 158.7 | 684.7 | 113.5 | 63.1 | 63.1 | 111.3 | 110.5 | 19.9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7730 | 1.5041 | 0.2576 | 46.3 | 0.2723 |
| `ex6b/4s4p/greedy_capture-vs-random/mandatory_extended` | desc | 20,000 | 658.0 | 182.6 | 789.5 | 131.2 | 74.2 | 74.2 | 128.7 | 131.1 | 22.3 | 0.0000 | 0.0000 | 0.0000 | 2.1189 | 1.7872 | 1.5375 | 0.2624 | 45.8 | 0.2692 |
| `ex6b/4s4p/greedy_capture-vs-random/optional` | desc | 20,000 | 473.4 | 131.8 | 568.1 | 94.4 | 47.6 | 47.6 | 77.6 | 72.1 | 17.8 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7556 | 1.4878 | 0.2519 | 42.8 | 0.2516 |
| `ex6b/4s4p/spread-vs-random/mandatory` | conf | 400,000 | 610.2 | 170.9 | 732.2 | 119.3 | 68.8 | 68.8 | 117.8 | 117.1 | 20.7 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7615 | 1.4822 | 0.2538 | 49.3 | 0.2897 |
| `ex6b/4s4p/spread-vs-random/mandatory_extended` | conf | 400,000 | 718.4 | 200.9 | 862.0 | 140.6 | 82.9 | 82.9 | 138.7 | 141.8 | 23.4 | 0.0000 | 0.0000 | 0.0000 | 2.4553 | 1.7767 | 1.5108 | 0.2589 | 49.2 | 0.2894 |
| `ex6b/4s4p/spread-vs-random/optional` | conf | 400,000 | 471.0 | 132.2 | 565.2 | 92.2 | 46.1 | 46.1 | 69.2 | 61.9 | 18.0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7621 | 1.4557 | 0.2540 | 44.5 | 0.2615 |
| `ex6c/4s4p/focus_front/barriers=False` | desc | 20,000 | 314.9 | 88.4 | 377.9 | 62.3 | 24.3 | 24.3 | 51.2 | 41.1 | 13.2 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7400 | 1.4874 | 0.2466 | 31.8 | 0.1869 |
| `ex6c/4s4p/focus_front/barriers=True` | desc | 20,000 | 321.6 | 90.1 | 385.9 | 63.9 | 25.1 | 25.1 | 52.9 | 41.5 | 13.4 | 0.0000 | 2.2022 | 24.8 | 0.0000 | 1.7384 | 1.4938 | 0.2461 | 31.8 | 0.1873 |
| `ex6c/4s4p/focus_rear/barriers=False` | desc | 20,000 | 592.1 | 164.9 | 710.5 | 117.1 | 62.0 | 62.0 | 83.5 | 74.1 | 22.4 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.8387 | 1.5168 | 0.2796 | 49.7 | 0.2926 |
| `ex6c/4s4p/focus_rear/barriers=True` | desc | 20,000 | 457.4 | 127.0 | 548.9 | 91.5 | 38.4 | 38.4 | 80.4 | 54.7 | 16.6 | 0.0000 | 27.8 | 243.3 | 0.0000 | 1.8899 | 1.5884 | 0.2966 | 37.8 | 0.2222 |
| `ex6c/4s4p/greedy_capture/barriers=False` | desc | 20,000 | 571.2 | 158.8 | 685.4 | 113.6 | 63.2 | 63.2 | 111.8 | 111.1 | 19.9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7826 | 1.5117 | 0.2609 | 46.3 | 0.2723 |
| `ex6c/4s4p/greedy_capture/barriers=True` | desc | 20,000 | 568.5 | 158.0 | 682.2 | 113.0 | 62.2 | 62.2 | 110.5 | 107.7 | 19.8 | 0.0000 | 11.6 | 63.1 | 0.0000 | 1.7799 | 1.5116 | 0.2600 | 46.3 | 0.2722 |
| `ex6c/4s4p/random/barriers=False` | desc | 20,000 | 437.7 | 122.1 | 525.2 | 87.1 | 41.6 | 41.6 | 66.1 | 59.0 | 17.2 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7568 | 1.4722 | 0.2523 | 40.9 | 0.2406 |
| `ex6c/4s4p/random/barriers=True` | desc | 20,000 | 430.6 | 120.1 | 516.8 | 85.7 | 39.9 | 39.9 | 64.6 | 55.9 | 17.0 | 0.0000 | 10.7 | 58.7 | 0.0000 | 1.7697 | 1.4970 | 0.2566 | 40.3 | 0.2368 |
| `ex6c/4s4p/spread/barriers=False` | desc | 20,000 | 621.3 | 173.7 | 745.5 | 121.6 | 65.6 | 65.6 | 85.4 | 76.4 | 23.2 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.8759 | 1.4957 | 0.2919 | 52.9 | 0.3111 |
| `ex6c/4s4p/spread/barriers=True` | desc | 20,000 | 560.0 | 156.8 | 672.0 | 109.3 | 53.6 | 53.6 | 84.0 | 64.9 | 20.7 | 0.0000 | 55.4 | 235.6 | 0.0000 | 1.8846 | 1.5086 | 0.2949 | 47.9 | 0.2818 |
| `ex6d/4s4p/focus_front-vs-random/barriers=False` | conf | 400,000 | 402.5 | 113.5 | 483.0 | 77.9 | 36.7 | 36.7 | 61.7 | 53.7 | 15.1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.6976 | 1.4276 | 0.2325 | 42.5 | 0.2498 |
| `ex6d/4s4p/focus_front-vs-random/barriers=True` | conf | 400,000 | 400.4 | 112.8 | 480.5 | 77.7 | 35.8 | 35.8 | 61.3 | 51.7 | 15.0 | 0.0000 | 8.4166 | 49.3 | 0.0000 | 1.7091 | 1.4321 | 0.2364 | 41.8 | 0.2460 |
| `ex6d/4s4p/focus_rear-vs-random/barriers=False` | desc | 20,000 | 466.3 | 130.7 | 559.6 | 91.6 | 45.4 | 45.4 | 69.2 | 61.7 | 17.8 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7631 | 1.4624 | 0.2543 | 44.0 | 0.2588 |
| `ex6d/4s4p/focus_rear-vs-random/barriers=True` | desc | 20,000 | 439.8 | 122.7 | 527.7 | 87.3 | 39.7 | 39.7 | 69.0 | 55.8 | 16.6 | 0.0000 | 15.1 | 112.9 | 0.0000 | 1.7798 | 1.4985 | 0.2599 | 40.5 | 0.2381 |
| `ex6d/4s4p/greedy_capture-vs-random/barriers=False` | desc | 20,000 | 473.9 | 132.0 | 568.7 | 94.4 | 47.7 | 47.7 | 77.4 | 71.8 | 17.9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7571 | 1.4788 | 0.2524 | 42.9 | 0.2523 |
| `ex6d/4s4p/greedy_capture-vs-random/barriers=True` | desc | 20,000 | 467.2 | 130.2 | 560.7 | 92.9 | 46.0 | 46.0 | 76.2 | 68.8 | 17.7 | 0.0000 | 11.0 | 60.1 | 0.0000 | 1.7538 | 1.4760 | 0.2513 | 42.5 | 0.2499 |
| `ex6d/4s4p/spread-vs-random/barriers=False` | conf | 400,000 | 470.7 | 132.2 | 564.9 | 92.1 | 46.0 | 46.0 | 69.2 | 61.8 | 18.0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7595 | 1.4529 | 0.2532 | 44.6 | 0.2621 |
| `ex6d/4s4p/spread-vs-random/barriers=True` | conf | 400,000 | 459.6 | 128.9 | 551.5 | 90.3 | 42.9 | 42.9 | 69.2 | 57.7 | 17.6 | 0.0000 | 20.9 | 104.1 | 0.0000 | 1.7842 | 1.4687 | 0.2614 | 42.8 | 0.2515 |
| `ex6e/6s2p/random/mandatory` | conf | 400,000 | 161.2 | 80.9 | 193.5 | 80.9 | 10.9 | 10.9 | 13.7 | 10.6 | 7.4625 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3181 | 1.2176 | 0.3181 | 62.1 | 0.3075 |
| `ex6e/6s2p/random/mandatory_extended` | desc | 20,000 | 173.9 | 87.2 | 208.6 | 87.2 | 12.1 | 12.1 | 14.8 | 11.9 | 7.8121 | 0.0000 | 0.0000 | 0.0000 | 0.4700 | 1.3248 | 1.2243 | 0.3247 | 63.7 | 0.3155 |
| `ex6e/6s2p/random/optional` | conf | 400,000 | 136.7 | 68.6 | 164.0 | 68.6 | 6.3377 | 6.3377 | 8.3226 | 5.0700 | 7.3747 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3058 | 1.2022 | 0.3058 | 50.6 | 0.2506 |
| `ex6e/6s3p/random/mandatory` | desc | 20,001 | 373.8 | 133.1 | 448.5 | 108.2 | 35.2 | 35.2 | 48.4 | 44.7 | 14.3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5675 | 1.3797 | 0.2838 | 56.2 | 0.2782 |
| `ex6e/6s3p/random/mandatory_extended` | desc | 20,001 | 419.8 | 149.4 | 503.8 | 121.4 | 40.4 | 40.4 | 54.2 | 51.7 | 15.5 | 0.0000 | 0.0000 | 0.0000 | 1.1953 | 1.5818 | 1.3933 | 0.2909 | 57.1 | 0.2829 |
| `ex6e/6s3p/random/optional` | desc | 20,001 | 289.9 | 103.1 | 347.9 | 84.2 | 21.5 | 21.5 | 26.0 | 20.1 | 12.9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5553 | 1.3431 | 0.2777 | 48.2 | 0.2388 |
| `ex6e/6s4p/random/mandatory` | desc | 20,000 | 697.8 | 193.6 | 837.5 | 139.2 | 77.0 | 77.0 | 113.9 | 114.8 | 21.6 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7710 | 1.4869 | 0.2570 | 57.1 | 0.2825 |
| `ex6e/6s4p/random/mandatory_extended` | desc | 20,000 | 798.5 | 221.0 | 958.3 | 160.0 | 89.6 | 89.6 | 130.4 | 134.5 | 23.9 | 0.0000 | 0.0000 | 0.0000 | 1.9991 | 1.8003 | 1.5311 | 0.2668 | 56.4 | 0.2790 |
| `ex6e/6s4p/random/optional` | desc | 20,000 | 517.0 | 144.0 | 620.6 | 103.1 | 48.1 | 48.1 | 60.3 | 53.7 | 18.4 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7461 | 1.4513 | 0.2487 | 50.7 | 0.2511 |
| `ex6e/6s6p/random/mandatory` | conf | 400,002 | 1,741 | 335.7 | 2,089 | 205.7 | 224.9 | 224.9 | 383.9 | 420.0 | 36.1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.0928 | 1.6521 | 0.2186 | 60.1 | 0.2975 |
| `ex6e/6s6p/random/mandatory_extended` | desc | 20,004 | 2,040 | 391.5 | 2,448 | 242.8 | 265.8 | 265.8 | 451.6 | 500.9 | 41.3 | 0.0000 | 0.0000 | 0.0000 | 3.9836 | 2.1309 | 1.6905 | 0.2262 | 58.5 | 0.2895 |
| `ex6e/6s6p/random/optional` | conf | 400,002 | 1,241 | 241.2 | 1,489 | 147.0 | 145.2 | 145.2 | 211.2 | 217.3 | 29.1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.0662 | 1.6135 | 0.2132 | 54.8 | 0.2712 |
| `ex6f/6s2p/focus_front-vs-random/mandatory` | desc | 20,000 | 150.7 | 75.6 | 180.9 | 75.6 | 9.7307 | 9.7307 | 13.9 | 10.5 | 6.8433 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.2954 | 1.2022 | 0.2954 | 63.2 | 0.3130 |
| `ex6f/6s2p/focus_front-vs-random/mandatory_extended` | desc | 20,000 | 159.9 | 80.2 | 191.9 | 80.2 | 10.6 | 10.6 | 14.8 | 11.5 | 7.0994 | 0.0000 | 0.0000 | 0.0000 | 0.3546 | 1.3022 | 1.2086 | 0.3022 | 64.8 | 0.3210 |
| `ex6f/6s2p/focus_front-vs-random/optional` | desc | 20,000 | 128.7 | 64.6 | 154.5 | 64.6 | 5.7610 | 5.7610 | 8.4353 | 5.1552 | 6.6814 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.2713 | 1.1756 | 0.2713 | 56.2 | 0.2783 |
| `ex6f/6s2p/focus_rear-vs-random/mandatory` | desc | 20,000 | 168.2 | 84.3 | 201.7 | 84.3 | 11.5 | 11.5 | 13.8 | 10.6 | 7.6178 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3172 | 1.1918 | 0.3172 | 70.1 | 0.3469 |
| `ex6f/6s2p/focus_rear-vs-random/mandatory_extended` | desc | 20,000 | 185.9 | 93.2 | 223.0 | 93.2 | 13.3 | 13.3 | 15.1 | 12.0 | 8.0858 | 0.0000 | 0.0000 | 0.0000 | 0.5308 | 1.3177 | 1.1993 | 0.3177 | 72.1 | 0.3567 |
| `ex6f/6s2p/focus_rear-vs-random/optional` | desc | 20,000 | 140.7 | 70.6 | 168.8 | 70.6 | 6.7104 | 6.7104 | 8.3869 | 5.0403 | 7.3949 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3033 | 1.1839 | 0.3033 | 54.9 | 0.2720 |
| `ex6f/6s2p/greedy_capture-vs-random/mandatory` | desc | 20,000 | 161.5 | 81.0 | 193.8 | 81.0 | 10.9 | 10.9 | 13.7 | 10.5 | 7.5056 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3189 | 1.2183 | 0.3189 | 61.7 | 0.3052 |
| `ex6f/6s2p/greedy_capture-vs-random/mandatory_extended` | desc | 20,000 | 175.9 | 88.2 | 211.1 | 88.2 | 12.3 | 12.3 | 14.9 | 12.0 | 7.8806 | 0.0000 | 0.0000 | 0.0000 | 0.4861 | 1.3280 | 1.2276 | 0.3281 | 62.6 | 0.3101 |
| `ex6f/6s2p/greedy_capture-vs-random/optional` | desc | 20,000 | 147.1 | 73.8 | 176.5 | 73.8 | 8.7137 | 8.7137 | 10.7 | 7.5752 | 7.1265 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.2743 | 1.1721 | 0.2743 | 62.8 | 0.3107 |
| `ex6f/6s2p/spread-vs-random/mandatory` | desc | 20,000 | 170.1 | 85.3 | 204.2 | 85.3 | 11.7 | 11.7 | 13.8 | 10.6 | 7.6289 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3026 | 1.1785 | 0.3025 | 72.6 | 0.3596 |
| `ex6f/6s2p/spread-vs-random/mandatory_extended` | desc | 20,000 | 190.4 | 95.5 | 228.5 | 95.5 | 13.7 | 13.7 | 15.5 | 12.6 | 8.1464 | 0.0000 | 0.0000 | 0.0000 | 0.5616 | 1.3138 | 1.1892 | 0.3139 | 76.1 | 0.3765 |
| `ex6f/6s2p/spread-vs-random/optional` | desc | 20,000 | 138.9 | 69.7 | 166.7 | 69.7 | 6.4398 | 6.4398 | 8.2521 | 4.9555 | 7.3331 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3057 | 1.1804 | 0.3057 | 56.9 | 0.2817 |
| `ex6f/6s3p/focus_front-vs-random/mandatory` | desc | 20,007 | 343.8 | 123.2 | 412.5 | 98.0 | 31.1 | 31.1 | 45.7 | 41.0 | 12.7 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5169 | 1.3420 | 0.2585 | 57.5 | 0.2847 |
| `ex6f/6s3p/focus_front-vs-random/mandatory_extended` | desc | 20,007 | 379.9 | 136.1 | 455.8 | 108.3 | 35.1 | 35.1 | 50.5 | 46.6 | 13.6 | 0.0000 | 0.0000 | 0.0000 | 1.0143 | 1.5395 | 1.3633 | 0.2697 | 57.8 | 0.2860 |
| `ex6f/6s3p/focus_front-vs-random/optional` | desc | 20,007 | 267.6 | 96.0 | 321.1 | 76.1 | 18.9 | 18.9 | 25.4 | 19.3 | 11.4 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.4879 | 1.2991 | 0.2440 | 51.4 | 0.2543 |
| `ex6f/6s3p/focus_rear-vs-random/mandatory` | desc | 20,007 | 399.5 | 142.9 | 479.3 | 114.1 | 38.4 | 38.4 | 50.4 | 46.5 | 14.9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5658 | 1.3578 | 0.2829 | 62.0 | 0.3072 |
| `ex6f/6s3p/focus_rear-vs-random/mandatory_extended` | desc | 20,007 | 456.9 | 163.4 | 548.4 | 130.6 | 45.0 | 45.0 | 57.7 | 55.0 | 16.3 | 0.0000 | 0.0000 | 0.0000 | 1.3507 | 1.5865 | 1.3831 | 0.2933 | 63.2 | 0.3128 |
| `ex6f/6s3p/focus_rear-vs-random/optional` | desc | 20,007 | 308.5 | 110.2 | 370.3 | 88.5 | 23.5 | 23.5 | 27.0 | 20.8 | 13.2 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5746 | 1.3304 | 0.2873 | 53.9 | 0.2666 |
| `ex6f/6s3p/greedy_capture-vs-random/mandatory` | desc | 20,007 | 373.4 | 133.0 | 448.1 | 108.0 | 35.1 | 35.1 | 48.5 | 44.8 | 14.3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5634 | 1.3874 | 0.2817 | 55.9 | 0.2768 |
| `ex6f/6s3p/greedy_capture-vs-random/mandatory_extended` | desc | 20,007 | 419.6 | 149.3 | 503.4 | 121.4 | 40.4 | 40.4 | 54.4 | 51.8 | 15.4 | 0.0000 | 0.0000 | 0.0000 | 1.1822 | 1.5856 | 1.3958 | 0.2928 | 57.3 | 0.2837 |
| `ex6f/6s3p/greedy_capture-vs-random/optional` | desc | 20,007 | 320.2 | 114.1 | 384.2 | 92.6 | 26.6 | 26.6 | 33.6 | 28.3 | 13.1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5334 | 1.3395 | 0.2667 | 53.6 | 0.2652 |
| `ex6f/6s3p/spread-vs-random/mandatory` | desc | 20,007 | 406.2 | 145.8 | 487.5 | 115.2 | 39.2 | 39.2 | 51.2 | 47.5 | 14.7 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5557 | 1.3466 | 0.2778 | 64.1 | 0.3172 |
| `ex6f/6s3p/spread-vs-random/mandatory_extended` | desc | 20,007 | 465.9 | 167.1 | 559.0 | 132.1 | 46.0 | 46.0 | 58.5 | 56.1 | 16.2 | 0.0000 | 0.0000 | 0.0000 | 1.3903 | 1.5818 | 1.3675 | 0.2909 | 64.6 | 0.3198 |
| `ex6f/6s3p/spread-vs-random/optional` | desc | 20,007 | 309.0 | 110.7 | 370.8 | 88.1 | 23.4 | 23.4 | 26.8 | 20.7 | 13.2 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5900 | 1.3272 | 0.2950 | 55.0 | 0.2725 |
| `ex6f/6s4p/focus_front-vs-random/mandatory` | desc | 20,000 | 638.2 | 179.1 | 765.8 | 123.7 | 68.5 | 68.5 | 105.0 | 103.6 | 18.7 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7106 | 1.4404 | 0.2369 | 59.0 | 0.2920 |
| `ex6f/6s4p/focus_front-vs-random/mandatory_extended` | desc | 20,000 | 721.1 | 201.9 | 865.2 | 140.1 | 78.4 | 78.4 | 118.9 | 119.9 | 20.5 | 0.0000 | 0.0000 | 0.0000 | 1.8082 | 1.7285 | 1.4795 | 0.2428 | 58.2 | 0.2882 |
| `ex6f/6s4p/focus_front-vs-random/optional` | desc | 20,000 | 470.9 | 133.0 | 565.1 | 90.6 | 42.0 | 42.0 | 56.4 | 48.9 | 15.7 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.6674 | 1.3925 | 0.2225 | 53.2 | 0.2635 |
| `ex6f/6s4p/focus_rear-vs-random/mandatory` | desc | 20,000 | 742.6 | 207.4 | 891.0 | 145.9 | 83.0 | 83.0 | 119.3 | 120.2 | 22.2 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7646 | 1.4713 | 0.2549 | 60.7 | 0.3004 |
| `ex6f/6s4p/focus_rear-vs-random/mandatory_extended` | desc | 20,000 | 866.9 | 241.7 | 1,040 | 170.5 | 98.7 | 98.7 | 139.1 | 143.6 | 25.0 | 0.0000 | 0.0000 | 0.0000 | 2.2598 | 1.7746 | 1.4970 | 0.2582 | 60.6 | 0.3001 |
| `ex6f/6s4p/focus_rear-vs-random/optional` | desc | 20,000 | 552.8 | 155.0 | 663.3 | 108.4 | 52.4 | 52.4 | 62.9 | 55.8 | 18.9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7575 | 1.4395 | 0.2525 | 54.8 | 0.2714 |
| `ex6f/6s4p/greedy_capture-vs-random/mandatory` | desc | 20,000 | 698.0 | 193.8 | 837.6 | 139.3 | 77.0 | 77.0 | 114.3 | 115.3 | 21.5 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7544 | 1.4891 | 0.2514 | 56.9 | 0.2819 |
| `ex6f/6s4p/greedy_capture-vs-random/mandatory_extended` | desc | 20,000 | 799.1 | 221.2 | 959.0 | 159.8 | 89.7 | 89.7 | 130.5 | 134.7 | 23.8 | 0.0000 | 0.0000 | 0.0000 | 2.0278 | 1.7858 | 1.5249 | 0.2619 | 56.5 | 0.2799 |
| `ex6f/6s4p/greedy_capture-vs-random/optional` | desc | 20,000 | 564.5 | 156.9 | 677.4 | 112.9 | 56.0 | 56.0 | 73.7 | 68.8 | 19.1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7330 | 1.4617 | 0.2443 | 53.0 | 0.2625 |
| `ex6f/6s4p/spread-vs-random/mandatory` | desc | 20,000 | 755.9 | 211.9 | 907.0 | 147.3 | 84.8 | 84.8 | 121.3 | 122.7 | 22.2 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7470 | 1.4576 | 0.2490 | 62.0 | 0.3071 |
| `ex6f/6s4p/spread-vs-random/mandatory_extended` | desc | 20,000 | 873.5 | 244.4 | 1,048 | 170.6 | 99.4 | 99.4 | 140.2 | 145.0 | 25.0 | 0.0000 | 0.0000 | 0.0000 | 2.2529 | 1.7852 | 1.4990 | 0.2617 | 60.9 | 0.3017 |
| `ex6f/6s4p/spread-vs-random/optional` | desc | 20,000 | 556.6 | 156.4 | 667.9 | 108.9 | 52.8 | 52.8 | 62.8 | 55.9 | 18.9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7644 | 1.4256 | 0.2548 | 54.9 | 0.2719 |
| `ex6f/6s6p/focus_front-vs-random/mandatory` | desc | 20,016 | 1,603 | 313.4 | 1,924 | 182.6 | 203.9 | 203.9 | 352.4 | 381.3 | 31.5 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.0296 | 1.6037 | 0.2059 | 61.7 | 0.3052 |
| `ex6f/6s6p/focus_front-vs-random/mandatory_extended` | desc | 20,016 | 1,868 | 363.6 | 2,242 | 213.4 | 239.4 | 239.4 | 412.2 | 452.7 | 35.6 | 0.0000 | 0.0000 | 0.0000 | 3.7638 | 2.0605 | 1.6344 | 0.2121 | 59.6 | 0.2948 |
| `ex6f/6s6p/focus_front-vs-random/optional` | desc | 20,016 | 1,130 | 223.6 | 1,357 | 127.3 | 128.9 | 128.9 | 192.9 | 194.9 | 24.6 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.9586 | 1.5209 | 0.1917 | 56.5 | 0.2796 |
| `ex6f/6s6p/focus_rear-vs-random/mandatory` | desc | 20,016 | 1,825 | 354.1 | 2,190 | 212.9 | 237.2 | 237.2 | 400.0 | 437.5 | 36.9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.0688 | 1.6349 | 0.2138 | 62.0 | 0.3069 |
| `ex6f/6s6p/focus_rear-vs-random/mandatory_extended` | desc | 20,016 | 2,160 | 417.4 | 2,592 | 253.5 | 283.0 | 283.0 | 474.7 | 526.8 | 42.8 | 0.0000 | 0.0000 | 0.0000 | 4.2991 | 2.1302 | 1.6898 | 0.2260 | 60.0 | 0.2968 |
| `ex6f/6s6p/focus_rear-vs-random/optional` | desc | 20,016 | 1,316 | 257.4 | 1,579 | 153.9 | 155.9 | 155.9 | 220.8 | 227.3 | 30.4 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.0670 | 1.6000 | 0.2134 | 56.8 | 0.2812 |
| `ex6f/6s6p/greedy_capture-vs-random/mandatory` | desc | 20,016 | 1,737 | 335.2 | 2,085 | 205.5 | 224.3 | 224.3 | 383.3 | 419.4 | 36.1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.0794 | 1.6480 | 0.2159 | 59.9 | 0.2967 |
| `ex6f/6s6p/greedy_capture-vs-random/mandatory_extended` | desc | 20,016 | 2,036 | 390.9 | 2,444 | 242.1 | 265.2 | 265.2 | 450.7 | 499.9 | 41.4 | 0.0000 | 0.0000 | 0.0000 | 3.9495 | 2.1456 | 1.6994 | 0.2291 | 58.4 | 0.2889 |
| `ex6f/6s6p/greedy_capture-vs-random/optional` | desc | 20,016 | 1,327 | 257.5 | 1,593 | 157.3 | 159.4 | 159.4 | 239.4 | 250.6 | 30.4 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.0742 | 1.6186 | 0.2148 | 56.4 | 0.2793 |
| `ex6f/6s6p/spread-vs-random/mandatory` | desc | 20,016 | 1,834 | 357.0 | 2,201 | 213.2 | 238.5 | 238.5 | 401.0 | 438.9 | 37.1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.0767 | 1.6291 | 0.2153 | 61.9 | 0.3067 |
| `ex6f/6s6p/spread-vs-random/mandatory_extended` | desc | 20,016 | 2,170 | 420.6 | 2,604 | 253.5 | 284.6 | 284.6 | 475.7 | 528.1 | 42.6 | 0.0000 | 0.0000 | 0.0000 | 4.2931 | 2.1074 | 1.6737 | 0.2215 | 60.4 | 0.2989 |
| `ex6f/6s6p/spread-vs-random/optional` | desc | 20,016 | 1,319 | 258.8 | 1,583 | 152.9 | 156.0 | 156.0 | 220.8 | 227.3 | 29.9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.0478 | 1.5792 | 0.2096 | 57.8 | 0.2861 |
| `ex7/2p/4s-adjacent/focus_front` | conf | 200,000 | 102.8 | 51.7 | 123.4 | 51.7 | 3.9324 | 3.9324 | 8.5273 | 5.0112 | 6.3870 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.2917 | 1.2156 | 0.2917 | 37.7 | 0.2215 |
| `ex7/2p/4s-adjacent/focus_rear` | conf | 200,000 | 123.4 | 61.9 | 148.1 | 61.9 | 5.9137 | 5.9137 | 9.1907 | 5.3833 | 7.0886 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3030 | 1.1919 | 0.3030 | 41.8 | 0.2461 |
| `ex7/2p/4s-adjacent/greedy_capture` | conf | 200,000 | 137.7 | 69.1 | 165.2 | 69.1 | 9.5354 | 9.5354 | 14.6 | 11.2 | 7.0705 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3191 | 1.2199 | 0.3191 | 54.1 | 0.3185 |
| `ex7/2p/4s-adjacent/random` | conf | 200,000 | 117.9 | 59.2 | 141.4 | 59.2 | 5.7241 | 5.7241 | 9.2374 | 5.7062 | 6.9853 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3123 | 1.2143 | 0.3123 | 42.1 | 0.2479 |
| `ex7/2p/4s-adjacent/spread` | conf | 200,000 | 120.2 | 60.4 | 144.3 | 60.4 | 5.2578 | 5.2578 | 8.8005 | 5.1548 | 6.8141 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.2961 | 1.1903 | 0.2961 | 39.4 | 0.2315 |
| `ex7/2p/4s-opposite/focus_front` | conf | 200,000 | 102.4 | 51.5 | 122.9 | 51.5 | 3.8057 | 3.8057 | 8.0364 | 4.3965 | 7.2086 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3060 | 1.2291 | 0.3060 | 35.9 | 0.2113 |
| `ex7/2p/4s-opposite/focus_rear` | conf | 200,000 | 122.6 | 61.6 | 147.1 | 61.6 | 5.1396 | 5.1396 | 8.1264 | 4.3445 | 7.9791 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3526 | 1.2431 | 0.3526 | 32.8 | 0.1928 |
| `ex7/2p/4s-opposite/greedy_capture` | conf | 200,000 | 141.5 | 71.0 | 169.8 | 71.0 | 9.8547 | 9.8547 | 14.0 | 10.6 | 7.6887 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3177 | 1.2212 | 0.3177 | 54.4 | 0.3199 |
| `ex7/2p/4s-opposite/random` | conf | 200,000 | 117.9 | 59.2 | 141.5 | 59.2 | 5.4764 | 5.4764 | 8.5053 | 4.9261 | 7.3680 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3211 | 1.2225 | 0.3211 | 40.0 | 0.2354 |
| `ex7/2p/4s-opposite/spread` | conf | 200,000 | 119.6 | 60.1 | 143.5 | 60.1 | 4.4601 | 4.4601 | 7.7676 | 4.1163 | 8.0417 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3638 | 1.2535 | 0.3638 | 29.3 | 0.1725 |
| `ex7/3p/6s-adjacent/random` | conf | 200,001 | 289.7 | 103.1 | 347.7 | 84.1 | 21.4 | 21.4 | 26.2 | 20.3 | 12.9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5519 | 1.3474 | 0.2760 | 48.5 | 0.2399 |
| `ex7/3p/6s-adjacent/spread` | conf | 200,001 | 349.4 | 125.3 | 419.3 | 99.2 | 26.6 | 26.6 | 28.0 | 21.2 | 13.6 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.6579 | 1.3501 | 0.3290 | 60.8 | 0.3012 |
| `ex7/3p/6s-spread/random` | conf | 200,001 | 296.6 | 105.4 | 355.9 | 86.2 | 21.5 | 21.5 | 23.8 | 17.7 | 13.6 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5558 | 1.3470 | 0.2779 | 48.5 | 0.2400 |
| `ex7/3p/6s-spread/spread` | conf | 200,001 | 375.1 | 134.0 | 450.1 | 107.5 | 28.3 | 28.3 | 26.2 | 19.0 | 17.0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7003 | 1.3826 | 0.3501 | 59.3 | 0.2938 |
| `ex8/4s4p/greedy_capture-vs-random/mandatory` | conf | 250,000 | 570.4 | 158.6 | 684.6 | 113.4 | 63.1 | 63.1 | 111.3 | 110.6 | 19.9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7677 | 1.5065 | 0.2559 | 46.3 | 0.2721 |
| `ex8/4s4p/greedy_capture-vs-random/optional` | conf | 250,000 | 473.5 | 131.9 | 568.2 | 94.3 | 47.6 | 47.6 | 77.6 | 72.1 | 17.9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7556 | 1.4788 | 0.2519 | 43.2 | 0.2542 |
| `ex8/6s2p/random/baseline` | conf | 250,000 | 136.7 | 68.6 | 164.1 | 68.6 | 6.3557 | 6.3557 | 8.3056 | 5.0620 | 7.3501 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.3058 | 1.2030 | 0.3058 | 50.7 | 0.2511 |
| `ex8/6s3p/random/baseline` | conf | 250,002 | 289.8 | 103.1 | 347.8 | 84.1 | 21.4 | 21.4 | 26.2 | 20.3 | 12.9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.5521 | 1.3464 | 0.2760 | 48.4 | 0.2398 |
| `ex8/6s4p/random/baseline` | conf | 250,000 | 516.3 | 143.8 | 619.6 | 103.0 | 48.0 | 48.0 | 60.3 | 53.7 | 18.3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7451 | 1.4512 | 0.2484 | 50.4 | 0.2497 |
| `ex8/6s6p/random/baseline` | conf | 250,002 | 1,241 | 241.4 | 1,490 | 147.0 | 145.3 | 145.3 | 211.3 | 217.5 | 29.2 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2.0719 | 1.6166 | 0.2144 | 54.7 | 0.2707 |
| `ex9/4s4p/focus_front/barriers` | conf | 600,000 | 400.5 | 112.9 | 480.6 | 77.6 | 35.9 | 35.9 | 61.4 | 51.7 | 15.0 | 0.0000 | 8.4248 | 49.4 | 0.0000 | 1.7064 | 1.4313 | 0.2355 | 41.8 | 0.2461 |
| `ex9/4s4p/focus_front/baseline` | conf | 600,000 | 402.4 | 113.5 | 482.9 | 77.8 | 36.7 | 36.7 | 61.7 | 53.7 | 15.1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.6964 | 1.4276 | 0.2321 | 42.5 | 0.2499 |
| `ex9/4s4p/focus_front/bonus_forfeited` | conf | 600,000 | 409.5 | 115.4 | 487.7 | 79.3 | 37.0 | 37.0 | 65.7 | 55.0 | 15.2 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7080 | 1.4466 | 0.2360 | 40.4 | 0.2376 |
| `ex9/4s4p/focus_front/bonus_quick` | conf | 600,000 | 362.4 | 101.5 | 538.8 | 71.3 | 42.7 | 42.7 | 33.2 | 26.9 | 16.3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.6735 | 1.4060 | 0.2245 | 38.3 | 0.2252 |
| `ex9/4s4p/focus_front/capture=mandatory` | conf | 600,000 | 528.0 | 148.1 | 633.6 | 102.8 | 56.7 | 56.7 | 102.9 | 100.1 | 17.8 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7312 | 1.4713 | 0.2437 | 46.9 | 0.2762 |
| `ex9/4s4p/focus_front/capture=mandatory_extended` | conf | 600,000 | 603.7 | 169.0 | 724.4 | 117.5 | 66.2 | 66.2 | 117.8 | 117.6 | 19.7 | 0.0000 | 0.0000 | 0.0000 | 1.9263 | 1.7501 | 1.4987 | 0.2500 | 46.9 | 0.2757 |
| `ex9/4s4p/focus_front/cold_start=free_entry` | conf | 600,000 | 453.1 | 131.4 | 543.8 | 78.5 | 69.2 | 69.2 | 8.3710 | 9.2760 | 14.1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.4041 | 1.1897 | 0.1347 | 64.0 | 0.3763 |
| `ex9/4s4p/focus_front/cold_start=strict` | conf | 600,000 | 419.8 | 118.0 | 503.8 | 81.9 | 36.2 | 36.2 | 80.5 | 76.3 | 12.0 | 4.9985 | 0.0000 | 0.0000 | 0.0000 | 1.7152 | 1.4323 | 0.2384 | 43.3 | 0.2545 |
| `ex9/4s4p/focus_front/dreimal` | conf | 600,000 | 398.5 | 111.8 | 525.5 | 78.1 | 42.4 | 42.4 | 32.6 | 25.8 | 16.2 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.6614 | 1.3867 | 0.2205 | 41.3 | 0.2427 |
| `ex9/4s4p/focus_front/goal_no_jump` | conf | 600,000 | 459.1 | 127.5 | 550.9 | 92.4 | 41.3 | 41.3 | 81.9 | 58.2 | 17.2 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.8025 | 1.5733 | 0.2675 | 30.6 | 0.1797 |
| `ex9/4s4p/focus_rear/barriers` | conf | 600,000 | 439.9 | 122.7 | 527.8 | 87.4 | 39.8 | 39.8 | 68.8 | 55.6 | 16.7 | 0.0000 | 15.1 | 113.0 | 0.0000 | 1.7862 | 1.5014 | 0.2621 | 40.5 | 0.2383 |
| `ex9/4s4p/focus_rear/baseline` | conf | 600,000 | 467.2 | 130.9 | 560.6 | 91.9 | 45.6 | 45.6 | 69.1 | 61.6 | 18.0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7623 | 1.4650 | 0.2541 | 43.9 | 0.2584 |
| `ex9/4s4p/focus_rear/bonus_forfeited` | conf | 600,000 | 474.7 | 132.9 | 565.8 | 93.5 | 45.9 | 45.9 | 73.3 | 62.9 | 18.1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7719 | 1.4786 | 0.2573 | 41.8 | 0.2457 |
| `ex9/4s4p/focus_rear/bonus_quick` | conf | 600,000 | 429.7 | 119.5 | 640.3 | 86.1 | 54.4 | 54.4 | 36.9 | 31.8 | 20.1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7485 | 1.4437 | 0.2495 | 39.5 | 0.2324 |
| `ex9/4s4p/focus_rear/capture=mandatory` | conf | 600,000 | 603.5 | 168.6 | 724.2 | 118.6 | 67.8 | 67.8 | 116.8 | 115.7 | 20.6 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7658 | 1.4916 | 0.2553 | 48.6 | 0.2858 |
| `ex9/4s4p/focus_rear/capture=mandatory_extended` | conf | 600,000 | 709.2 | 197.7 | 851.1 | 139.7 | 81.5 | 81.5 | 137.1 | 139.8 | 23.4 | 0.0000 | 0.0000 | 0.0000 | 2.4083 | 1.7872 | 1.5214 | 0.2624 | 48.5 | 0.2853 |
| `ex9/4s4p/focus_rear/cold_start=free_entry` | conf | 600,000 | 477.9 | 136.7 | 573.5 | 87.1 | 74.3 | 74.3 | 8.4531 | 9.5904 | 15.8 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.4700 | 1.2584 | 0.1567 | 58.2 | 0.3422 |
| `ex9/4s4p/focus_rear/cold_start=strict` | conf | 600,000 | 484.7 | 135.4 | 581.6 | 96.0 | 45.1 | 45.1 | 87.9 | 84.3 | 14.9 | 4.9960 | 0.0000 | 0.0000 | 0.0000 | 1.7803 | 1.4709 | 0.2601 | 44.4 | 0.2612 |
| `ex9/4s4p/focus_rear/dreimal` | conf | 600,000 | 466.3 | 130.0 | 614.2 | 92.9 | 52.8 | 52.8 | 35.7 | 29.8 | 19.4 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7294 | 1.4225 | 0.2431 | 42.8 | 0.2515 |
| `ex9/4s4p/focus_rear/goal_no_jump` | conf | 600,000 | 505.9 | 141.9 | 607.1 | 99.7 | 48.2 | 48.2 | 84.8 | 64.1 | 18.9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7490 | 1.4832 | 0.2497 | 37.1 | 0.2185 |
| `ex9/4s4p/greedy_capture/barriers` | conf | 600,000 | 467.3 | 130.2 | 560.7 | 92.9 | 45.9 | 45.9 | 76.2 | 68.7 | 17.6 | 0.0000 | 11.0 | 60.0 | 0.0000 | 1.7539 | 1.4790 | 0.2513 | 42.7 | 0.2512 |
| `ex9/4s4p/greedy_capture/baseline` | conf | 600,000 | 473.1 | 131.8 | 567.7 | 94.2 | 47.5 | 47.5 | 77.6 | 72.0 | 17.9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7507 | 1.4770 | 0.2502 | 43.2 | 0.2543 |
| `ex9/4s4p/greedy_capture/bonus_forfeited` | conf | 600,000 | 480.6 | 133.8 | 573.0 | 95.8 | 47.9 | 47.9 | 81.7 | 73.4 | 18.1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7613 | 1.4949 | 0.2538 | 41.1 | 0.2419 |
| `ex9/4s4p/greedy_capture/bonus_quick` | conf | 600,000 | 437.6 | 120.7 | 665.2 | 89.2 | 58.6 | 58.6 | 40.5 | 38.2 | 20.6 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7486 | 1.4692 | 0.2495 | 38.2 | 0.2247 |
| `ex9/4s4p/greedy_capture/capture=mandatory` | conf | 600,000 | 570.9 | 158.7 | 685.1 | 113.5 | 63.1 | 63.1 | 111.4 | 110.7 | 19.9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7710 | 1.5092 | 0.2570 | 46.2 | 0.2720 |
| `ex9/4s4p/greedy_capture/capture=mandatory_extended` | conf | 600,000 | 660.9 | 183.3 | 793.0 | 131.9 | 74.7 | 74.7 | 129.1 | 131.7 | 22.4 | 0.0000 | 0.0000 | 0.0000 | 2.1359 | 1.7950 | 1.5397 | 0.2650 | 46.0 | 0.2707 |
| `ex9/4s4p/greedy_capture/cold_start=free_entry` | conf | 600,000 | 782.9 | 214.9 | 939.5 | 158.9 | 164.6 | 164.6 | 8.3541 | 14.9 | 33.0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.6988 | 1.3885 | 0.2329 | 60.4 | 0.3552 |
| `ex9/4s4p/greedy_capture/cold_start=strict` | conf | 600,000 | 490.7 | 136.3 | 588.8 | 98.3 | 46.9 | 46.9 | 96.3 | 94.6 | 14.9 | 4.9904 | 0.0000 | 0.0000 | 0.0000 | 1.7655 | 1.4871 | 0.2552 | 43.7 | 0.2570 |
| `ex9/4s4p/greedy_capture/dreimal` | conf | 600,000 | 475.0 | 131.4 | 635.7 | 96.0 | 56.6 | 56.6 | 39.2 | 35.8 | 19.8 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7222 | 1.4389 | 0.2407 | 41.7 | 0.2453 |
| `ex9/4s4p/greedy_capture/goal_no_jump` | conf | 600,000 | 501.0 | 139.0 | 601.2 | 100.8 | 49.4 | 49.4 | 89.0 | 74.3 | 18.7 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7320 | 1.4921 | 0.2440 | 36.7 | 0.2160 |
| `ex9/4s4p/random/barriers` | conf | 600,000 | 430.9 | 120.2 | 517.0 | 85.6 | 39.9 | 39.9 | 64.6 | 55.8 | 17.0 | 0.0000 | 10.7 | 58.8 | 0.0000 | 1.7611 | 1.4781 | 0.2537 | 40.6 | 0.2386 |
| `ex9/4s4p/random/baseline` | conf | 600,000 | 438.2 | 122.2 | 525.8 | 87.1 | 41.7 | 41.7 | 66.1 | 59.0 | 17.3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7578 | 1.4765 | 0.2526 | 41.2 | 0.2423 |
| `ex9/4s4p/random/bonus_forfeited` | conf | 600,000 | 445.2 | 124.1 | 530.5 | 88.6 | 42.0 | 42.0 | 70.0 | 60.2 | 17.4 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7656 | 1.4934 | 0.2552 | 39.2 | 0.2305 |
| `ex9/4s4p/random/bonus_quick` | conf | 600,000 | 399.2 | 110.3 | 595.6 | 81.2 | 49.3 | 49.3 | 34.9 | 30.1 | 19.3 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7563 | 1.4690 | 0.2521 | 36.2 | 0.2131 |
| `ex9/4s4p/random/capture=mandatory` | conf | 600,000 | 570.9 | 158.7 | 685.1 | 113.5 | 63.1 | 63.1 | 111.4 | 110.7 | 19.9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7716 | 1.5087 | 0.2572 | 46.2 | 0.2719 |
| `ex9/4s4p/random/capture=mandatory_extended` | conf | 600,000 | 660.8 | 183.3 | 793.0 | 131.8 | 74.7 | 74.7 | 129.1 | 131.7 | 22.4 | 0.0000 | 0.0000 | 0.0000 | 2.1396 | 1.7942 | 1.5398 | 0.2647 | 46.2 | 0.2716 |
| `ex9/4s4p/random/cold_start=free_entry` | conf | 600,000 | 588.8 | 163.3 | 706.5 | 117.3 | 104.9 | 104.9 | 8.4150 | 9.2318 | 25.5 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7151 | 1.3870 | 0.2384 | 53.6 | 0.3155 |
| `ex9/4s4p/random/cold_start=strict` | conf | 600,000 | 455.6 | 126.7 | 546.7 | 91.3 | 41.2 | 41.2 | 84.8 | 81.6 | 14.2 | 5.0080 | 0.0000 | 0.0000 | 0.0000 | 1.7737 | 1.4848 | 0.2579 | 41.7 | 0.2454 |
| `ex9/4s4p/random/dreimal` | conf | 600,000 | 437.3 | 121.2 | 577.1 | 88.3 | 48.5 | 48.5 | 34.2 | 28.6 | 18.7 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7261 | 1.4373 | 0.2420 | 39.8 | 0.2341 |
| `ex9/4s4p/random/goal_no_jump` | conf | 600,000 | 465.2 | 129.3 | 558.3 | 93.5 | 43.4 | 43.4 | 77.4 | 60.9 | 18.0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7418 | 1.4988 | 0.2473 | 34.6 | 0.2035 |
| `ex9/4s4p/spread/barriers` | conf | 600,000 | 459.7 | 128.9 | 551.6 | 90.3 | 42.9 | 42.9 | 69.2 | 57.8 | 17.6 | 0.0000 | 20.9 | 104.0 | 0.0000 | 1.7845 | 1.4726 | 0.2615 | 42.7 | 0.2512 |
| `ex9/4s4p/spread/baseline` | conf | 600,000 | 471.0 | 132.2 | 565.2 | 92.2 | 46.1 | 46.1 | 69.2 | 61.9 | 18.0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7613 | 1.4535 | 0.2538 | 44.5 | 0.2616 |
| `ex9/4s4p/spread/bonus_forfeited` | conf | 600,000 | 478.5 | 134.3 | 570.4 | 93.7 | 46.4 | 46.4 | 73.4 | 63.3 | 18.1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7694 | 1.4691 | 0.2565 | 42.5 | 0.2499 |
| `ex9/4s4p/spread/bonus_quick` | conf | 600,000 | 433.1 | 120.7 | 645.2 | 86.4 | 54.9 | 54.9 | 36.8 | 31.9 | 20.1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7436 | 1.4325 | 0.2479 | 40.1 | 0.2359 |
| `ex9/4s4p/spread/capture=mandatory` | conf | 600,000 | 610.4 | 171.0 | 732.4 | 119.3 | 68.8 | 68.8 | 117.9 | 117.1 | 20.7 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7592 | 1.4795 | 0.2531 | 49.2 | 0.2895 |
| `ex9/4s4p/spread/capture=mandatory_extended` | conf | 600,000 | 718.4 | 200.9 | 862.1 | 140.6 | 82.9 | 82.9 | 138.7 | 141.8 | 23.4 | 0.0000 | 0.0000 | 0.0000 | 2.4572 | 1.7779 | 1.5102 | 0.2593 | 49.1 | 0.2890 |
| `ex9/4s4p/spread/cold_start=free_entry` | conf | 600,000 | 660.3 | 184.6 | 792.4 | 128.5 | 124.5 | 124.5 | 8.5236 | 8.4915 | 28.1 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7332 | 1.3292 | 0.2444 | 61.7 | 0.3631 |
| `ex9/4s4p/spread/cold_start=strict` | conf | 600,000 | 488.6 | 136.7 | 586.3 | 96.4 | 45.6 | 45.6 | 88.0 | 84.5 | 15.0 | 4.9922 | 0.0000 | 0.0000 | 0.0000 | 1.7823 | 1.4641 | 0.2608 | 45.0 | 0.2649 |
| `ex9/4s4p/spread/dreimal` | conf | 600,000 | 469.0 | 131.0 | 617.5 | 93.1 | 53.2 | 53.2 | 35.7 | 29.8 | 19.4 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7272 | 1.4133 | 0.2424 | 43.3 | 0.2545 |
| `ex9/4s4p/spread/goal_no_jump` | conf | 600,000 | 508.5 | 142.9 | 610.2 | 99.7 | 48.6 | 48.6 | 84.5 | 64.3 | 18.9 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.7418 | 1.4705 | 0.2473 | 37.9 | 0.2227 |

---

Generated by `madnlab report`. Every number is reproducible from the master seeds in `campaigns/*.json` and the analysis seed above (NF-6, NF-7).

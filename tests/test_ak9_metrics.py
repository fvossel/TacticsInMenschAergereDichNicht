"""AK-9 — metric cross-validation.

An independent implementation walks the event log and reproduces every §6.2
summary field the log can support.

§4.1 forbids analyses from re-deriving a number the summary row already
carries, which removes the only redundant path: a wrong ``lead_changes`` or
``winner_rank_at_50`` passes AK-1 through AK-7 unchanged and lands in
``docs/results.md``. This is the one place that rule is broken on purpose.

The two routes are genuinely different. The loop accumulates counters while it
plays; the reference reconstructs the board from the event stream and
recomputes from positions. Two implementations agreeing is evidence; one
implementation called twice is not.
"""

from __future__ import annotations

import pytest

from madnlab.analysis.reference import derive_from_events
from madnlab.engine.geometry import SeatPattern
from madnlab.engine.rules import CaptureMode, ColdStart, RuleSet
from madnlab.run.game import GameSpec, play_indexed_game

#: Fields the event log can support. The seeds and the config echo are not
#: derivable from a stream of moves and are deliberately not claimed.
CROSS_CHECKED = (
    "turns",
    "dice_rolls",
    "turns_to_first_win",
    "captures_total",
    "captures_by_seat",
    "captured_by_seat",
    "passes_by_seat",
    "entry_waits_by_seat",
    "lead_changes",
    "turns_without_leader",
    "time_in_lead_by_seat",
    "extra_laps_by_seat",
    "barriers_formed",
    "barrier_turns_by_seat",
    "forced_extra_lap_offered",
    "winner_rank_at_50",
    "winner_rank_at_75",
    "winner_rank_at_50_tied",
    "comeback",
    "comeback_rank_threshold",
    "comeback_depth",
    "final_margin",
    "final_margin_norm",
    "ranks",
    "winner",
)

CASES = [
    ("baseline-4p", 4, 4, RuleSet(), ("RANDOM",) * 4),
    (
        "extended-barriers-6p",
        6,
        6,
        RuleSet(capture_mode=CaptureMode.MANDATORY_EXTENDED, barriers=True),
        ("SPREAD", "RANDOM", "FOCUS_FRONT", "FOCUS_REAR", "GREEDY_CAPTURE", "RANDOM"),
    ),
    (
        "strict-dreimal-4p",
        4,
        4,
        RuleSet(
            cold_start=ColdStart.STRICT,
            dreimal_wuerfeln=True,
            bonus_roll_after_quick_entry=True,
        ),
        ("SPREAD",) * 4,
    ),
    (
        "free-nojump-3p",
        4,
        3,
        RuleSet(cold_start=ColdStart.FREE_ENTRY, goal_no_jump=True),
        ("FOCUS_FRONT", "FOCUS_REAR", "GREEDY_CAPTURE"),
    ),
    (
        "mandatory-forfeited-2p",
        4,
        2,
        RuleSet(capture_mode=CaptureMode.MANDATORY, bonus_roll_forfeited=True),
        ("GREEDY_CAPTURE", "SPREAD"),
    ),
]


@pytest.mark.parametrize(
    ("name", "seats", "players", "rules", "agents"), CASES, ids=[c[0] for c in CASES]
)
def test_every_summary_field_is_reproduced_from_the_event_log(
    name, seats, players, rules, agents
):
    spec = GameSpec(
        cell_key=f"ak9/{name}",
        seats=seats,
        players=players,
        seat_pattern=SeatPattern.ADJACENT,
        rules=rules,
        agent_ids=agents,
        master_seed=31337,
    )
    for index in range(12):
        run = play_indexed_game(spec, index)
        reference = derive_from_events(run.header, run.events)
        for field in CROSS_CHECKED:
            assert reference[field] == getattr(run.summary, field), (
                f"{name} game {index}: {field}\n"
                f"  loop      {getattr(run.summary, field)}\n"
                f"  reference {reference[field]}"
            )


def test_cross_checked_covers_everything_the_walker_derives():
    """The coverage list must not be maintainable by hand.

    ``CROSS_CHECKED`` used to be a hand-written tuple, and every §6.2 field
    added after it was written escaped AK-9 in silence — which is how
    ``winner_rank_at_50`` came to be named in the module docstring as the
    exact metric AK-9 exists to protect while not being checked at all
    (D-75). This asserts the list is complete, so the next field cannot
    repeat it: anything the walker derives that is also a summary field has
    to be compared.
    """
    from madnlab.analysis.reference import derive_from_events as _derive
    from madnlab.eventlog.writer import SummaryRow

    spec = GameSpec(
        cell_key="ak9/coverage",
        seats=4,
        players=4,
        seat_pattern=SeatPattern.ADJACENT,
        rules=RuleSet(barriers=True),
        agent_ids=("RANDOM",) * 4,
        master_seed=4242,
    )
    run = play_indexed_game(spec, 0)
    derived = set(_derive(run.header, run.events))
    summary_fields = set(SummaryRow._fields)
    must_check = derived & summary_fields
    missing = must_check - set(CROSS_CHECKED)
    assert not missing, (
        f"the walker derives {sorted(missing)} and the summary row carries "
        f"them, but AK-9 does not compare them"
    )


def test_the_reference_reconstructs_the_final_board():
    """Stronger than the counters: the whole position vector must match.

    A counter can agree by luck; sixteen positions reconstructed from moves and
    captures cannot.
    """
    spec = GameSpec(
        cell_key="ak9/positions",
        seats=6,
        players=6,
        seat_pattern=SeatPattern.ADJACENT,
        rules=RuleSet(capture_mode=CaptureMode.MANDATORY_EXTENDED, barriers=True),
        agent_ids=("SPREAD", "RANDOM", "FOCUS_FRONT", "FOCUS_REAR", "GREEDY_CAPTURE", "RANDOM"),
        master_seed=8080,
    )
    for index in range(8):
        run = play_indexed_game(spec, index)
        reference = derive_from_events(run.header, run.events)
        finished = set(run.summary.ranks[: len(run.summary.ranks) - 1])
        board_ring = 48
        for seat in finished:
            positions = reference["final_positions"][seat * 4 : seat * 4 + 4]
            assert all(pos > board_ring for pos in positions), (
                f"seat {seat} is recorded as finished but the reconstructed "
                f"board has it at {positions}"
            )


def test_pass_events_are_per_roll_but_passes_are_per_turn():
    """D-71, which AK-9 found by disagreeing.

    §4.1 emits one ``pass`` event per unusable roll; §6.2 counts turns with no
    legal move. A turn of three attempts that never moves is one pass and three
    events, so counting events over-reports by the number of extra rolls.
    """
    from madnlab.eventlog.events import PassEvent, RollEvent

    spec = GameSpec(
        cell_key="ak9/passes",
        seats=4,
        players=4,
        seat_pattern=SeatPattern.ADJACENT,
        rules=RuleSet(cold_start=ColdStart.STRICT, dreimal_wuerfeln=True),
        agent_ids=("RANDOM",) * 4,
        master_seed=606,
    )
    multi_roll_pass_turns = 0
    for index in range(20):
        run = play_indexed_game(spec, index)
        event_passes = sum(1 for e in run.events if isinstance(e, PassEvent))
        turn_passes = sum(run.summary.passes_by_seat)
        assert event_passes >= turn_passes
        if event_passes > turn_passes:
            multi_roll_pass_turns += 1
        assert derive_from_events(run.header, run.events)["passes_by_seat"] == (
            run.summary.passes_by_seat
        )
        assert any(isinstance(e, RollEvent) and e.attempt > 1 for e in run.events)
    assert multi_roll_pass_turns > 0, (
        "no game exercised a multi-roll pass turn, so this test proves nothing"
    )

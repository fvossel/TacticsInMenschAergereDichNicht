"""AK-3 — the replay validator.

At least 1,000 seed-random games across mixed configurations, re-simulated from their headers
with exact event-stream equality.

The validator is given the header and nothing else, which is what §4.3 claims. The corpus covers
the arms where the runner resolves a value rather than deriving it (the drawn starting seat) and
where the engine carries state the header does not name (the extra laps of
``mandatory_extended``).
"""

from __future__ import annotations

import random

import pytest

from madnlab import ENGINE_VERSION
from madnlab.engine.geometry import SeatPattern
from madnlab.engine.rules import CaptureMode, ColdStart, RuleSet
from madnlab.eventlog.events import MoveEvent
from madnlab.eventlog.replay import VersionSkewError, compare, replay, validate
from madnlab.run.game import GameSpec, play_indexed_game

AGENT_IDS = ("RANDOM", "SPREAD", "FOCUS_FRONT", "FOCUS_REAR", "GREEDY_CAPTURE")

#: Corpus size AK-3 requires, split across the configurations below.
AK3_GAMES = 1000


def _random_spec(rng: random.Random, index: int) -> GameSpec:
    seats = rng.choice([4, 6])
    players = rng.randint(2, seats)
    pattern = SeatPattern.ADJACENT
    if players == 2 and rng.random() < 0.4:
        pattern = SeatPattern.OPPOSITE
    elif seats % players == 0 and rng.random() < 0.4:
        pattern = SeatPattern.SPREAD
    rules = RuleSet(
        cold_start=rng.choice(list(ColdStart)),
        capture_mode=rng.choice(list(CaptureMode)),
        barriers=rng.random() < 0.5,
        goal_no_jump=rng.random() < 0.5,
        dreimal_wuerfeln=rng.random() < 0.5,
    )
    if rules.dreimal_wuerfeln and rng.random() < 0.5:
        rules = rules._replace(bonus_roll_after_quick_entry=True)
    if rng.random() < 0.3:
        rules = rules._replace(bonus_roll_forfeited=True)
    return GameSpec(
        cell_key=f"ak3/{seats}s{players}p/{index}",
        seats=seats,
        players=players,
        seat_pattern=pattern,
        rules=rules,
        agent_ids=tuple(rng.choice(AGENT_IDS) for _ in range(players)),
        master_seed=rng.getrandbits(48),
    )


def test_replay_reproduces_a_thousand_games_across_mixed_configs():
    rng = random.Random(20260801)
    checked = 0
    for index in range(AK3_GAMES // 4):
        spec = _random_spec(rng, index)
        for game_index in range(4):
            run = play_indexed_game(spec, game_index)
            mismatch = validate(run.header, run.events)
            assert mismatch is None, (
                f"{spec.cell_key} game {game_index}\n"
                f"rules={spec.rules}\nagents={spec.agent_ids}\n"
                + (mismatch.describe() if mismatch else "")
            )
            checked += 1
    assert checked >= AK3_GAMES


def test_replay_needs_only_the_header():
    """§4.3: the header alone reproduces the event stream, with no side channel from the runner."""
    spec = GameSpec(
        cell_key="ak3/header-only",
        seats=6,
        players=4,
        seat_pattern=SeatPattern.ADJACENT,
        rules=RuleSet(capture_mode=CaptureMode.MANDATORY_EXTENDED, barriers=True),
        agent_ids=("SPREAD", "RANDOM", "FOCUS_REAR", "GREEDY_CAPTURE"),
        master_seed=4711,
    )
    run = play_indexed_game(spec, 3)
    assert replay(run.header) == run.events


def test_the_drawn_starting_seat_is_reproduced_not_redrawn():
    """The one value the runner resolves rather than derives (§9 D-6)."""
    spec = GameSpec(
        cell_key="ak3/start",
        seats=4,
        players=4,
        seat_pattern=SeatPattern.ADJACENT,
        rules=RuleSet(),
        agent_ids=("RANDOM",) * 4,
        master_seed=13,
    )
    starts = {play_indexed_game(spec, i).header.starting_seat for i in range(40)}
    assert len(starts) > 1, "the draw must actually vary, or this proves nothing"
    for index in range(40):
        run = play_indexed_game(spec, index)
        assert replay(run.header)[0] == run.events[0]
        assert validate(run.header, run.events) is None


def test_mismatch_reporting_actually_reports_the_position():
    """A mismatch names the position at which the two streams diverge.

    ``describe()`` renders the text a failing AK-3 run prints, so the assertions read that text
    rather than the fields: the position has to appear as a number, not as a bound-method repr,
    and the stream that has already ended has to render as ``<end>``.
    """
    spec = GameSpec(
        cell_key="ak3/mismatch", seats=4, players=2, seat_pattern=SeatPattern.OPPOSITE,
        rules=RuleSet(), agent_ids=("RANDOM", "SPREAD"), master_seed=2,
    )
    run = play_indexed_game(spec, 0)
    truncated = run.events[:-1]
    mismatch = compare(run.events, truncated)
    assert mismatch is not None
    assert mismatch.at == len(truncated)
    text = mismatch.describe()
    assert f"event {len(truncated)} differs" in text
    assert "method" not in text and "<end>" in text
    assert compare(run.events, run.events) is None


def test_version_skew_is_refused_rather_than_reported_as_a_mismatch():
    """D-33: a cross-version replay raises rather than being reported as an event mismatch."""
    spec = GameSpec(
        cell_key="ak3/skew", seats=4, players=2, seat_pattern=SeatPattern.OPPOSITE,
        rules=RuleSet(), agent_ids=("RANDOM", "SPREAD"), master_seed=1,
    )
    run = play_indexed_game(spec, 0)
    with pytest.raises(VersionSkewError, match="engine"):
        replay(run.header._replace(engine_version="0.0.0-other"))
    with pytest.raises(VersionSkewError, match="schema"):
        replay(run.header._replace(schema_version="99"))
    assert run.header.engine_version == ENGINE_VERSION


def test_the_offered_legal_set_and_chosen_index_agree(request):
    """§4.1: the log lets AK-5 be audited without re-simulating."""
    spec = GameSpec(
        cell_key="ak3/offered", seats=4, players=4, seat_pattern=SeatPattern.ADJACENT,
        rules=RuleSet(capture_mode=CaptureMode.MANDATORY, barriers=True),
        agent_ids=("GREEDY_CAPTURE", "RANDOM", "SPREAD", "FOCUS_FRONT"), master_seed=555,
    )
    seen = 0
    for index in range(20):
        for event in play_indexed_game(spec, index).events:
            if isinstance(event, MoveEvent):
                assert 0 <= event.chosen < len(event.legal)
                piece, from_pos, to_pos, kind, _captures = event.legal[event.chosen]
                assert (piece, from_pos, to_pos, kind) == (
                    event.piece, event.from_pos, event.to_pos, event.kind,
                )
                seen += 1
    assert seen > 500

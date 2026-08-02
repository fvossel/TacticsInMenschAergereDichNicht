"""AK-1 — rule conformance from hand-crafted scenarios.

One test per clause of requirements §11's AK-1 list, plus nine scenarios §11 does not name.
Each test cites the clause or ledger row it pins.
"""

from __future__ import annotations

import pytest

from madnlab.engine.geometry import SeatPattern, board_for, occupied_seats
from madnlab.engine.moves import MoveKind, legal_moves, legal_moves_with_restriction
from madnlab.engine.rules import (
    BASELINE,
    CaptureMode,
    ColdStart,
    InadmissibleRuleSetError,
    RuleSet,
)
from madnlab.engine.state import initial_state
from tests.conftest import FREE, STRICT, pos_on_field, state_for, targets

MANDATORY = RuleSet(cold_start=ColdStart.STRICT, capture_mode=CaptureMode.MANDATORY)
EXTENDED = RuleSet(
    cold_start=ColdStart.STRICT, capture_mode=CaptureMode.MANDATORY_EXTENDED
)
NO_JUMP = RuleSet(cold_start=ColdStart.STRICT, goal_no_jump=True)
BARRIERS = RuleSet(cold_start=ColdStart.STRICT, barriers=True)


# -- GM-3.2 setup, and the cold_start axis (§11 "all four cold_start cases") --


def test_baseline_setup_is_one_piece_out(b4):
    """GM-3.2 / D-55: one piece on the entry field, three in the yard."""
    seats = occupied_seats(4, 4, SeatPattern.ADJACENT)
    state = initial_state(b4, seats, BASELINE)
    for seat in seats:
        assert state.seat_positions(seat) == (1, 0, 0, 0)


@pytest.mark.parametrize(
    ("cold_start", "expected"),
    [(ColdStart.STRICT, (0, 0, 0, 0)), (ColdStart.FREE_ENTRY, (0, 0, 0, 0))],
)
def test_non_baseline_cold_starts_begin_in_the_yard(b4, cold_start, expected):
    seats = occupied_seats(4, 4, SeatPattern.ADJACENT)
    state = initial_state(b4, seats, RuleSet(cold_start=cold_start))
    assert state.seat_positions(0) == expected


def test_strict_needs_a_six_to_enter(b4):
    """GM-3.5 under ``strict``."""
    state = state_for(b4)
    assert legal_moves(b4, state, 0, 3, STRICT) == ()
    moves, restriction = legal_moves_with_restriction(b4, state, 0, 6, STRICT)
    assert restriction is restriction.FORCED_ENTRY
    assert [m.kind for m in moves] == [MoveKind.ENTER]


def test_free_entry_is_an_ordinary_never_forced_move(b4):
    """D-7: any value enters, entering is never forced, clearing still applies."""
    moves, restriction = legal_moves_with_restriction(b4, state_for(b4), 0, 3, FREE)
    assert restriction is restriction.NONE
    assert [m.kind for m in moves] == [MoveKind.ENTER]

    # Clearing still applies under free_entry.
    moves, restriction = legal_moves_with_restriction(
        b4, state_for(b4, s0=(1, 0, 0, 0)), 0, 3, FREE
    )
    assert restriction is restriction.CLEARING
    assert all(m.piece == 0 for m in moves)


def test_free_entry_makes_both_entry_axes_inert():
    """D-13: the collapse that turns 216 admissible EX-4 cells into 168."""
    assert FREE.entry_axes_are_inert
    assert RuleSet(cold_start=ColdStart.FREE_ENTRY, dreimal_wuerfeln=True).entry_attempts == 1
    assert RuleSet(dreimal_wuerfeln=True).entry_attempts == 3
    assert RuleSet().entry_attempts == 1


def test_bonus_roll_requires_the_three_attempts_variant():
    """GM-4 nesting; the validator names the error rather than coercing."""
    with pytest.raises(InadmissibleRuleSetError, match="dreimal_wuerfeln"):
        RuleSet(bonus_roll_after_quick_entry=True).validate()
    RuleSet(bonus_roll_after_quick_entry=True, dreimal_wuerfeln=True).validate()


# -- GM-3.4 / GM-3.5 / GM-5.1: the priority lattice ---------------------------


def test_clearing_is_forced_from_turn_one_under_the_baseline(b4):
    """GM-3.4 + D-55: with a piece already on the entry field, clearing binds from turn one."""
    seats = occupied_seats(4, 4, SeatPattern.ADJACENT)
    state = initial_state(b4, seats, BASELINE)
    for roll in range(1, 7):
        moves, restriction = legal_moves_with_restriction(b4, state, 0, roll, BASELINE)
        assert restriction is restriction.CLEARING
        assert all(m.piece == 0 for m in moves)


def test_forced_entry_outranks_mandatory_capture(b4):
    """D-9: clearing > forced entry > mandatory capture.

    A 6 is rolled, a yard piece is available, and a capture is available elsewhere. The 6 goes
    to entry and the capture is not forced.
    """
    # seat 0 piece 1 on pos 5; seat 1 piece 0 where seat 0's pos 5+6=11 lands.
    victim = pos_on_field(b4, 1, b4.ring_field(0, 11))

    # Precondition against a vacuous pass: the capture really is on the table for this piece and
    # roll. It has to be checked on a state *without* a yard piece — with one, GM-3.5's forced
    # entry already narrows the set even at capture_mode=optional, which is the interaction
    # under test.
    no_yard = state_for(b4, s0=(20, 5, 21, 22), s1=(victim,))
    assert any(m.captures == 4 for m in legal_moves(b4, no_yard, 0, 6, STRICT))

    state = state_for(b4, s0=(0, 5, 0, 0), s1=(victim,))
    moves, restriction = legal_moves_with_restriction(b4, state, 0, 6, MANDATORY)
    assert restriction is restriction.FORCED_ENTRY
    assert [m.kind for m in moves] == [MoveKind.ENTER]


def test_clearing_outranks_mandatory_capture(b4):
    """D-9 / §2.5: the capture restriction does not apply inside clearing."""
    victim = pos_on_field(b4, 1, b4.ring_field(0, 4))
    state = state_for(b4, s0=(1, 0, 0, 7), s1=(victim,))
    assert any(m.captures == 4 for m in legal_moves(b4, state, 0, 3, STRICT))
    moves, restriction = legal_moves_with_restriction(b4, state, 0, 3, MANDATORY)
    assert restriction is restriction.CLEARING
    assert all(m.piece == 0 for m in moves)


def test_mandatory_capture_narrows_the_legal_set(b4):
    """GM-5: with a capture available the set is exactly the capturing moves."""
    victim_pos = pos_on_field(b4, 1, b4.ring_field(0, 8))
    state = state_for(b4, s0=(5, 20, 0, 0), s1=(victim_pos,))
    optional = legal_moves(b4, state, 0, 3, STRICT)
    assert len(optional) == 2

    moves, restriction = legal_moves_with_restriction(b4, state, 0, 3, MANDATORY)
    assert restriction is restriction.CAPTURE
    assert len(moves) == 1 and moves[0].captures == 4


# -- GM-3.8 / goal column -----------------------------------------------------


@pytest.mark.parametrize(
    ("roll", "expected"), [(1, [41]), (2, [42]), (3, [43]), (4, [44]), (5, []), (6, [])]
)
def test_goal_entry_requires_a_fitting_roll(b4, roll, expected):
    """GM-3.8, verified official: entry into the goal needs an exact fit."""
    state = state_for(b4, s0=(40,))
    assert targets(legal_moves(b4, state, 0, roll, STRICT), piece=0) == expected


def test_no_overshoot_inside_the_goal_column(b4):
    """D-54, project choice: no bounce-back — an overshooting move is not generated."""
    state = state_for(b4, s0=(43, 44))
    assert targets(legal_moves(b4, state, 0, 1, STRICT), piece=0) == []
    assert targets(legal_moves(b4, state, 0, 2, STRICT), piece=0) == []


def test_goal_jumping_is_allowed_by_default_and_forbidden_by_the_flag(b4):
    """GM-3.8 baseline vs. the ``goal_no_jump`` variant."""
    state = state_for(b4, s0=(40, 41))
    assert targets(legal_moves(b4, state, 0, 3, STRICT), piece=0) == [43]
    assert targets(legal_moves(b4, state, 0, 3, NO_JUMP), piece=0) == []


def test_goal_no_jump_last_piece_enters_on_the_first_field(b4):
    """D-53: the variant's second sentence follows from the no-jump rule.

    With three pieces home on the deeper indices, the last one can only enter on the first goal
    field — every deeper field is occupied and every longer path crosses one.
    """
    state = state_for(b4, s0=(40, 42, 43, 44))
    assert targets(legal_moves(b4, state, 0, 1, NO_JUMP), piece=0) == [41]
    for roll in (2, 3, 4):
        assert targets(legal_moves(b4, state, 0, roll, NO_JUMP), piece=0) == []


def test_goal_column_is_single_occupancy(b4):
    """GM-3.7 / D-34: the target goal field must be free in either variant."""
    state = state_for(b4, s0=(40, 42))
    for rules in (STRICT, NO_JUMP):
        assert targets(legal_moves(b4, state, 0, 2, rules), piece=0) == []


# -- GM-6 barriers ------------------------------------------------------------


def test_barrier_forms_only_with_the_flag(b4):
    """GM-6.1 vs. GM-3.6's no-stacking clause."""
    state = state_for(b4, s0=(5, 8))
    assert targets(legal_moves(b4, state, 0, 3, STRICT), piece=0) == []
    assert targets(legal_moves(b4, state, 0, 3, BARRIERS), piece=0) == [8]


def test_barrier_blocks_landing_and_passing(b4):
    """GM-6.2, for the owner's third piece and for opponents alike."""
    blocked_at = pos_on_field(b4, 1, b4.ring_field(0, 5))
    state = state_for(b4, s0=(5, 5, 2), s1=(blocked_at - 4,))
    assert b4.ring_field(1, blocked_at) == b4.ring_field(0, 5)
    assert targets(legal_moves(b4, state, 1, 4, BARRIERS), piece=4) == []  # land
    assert targets(legal_moves(b4, state, 1, 6, BARRIERS), piece=4) == []  # pass
    assert targets(legal_moves(b4, state, 1, 3, BARRIERS), piece=4) == [blocked_at - 1]
    assert targets(legal_moves(b4, state, 0, 3, BARRIERS), piece=2) == []  # own third


def test_barrier_pieces_cannot_be_captured(b4):
    """GM-6.3, which falls out of the two-occupant landing rule.

    Stated as a differential against the single-piece case: with one opponent piece on the field
    the move is a capture, with two it does not exist at all. A bare "no capturing move"
    assertion passes vacuously whenever the mover has no move either.
    """
    target = pos_on_field(b4, 1, b4.ring_field(0, 5))
    single = state_for(b4, s0=(2,), s1=(target,))
    assert [m.captures for m in legal_moves(b4, single, 0, 3, BARRIERS)] == [4]

    barrier = state_for(b4, s0=(2,), s1=(target, target))
    assert legal_moves(b4, barrier, 0, 3, BARRIERS) == ()


def test_barrier_must_be_broken_under_compulsion(b4):
    """GM-6.4: no extra rule needed, it falls out of compulsory moving."""
    state = state_for(b4, s0=(5, 5))
    moves = legal_moves(b4, state, 0, 3, BARRIERS)
    assert len(moves) == 1 and moves[0].from_pos == 5


def test_barrier_on_the_own_entry_field_does_not_suspend_clearing(b4):
    """D-4(a)."""
    state = state_for(b4, s0=(1, 1, 0, 20))
    moves, restriction = legal_moves_with_restriction(b4, state, 0, 3, BARRIERS)
    assert restriction is restriction.CLEARING
    assert len(moves) == 1 and moves[0].from_pos == 1


# -- GM-5 mandatory_extended --------------------------------------------------


def test_extended_capture_forces_an_extra_lap(b4):
    """GM-5: the move past the own goal entry exists only when it captures."""
    state = state_for(b4, s0=(39,), s1=(32,))
    assert targets(legal_moves(b4, state, 0, 3, STRICT), piece=0) == [42]

    moves, restriction = legal_moves_with_restriction(b4, state, 0, 3, EXTENDED)
    assert restriction is restriction.CAPTURE
    assert len(moves) == 1
    assert moves[0].extra_lap and moves[0].to_pos == 2


def test_extended_lap_is_not_generated_without_a_capture(b4):
    state = state_for(b4, s0=(39,))
    moves = legal_moves(b4, state, 0, 3, EXTENDED)
    assert not any(m.extra_lap for m in moves)


def test_extended_lap_path_scan_crosses_the_ring_wrap(b4):
    """GM-6.2 on the extended lap: the barrier scan follows the move across pos == R."""
    extended_barriers = RuleSet(
        cold_start=ColdStart.STRICT,
        capture_mode=CaptureMode.MANDATORY_EXTENDED,
        barriers=True,
    )
    # An opponent barrier sits on seat 0's lap position 1, between origin and
    # the capture target on lap position 2.
    blocker = pos_on_field(b4, 1, b4.ring_field(0, 1))
    blocked = state_for(b4, s0=(39,), s1=(32, blocker, blocker))
    assert not any(m.extra_lap for m in legal_moves(b4, blocked, 0, 3, extended_barriers))

    clear = state_for(b4, s0=(39,), s1=(32,))
    assert any(m.extra_lap for m in legal_moves(b4, clear, 0, 3, extended_barriers))


# -- D-60 / D-61: no behavioural duplicates in the legal set ------------------


@pytest.mark.parametrize("yard_pieces", [1, 2, 3, 4])
def test_exactly_one_entry_move_regardless_of_yard_count(b4, yard_pieces):
    """D-60: yard pieces are interchangeable, so entry contributes one move, not one per piece."""
    on_ring = [20 + i for i in range(4 - yard_pieces)]
    state = state_for(b4, s0=tuple(on_ring) + (0,) * yard_pieces)
    moves = legal_moves(b4, state, 0, 6, RuleSet(cold_start=ColdStart.STRICT))
    assert sum(1 for m in moves if m.kind is MoveKind.ENTER) == 1


def test_barrier_does_not_duplicate_ring_moves(b4):
    """D-61: the two pieces of a barrier are interchangeable and yield a single ring move."""
    state = state_for(b4, s0=(5, 5, 20, 30))
    moves = legal_moves(b4, state, 0, 3, BARRIERS)
    assert len(moves) == 3
    assert len({(m.from_pos, m.to_pos, m.kind, m.captures, m.extra_lap) for m in moves}) == 3
    assert min(m.piece for m in moves if m.from_pos == 5) == 0


def test_barrier_does_not_duplicate_goal_entry_or_extra_lap(b4):
    """D-61 across the other two generating branches."""
    goal = legal_moves(b4, state_for(b4, s0=(38, 38, 20, 30)), 0, 4, BARRIERS)
    assert sum(1 for m in goal if m.kind is MoveKind.GOAL_ENTER) == 1

    extended_barriers = RuleSet(
        cold_start=ColdStart.STRICT,
        capture_mode=CaptureMode.MANDATORY_EXTENDED,
        barriers=True,
    )
    lap = legal_moves(b4, state_for(b4, s0=(39, 39), s1=(32,)), 0, 3, extended_barriers)
    assert sum(1 for m in lap if m.extra_lap) == 1


def test_forced_sets_inherit_the_deduplication(b4):
    """D-61: the clearing and capture filters preserve the deduplication of the full set."""
    clearing, restriction = legal_moves_with_restriction(
        b4, state_for(b4, s0=(1, 1, 0, 20)), 0, 3, BARRIERS
    )
    assert restriction is restriction.CLEARING and len(clearing) == 1

    mandatory_barriers = RuleSet(
        cold_start=ColdStart.STRICT, barriers=True, capture_mode=CaptureMode.MANDATORY
    )
    victim_pos = pos_on_field(b4, 1, b4.ring_field(0, 15))
    capture, restriction = legal_moves_with_restriction(
        b4, state_for(b4, s0=(12, 12), s1=(victim_pos,)), 0, 3, mandatory_barriers
    )
    assert restriction is restriction.CAPTURE and len(capture) == 1


# -- domain guards (D-62, D-63) ----------------------------------------------


@pytest.mark.parametrize("roll", [-2, 0, 7, 12])
def test_roll_outside_the_die_is_rejected(b4, roll):
    with pytest.raises(ValueError, match="d6"):
        legal_moves(b4, state_for(b4), 0, roll, STRICT)


@pytest.mark.parametrize("seat", [-1, 4, 9])
def test_seat_outside_the_board_is_rejected(b4, seat):
    with pytest.raises(ValueError, match="out of range"):
        legal_moves(b4, state_for(b4), seat, 3, STRICT)


def test_no_goal_move_can_land_back_on_the_ring(b4):
    """D-62: a goal move always ends past the ring, never back on it."""
    state = state_for(b4, s0=(41, 0, 0, 0))
    for roll in range(1, 7):
        for move in legal_moves(b4, state, 0, roll, STRICT):
            if move.kind is MoveKind.GOAL:
                assert move.to_pos > b4.ring_length


# -- geometry (GM-1) ---------------------------------------------------------


@pytest.mark.parametrize("seats", [4, 6])
def test_goal_entry_field_is_the_field_at_the_last_ring_position(seats):
    board = board_for(seats)
    for seat in range(seats):
        assert board.goal_entry_field(seat) == board.ring_field(seat, board.ring_length)


@pytest.mark.parametrize(("seats", "expected"), [(4, 170), (6, 202)])
def test_max_progress_per_seat(seats, expected):
    assert board_for(seats).max_progress_per_seat == expected


def test_entry_fields_are_distinct_and_evenly_spaced():
    for seats in (4, 6):
        board = board_for(seats)
        fields = [board.entry_field(s) for s in range(seats)]
        assert len(set(fields)) == seats
        assert board.spacing * seats == board.ring_length


def test_spread_and_opposite_seat_tuples():
    """D-65 pins the tuple that goes into every cell key."""
    assert occupied_seats(6, 3, SeatPattern.SPREAD) == (0, 2, 4)
    assert occupied_seats(6, 2, SeatPattern.SPREAD) == (0, 3)
    assert occupied_seats(4, 2, SeatPattern.SPREAD) == (0, 2)
    assert occupied_seats(4, 3, SeatPattern.ADJACENT) == (0, 1, 2)
    assert occupied_seats(4, 2, SeatPattern.OPPOSITE) == (0, 2)
    with pytest.raises(ValueError, match="divide"):
        occupied_seats(4, 3, SeatPattern.SPREAD)


def test_player_count_bounds_cite_the_clause_that_fired():
    """D-66: each bound carries its own message."""
    with pytest.raises(ValueError, match="do not fit"):
        occupied_seats(4, 5, SeatPattern.ADJACENT)
    with pytest.raises(ValueError, match="below the measured range"):
        occupied_seats(4, 1, SeatPattern.ADJACENT)

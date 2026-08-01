"""AK-1 property sweeps — invariants that must hold in every arm.

Scenario tests pin the clause they were written for. These pin properties that
have to survive every rule combination, which is where the class of bug D-61
belongs: it produced no wrong *move*, only a wrong *multiplicity*, so no
per-clause assertion could have caught it.
"""

from __future__ import annotations

import random
from collections import Counter

import pytest

from madnlab.engine.geometry import PIECES_PER_SEAT, Board, board_for
from madnlab.engine.moves import legal_moves, legal_moves_with_restriction
from madnlab.engine.rules import CaptureMode, ColdStart, RuleSet
from madnlab.engine.state import GameState

#: Every combination of the axes that can affect legality. The entry-phase
#: axes (``dreimal_wuerfeln``, ``bonus_roll_*``) belong to the turn structure,
#: not to the legal-move set, so they are not swept here.
ARMS = [
    RuleSet(cold_start=cs, capture_mode=cm, barriers=b, goal_no_jump=g)
    for cs in ColdStart
    for cm in CaptureMode
    for b in (False, True)
    for g in (False, True)
]


def _reachable_state(board: Board, rng: random.Random) -> GameState:
    """A random state respecting the invariants a real game maintains.

    Goal columns hold at most one piece per field (D-34) and no more than two
    pieces share a ring field, which is the most a barrier can hold (GM-6.1).
    """
    n = board.seats * PIECES_PER_SEAT
    positions = [0] * n
    for i in range(n):
        draw = rng.random()
        if draw < 0.30:
            positions[i] = 0
        elif draw < 0.92:
            positions[i] = rng.randint(1, board.ring_length)
        else:
            positions[i] = board.ring_length + rng.randint(1, 4)

    for seat in range(board.seats):
        base = seat * PIECES_PER_SEAT
        slice_ = positions[base : base + PIECES_PER_SEAT]
        goal_seen: set[int] = set()
        for offset, pos in enumerate(slice_):
            if pos > board.ring_length:
                if pos in goal_seen:
                    positions[base + offset] = 0
                else:
                    goal_seen.add(pos)
        counts = Counter(
            pos for pos in positions[base : base + PIECES_PER_SEAT]
            if 1 <= pos <= board.ring_length
        )
        for pos, count in counts.items():
            if count > 2:
                extra = [
                    base + offset
                    for offset in range(PIECES_PER_SEAT)
                    if positions[base + offset] == pos
                ][2:]
                for index in extra:
                    positions[index] = 0
    return GameState(positions=tuple(positions))


def _successor_key(state: GameState, seat: int, move) -> tuple[int, ...]:
    """The moving seat's own position multiset after ``move``.

    Two moves that produce the same key are the same decision as far as the
    engine and §6 can observe: progress is a sum, and the ranking key is a
    function of position, so a transposition of two of a seat's own slots is
    invisible everywhere.
    """
    positions = list(state.positions)
    positions[move.piece] = move.to_pos
    if move.captures is not None:
        positions[move.captures] = 0
    base = seat * PIECES_PER_SEAT
    return tuple(sorted(positions[base : base + PIECES_PER_SEAT]))


@pytest.mark.parametrize("seats", [4, 6])
def test_every_legal_move_leads_to_a_distinct_successor(seats):
    """D-61, stated as the invariant rather than as the rule.

    Checkable in every arm rather than only under barriers, so it guards
    against the next variant of the bug rather than the one already fixed.
    """
    board = board_for(seats)
    rng = random.Random(20260801 + seats)
    checked = 0
    for _ in range(3000):
        state = _reachable_state(board, rng)
        rules = ARMS[rng.randrange(len(ARMS))]
        seat = rng.randrange(board.seats)
        roll = rng.randint(1, 6)
        moves = legal_moves(board, state, seat, roll, rules)
        keys = [_successor_key(state, seat, m) for m in moves]
        assert len(keys) == len(set(keys)), (
            f"duplicate successor: seats={seats} seat={seat} roll={roll} "
            f"rules={rules} positions={state.positions}"
        )
        checked += 1
    assert checked == 3000


@pytest.mark.parametrize("seats", [4, 6])
def test_legal_moves_is_total_and_pure(seats):
    """§3.1 / GM-7: never raises in the domain, never mutates its arguments."""
    board = board_for(seats)
    rng = random.Random(4242 + seats)
    for _ in range(2000):
        state = _reachable_state(board, rng)
        rules = ARMS[rng.randrange(len(ARMS))]
        seat = rng.randrange(board.seats)
        roll = rng.randint(1, 6)
        before = state.positions
        moves = legal_moves(board, state, seat, roll, rules)
        assert isinstance(moves, tuple)
        assert state.positions == before
        for move in moves:
            assert move.piece // PIECES_PER_SEAT == seat
            assert 0 <= move.to_pos <= board.max_progress_per_piece
            if move.captures is not None:
                assert move.captures // PIECES_PER_SEAT != seat


@pytest.mark.parametrize("seats", [4, 6])
def test_canonical_order_is_deterministic_and_goal_first(seats):
    """D-3, and NF-1's requirement that the order depend on inputs only."""
    board = board_for(seats)
    rng = random.Random(99 + seats)
    for _ in range(1500):
        state = _reachable_state(board, rng)
        rules = ARMS[rng.randrange(len(ARMS))]
        seat = rng.randrange(board.seats)
        roll = rng.randint(1, 6)
        first = legal_moves(board, state, seat, roll, rules)
        assert first == legal_moves(board, state, seat, roll, rules)
        groups = [0 if m.to_pos > board.ring_length else 1 for m in first]
        assert groups == sorted(groups), "goal moves must precede ring moves"
        keys = [
            (0 if m.to_pos > board.ring_length else 1, m.piece, m.to_pos) for m in first
        ]
        assert keys == sorted(keys)


@pytest.mark.parametrize("seats", [4, 6])
def test_forcing_never_widens_the_legal_set(seats):
    """GM-5.1: each lattice clause is a filter, so it can only narrow.

    Compared against ``capture_mode = optional`` with the other axes held
    fixed, which is the only comparison where the candidate sets coincide —
    ``mandatory_extended`` generates the extra-lap move that ``optional`` does
    not, so it is excluded here and covered by its own scenario test.
    """
    board = board_for(seats)
    rng = random.Random(7 + seats)
    for _ in range(2000):
        state = _reachable_state(board, rng)
        base = RuleSet(
            cold_start=ColdStart(rng.choice(list(ColdStart))),
            barriers=rng.random() < 0.5,
            goal_no_jump=rng.random() < 0.5,
        )
        seat = rng.randrange(board.seats)
        roll = rng.randint(1, 6)
        optional = set(legal_moves(board, state, seat, roll, base))
        forced, restriction = legal_moves_with_restriction(
            board, state, seat, roll, base._replace(capture_mode=CaptureMode.MANDATORY)
        )
        assert set(forced) <= optional
        if restriction is restriction.CAPTURE:
            assert forced and all(m.captures is not None for m in forced)

"""The five v1 agent policies (§3.2).

Every agent is a pure function that returns an element of ``legal``. None of
them re-implements any part of legality: the choice set comes from
:func:`madnlab.engine.moves.legal_moves` and nothing else (GM-7).

Signature
---------
§3.1 writes the contract as ``choose(state, roll, legal, rng)``. The
implementation adds ``board`` and ``seat``, which the ranking key needs and
which the shorthand elides; the properties §3.1 actually requires — pure,
total, and deterministic given ``(state, roll, agent seed)`` — are unchanged
(D-67).

Draw discipline
---------------
Every agent consumes **exactly one** draw from its stream per decision,
including when ``len(legal) == 1`` and including the deterministic policies
that ignore the value (D-37). Without this a later short-circuit optimization
would desynchronize a seat's stream and silently invalidate published logs
while AK-2 still passed.
"""

from __future__ import annotations

import random
from collections.abc import Callable, Sequence

from madnlab.engine.geometry import Board, PieceLocation
from madnlab.engine.moves import Move, MoveKind
from madnlab.engine.state import GameState

#: The agent contract (§3.1, D-67).
Agent = Callable[[Board, GameState, int, int, Sequence[Move], random.Random], Move]


def _track_rank(board: Board, state: GameState, move: Move) -> int | None:
    """Ranking key for ``move``'s piece: progress restricted to the ring.

    ``None`` for a piece in the yard or in the goal column, which D-43a
    excludes from the ranking entirely.
    """
    pos = state.positions[move.piece]
    return pos if board.location(pos) is PieceLocation.RING else None


def _entry_move(legal: Sequence[Move]) -> Move | None:
    for move in legal:
        if move.kind is MoveKind.ENTER:
            return move
    return None


def random_agent(
    board: Board,
    state: GameState,
    seat: int,
    roll: int,
    legal: Sequence[Move],
    rng: random.Random,
) -> Move:
    """Uniform choice over ``legal``. The control arm for every comparison."""
    return legal[rng.randrange(len(legal))]


def greedy_capture(
    board: Board,
    state: GameState,
    seat: int,
    roll: int,
    legal: Sequence[Move],
    rng: random.Random,
) -> Move:
    """Uniform over capturing moves if any exist, else uniform over ``legal``.

    Deliberately ``RANDOM`` plus a capture filter and nothing else, so the
    ``RANDOM`` -> ``GREEDY_CAPTURE`` contrast isolates capture-seeking exactly
    (D-44). A control for the RQ-1/RQ-2 estimands, not a strategy under study.
    """
    index = rng.randrange(len(legal))
    captures = [m for m in legal if m.captures is not None]
    if not captures:
        return legal[index]
    return captures[index % len(captures)]


def spread(
    board: Board,
    state: GameState,
    seat: int,
    roll: int,
    legal: Sequence[Move],
    rng: random.Random,
) -> Move:
    """Advance all pieces evenly: enter when possible, else move the rearmost.

    Tie-break is the lowest piece index, then canonical move order — and since
    ``legal`` arrives in canonical order (D-3), a stable ``min`` over
    ``(rank, piece)`` implements both.
    """
    rng.random()  # D-37: one draw per decision even when unused
    entry = _entry_move(legal)
    if entry is not None:
        return entry
    ranked = [(r, m.piece, m) for m in legal if (r := _track_rank(board, state, m)) is not None]
    if not ranked:
        # Every legal move belongs to a yard or goal piece, so nothing is
        # rankable. §3.1 requires totality: fall through to canonical order.
        return legal[0]
    return min(ranked, key=lambda t: (t[0], t[1]))[2]


def _focus(
    board: Board,
    state: GameState,
    legal: Sequence[Move],
    *,
    front: bool,
) -> Move:
    """Shared body of the two focus policies.

    The protagonist is the most (``front``) or least advanced own piece **on
    the ring**, recomputed every decision. If a protagonist move is legal it is
    played; otherwise an entry move; otherwise the fallback the two policies
    define differently — ``FOCUS_FRONT`` keeps non-protagonists back,
    ``FOCUS_REAR`` pushes them ahead (D-36).
    """
    on_ring = [
        (pos, index)
        for index, pos in enumerate(state.positions)
        if board.location(pos) is PieceLocation.RING
        and index // 4 == legal[0].piece // 4
    ]
    if on_ring:
        protagonist = (max if front else min)(on_ring, key=lambda t: (t[0], -t[1]))[1]
        for move in legal:
            if move.piece == protagonist:
                return move

    entry = _entry_move(legal)
    if entry is not None:
        return entry

    ranked = [(r, m.piece, m) for m in legal if (r := _track_rank(board, state, m)) is not None]
    if not ranked:
        return legal[0]
    # FOCUS_FRONT keeps the others back (move the rearmost); FOCUS_REAR pushes
    # them ahead (move the frontmost). Piece index ascending breaks ties in
    # both directions.
    return min(ranked, key=lambda t: (t[0] if front else -t[0], t[1]))[2]


def focus_front(
    board: Board,
    state: GameState,
    seat: int,
    roll: int,
    legal: Sequence[Move],
    rng: random.Random,
) -> Move:
    """Single-piece focus on the most advanced own ring piece."""
    rng.random()  # D-37
    return _focus(board, state, legal, front=True)


def focus_rear(
    board: Board,
    state: GameState,
    seat: int,
    roll: int,
    legal: Sequence[Move],
    rng: random.Random,
) -> Move:
    """Single-piece focus on the least advanced own ring piece."""
    rng.random()  # D-37
    return _focus(board, state, legal, front=False)


#: Registry keyed by the ids §3.2 uses. The campaign config names agents by
#: these strings, so they are part of the log schema.
REGISTRY: dict[str, Agent] = {
    "RANDOM": random_agent,
    "SPREAD": spread,
    "FOCUS_FRONT": focus_front,
    "FOCUS_REAR": focus_rear,
    "GREEDY_CAPTURE": greedy_capture,
}

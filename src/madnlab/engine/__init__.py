"""Board geometry, state, rule configuration and legality.

``legal_moves`` in :mod:`madnlab.engine.moves` is the single source of truth for legality (GM-7):
the game loop, every agent, the replay validator and the UI all consume that one function.

Each type is re-exported next to its validating constructor — :class:`Board` with
:func:`board_for`, :class:`GameState` with :func:`initial_state` — so a consumer can build both
arguments :func:`legal_moves` needs without reaching into submodules.
"""

from madnlab.engine.geometry import POS_YARD, Board, PieceLocation, board_for
from madnlab.engine.moves import Move, MoveKind, Restriction, legal_moves
from madnlab.engine.rules import (
    BASELINE,
    CaptureEnforcement,
    CaptureMode,
    ColdStart,
    GameEndMode,
    InadmissibleRuleSetError,
    RuleSet,
)
from madnlab.engine.state import GameState, initial_state, progress_of_seat

__all__ = [
    "BASELINE",
    "POS_YARD",
    "Board",
    "CaptureEnforcement",
    "CaptureMode",
    "ColdStart",
    "GameEndMode",
    "GameState",
    "InadmissibleRuleSetError",
    "Move",
    "MoveKind",
    "PieceLocation",
    "Restriction",
    "RuleSet",
    "board_for",
    "initial_state",
    "legal_moves",
    "progress_of_seat",
]

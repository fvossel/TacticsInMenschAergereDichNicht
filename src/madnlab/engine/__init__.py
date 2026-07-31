"""Board geometry, state, rule configuration and legality.

``legal_moves`` in :mod:`madnlab.engine.moves` is the single source of truth
for legality (GM-7): the game loop, every agent, the replay validator and the
UI all consume that one function, and no agent re-implements any part of it.
"""

from madnlab.engine.geometry import POS_YARD, Board, PieceLocation, location_of
from madnlab.engine.moves import Move, MoveKind, legal_moves
from madnlab.engine.rules import (
    CaptureEnforcement,
    CaptureMode,
    ColdStart,
    GameEndMode,
    RuleSet,
)
from madnlab.engine.state import GameState, progress_of_seat

__all__ = [
    "POS_YARD",
    "Board",
    "CaptureEnforcement",
    "CaptureMode",
    "ColdStart",
    "GameEndMode",
    "GameState",
    "Move",
    "MoveKind",
    "PieceLocation",
    "RuleSet",
    "legal_moves",
    "location_of",
    "progress_of_seat",
]

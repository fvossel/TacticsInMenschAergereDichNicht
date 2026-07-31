"""MadnLab — a measurement engine for Mensch aergere Dich nicht.

The product is measurement series with uncertainty estimates; simulated games
are a by-product. See ``docs/requirements.md`` for the specification and
``docs/decisions.md`` for the decision ledger that every module references.
"""

__version__ = "0.1.0"

#: Engine version recorded in every log header (LG-1) and checked by the
#: replay validator (LG-3). Bump whenever a change can alter a game's event
#: stream; regenerating the goldens is part of the bump (D-33).
ENGINE_VERSION = "0.1.0"

"""MadnLab — a measurement engine for Mensch aergere Dich nicht.

The output is measurement series with uncertainty estimates; simulated games are a by-product.
``docs/requirements.md`` holds the specification and ``docs/decisions.md`` the decision ledger;
the tags cited throughout the source (LG-1, D-33, ...) are their requirement and decision ids.
"""

__version__ = "0.1.0"

#: Engine version stamped into every log header (LG-1) and checked by the replay validator (LG-3).
#: Independent of ``__version__``: bump it whenever a change can alter a game's event stream, and
#: regenerate the goldens in the same commit (D-33).
ENGINE_VERSION = "0.1.0"

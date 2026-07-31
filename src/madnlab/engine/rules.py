"""Rule configuration (GM-4) — the seven measured axes plus engine settings.

Defaults are the baseline rule set of requirements §2.3: the official Schmidt
Spiele rules, pinned to Art. 49020/49021 (2006) for structure and Art. 51204
(2023) for mechanical clauses absent from it (D-50).

Two corrections against the version 1 draft are baked into the defaults here,
both verified against the official text:

* ``cold_start`` defaults to :attr:`ColdStart.ONE_PIECE_OUT` — one piece on the
  entry field, three in the yard. The draft had ``strict`` (all four in the
  yard) as "the Schmidt baseline"; the two were inverted (D-55).
* ``dreimal_wuerfeln`` defaults to off. The three-attempts rule is an optional
  *Spielvariante*, and a post-capture recovery rule at that — not the popular
  "three tries to get your first piece out" house rule (D-51).
"""

from __future__ import annotations

import enum
from typing import NamedTuple


class ColdStart(enum.StrEnum):
    """How pieces begin the game and what is needed to bring them out."""

    #: The official setup (GM-3.2): one piece on the own entry field, three in
    #: the yard; a 6 is required for each of those three.
    ONE_PIECE_OUT = "one_piece_out"

    #: All four pieces begin in the yard; a 6 is required to enter. Appears in
    #: no official edition and is measured as an ordinary variant arm.
    STRICT = "strict"

    #: All four pieces begin in the yard, but any roll value may be used to
    #: enter. The roll is consumed; entering is an ordinary legal move and is
    #: never forced (D-7).
    FREE_ENTRY = "free_entry"

    @property
    def requires_six_to_enter(self) -> bool:
        """Whether bringing a piece out of the yard needs a 6."""
        return self is not ColdStart.FREE_ENTRY


class CaptureMode(enum.StrEnum):
    """Schlagzwang axis (GM-5)."""

    #: Baseline. The official base rules say expressly "Es herrscht aber kein
    #: Schlagzwang."
    OPTIONAL = "optional"

    #: If the roll admits a capture, the legal set is restricted to capturing
    #: moves — subject to the GM-5.1 priority lattice.
    MANDATORY = "mandatory"

    #: Additionally, a capture must be taken even when the capturing path
    #: passes the own goal entry; the piece then continues on the ring for
    #: another lap.
    MANDATORY_EXTENDED = "mandatory_extended"

    @property
    def is_forcing(self) -> bool:
        return self is not CaptureMode.OPTIONAL


class CaptureEnforcement(enum.StrEnum):
    """How a violated capture obligation is handled (GM-5.2)."""

    #: v1: illegal moves are filtered out of the legal-move set, so agents
    #: cannot violate the rule at all.
    ENFORCE = "enforce"

    #: The "pusten" penalty branch. Out of scope for v1 (§12); the value
    #: exists from day one so logs and configs never need a schema break.
    PENALIZE = "penalize"


class GameEndMode(enum.StrEnum):
    """When a game stops (GM-3.11)."""

    #: Play until all but one seat have finished; ranks are the realized
    #: finishing order. The v1 campaigns use this exclusively.
    PLAY_OUT = "play_out"

    #: Stop at the first finisher; remaining ranks by total progress with ties
    #: reported. Available as a config value, unused by the v1 campaigns.
    FIRST_WINNER = "first_winner"


class RuleSet(NamedTuple):
    """A fully resolved rule configuration.

    Defaults are the §2.3 baseline. ``validate`` enforces the nesting of the
    two entry-phase axes; the campaign runner calls it so an inadmissible cell
    fails with a named error rather than being silently coerced (D-13).
    """

    # -- the seven measured axes (GM-4) ------------------------------------
    cold_start: ColdStart = ColdStart.ONE_PIECE_OUT
    dreimal_wuerfeln: bool = False
    bonus_roll_after_quick_entry: bool = False
    bonus_roll_forfeited: bool = False
    goal_no_jump: bool = False
    capture_mode: CaptureMode = CaptureMode.OPTIONAL
    barriers: bool = False

    # -- engine settings, not measured axes --------------------------------
    game_end_mode: GameEndMode = GameEndMode.PLAY_OUT
    capture_enforcement: CaptureEnforcement = CaptureEnforcement.ENFORCE

    # ----------------------------------------------------------------------

    def validate(self) -> None:
        """Raise :class:`InadmissibleRuleSet` if the combination is invalid."""
        if self.bonus_roll_after_quick_entry and not self.dreimal_wuerfeln:
            raise InadmissibleRuleSet(
                "bonus_roll_after_quick_entry requires dreimal_wuerfeln=True: the "
                "bonus is granted for entering on the 1st or 2nd of the three "
                "attempts, and without the variant there are no attempts (GM-4)"
            )
        if self.capture_enforcement is CaptureEnforcement.PENALIZE:
            raise InadmissibleRuleSet(
                "capture_enforcement='penalize' is out of scope for v1: it is only "
                "meaningful with fallible agents that can overlook a capture, plus "
                "an opponent policy for choosing the blown piece (§12)"
            )

    @property
    def entry_attempts(self) -> int:
        """Rolls granted per turn while the D-1 condition holds.

        The three-attempts variant never fires under ``free_entry``: entering
        does not need a 6 there, so rolling repeatedly for one is meaningless.
        """
        if self.dreimal_wuerfeln and self.cold_start.requires_six_to_enter:
            return 3
        return 1

    @property
    def entry_axes_are_inert(self) -> bool:
        """Whether both entry-phase axes have no behavioural effect.

        True under ``free_entry``. This is what collapses 72 of EX-4's
        admissible cells to 24 distinct behaviours (D-13), and AK-1 asserts it
        directly rather than leaving it as a counting argument.
        """
        return not self.cold_start.requires_six_to_enter


class InadmissibleRuleSet(ValueError):
    """Raised for a rule combination the specification does not define."""


#: The §2.3 baseline, for tests and for the ``EX-1`` calibration campaign.
BASELINE = RuleSet()

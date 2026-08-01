"""One game, end to end: config in, header + events + summary row out.

This is the seam AK-3 needs. The replay validator re-runs
:func:`play_indexed_game` from a header alone and compares event streams, so
everything that shapes a game has to come out of the header — which is why the
resolved starting seat is a header field rather than something the runner
keeps to itself.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import NamedTuple

from madnlab import ENGINE_VERSION
from madnlab.agents.policies import REGISTRY
from madnlab.engine.geometry import SeatPattern, board_for, occupied_seats
from madnlab.engine.loop import GameOutcome, play_game
from madnlab.engine.rules import RuleSet
from madnlab.engine.state import initial_state
from madnlab.eventlog.events import SCHEMA_VERSION, Event, LogHeader
from madnlab.eventlog.writer import SummaryRow
from madnlab.run import counterbalance, seeds

#: The pre-registration tag a run was executed under (§14). Recorded in every
#: header and every summary row. The placeholder this held before the freeze
#: was ``unfrozen``; the data generated under it was discarded rather than
#: relabelled, so no published row carries it (D-73).
PREREG_VERSION = "prereg-v1"


class GameSpec(NamedTuple):
    """A campaign cell, resolved. One of these plus an index defines a game."""

    cell_key: str
    seats: int
    players: int
    seat_pattern: SeatPattern
    rules: RuleSet
    #: Agent id per occupied seat, in seat order. Under counterbalancing this
    #: is the *canonical* assignment; the arrangement actually played is
    #: derived per game index (§7.3) and recorded in the header.
    agent_ids: tuple[str, ...]
    master_seed: int
    #: §7.3 counterbalancing. Off only for one-off games and for replay, which
    #: takes the resolved assignment from the header instead.
    counterbalanced: bool = True
    #: Override D-39's permutation trigger. ``None`` uses the rule.
    force_full_permutations: bool | None = None

    def occupied(self) -> tuple[int, ...]:
        return occupied_seats(self.seats, self.players, self.seat_pattern)

    def agent_map(self) -> dict[int, str]:
        return dict(zip(self.occupied(), self.agent_ids, strict=True))

    def balance(self) -> counterbalance.Balance:
        return counterbalance.plan(
            self.agent_ids, self.occupied(), force_full=self.force_full_permutations
        )


class GameRun(NamedTuple):
    header: LogHeader
    events: list[Event]
    outcome: GameOutcome
    summary: SummaryRow


def _rules_wire(rules: RuleSet) -> tuple[tuple[str, str], ...]:
    """Rule flags as ordered ``(name, value)`` pairs for the header."""
    return tuple((field, str(getattr(rules, field))) for field in rules._fields)


def build_header(
    spec: GameSpec,
    game_index: int,
    starting_seat: int,
    agent_map: dict[int, str] | None = None,
) -> LogHeader:
    seed = seeds.game_seed(spec.master_seed, spec.cell_key, game_index)
    resolved_agents = agent_map if agent_map is not None else spec.agent_map()
    return LogHeader(
        schema_version=SCHEMA_VERSION,
        engine_version=ENGINE_VERSION,
        prereg_version=PREREG_VERSION,
        cell_key=spec.cell_key,
        game_index=game_index,
        master_seed=spec.master_seed,
        game_seed=seed,
        seats=spec.seats,
        seat_pattern=str(spec.seat_pattern),
        occupied_seats=spec.occupied(),
        starting_seat=starting_seat,
        agents=tuple(sorted(resolved_agents.items())),
        rules=_rules_wire(spec.rules),
    )


def play_indexed_game(
    spec: GameSpec,
    game_index: int,
    record_events: bool = True,
    starting_seat: int | None = None,
    n_requested: int = 0,
) -> GameRun:
    """Play game ``game_index`` of ``spec``.

    ``starting_seat`` overrides the seeded draw, which is what §7.3's
    counterbalancing does and what replay does when reading a header back.
    """
    spec.rules.validate()
    board = board_for(spec.seats)
    seats: Sequence[int] = spec.occupied()
    seed = seeds.game_seed(spec.master_seed, spec.cell_key, game_index)
    streams = seeds.derive(seed, seats)

    # §7.3: the arrangement and the starting seat come from the game index, so
    # a complete block covers every combination exactly once. The seeded draw
    # (D-6) is the uncounterbalanced fallback, and an explicit override is what
    # replay uses — it reads the resolved value back out of the header rather
    # than re-deriving it.
    if spec.counterbalanced:
        balance = spec.balance()
        balance_block = balance.block
        assignment, balanced_start, rotation_index, start_index = balance.assign(
            game_index
        )
    else:
        balance_block = 1
        assignment = spec.agent_ids
        balanced_start = seeds.draw_start_seat(streams, seats)
        rotation_index = start_index = 0
    resolved_start = starting_seat if starting_seat is not None else balanced_start
    agent_names = dict(zip(seats, assignment, strict=True))

    agents = {seat: REGISTRY[name] for seat, name in agent_names.items()}
    events: list[Event] | None = [] if record_events else None
    outcome = play_game(
        board,
        seats,
        spec.rules,
        agents,
        initial_state(board, tuple(seats), spec.rules),
        streams.dice,
        streams.agents,
        resolved_start,
        record=events,
    )
    header = build_header(spec, game_index, resolved_start, agent_names)
    summary = SummaryRow(
        cell_key=spec.cell_key,
        game_index=game_index,
        game_seed=seed,
        prereg_version=PREREG_VERSION,
        engine_version=ENGINE_VERSION,
        seats=spec.seats,
        players=spec.players,
        seat_pattern=str(spec.seat_pattern),
        starting_seat=resolved_start,
        n_requested=n_requested,
        n_effective=(
            -(-n_requested // balance_block) * balance_block if n_requested else 0
        ),
        balance_block=balance_block,
        rotation_index=rotation_index,
        starting_seat_index=start_index,
        winner=outcome.winner,
        ranks=outcome.ranks,
        turns=outcome.turns,
        rounds=outcome.rounds,
        dice_rolls=outcome.dice_rolls,
        turns_to_first_win=outcome.turns_to_first_win,
        rounds_to_first_win=outcome.rounds_to_first_win,
        captures_total=outcome.captures_total,
        captures_by_seat=outcome.captures_by_seat,
        captured_by_seat=outcome.captured_by_seat,
        passes_by_seat=outcome.passes_by_seat,
        entry_waits_by_seat=outcome.entry_waits_by_seat,
        lead_changes=outcome.lead_changes,
        turns_without_leader=outcome.turns_without_leader,
        time_in_lead_by_seat=outcome.time_in_lead_by_seat,
        extra_laps_by_seat=outcome.extra_laps_by_seat,
        barriers_formed=outcome.barriers_formed,
        barrier_turns=outcome.barrier_turns,
        barrier_turns_by_seat=outcome.barrier_turns_by_seat,
        capture_forcing_offered=outcome.capture_forcing_offered,
        capture_forcing_violations=outcome.capture_forcing_violations,
        forced_extra_lap_offered=outcome.forced_extra_lap_offered,
        forced_extra_lap_violations=outcome.forced_extra_lap_violations,
        winner_rank_at_50=outcome.winner_rank_at_50,
        winner_rank_at_75=outcome.winner_rank_at_75,
        winner_rank_at_50_tied=outcome.winner_rank_at_50_tied,
        comeback=outcome.comeback,
        comeback_rank_threshold=outcome.comeback_rank_threshold,
        comeback_depth=outcome.comeback_depth,
        final_margin=outcome.final_margin,
        final_margin_norm=outcome.final_margin_norm,
        stalemate=outcome.stalemate,
        abandoned=outcome.abandoned,
    )
    return GameRun(header=header, events=events or [], outcome=outcome, summary=summary)

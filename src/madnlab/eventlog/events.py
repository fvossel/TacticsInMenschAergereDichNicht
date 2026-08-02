"""Event records (LG-1).

Every event is a NamedTuple whose field order is the serialization order (D-33): the canonical
writer emits the fields in declaration order, so reordering them is a log-schema change and must
bump :data:`SCHEMA_VERSION`.

The event stream is what AK-3's replay validator compares, so an event carries every decision the
engine made rather than only the resulting state. Recording the full offered legal-move set and the
chosen index lets a sampled log be audited for AK-5 without re-simulating (§4.1).
"""

from __future__ import annotations

from typing import NamedTuple

#: Bumped whenever the event schema, the field order, or the canonical serialization changes.
#: Recorded in the header and checked on replay.
SCHEMA_VERSION = "1"


class RollEvent(NamedTuple):
    seat: int
    value: int
    #: 1-based index within the turn's roll sequence: the attempt phase first, then any extra
    #: rolls (D-10).
    attempt: int


class MoveEvent(NamedTuple):
    seat: int
    piece: int
    from_pos: int
    to_pos: int
    kind: str
    #: The full offered set, one ``(piece, from_pos, to_pos, kind, captures)`` per entry.
    #: ``captures`` lets AK-5 be audited from the log alone.
    legal: tuple[tuple[int, int, int, str, int | None], ...]
    #: Index into :attr:`legal` of the move that was played.
    chosen: int
    #: Which clause of the GM-5.1 lattice narrowed the set, if any.
    restriction: str


class CaptureEvent(NamedTuple):
    captor_seat: int
    captor_piece: int
    victim_seat: int
    victim_piece: int
    field: int


class BarrierEvent(NamedTuple):
    seat: int
    field: int
    formed: bool


class PassEvent(NamedTuple):
    seat: int


class FinishEvent(NamedTuple):
    seat: int
    #: 1-based finishing position, i.e. the seat's rank under ``play_out``.
    place: int


class GameEndEvent(NamedTuple):
    ranks: tuple[int, ...]


Event = (
    RollEvent
    | MoveEvent
    | CaptureEvent
    | BarrierEvent
    | PassEvent
    | FinishEvent
    | GameEndEvent
)

#: Wire tag per event type. Explicit rather than derived from the class name, so renaming a class
#: is not silently a schema change.
KIND: dict[type, str] = {
    RollEvent: "roll",
    MoveEvent: "move",
    CaptureEvent: "capture",
    BarrierEvent: "barrier",
    PassEvent: "pass",
    FinishEvent: "finish",
    GameEndEvent: "game_end",
}


class LogHeader(NamedTuple):
    """The header record (§4.1).

    §4.3 requires a game to be reproducible from ``header + engine version`` alone, so every value
    the runner resolved rather than derived — the drawn starting seat above all — is recorded here.
    """

    schema_version: str
    engine_version: str
    prereg_version: str
    cell_key: str
    game_index: int
    master_seed: int
    game_seed: int
    seats: int
    seat_pattern: str
    occupied_seats: tuple[int, ...]
    starting_seat: int
    agents: tuple[tuple[int, str], ...]
    rules: tuple[tuple[str, str], ...]

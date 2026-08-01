"""Canonical JSONL serialization (D-33).

"Byte-identical" (LG-3, AK-2) is only a meaningful claim once the encoding is
pinned, so it is pinned here and nowhere else:

* UTF-8, with non-ASCII escaped so the bytes do not depend on the locale
* an explicit ``\\n`` terminator, never the platform's
* fixed key order — the declaration order of the event's fields, which is why
  reordering a field in :mod:`madnlab.eventlog.events` is a schema change
* ``separators=(",", ":")``, so no whitespace can drift
* shortest round-trip float representation, which is Python's ``repr`` — the
  event stream carries no floats today, and this exists so that stays true by
  construction rather than by luck
"""

from __future__ import annotations

import json
from collections.abc import Iterable, Iterator
from typing import Any, NamedTuple, TextIO

from madnlab.eventlog.events import KIND, Event, LogHeader

_SEPARATORS = (",", ":")


def _plain(value: Any) -> Any:
    """Reduce a value to something ``json`` serializes deterministically."""
    if isinstance(value, tuple | list):
        return [_plain(item) for item in value]
    if isinstance(value, dict):
        return {str(k): _plain(v) for k, v in value.items()}
    if isinstance(value, bool | int | str) or value is None:
        return value
    if isinstance(value, float):
        # repr is the shortest string that round-trips (PEP 3141 / CPython).
        return float(repr(value))
    return str(value)


def canonical_dumps(payload: dict[str, Any]) -> str:
    """One canonical JSON line, without its terminator."""
    return json.dumps(
        payload,
        ensure_ascii=True,
        separators=_SEPARATORS,
        sort_keys=False,
        allow_nan=False,
    )


def event_payload(event: Event) -> dict[str, Any]:
    """An event as an ordered mapping, tag first then declaration order."""
    payload: dict[str, Any] = {"e": KIND[type(event)]}
    for field in event._fields:
        payload[field] = _plain(getattr(event, field))
    return payload


def header_payload(header: LogHeader) -> dict[str, Any]:
    payload: dict[str, Any] = {"e": "header"}
    for field in header._fields:
        payload[field] = _plain(getattr(header, field))
    return payload


def iter_lines(header: LogHeader, events: Iterable[Event]) -> Iterator[str]:
    """The complete log as canonical lines, header first."""
    yield canonical_dumps(header_payload(header))
    for event in events:
        yield canonical_dumps(event_payload(event))


def write_log(stream: TextIO, header: LogHeader, events: Iterable[Event]) -> None:
    """Write a game log. ``stream`` must be opened with ``newline=""``.

    The explicit ``\\n`` is the point: with the default newline translation
    Windows would emit ``\\r\\n`` and the same seed would produce different
    bytes on different platforms, which is exactly what AK-2 asserts cannot
    happen.
    """
    for line in iter_lines(header, events):
        stream.write(line)
        stream.write("\n")


def log_bytes(header: LogHeader, events: Iterable[Event]) -> bytes:
    """The log as the bytes that would be written. Used by AK-2."""
    return "".join(line + "\n" for line in iter_lines(header, events)).encode("utf-8")


class SummaryRow(NamedTuple):
    """One row of ``summary.jsonl`` (LG-2).

    The key set is fixed per schema version and does **not** vary by arm
    (D-22): arm-specific counters are always present and zero when
    inapplicable, so a campaign's rows are a rectangle no matter which flags
    the cell had.
    """

    cell_key: str
    game_index: int
    game_seed: int
    prereg_version: str
    engine_version: str
    seats: int
    players: int
    seat_pattern: str
    starting_seat: int
    #: §7.3 counterbalancing, recorded per row so a seat effect can never
    #: be averaged away without the arrangement it came from (D-39).
    n_requested: int
    n_effective: int
    balance_block: int
    rotation_index: int
    starting_seat_index: int
    winner: int
    ranks: tuple[int, ...]
    turns: int
    rounds: int
    dice_rolls: int
    turns_to_first_win: int
    rounds_to_first_win: int
    captures_total: int
    captures_by_seat: tuple[int, ...]
    passes_by_seat: tuple[int, ...]
    lead_changes: int
    turns_without_leader: int
    time_in_lead_by_seat: tuple[int, ...]
    extra_laps_by_seat: tuple[int, ...]
    barriers_formed: int
    barrier_turns: int
    capture_forcing_offered: int
    capture_forcing_violations: int
    #: True when the game ended in deadlock rather than with a finisher (D-69).
    stalemate: bool
    #: True when the game hit the turn bound unfinished (D-70).
    abandoned: bool


def summary_line(row: SummaryRow) -> str:
    payload = {field: _plain(getattr(row, field)) for field in row._fields}
    return canonical_dumps(payload)

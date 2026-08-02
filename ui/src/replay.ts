/**
 * Replaying an event stream into board states (UI-4) and the running §6
 * metrics the info panel shows (UI-5).
 *
 * The viewer never re-derives legality: under GM-7 that belongs to a single
 * engine function. Everything here is a fold over recorded events.
 */

import type { Event, GameLog } from "./log";

export const PIECES_PER_SEAT = 4;
export const GOAL_FIELDS = 4;

export interface Geometry {
  seats: number;
  ringLength: number;
  spacing: number;
}

const RING_LENGTH: Record<number, number> = { 4: 40, 6: 48 };
const SPACING: Record<number, number> = { 4: 10, 6: 8 };

export function geometryFor(seats: number): Geometry {
  const ringLength = RING_LENGTH[seats];
  const spacing = SPACING[seats];
  if (ringLength === undefined || spacing === undefined) {
    throw new Error(`unsupported seat count ${seats}: the boards are 4 and 6 (§2.1)`);
  }
  return { seats, ringLength, spacing };
}

/** Absolute ring field of `seat`'s piece at `pos`. Mirrors Board.ring_field. */
export function ringField(geometry: Geometry, seat: number, pos: number): number {
  return (((seat * geometry.spacing + pos - 1) % geometry.ringLength) + geometry.ringLength) %
    geometry.ringLength;
}

/** Progress of a seat with all four pieces home: the sum of the top GOAL_FIELDS positions. */
export function maxProgressPerSeat(geometry: Geometry): number {
  const top = geometry.ringLength + GOAL_FIELDS;
  let total = 0;
  for (let i = top - GOAL_FIELDS + 1; i <= top; i += 1) total += i;
  return total;
}

/** A board state plus the running metrics at one point in the stream. */
export interface Frame {
  /** Index of the event that produced this frame; -1 is the opening position. */
  eventIndex: number;
  positions: number[];
  /** Seat whose turn it is, or null before the first roll. */
  activeSeat: number | null;
  roll: number | null;
  attempt: number | null;
  offered: Event | null;
  turns: number;
  diceRolls: number;
  captures: number;
  capturesBySeat: number[];
  passesBySeat: number[];
  leader: number | null;
  leadChanges: number;
  finished: number[];
  /** Event index at which the first seat finished, or null while contested. */
  firstWinAt: number | null;
  barrierFields: Set<number>;
}

function emptyFrame(log: GameLog, geometry: Geometry): Frame {
  const positions = new Array<number>(geometry.seats * PIECES_PER_SEAT).fill(0);
  const coldStart = new Map(log.header.rules).get("cold_start");
  if (coldStart === "one_piece_out") {
    for (const seat of log.header.occupied_seats) positions[seat * PIECES_PER_SEAT] = 1;
  }
  return {
    eventIndex: -1,
    positions,
    activeSeat: null,
    roll: null,
    attempt: null,
    offered: null,
    turns: 0,
    diceRolls: 0,
    captures: 0,
    capturesBySeat: new Array<number>(geometry.seats).fill(0),
    passesBySeat: new Array<number>(geometry.seats).fill(0),
    leader: null,
    leadChanges: 0,
    finished: [],
    firstWinAt: null,
    barrierFields: new Set(),
  };
}

function cloneFrame(frame: Frame): Frame {
  return {
    ...frame,
    positions: [...frame.positions],
    capturesBySeat: [...frame.capturesBySeat],
    passesBySeat: [...frame.passesBySeat],
    finished: [...frame.finished],
    barrierFields: new Set(frame.barrierFields),
  };
}

function seatTotal(positions: number[], seat: number): number {
  let total = 0;
  for (let p = 0; p < PIECES_PER_SEAT; p += 1) total += positions[seat * PIECES_PER_SEAT + p] ?? 0;
  return total;
}

/**
 * Recompute leader(t) as §6.1 defines it: unique argmax; on ties the
 * previous leader if it is still tied for the maximum, else the lowest tied
 * seat index; null until a strict maximum exists.
 */
function updateLeader(frame: Frame, occupied: number[]): void {
  if (frame.finished.length > 0) return;
  let best = -1;
  const tied: number[] = [];
  for (const seat of occupied) {
    const total = seatTotal(frame.positions, seat);
    if (total > best) {
      best = total;
      tied.length = 0;
      tied.push(seat);
    } else if (total === best) {
      tied.push(seat);
    }
  }
  let next: number | null;
  if (tied.length === 1) next = tied[0] ?? null;
  else if (frame.leader !== null && tied.includes(frame.leader)) next = frame.leader;
  else if (frame.leader !== null) next = Math.min(...tied);
  else next = null;
  if (next !== null && frame.leader !== null && next !== frame.leader) frame.leadChanges += 1;
  frame.leader = next;
}

/**
 * Fold the whole stream into one frame per event, plus the opening position.
 *
 * Frames are materialised rather than recomputed on demand: stepping backwards
 * is as common as stepping forwards in a replay viewer, and a 2,400-event game
 * costs a few hundred kilobytes.
 */
export function buildFrames(log: GameLog): Frame[] {
  const geometry = geometryFor(log.header.seats);
  const occupied = log.header.occupied_seats;
  const frames: Frame[] = [emptyFrame(log, geometry)];
  let current = frames[0] as Frame;

  for (const [index, event] of log.events.entries()) {
    const next = cloneFrame(current);
    next.eventIndex = index;
    next.offered = null;

    switch (event.e) {
      case "roll": {
        if (event.attempt === 1) {
          if (next.activeSeat !== null) updateLeader(next, occupied);
          next.turns += 1;
        }
        next.activeSeat = event.seat;
        next.roll = event.value;
        next.attempt = event.attempt;
        next.diceRolls += 1;
        break;
      }
      case "move": {
        next.positions[event.piece] = event.to_pos;
        next.offered = event;
        break;
      }
      case "capture": {
        next.positions[event.victim_seat * PIECES_PER_SEAT + event.victim_piece] = 0;
        next.captures += 1;
        next.capturesBySeat[event.captor_seat] =
          (next.capturesBySeat[event.captor_seat] ?? 0) + 1;
        break;
      }
      case "barrier": {
        if (event.formed) next.barrierFields.add(event.field);
        else next.barrierFields.delete(event.field);
        break;
      }
      case "pass": {
        next.passesBySeat[event.seat] = (next.passesBySeat[event.seat] ?? 0) + 1;
        break;
      }
      case "finish": {
        next.finished.push(event.seat);
        if (next.firstWinAt === null) next.firstWinAt = index;
        break;
      }
      case "game_end": {
        updateLeader(next, occupied);
        break;
      }
    }
    frames.push(next);
    current = next;
  }
  return frames;
}

export type EventFilter =
  | "all"
  | "moves"
  | "captures"
  | "entries"
  | "barriers"
  | "passes";

export function matchesFilter(event: Event, filter: EventFilter): boolean {
  switch (filter) {
    case "all":
      return true;
    case "moves":
      return event.e === "move";
    case "captures":
      return event.e === "capture";
    case "entries":
      return event.e === "move" && event.kind === "enter";
    case "barriers":
      return event.e === "barrier";
    case "passes":
      return event.e === "pass";
  }
}

export function describeEvent(event: Event): string {
  switch (event.e) {
    case "roll":
      return `seat ${event.seat} rolls ${event.value}${event.attempt > 1 ? ` (roll ${event.attempt})` : ""}`;
    case "move": {
      const forced = event.restriction === "none" ? "" : ` [${event.restriction}]`;
      return `seat ${event.seat} piece ${event.piece % PIECES_PER_SEAT}: ${event.from_pos} → ${event.to_pos} (${event.kind})${forced}`;
    }
    case "capture":
      return `seat ${event.captor_seat} captures seat ${event.victim_seat} piece ${event.victim_piece} on field ${event.field}`;
    case "barrier":
      return `seat ${event.seat} ${event.formed ? "forms" : "breaks"} a barrier on field ${event.field}`;
    case "pass":
      return `seat ${event.seat} has no legal move`;
    case "finish":
      return `seat ${event.seat} finishes (place ${event.place})`;
    case "game_end":
      return `game ends, ranks ${event.ranks.join(" > ")}`;
  }
}

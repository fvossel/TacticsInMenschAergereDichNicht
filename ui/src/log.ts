/**
 * Parsing MadnLab event logs (LG-1).
 *
 * The wire format is one canonical JSON object per line, header first, with an `e` tag naming
 * the record kind (D-33). Records are read by field name and never by position, so adding a
 * field to the schema is additive rather than breaking.
 */

export const SUPPORTED_SCHEMA = "1";

export type MoveKind = "enter" | "ring" | "goal_enter" | "goal";
export type Restriction = "none" | "clearing" | "forced_entry" | "capture";

/** One entry of the offered legal-move set: piece, from, to, kind, captured. */
export type OfferedMove = [number, number, number, MoveKind, number | null];

export interface Header {
  schema_version: string;
  engine_version: string;
  prereg_version: string;
  cell_key: string;
  game_index: number;
  master_seed: number;
  game_seed: number;
  seats: number;
  seat_pattern: string;
  occupied_seats: number[];
  starting_seat: number;
  agents: [number, string][];
  rules: [string, string][];
}

export type Event =
  | { e: "roll"; seat: number; value: number; attempt: number }
  | {
      e: "move";
      seat: number;
      piece: number;
      from_pos: number;
      to_pos: number;
      kind: MoveKind;
      legal: OfferedMove[];
      chosen: number;
      restriction: Restriction;
    }
  | {
      e: "capture";
      captor_seat: number;
      captor_piece: number;
      victim_seat: number;
      victim_piece: number;
      field: number;
    }
  | { e: "barrier"; seat: number; field: number; formed: boolean }
  | { e: "pass"; seat: number }
  | { e: "finish"; seat: number; place: number }
  | { e: "game_end"; ranks: number[] };

export interface GameLog {
  header: Header;
  events: Event[];
}

/** Thrown when the input is not a readable log of the supported schema. */
export class LogParseError extends Error {}

/** Parse a JSONL event log. Blank lines are tolerated; anything else is not. */
export function parseLog(text: string): GameLog {
  const lines = text.split(/\r?\n/).filter((line) => line.trim().length > 0);
  if (lines.length === 0) throw new LogParseError("the file is empty");

  let header: Header | null = null;
  const events: Event[] = [];

  for (const [index, line] of lines.entries()) {
    let record: Record<string, unknown>;
    try {
      record = JSON.parse(line) as Record<string, unknown>;
    } catch (error) {
      throw new LogParseError(`line ${index + 1} is not valid JSON: ${String(error)}`);
    }
    if (record["e"] === "header") {
      if (header !== null) throw new LogParseError(`line ${index + 1}: a second header`);
      header = record as unknown as Header;
      continue;
    }
    if (header === null) {
      throw new LogParseError("the first record must be the header (§4.1)");
    }
    // The final record of a self-contained log is the summary row, which carries no `e` tag.
    // It is not an event, so it is skipped rather than rejected.
    if (typeof record["e"] !== "string") continue;
    events.push(record as unknown as Event);
  }

  if (header === null) throw new LogParseError("no header record");
  if (header.schema_version !== SUPPORTED_SCHEMA) {
    throw new LogParseError(
      `log schema ${header.schema_version} but this viewer reads ${SUPPORTED_SCHEMA}. ` +
        `A cross-schema read is refused rather than shown wrong (D-33).`,
    );
  }
  return { header, events };
}

/** Rule flags as a map, for the info panel (UI-5). */
export function ruleMap(header: Header): Map<string, string> {
  return new Map(header.rules);
}

/** Agent name registered for `seat`, or `-` when the seat carries none. */
export function agentFor(header: Header, seat: number): string {
  return header.agents.find(([s]) => s === seat)?.[1] ?? "-";
}

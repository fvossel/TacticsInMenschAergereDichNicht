/**
 * The replay viewer shell: controls (UI-4), info panels (UI-5) and the
 * aggregate view (UI-6).
 */

import "./style.css";
import { SEAT_COLORS, highlightedFields, renderBoard } from "./board";
import { agentFor, parseLog, ruleMap, type GameLog } from "./log";
import {
  PIECES_PER_SEAT,
  buildFrames,
  describeEvent,
  geometryFor,
  matchesFilter,
  maxProgressPerSeat,
  type EventFilter,
  type Frame,
} from "./replay";

interface State {
  log: GameLog | null;
  frames: Frame[];
  cursor: number;
  playing: boolean;
  speed: number;
  filter: EventFilter;
  timer: number | null;
}

const state: State = {
  log: null,
  frames: [],
  cursor: 0,
  playing: false,
  speed: 8,
  filter: "all",
  timer: null,
};

const $ = <T extends HTMLElement>(id: string): T => {
  const node = document.getElementById(id);
  if (node === null) throw new Error(`missing element #${id}`);
  return node as T;
};

// -- loading ----------------------------------------------------------------

function loadLog(text: string, name: string): void {
  try {
    const log = parseLog(text);
    state.log = log;
    state.frames = buildFrames(log);
    state.cursor = 0;
    stopPlayback();
    $("status").textContent = `${name} — ${log.events.length} events, ${log.header.seats}-seat board`;
    $("status").classList.remove("error");
    $("viewer").hidden = false;
    renderAll();
  } catch (error) {
    $("status").textContent = `Could not read ${name}: ${String(error)}`;
    $("status").classList.add("error");
    $("viewer").hidden = true;
  }
}

function loadAggregate(text: string, name: string): void {
  try {
    const payload = JSON.parse(text) as Record<string, unknown>;
    renderAggregate(payload, name);
    $("aggregate").hidden = false;
  } catch (error) {
    $("status").textContent = `Could not read ${name}: ${String(error)}`;
    $("status").classList.add("error");
  }
}

function handleFile(file: File): void {
  const reader = new FileReader();
  reader.onload = () => {
    const text = String(reader.result);
    if (file.name.endsWith(".json")) loadAggregate(text, file.name);
    else loadLog(text, file.name);
  };
  reader.readAsText(file);
}

// -- playback ---------------------------------------------------------------

function stopPlayback(): void {
  state.playing = false;
  if (state.timer !== null) {
    window.clearInterval(state.timer);
    state.timer = null;
  }
  $("play").textContent = "Play";
}

function togglePlayback(): void {
  if (state.playing) {
    stopPlayback();
    return;
  }
  state.playing = true;
  $("play").textContent = "Pause";
  state.timer = window.setInterval(() => {
    if (state.cursor >= state.frames.length - 1) {
      stopPlayback();
      return;
    }
    state.cursor += 1;
    renderAll();
  }, 1000 / state.speed);
}

function seek(to: number): void {
  state.cursor = Math.max(0, Math.min(state.frames.length - 1, to));
  renderAll();
}

// -- rendering --------------------------------------------------------------

function renderAll(): void {
  const log = state.log;
  if (log === null) return;
  const frame = state.frames[state.cursor];
  if (frame === undefined) return;
  const geometry = geometryFor(log.header.seats);

  const boardHost = $("board-host");
  boardHost.replaceChildren(
    renderBoard(frame, {
      geometry,
      occupied: log.header.occupied_seats,
      highlighted: highlightedFields(frame, geometry),
    }),
  );

  const scrubber = $<HTMLInputElement>("scrubber");
  scrubber.max = String(state.frames.length - 1);
  scrubber.value = String(state.cursor);
  $("position").textContent = `${state.cursor} / ${state.frames.length - 1}`;

  renderRoll(frame);
  renderSeats(log, frame, geometry);
  renderMetrics(log, frame);
  renderEventList(log, frame);
  renderMeta(log);
}

function renderRoll(frame: Frame): void {
  const parts: string[] = [];
  if (frame.activeSeat !== null) parts.push(`seat ${frame.activeSeat}`);
  if (frame.roll !== null) {
    parts.push(`rolled ${frame.roll}${frame.attempt !== null && frame.attempt > 1 ? ` (roll ${frame.attempt})` : ""}`);
  }
  $("roll").textContent = parts.length > 0 ? parts.join(" ") : "not started";

  const host = $("offered");
  const offered = frame.offered;
  if (offered === null || offered.e !== "move") {
    host.replaceChildren(document.createTextNode("—"));
    return;
  }
  const list = document.createElement("ol");
  offered.legal.forEach(([piece, from, to, kind, captures], index) => {
    const item = document.createElement("li");
    if (index === offered.chosen) item.className = "chosen";
    item.textContent =
      `piece ${piece % PIECES_PER_SEAT}: ${from} → ${to} (${kind})` +
      (captures !== null ? ` captures ${Math.floor(captures / PIECES_PER_SEAT)}.${captures % PIECES_PER_SEAT}` : "");
    list.append(item);
  });
  const note = document.createElement("p");
  note.className = "restriction";
  note.textContent =
    offered.restriction === "none"
      ? "no restriction in force"
      : `legal set narrowed by: ${offered.restriction}`;
  host.replaceChildren(list, note);
}

function renderSeats(log: GameLog, frame: Frame, geometry: ReturnType<typeof geometryFor>): void {
  const max = maxProgressPerSeat(geometry);
  const host = $("seats");
  host.replaceChildren();
  for (const seat of log.header.occupied_seats) {
    let progress = 0;
    for (let piece = 0; piece < PIECES_PER_SEAT; piece += 1) {
      progress += frame.positions[seat * PIECES_PER_SEAT + piece] ?? 0;
    }
    const row = document.createElement("div");
    row.className = "seat-row";
    const finishedAt = frame.finished.indexOf(seat);
    row.innerHTML = `
      <span class="swatch" style="background:${SEAT_COLORS[seat % 6]}"></span>
      <span class="seat-name">seat ${seat} <em>${agentFor(log.header, seat)}</em></span>
      <span class="bar"><span class="fill" style="width:${((progress / max) * 100).toFixed(1)}%;background:${SEAT_COLORS[seat % 6]}"></span></span>
      <span class="num">${((progress / max) * 100).toFixed(1)}%</span>
      <span class="num">${frame.capturesBySeat[seat] ?? 0} cap</span>
      <span class="num">${frame.passesBySeat[seat] ?? 0} pass</span>
      <span class="flag">${frame.leader === seat ? "leader" : ""}${finishedAt >= 0 ? ` finished #${finishedAt + 1}` : ""}</span>`;
    host.append(row);
  }
}

function renderMetrics(log: GameLog, frame: Frame): void {
  // Dynamics metrics are counted over the segment that ends at the first finisher (§6.2), so
  // the lead-change row is labelled closed once a seat has finished.
  const segmentClosed = frame.firstWinAt !== null;
  const rows: [string, string][] = [
    ["turns", String(frame.turns)],
    ["dice rolls", String(frame.diceRolls)],
    ["captures", String(frame.captures)],
    ["lead changes", `${frame.leadChanges}${segmentClosed ? " (segment closed)" : ""}`],
    ["leader", frame.leader === null ? "none yet" : `seat ${frame.leader}`],
    ["finished", frame.finished.length === 0 ? "—" : frame.finished.join(", ")],
    ["barriers standing", String(frame.barrierFields.size)],
  ];
  $("metrics").innerHTML = rows
    .map(([label, value]) => `<div><dt>${label}</dt><dd>${value}</dd></div>`)
    .join("");
  void log;
}

function renderEventList(log: GameLog, frame: Frame): void {
  const host = $("events");
  const list = document.createElement("ol");
  const from = Math.max(0, state.cursor - 60);
  const to = Math.min(log.events.length, state.cursor + 60);
  for (let index = from; index < to; index += 1) {
    const event = log.events[index];
    if (event === undefined || !matchesFilter(event, state.filter)) continue;
    const item = document.createElement("li");
    item.value = index + 1;
    item.textContent = describeEvent(event);
    item.className = index === frame.eventIndex ? "current" : "";
    item.addEventListener("click", () => seek(index + 1));
    list.append(item);
  }
  host.replaceChildren(list);
  host.querySelector(".current")?.scrollIntoView({ block: "center" });
}

function renderMeta(log: GameLog): void {
  const rules = ruleMap(log.header);
  const entries = [
    ["cell", log.header.cell_key],
    ["game index", String(log.header.game_index)],
    ["engine", log.header.engine_version],
    ["prereg", log.header.prereg_version],
    ["master seed", String(log.header.master_seed)],
    ["game seed", String(log.header.game_seed)],
    ["starting seat", String(log.header.starting_seat)],
    ...[...rules.entries()],
  ];
  $("meta").innerHTML = entries
    .map(([label, value]) => `<div><dt>${label}</dt><dd>${value}</dd></div>`)
    .join("");
}

// -- UI-6 aggregate view ----------------------------------------------------

function renderAggregate(payload: Record<string, unknown>, name: string): void {
  const cells = (payload["cells"] ?? []) as Record<string, unknown>[];
  const rows = cells
    .map((cell) => {
      const rules = (cell["rules"] ?? {}) as Record<string, string>;
      const flags = Object.entries(rules)
        .filter(([, value]) => value !== "False" && value !== "optional" && value !== "one_piece_out")
        .map(([key, value]) => `${key}=${value}`)
        .join(" ");
      return `<tr><td>${String(cell["key"])}</td><td>${String(cell["seats"])}s/${String(cell["players"])}p</td>
        <td>${(cell["agents"] as string[]).join(", ")}</td>
        <td class="num">${Number(cell["games_effective"]).toLocaleString()}</td>
        <td class="num">${String(cell["balance_block"])}</td>
        <td>${flags || "baseline"}</td></tr>`;
    })
    .join("");
  $("aggregate-title").textContent = `${String(payload["name"] ?? name)} — resolved configuration`;
  $("aggregate-body").innerHTML = rows;
}

// -- wiring -----------------------------------------------------------------

function main(): void {
  $("file").addEventListener("change", (event) => {
    const input = event.target as HTMLInputElement;
    const file = input.files?.[0];
    if (file) handleFile(file);
  });

  const drop = $("drop");
  drop.addEventListener("dragover", (event) => {
    event.preventDefault();
    drop.classList.add("over");
  });
  drop.addEventListener("dragleave", () => drop.classList.remove("over"));
  drop.addEventListener("drop", (event) => {
    event.preventDefault();
    drop.classList.remove("over");
    const file = event.dataTransfer?.files?.[0];
    if (file) handleFile(file);
  });

  $("first").addEventListener("click", () => seek(0));
  $("prev").addEventListener("click", () => seek(state.cursor - 1));
  $("next").addEventListener("click", () => seek(state.cursor + 1));
  $("last").addEventListener("click", () => seek(state.frames.length - 1));
  $("play").addEventListener("click", togglePlayback);
  $<HTMLInputElement>("scrubber").addEventListener("input", (event) => {
    stopPlayback();
    seek(Number((event.target as HTMLInputElement).value));
  });
  $<HTMLInputElement>("speed").addEventListener("input", (event) => {
    state.speed = Number((event.target as HTMLInputElement).value);
    $("speed-label").textContent = `${state.speed}/s`;
    if (state.playing) {
      stopPlayback();
      togglePlayback();
    }
  });
  $<HTMLSelectElement>("filter").addEventListener("change", (event) => {
    state.filter = (event.target as HTMLSelectElement).value as EventFilter;
    renderAll();
  });

  document.addEventListener("keydown", (event) => {
    if (state.log === null) return;
    if (event.key === "ArrowRight") seek(state.cursor + 1);
    else if (event.key === "ArrowLeft") seek(state.cursor - 1);
    else if (event.key === " ") {
      event.preventDefault();
      togglePlayback();
    }
  });

  // Expose the loader so AK-6 can drive the viewer from a headless browser
  // without synthesising a file-input event.
  (window as unknown as Record<string, unknown>)["madnlabLoad"] = (text: string, name = "log") =>
    loadLog(text, name);
  (window as unknown as Record<string, unknown>)["madnlabState"] = () => ({
    cursor: state.cursor,
    frames: state.frames.length,
    positions: state.frames[state.cursor]?.positions,
    finished: state.frames[state.cursor]?.finished,
    turns: state.frames[state.cursor]?.turns,
    captures: state.frames[state.cursor]?.captures,
  });
}

main();

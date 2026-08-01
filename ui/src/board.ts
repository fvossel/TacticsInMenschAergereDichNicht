/**
 * Board rendering (UI-3).
 *
 * One renderer for both geometries. The ring is drawn as a ring — schematic
 * rather than the classic cross — because the same code then serves the 4-seat
 * and 6-seat boards without a per-board layout table, which is the property
 * §2.1 asks of the engine and there is no reason for the viewer to give it up.
 * The cross skin is a nice-to-have, not a requirement.
 */

import type { Frame, Geometry } from "./replay";
import { GOAL_FIELDS, PIECES_PER_SEAT, ringField } from "./replay";

export const SEAT_COLORS = [
  "#d94f4f",
  "#2f7fd1",
  "#2fa855",
  "#e0a020",
  "#8e5bd0",
  "#20a8a8",
];

const SIZE = 620;
const CENTER = SIZE / 2;
const RING_RADIUS = 250;
const FIELD_RADIUS = 11;

/** Angle of a ring field. Field 0 sits at the top, and the ring runs clockwise. */
function fieldAngle(geometry: Geometry, field: number): number {
  return (field / geometry.ringLength) * Math.PI * 2 - Math.PI / 2;
}

function ringPoint(geometry: Geometry, field: number, radius = RING_RADIUS): [number, number] {
  const angle = fieldAngle(geometry, field);
  return [CENTER + Math.cos(angle) * radius, CENTER + Math.sin(angle) * radius];
}

function svgEl<K extends keyof SVGElementTagNameMap>(
  name: K,
  attrs: Record<string, string | number>,
): SVGElementTagNameMap[K] {
  const node = document.createElementNS("http://www.w3.org/2000/svg", name);
  for (const [key, value] of Object.entries(attrs)) node.setAttribute(key, String(value));
  return node;
}

export interface BoardOptions {
  geometry: Geometry;
  occupied: number[];
  /** Ring fields the current offered move set can reach, highlighted (UI-4). */
  highlighted: Set<number>;
}

export function renderBoard(frame: Frame, options: BoardOptions): SVGSVGElement {
  const { geometry, occupied, highlighted } = options;
  const svg = svgEl("svg", {
    viewBox: `0 0 ${SIZE} ${SIZE}`,
    class: "board",
    role: "img",
    "aria-label": `${geometry.seats}-seat board`,
  });

  // -- ring fields ---------------------------------------------------------
  for (let field = 0; field < geometry.ringLength; field += 1) {
    const [x, y] = ringPoint(geometry, field);
    const owner = occupied.find((seat) => ringField(geometry, seat, 1) === field);
    const isBarrier = frame.barrierFields.has(field);
    const circle = svgEl("circle", {
      cx: x,
      cy: y,
      r: FIELD_RADIUS,
      class: `field${owner !== undefined ? " entry" : ""}${isBarrier ? " barrier" : ""}${
        highlighted.has(field) ? " target" : ""
      }`,
    });
    if (owner !== undefined) circle.setAttribute("stroke", SEAT_COLORS[owner % 6] ?? "#888");
    svg.append(circle);
  }

  // -- goal columns, radiating inward from each seat's goal entry -----------
  for (const seat of occupied) {
    const entryField = ringField(geometry, seat, geometry.ringLength);
    const angle = fieldAngle(geometry, entryField);
    for (let index = 0; index < GOAL_FIELDS; index += 1) {
      const radius = RING_RADIUS - 34 - index * 30;
      svg.append(
        svgEl("circle", {
          cx: CENTER + Math.cos(angle) * radius,
          cy: CENTER + Math.sin(angle) * radius,
          r: FIELD_RADIUS - 1,
          class: "goal",
          stroke: SEAT_COLORS[seat % 6] ?? "#888",
        }),
      );
    }
  }

  // -- yards ---------------------------------------------------------------
  for (const seat of occupied) {
    const angle = fieldAngle(geometry, ringField(geometry, seat, 1));
    for (let index = 0; index < PIECES_PER_SEAT; index += 1) {
      const radius = RING_RADIUS + 32 + (index % 2) * 26;
      const spread = (index < 2 ? -1 : 1) * 0.055;
      svg.append(
        svgEl("circle", {
          cx: CENTER + Math.cos(angle + spread) * radius,
          cy: CENTER + Math.sin(angle + spread) * radius,
          r: FIELD_RADIUS - 2,
          class: "yard",
          stroke: SEAT_COLORS[seat % 6] ?? "#888",
        }),
      );
    }
  }

  // -- pieces --------------------------------------------------------------
  // Drawn last so they sit above the fields, and grouped per field so a
  // barrier's two pieces are visibly offset rather than one hiding the other.
  const perField = new Map<string, number>();
  for (const seat of occupied) {
    for (let piece = 0; piece < PIECES_PER_SEAT; piece += 1) {
      const pos = frame.positions[seat * PIECES_PER_SEAT + piece] ?? 0;
      const color = SEAT_COLORS[seat % 6] ?? "#888";
      let cx: number;
      let cy: number;

      if (pos === 0) {
        const slot = perField.get(`yard-${seat}`) ?? 0;
        perField.set(`yard-${seat}`, slot + 1);
        const angle = fieldAngle(geometry, ringField(geometry, seat, 1));
        const radius = RING_RADIUS + 32 + (slot % 2) * 26;
        const spread = (slot < 2 ? -1 : 1) * 0.055;
        cx = CENTER + Math.cos(angle + spread) * radius;
        cy = CENTER + Math.sin(angle + spread) * radius;
      } else if (pos <= geometry.ringLength) {
        const field = ringField(geometry, seat, pos);
        const stack = perField.get(`ring-${field}`) ?? 0;
        perField.set(`ring-${field}`, stack + 1);
        const [x, y] = ringPoint(geometry, field, RING_RADIUS + stack * 9);
        cx = x;
        cy = y;
      } else {
        const index = pos - geometry.ringLength - 1;
        const angle = fieldAngle(geometry, ringField(geometry, seat, geometry.ringLength));
        const radius = RING_RADIUS - 34 - index * 30;
        cx = CENTER + Math.cos(angle) * radius;
        cy = CENTER + Math.sin(angle) * radius;
      }

      const node = svgEl("circle", { cx, cy, r: FIELD_RADIUS - 3, class: "piece", fill: color });
      node.append(
        svgEl("title", {}).appendChild(
          document.createTextNode(`seat ${seat} piece ${piece} @ ${pos}`),
        ).parentNode as SVGElement,
      );
      svg.append(node);
    }
  }

  return svg;
}

/** Ring fields the offered move set can land on, for the UI-4 highlight. */
export function highlightedFields(frame: Frame, geometry: Geometry): Set<number> {
  const fields = new Set<number>();
  const offered = frame.offered;
  if (offered === null || offered.e !== "move") return fields;
  for (const [piece, , toPos] of offered.legal) {
    if (toPos >= 1 && toPos <= geometry.ringLength) {
      fields.add(ringField(geometry, Math.floor(piece / PIECES_PER_SEAT), toPos));
    }
  }
  return fields;
}

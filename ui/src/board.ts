/**
 * Board rendering (UI-3).
 *
 * The 4-seat board is the cross on an 11×11 grid: 40 fields around its outer edge, four yards
 * in the corners, and four goal columns running into the middle. It is built from one quadrant
 * of ten fields rotated three times, so §2.1's property that positions are a pure function of
 * (seats, seat index) carries into the drawing.
 *
 * The 6-seat board has no canonical printing, so it is the same construction generalised: six
 * arms, with the radius following the V the cross makes (5.1 → 1.41 → 5.1 grid units per
 * quadrant).
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
const FIELD_RADIUS = 12;
/**
 * Breathing room in the viewBox rather than shrunk content. The outermost things on the board
 * are the yards, and on the 6-seat star they sit at radius 0.56·SIZE from a centre at 0.5·SIZE,
 * so they run past the edge of the track's own square. The stroke on the outline adds another
 * 13 a side.
 */
const PAD = 66;

/** The 11×11 grid the classic 4-player board is printed on. */
const GRID = 11;
const CELL = SIZE / GRID;

type Point = [number, number];

function cellPoint([gx, gy]: Point): Point {
  return [(gx + 0.5) * CELL, (gy + 0.5) * CELL];
}

/** Quarter turn about the board centre. */
function rotate([gx, gy]: Point): Point {
  return [GRID - 1 - gy, gx];
}

function rotateTimes(point: Point, times: number): Point {
  let result = point;
  for (let index = 0; index < times; index += 1) result = rotate(result);
  return result;
}

/**
 * One quadrant of the ring: five fields inward along an arm's edge, four back out along the next
 * arm's edge, then the field at the tip. Field 0 is seat 0's entry, and rotating the quadrant
 * puts every other entry exactly `spacing` fields later, as §2.1 requires.
 */
const QUADRANT: Point[] = [
  [0, 4], [1, 4], [2, 4], [3, 4], [4, 4],
  [4, 3], [4, 2], [4, 1], [4, 0], [5, 0],
];

/** Seat 0's goal column, running inward between the two horizontal arms. */
const GOAL_COLUMN: Point[] = [[1, 5], [2, 5], [3, 5], [4, 5]];

/** Seat 0's yard: the corner block beside its entry. */
const YARD_BLOCK: Point[] = [[0, 0], [1, 0], [0, 1], [1, 1]];

/** The 6-arm generalisation, with the cross's V-shaped radius profile. */
function starPoint(geometry: Geometry, field: number): Point {
  const perArm = geometry.spacing;
  const arm = Math.floor(field / perArm);
  const index = field % perArm;
  const inward = Math.ceil(perArm / 2);
  const outer = SIZE * 0.40;
  const inner = SIZE * 0.13;
  const along =
    index < inward
      ? index / (inward - 1)
      : 1 - (index - inward + 1) / (perArm - inward);
  const radius = outer - (outer - inner) * along;
  const angle =
    ((arm + (index + 0.5) / perArm) / geometry.seats) * Math.PI * 2 - Math.PI / 2;
  return [CENTER + Math.cos(angle) * radius, CENTER + Math.sin(angle) * radius];
}

/** Absolute position of ring field `field`. */
export function fieldPoint(geometry: Geometry, field: number): Point {
  if (geometry.seats !== 4) return starPoint(geometry, field);
  const arm = Math.floor(field / geometry.spacing);
  const index = field % geometry.spacing;
  return cellPoint(rotateTimes(QUADRANT[index] as Point, arm));
}

/** Position of `seat`'s goal field `index` (0 = outermost). */
function goalPoint(geometry: Geometry, seat: number, index: number): Point {
  if (geometry.seats === 4) {
    return cellPoint(rotateTimes(GOAL_COLUMN[index] as Point, seat));
  }
  const [x, y] = starPoint(geometry, ringField(geometry, seat, geometry.ringLength));
  const angle = Math.atan2(y - CENTER, x - CENTER);
  const radius = SIZE * 0.23 - index * (SIZE * 0.042);
  return [CENTER + Math.cos(angle) * radius, CENTER + Math.sin(angle) * radius];
}

/** Position of `seat`'s yard slot `index`. */
function yardPoint(geometry: Geometry, seat: number, index: number): Point {
  if (geometry.seats === 4) {
    return cellPoint(rotateTimes(YARD_BLOCK[index] as Point, seat));
  }
  const [x, y] = starPoint(geometry, ringField(geometry, seat, 1));
  const angle = Math.atan2(y - CENTER, x - CENTER);
  // Set well clear of the track. On the star the entry field sits at an arm tip, so the yard
  // radius has to exceed the track's outer radius for a yard to land on the board rather than
  // beside it.
  const radius = SIZE * 0.51 + (index % 2) * (SIZE * 0.05);
  const spread = (index < 2 ? -1 : 1) * 0.058;
  return [
    CENTER + Math.cos(angle + spread) * radius,
    CENTER + Math.sin(angle + spread) * radius,
  ];
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
    viewBox: `${-PAD} ${-PAD} ${SIZE + 2 * PAD} ${SIZE + 2 * PAD}`,
    class: "board",
    role: "img",
    "aria-label": `${geometry.seats}-seat board`,
  });

  // The printed outline of the track: the ring fields in order are exactly the cross's perimeter.
  const outline: Point[] = [];
  for (let field = 0; field < geometry.ringLength; field += 1) {
    outline.push(fieldPoint(geometry, field));
  }
  svg.append(
    svgEl("polygon", {
      points: outline.map(([x, y]) => `${x},${y}`).join(" "),
      class: "board-outline",
    }),
  );

  for (let field = 0; field < geometry.ringLength; field += 1) {
    const [x, y] = fieldPoint(geometry, field);
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

  // Goals and yards are drawn for every seat the board has, occupied or not: the seat count is a
  // property of the geometry rather than of the player count, and cells with players < seats
  // always leave some of them vacant.
  for (let seat = 0; seat < geometry.seats; seat += 1) {
    const color = SEAT_COLORS[seat % 6] ?? "#888";
    const vacant = occupied.includes(seat) ? "" : " vacant";
    for (let index = 0; index < GOAL_FIELDS; index += 1) {
      const [x, y] = goalPoint(geometry, seat, index);
      svg.append(
        svgEl("circle", {
          cx: x, cy: y, r: FIELD_RADIUS - 1, class: `goal${vacant}`, stroke: color,
        }),
      );
    }
    for (let index = 0; index < PIECES_PER_SEAT; index += 1) {
      const [x, y] = yardPoint(geometry, seat, index);
      svg.append(
        svgEl("circle", {
          cx: x, cy: y, r: FIELD_RADIUS - 2, class: `yard${vacant}`, stroke: color,
        }),
      );
    }
  }

  // Pieces last, so they sit above the fields, and offset per field so both of a barrier's two
  // pieces stay visible.
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
        [cx, cy] = yardPoint(geometry, seat, slot);
      } else if (pos <= geometry.ringLength) {
        const field = ringField(geometry, seat, pos);
        const stack = perField.get(`ring-${field}`) ?? 0;
        perField.set(`ring-${field}`, stack + 1);
        const [x, y] = fieldPoint(geometry, field);
        cx = x + stack * 7;
        cy = y - stack * 7;
      } else {
        [cx, cy] = goalPoint(geometry, seat, pos - geometry.ringLength - 1);
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

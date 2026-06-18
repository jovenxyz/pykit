"""Bresenham's line and circle rasterization."""
from __future__ import annotations

from typing import List, Tuple

Point = Tuple[int, int]


def line(x0: int, y0: int, x1: int, y1: int) -> List[Point]:
    """Return every integer pixel on the line from ``(x0, y0)`` to ``(x1, y1)``."""
    points: List[Point] = []
    dx = abs(x1 - x0)
    dy = -abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx + dy
    x, y = x0, y0
    while True:
        points.append((x, y))
        if x == x1 and y == y1:
            return points
        e2 = 2 * err
        if e2 >= dy:
            err += dy
            x += sx
        if e2 <= dx:
            err += dx
            y += sy


def circle(cx: int, cy: int, radius: int) -> List[Point]:
    """Return every integer pixel on the circle of ``radius`` at ``(cx, cy)``."""
    if radius < 0:
        raise ValueError("radius must be non-negative")
    points: List[Point] = []
    x = radius
    y = 0
    err = 0
    while x >= y:
        points.extend([
            (cx + x, cy + y), (cx + y, cy + x),
            (cx - y, cy + x), (cx - x, cy + y),
            (cx - x, cy - y), (cx - y, cy - x),
            (cx + y, cy - x), (cx + x, cy - y),
        ])
        y += 1
        err += 1 + 2 * y
        if 2 * (err - x) + 1 > 0:
            x -= 1
            err += 1 - 2 * x
    seen = set()
    deduped: List[Point] = []
    for p in points:
        if p not in seen:
            seen.add(p)
            deduped.append(p)
    return deduped

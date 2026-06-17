"""Andrew's monotone chain convex hull on 2-D points."""
from __future__ import annotations

from typing import List, Sequence, Tuple

Point = Tuple[float, float]


def _cross(o: Point, a: Point, b: Point) -> float:
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def convex_hull(points: Sequence[Point]) -> List[Point]:
    """Return the convex hull of ``points`` in counter-clockwise order.

    Collinear and duplicate points on the hull edges are excluded. The
    first point is the lexicographically smallest one.
    """
    cleaned = sorted(set(points))
    if len(cleaned) <= 2:
        return list(cleaned)
    lower: List[Point] = []
    for p in cleaned:
        while len(lower) >= 2 and _cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper: List[Point] = []
    for p in reversed(cleaned):
        while len(upper) >= 2 and _cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]


def polygon_area(points: Sequence[Point]) -> float:
    """Return the signed area of a simple polygon (positive when CCW)."""
    n = len(points)
    if n < 3:
        return 0.0
    total = 0.0
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        total += x1 * y2 - x2 * y1
    return total / 2

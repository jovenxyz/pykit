"""Point-in-polygon tests and basic measurements for simple 2-D polygons."""
from __future__ import annotations

from typing import Sequence, Tuple

Point = Tuple[float, float]


def point_in_polygon(point: Point, polygon: Sequence[Point]) -> bool:
    """Return ``True`` if ``point`` is inside ``polygon`` (ray-cast test)."""
    if len(polygon) < 3:
        raise ValueError("polygon must have at least three vertices")
    x, y = point
    inside = False
    n = len(polygon)
    j = n - 1
    for i in range(n):
        xi, yi = polygon[i]
        xj, yj = polygon[j]
        if ((yi > y) != (yj > y)) and (
            x < (xj - xi) * (y - yi) / (yj - yi) + xi
        ):
            inside = not inside
        j = i
    return inside


def bounding_box(polygon: Sequence[Point]) -> Tuple[Point, Point]:
    """Return ``(min_corner, max_corner)`` of the axis-aligned bounding box."""
    if not polygon:
        raise ValueError("polygon must have at least one vertex")
    xs = [p[0] for p in polygon]
    ys = [p[1] for p in polygon]
    return (min(xs), min(ys)), (max(xs), max(ys))


def signed_area(polygon: Sequence[Point]) -> float:
    """Signed shoelace area (positive when vertices are counter-clockwise)."""
    n = len(polygon)
    if n < 3:
        return 0.0
    total = 0.0
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]
        total += x1 * y2 - x2 * y1
    return total / 2

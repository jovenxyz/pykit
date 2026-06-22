"""Triangle geometry: classification, area (Heron), perimeter, angles, centroid."""
from __future__ import annotations
from dataclasses import dataclass
import math


def _valid_sides(a: float, b: float, c: float) -> bool:
    return a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a


def is_triangle(a: float, b: float, c: float) -> bool:
    return _valid_sides(a, b, c)


def perimeter(a: float, b: float, c: float) -> float:
    if not _valid_sides(a, b, c):
        raise ValueError("invalid triangle sides")
    return a + b + c


def area(a: float, b: float, c: float) -> float:
    """Heron's formula."""
    if not _valid_sides(a, b, c):
        raise ValueError("invalid triangle sides")
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


def classify_by_sides(a: float, b: float, c: float) -> str:
    if not _valid_sides(a, b, c):
        raise ValueError("invalid triangle sides")
    if math.isclose(a, b) and math.isclose(b, c):
        return "equilateral"
    if math.isclose(a, b) or math.isclose(b, c) or math.isclose(a, c):
        return "isosceles"
    return "scalene"


def classify_by_angles(a: float, b: float, c: float) -> str:
    if not _valid_sides(a, b, c):
        raise ValueError("invalid triangle sides")
    sides = sorted([a, b, c])
    x, y, z = sides
    lhs = x * x + y * y
    rhs = z * z
    if math.isclose(lhs, rhs):
        return "right"
    if lhs > rhs:
        return "acute"
    return "obtuse"


def angles(a: float, b: float, c: float) -> tuple[float, float, float]:
    """Return interior angles (radians) opposite to a, b, c via law of cosines."""
    if not _valid_sides(a, b, c):
        raise ValueError("invalid triangle sides")
    A = math.acos((b * b + c * c - a * a) / (2 * b * c))
    B = math.acos((a * a + c * c - b * b) / (2 * a * c))
    C = math.pi - A - B
    return A, B, C


@dataclass(frozen=True)
class Point:
    x: float
    y: float


def centroid(p1: Point, p2: Point, p3: Point) -> Point:
    return Point((p1.x + p2.x + p3.x) / 3, (p1.y + p2.y + p3.y) / 3)


def area_from_points(p1: Point, p2: Point, p3: Point) -> float:
    """Shoelace formula."""
    return abs(
        p1.x * (p2.y - p3.y) + p2.x * (p3.y - p1.y) + p3.x * (p1.y - p2.y)
    ) / 2

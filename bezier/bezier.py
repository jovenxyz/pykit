"""Quadratic and cubic Bezier curve evaluation and sampling."""
from __future__ import annotations

from typing import List, Tuple

Point = Tuple[float, float]


def quadratic(p0: Point, p1: Point, p2: Point, t: float) -> Point:
    """Evaluate a quadratic Bezier curve at parameter ``t in [0, 1]``."""
    if not 0 <= t <= 1:
        raise ValueError("t must be in [0, 1]")
    u = 1 - t
    x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
    y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
    return x, y


def cubic(p0: Point, p1: Point, p2: Point, p3: Point, t: float) -> Point:
    """Evaluate a cubic Bezier curve at parameter ``t in [0, 1]``."""
    if not 0 <= t <= 1:
        raise ValueError("t must be in [0, 1]")
    u = 1 - t
    uu = u * u
    tt = t * t
    x = (
        uu * u * p0[0]
        + 3 * uu * t * p1[0]
        + 3 * u * tt * p2[0]
        + tt * t * p3[0]
    )
    y = (
        uu * u * p0[1]
        + 3 * uu * t * p1[1]
        + 3 * u * tt * p2[1]
        + tt * t * p3[1]
    )
    return x, y


def sample(control_points: List[Point], *, steps: int = 32) -> List[Point]:
    """Sample a Bezier curve (quadratic or cubic) at ``steps + 1`` points."""
    if steps <= 0:
        raise ValueError("steps must be positive")
    if len(control_points) == 3:
        evaluator = lambda t: quadratic(*control_points, t)
    elif len(control_points) == 4:
        evaluator = lambda t: cubic(*control_points, t)
    else:
        raise ValueError("only quadratic (3) and cubic (4) curves are supported")
    return [evaluator(i / steps) for i in range(steps + 1)]


def de_casteljau(control_points: List[Point], t: float) -> Point:
    """Evaluate a Bezier curve of arbitrary degree via De Casteljau."""
    if not 0 <= t <= 1:
        raise ValueError("t must be in [0, 1]")
    if not control_points:
        raise ValueError("at least one control point is required")
    points = [tuple(p) for p in control_points]
    while len(points) > 1:
        points = [
            (
                (1 - t) * a[0] + t * b[0],
                (1 - t) * a[1] + t * b[1],
            )
            for a, b in zip(points, points[1:])
        ]
    return points[0]

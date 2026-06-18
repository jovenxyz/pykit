"""2D vector helpers."""
from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass(frozen=True)
class Vec2:
    x: float
    y: float

    def __add__(self, other: "Vec2") -> "Vec2":
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vec2") -> "Vec2":
        return Vec2(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float) -> "Vec2":
        return Vec2(self.x * scalar, self.y * scalar)

    __rmul__ = __mul__

    def __neg__(self) -> "Vec2":
        return Vec2(-self.x, -self.y)

    def dot(self, other: "Vec2") -> float:
        return self.x * other.x + self.y * other.y

    def cross(self, other: "Vec2") -> float:
        """Scalar Z-component of the 3-D cross product."""
        return self.x * other.y - self.y * other.x

    def length(self) -> float:
        return math.hypot(self.x, self.y)

    def length_squared(self) -> float:
        return self.x * self.x + self.y * self.y

    def normalize(self) -> "Vec2":
        length = self.length()
        if length == 0:
            raise ValueError("cannot normalise the zero vector")
        return Vec2(self.x / length, self.y / length)

    def rotate(self, radians: float) -> "Vec2":
        c, s = math.cos(radians), math.sin(radians)
        return Vec2(self.x * c - self.y * s, self.x * s + self.y * c)

    def angle(self) -> float:
        """Angle (radians) of the vector from the positive X axis."""
        return math.atan2(self.y, self.x)


def distance(a: Vec2, b: Vec2) -> float:
    return (a - b).length()


def lerp(a: Vec2, b: Vec2, t: float) -> Vec2:
    """Linear interpolation between ``a`` and ``b`` at ``t in [0, 1]``."""
    return Vec2(a.x + (b.x - a.x) * t, a.y + (b.y - a.y) * t)

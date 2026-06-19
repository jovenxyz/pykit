"""3D vector helpers."""
from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass(frozen=True)
class Vec3:
    x: float
    y: float
    z: float

    def __add__(self, other: "Vec3") -> "Vec3":
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: "Vec3") -> "Vec3":
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar: float) -> "Vec3":
        return Vec3(self.x * scalar, self.y * scalar, self.z * scalar)

    __rmul__ = __mul__

    def __neg__(self) -> "Vec3":
        return Vec3(-self.x, -self.y, -self.z)

    def dot(self, other: "Vec3") -> float:
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other: "Vec3") -> "Vec3":
        return Vec3(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x,
        )

    def length(self) -> float:
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def length_squared(self) -> float:
        return self.x * self.x + self.y * self.y + self.z * self.z

    def normalize(self) -> "Vec3":
        length = self.length()
        if length == 0:
            raise ValueError("cannot normalise the zero vector")
        return Vec3(self.x / length, self.y / length, self.z / length)


def distance(a: Vec3, b: Vec3) -> float:
    return (a - b).length()


def lerp(a: Vec3, b: Vec3, t: float) -> Vec3:
    return Vec3(
        a.x + (b.x - a.x) * t,
        a.y + (b.y - a.y) * t,
        a.z + (b.z - a.z) * t,
    )


def angle_between(a: Vec3, b: Vec3) -> float:
    """Return the angle in radians between two non-zero vectors."""
    la = a.length()
    lb = b.length()
    if la == 0 or lb == 0:
        raise ValueError("angle is undefined for the zero vector")
    cos_theta = max(-1.0, min(1.0, a.dot(b) / (la * lb)))
    return math.acos(cos_theta)

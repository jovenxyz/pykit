"""Quaternion arithmetic for 3D rotations."""
from __future__ import annotations
from dataclasses import dataclass
import math


@dataclass(frozen=True)
class Quaternion:
    w: float
    x: float
    y: float
    z: float

    def __add__(self, other: "Quaternion") -> "Quaternion":
        return Quaternion(self.w + other.w, self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: "Quaternion") -> "Quaternion":
        return Quaternion(self.w - other.w, self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if isinstance(other, Quaternion):
            a1, b1, c1, d1 = self.w, self.x, self.y, self.z
            a2, b2, c2, d2 = other.w, other.x, other.y, other.z
            return Quaternion(
                a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2,
                a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2,
                a1 * c2 - b1 * d2 + c1 * a2 + d1 * b2,
                a1 * d2 + b1 * c2 - c1 * b2 + d1 * a2,
            )
        return Quaternion(self.w * other, self.x * other, self.y * other, self.z * other)

    def __rmul__(self, scalar: float) -> "Quaternion":
        return self.__mul__(scalar)

    def conjugate(self) -> "Quaternion":
        return Quaternion(self.w, -self.x, -self.y, -self.z)

    def norm_squared(self) -> float:
        return self.w * self.w + self.x * self.x + self.y * self.y + self.z * self.z

    def norm(self) -> float:
        return math.sqrt(self.norm_squared())

    def normalize(self) -> "Quaternion":
        n = self.norm()
        if n == 0:
            raise ValueError("cannot normalize zero quaternion")
        return Quaternion(self.w / n, self.x / n, self.y / n, self.z / n)

    def inverse(self) -> "Quaternion":
        n2 = self.norm_squared()
        if n2 == 0:
            raise ValueError("zero quaternion has no inverse")
        c = self.conjugate()
        return Quaternion(c.w / n2, c.x / n2, c.y / n2, c.z / n2)


def from_axis_angle(axis: tuple[float, float, float], angle: float) -> Quaternion:
    ax, ay, az = axis
    n = math.sqrt(ax * ax + ay * ay + az * az)
    if n == 0:
        raise ValueError("axis must be non-zero")
    ax, ay, az = ax / n, ay / n, az / n
    half = angle / 2
    s = math.sin(half)
    return Quaternion(math.cos(half), ax * s, ay * s, az * s)


def rotate_vector(q: Quaternion, v: tuple[float, float, float]) -> tuple[float, float, float]:
    p = Quaternion(0.0, v[0], v[1], v[2])
    r = q * p * q.conjugate()
    return (r.x, r.y, r.z)

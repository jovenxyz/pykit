"""2x2 matrix algebra: arithmetic, determinant, inverse, transpose, eigenvalues."""
from __future__ import annotations
from dataclasses import dataclass
import math


@dataclass(frozen=True)
class Mat2:
    a: float
    b: float
    c: float
    d: float  # [[a, b], [c, d]]

    def __add__(self, other: "Mat2") -> "Mat2":
        return Mat2(self.a + other.a, self.b + other.b, self.c + other.c, self.d + other.d)

    def __sub__(self, other: "Mat2") -> "Mat2":
        return Mat2(self.a - other.a, self.b - other.b, self.c - other.c, self.d - other.d)

    def __mul__(self, other):
        if isinstance(other, Mat2):
            return Mat2(
                self.a * other.a + self.b * other.c,
                self.a * other.b + self.b * other.d,
                self.c * other.a + self.d * other.c,
                self.c * other.b + self.d * other.d,
            )
        return Mat2(self.a * other, self.b * other, self.c * other, self.d * other)

    def __rmul__(self, scalar: float) -> "Mat2":
        return self.__mul__(scalar)

    def apply(self, v: tuple[float, float]) -> tuple[float, float]:
        x, y = v
        return (self.a * x + self.b * y, self.c * x + self.d * y)

    def transpose(self) -> "Mat2":
        return Mat2(self.a, self.c, self.b, self.d)

    def det(self) -> float:
        return self.a * self.d - self.b * self.c

    def trace(self) -> float:
        return self.a + self.d

    def inverse(self) -> "Mat2":
        d = self.det()
        if d == 0:
            raise ValueError("matrix is singular; no inverse")
        return Mat2(self.d / d, -self.b / d, -self.c / d, self.a / d)

    def eigenvalues(self) -> tuple[complex, complex]:
        """Eigenvalues via the characteristic polynomial λ² − tr λ + det = 0."""
        t = self.trace()
        disc = t * t - 4 * self.det()
        if disc >= 0:
            r = math.sqrt(disc)
            return ((t + r) / 2, (t - r) / 2)
        r = math.sqrt(-disc)
        return (complex(t / 2, r / 2), complex(t / 2, -r / 2))


def identity() -> Mat2:
    return Mat2(1, 0, 0, 1)


def rotation(angle: float) -> Mat2:
    """2D rotation matrix."""
    c, s = math.cos(angle), math.sin(angle)
    return Mat2(c, -s, s, c)


def scale(sx: float, sy: float | None = None) -> Mat2:
    if sy is None:
        sy = sx
    return Mat2(sx, 0, 0, sy)

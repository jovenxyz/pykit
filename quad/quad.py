"""Numerical integration: trapezoidal rule and Simpson's rule."""
from __future__ import annotations

from typing import Callable


def trapezoidal(
    f: Callable[[float], float],
    a: float,
    b: float,
    *,
    n: int = 1000,
) -> float:
    """Approximate the integral of ``f`` on ``[a, b]`` (composite trapezoidal)."""
    if n <= 0:
        raise ValueError("n must be positive")
    if a == b:
        return 0.0
    h = (b - a) / n
    total = (f(a) + f(b)) / 2
    for i in range(1, n):
        total += f(a + i * h)
    return total * h


def simpson(
    f: Callable[[float], float],
    a: float,
    b: float,
    *,
    n: int = 1000,
) -> float:
    """Approximate the integral of ``f`` on ``[a, b]`` (composite Simpson)."""
    if n <= 0:
        raise ValueError("n must be positive")
    if n % 2:
        raise ValueError("n must be even for Simpson's rule")
    if a == b:
        return 0.0
    h = (b - a) / n
    total = f(a) + f(b)
    for i in range(1, n):
        x = a + i * h
        total += 4 * f(x) if i % 2 else 2 * f(x)
    return total * h / 3

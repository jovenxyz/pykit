"""Polynomial evaluation, differentiation, and Newton-method root finding."""
from __future__ import annotations

from typing import List, Sequence


def evaluate(coefficients: Sequence[float], x: float) -> float:
    """Evaluate ``a0 + a1*x + a2*x^2 + ... + an*x^n`` using Horner's method."""
    if not coefficients:
        return 0.0
    result = 0.0
    for coefficient in reversed(coefficients):
        result = result * x + coefficient
    return result


def derivative(coefficients: Sequence[float]) -> List[float]:
    """Return the coefficients of the formal derivative polynomial."""
    if len(coefficients) <= 1:
        return [0.0]
    return [coefficients[i] * i for i in range(1, len(coefficients))]


def degree(coefficients: Sequence[float]) -> int:
    """Return the degree, ignoring trailing zero coefficients."""
    last = -1
    for i, c in enumerate(coefficients):
        if c != 0:
            last = i
    return max(last, 0)


def newton_root(
    coefficients: Sequence[float],
    initial: float,
    *,
    tolerance: float = 1e-12,
    max_iterations: int = 100,
) -> float:
    """Find a real root near ``initial`` using Newton's method."""
    deriv = derivative(coefficients)
    x = initial
    for _ in range(max_iterations):
        fx = evaluate(coefficients, x)
        if abs(fx) < tolerance:
            return x
        dfx = evaluate(deriv, x)
        if dfx == 0:
            raise ValueError(f"derivative is zero at x={x}")
        x -= fx / dfx
    raise ValueError("Newton's method did not converge")

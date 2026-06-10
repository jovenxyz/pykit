"""Continued-fraction expansions and convergent rationals."""
from __future__ import annotations

from fractions import Fraction
from math import floor
from typing import List


def expand_rational(numerator: int, denominator: int) -> List[int]:
    """Return the continued-fraction expansion of ``numerator/denominator``."""
    if denominator == 0:
        raise ValueError("denominator must be non-zero")
    if denominator < 0:
        numerator, denominator = -numerator, -denominator
    coefficients: List[int] = []
    while denominator:
        q, r = divmod(numerator, denominator)
        coefficients.append(q)
        numerator, denominator = denominator, r
    return coefficients


def expand_real(value: float, *, terms: int = 10) -> List[int]:
    """Return up to ``terms`` continued-fraction coefficients of ``value``."""
    if terms < 1:
        raise ValueError("terms must be >= 1")
    coefficients: List[int] = []
    for _ in range(terms):
        whole = floor(value)
        coefficients.append(int(whole))
        frac = value - whole
        if frac == 0:
            break
        value = 1.0 / frac
    return coefficients


def convergent(coefficients: List[int]) -> Fraction:
    """Return the :class:`Fraction` from a finite continued-fraction expansion."""
    if not coefficients:
        raise ValueError("at least one coefficient is required")
    result = Fraction(coefficients[-1])
    for coefficient in reversed(coefficients[:-1]):
        result = coefficient + Fraction(1) / result
    return result


def convergents(coefficients: List[int]) -> List[Fraction]:
    """Return the sequence of convergents (partial expansions)."""
    return [convergent(coefficients[: i + 1]) for i in range(len(coefficients))]

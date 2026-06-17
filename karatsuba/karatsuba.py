"""Karatsuba's divide-and-conquer integer multiplication."""
from __future__ import annotations


def karatsuba(x: int, y: int, *, cutoff: int = 64) -> int:
    """Return ``x * y`` using Karatsuba's algorithm.

    Falls back to ordinary multiplication once either factor fits in
    ``cutoff`` bits, where the recursion overhead outweighs the savings.
    """
    if cutoff <= 0:
        raise ValueError("cutoff must be positive")
    sign = 1
    if x < 0:
        x = -x
        sign = -sign
    if y < 0:
        y = -y
        sign = -sign
    return sign * _karatsuba(x, y, cutoff)


def _karatsuba(x: int, y: int, cutoff: int) -> int:
    if x.bit_length() <= cutoff or y.bit_length() <= cutoff:
        return x * y
    n = max(x.bit_length(), y.bit_length())
    m = n // 2
    mask = (1 << m) - 1
    x_low = x & mask
    x_high = x >> m
    y_low = y & mask
    y_high = y >> m
    z0 = _karatsuba(x_low, y_low, cutoff)
    z2 = _karatsuba(x_high, y_high, cutoff)
    z1 = _karatsuba(x_low + x_high, y_low + y_high, cutoff) - z0 - z2
    return (z2 << (2 * m)) + (z1 << m) + z0

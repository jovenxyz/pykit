"""Convert between (x, y) coordinates and Hilbert-curve indices.

The Hilbert curve is a space-filling curve that preserves locality: points
close in 1-D index space are close in 2-D coordinate space.
"""
from __future__ import annotations

from typing import Tuple


def xy_to_d(order: int, x: int, y: int) -> int:
    """Convert ``(x, y)`` on a 2^order x 2^order grid to a Hilbert index."""
    n = 1 << order
    if not (0 <= x < n and 0 <= y < n):
        raise ValueError(f"coordinates must be in [0, {n})")
    d = 0
    s = n // 2
    while s > 0:
        rx = 1 if (x & s) > 0 else 0
        ry = 1 if (y & s) > 0 else 0
        d += s * s * ((3 * rx) ^ ry)
        x, y = _rotate(s, x, y, rx, ry)
        s //= 2
    return d


def d_to_xy(order: int, d: int) -> Tuple[int, int]:
    """Convert a Hilbert index back to ``(x, y)``."""
    n = 1 << order
    if not 0 <= d < n * n:
        raise ValueError(f"index must be in [0, {n * n})")
    x = y = 0
    s = 1
    t = d
    while s < n:
        rx = 1 & (t // 2)
        ry = 1 & (t ^ rx)
        x, y = _rotate(s, x, y, rx, ry)
        x += s * rx
        y += s * ry
        t //= 4
        s *= 2
    return x, y


def _rotate(s: int, x: int, y: int, rx: int, ry: int) -> Tuple[int, int]:
    if ry == 0:
        if rx == 1:
            x = s - 1 - x
            y = s - 1 - y
        x, y = y, x
    return x, y

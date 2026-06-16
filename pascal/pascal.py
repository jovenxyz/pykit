"""Pascal's triangle rows and binomial coefficients."""
from __future__ import annotations

from typing import List


def row(n: int) -> List[int]:
    """Return row ``n`` of Pascal's triangle (zero-indexed)."""
    if n < 0:
        raise ValueError("n must be non-negative")
    result = [1]
    for k in range(1, n + 1):
        result.append(result[-1] * (n - k + 1) // k)
    return result


def triangle(rows: int) -> List[List[int]]:
    """Return the first ``rows`` rows of Pascal's triangle."""
    if rows < 0:
        raise ValueError("rows must be non-negative")
    return [row(n) for n in range(rows)]


def binomial(n: int, k: int) -> int:
    """Return ``n choose k`` (binomial coefficient)."""
    if n < 0 or k < 0:
        raise ValueError("n and k must be non-negative")
    if k > n:
        return 0
    if k > n - k:
        k = n - k
    result = 1
    for i in range(k):
        result = result * (n - i) // (i + 1)
    return result

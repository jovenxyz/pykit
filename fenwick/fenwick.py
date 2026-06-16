"""Fenwick tree (Binary Indexed Tree) for prefix-sum queries."""
from __future__ import annotations

from typing import Union, Sequence


class Fenwick:
    """1-indexed prefix-sum structure with O(log n) updates and queries."""

    def __init__(self, size_or_values: Union[int, Sequence[float]]) -> None:
        if isinstance(size_or_values, int):
            if size_or_values < 0:
                raise ValueError("size must be non-negative")
            self._n = size_or_values
            self._tree = [0.0] * (self._n + 1)
        else:
            values = list(size_or_values)
            self._n = len(values)
            self._tree = [0.0] * (self._n + 1)
            # O(n) build.
            for i, value in enumerate(values, start=1):
                self._tree[i] += value
                j = i + (i & -i)
                if j <= self._n:
                    self._tree[j] += self._tree[i]

    def __len__(self) -> int:
        return self._n

    def add(self, index: int, delta: float) -> None:
        """Add ``delta`` to the value at zero-based ``index``."""
        if not 0 <= index < self._n:
            raise IndexError(f"index out of range: {index}")
        i = index + 1
        while i <= self._n:
            self._tree[i] += delta
            i += i & -i

    def prefix_sum(self, end: int) -> float:
        """Return the sum of values in ``[0, end)`` (half-open)."""
        if not 0 <= end <= self._n:
            raise IndexError(f"end out of range: {end}")
        i = end
        total = 0.0
        while i > 0:
            total += self._tree[i]
            i -= i & -i
        return total

    def range_sum(self, lo: int, hi: int) -> float:
        """Return the sum of values in the half-open range ``[lo, hi)``."""
        if not 0 <= lo <= hi <= self._n:
            raise IndexError(f"range out of bounds: [{lo}, {hi})")
        return self.prefix_sum(hi) - self.prefix_sum(lo)

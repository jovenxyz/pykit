"""A segment tree for range-sum queries with point updates."""
from __future__ import annotations

from typing import Sequence


class SegmentTree:
    """Sum-aggregating segment tree on a fixed-length sequence.

    ``query(lo, hi)`` returns the sum over the half-open interval
    ``[lo, hi)``; ``update(index, value)`` replaces the value at ``index``.
    Both operations run in O(log n).
    """

    def __init__(self, values: Sequence[float]) -> None:
        self._n = len(values)
        size = 1
        while size < max(self._n, 1):
            size *= 2
        self._size = size
        self._tree = [0.0] * (2 * size)
        for i, value in enumerate(values):
            self._tree[size + i] = value
        for i in range(size - 1, 0, -1):
            self._tree[i] = self._tree[2 * i] + self._tree[2 * i + 1]

    def __len__(self) -> int:
        return self._n

    def update(self, index: int, value: float) -> None:
        if not 0 <= index < self._n:
            raise IndexError(f"index out of range: {index}")
        i = self._size + index
        self._tree[i] = value
        i //= 2
        while i:
            self._tree[i] = self._tree[2 * i] + self._tree[2 * i + 1]
            i //= 2

    def query(self, lo: int, hi: int) -> float:
        if not 0 <= lo <= hi <= self._n:
            raise IndexError(f"range out of bounds: [{lo}, {hi})")
        left = self._size + lo
        right = self._size + hi
        total = 0.0
        while left < right:
            if left % 2 == 1:
                total += self._tree[left]
                left += 1
            if right % 2 == 1:
                right -= 1
                total += self._tree[right]
            left //= 2
            right //= 2
        return total

    def __getitem__(self, index: int) -> float:
        if not 0 <= index < self._n:
            raise IndexError(f"index out of range: {index}")
        return self._tree[self._size + index]

    def __setitem__(self, index: int, value: float) -> None:
        self.update(index, value)

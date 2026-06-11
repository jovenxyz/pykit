"""Streaming median over a stream of numbers (two-heap technique)."""
from __future__ import annotations

import heapq
from typing import List


class StreamingMedian:
    """Maintain the median of a number stream in O(log n) per push."""

    def __init__(self) -> None:
        # Lower half kept as a max-heap by negation.
        self._low: List[float] = []
        # Upper half kept as a min-heap.
        self._high: List[float] = []

    def push(self, value: float) -> None:
        if not self._low or value <= -self._low[0]:
            heapq.heappush(self._low, -value)
        else:
            heapq.heappush(self._high, value)
        if len(self._low) > len(self._high) + 1:
            heapq.heappush(self._high, -heapq.heappop(self._low))
        elif len(self._high) > len(self._low):
            heapq.heappush(self._low, -heapq.heappop(self._high))

    def median(self) -> float:
        """Return the current median.

        With an even count the average of the two middle values is returned.
        """
        if not self._low:
            raise ValueError("median of empty stream is undefined")
        if len(self._low) == len(self._high):
            return (-self._low[0] + self._high[0]) / 2
        return float(-self._low[0])

    def __len__(self) -> int:
        return len(self._low) + len(self._high)

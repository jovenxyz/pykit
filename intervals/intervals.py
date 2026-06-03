"""Merge and intersect closed integer intervals."""
from __future__ import annotations

from typing import Iterable, List, Optional, Tuple

Interval = Tuple[int, int]


def merge(intervals: Iterable[Interval]) -> List[Interval]:
    """Return a sorted list of non-overlapping, non-adjacent intervals.

    Adjacent or overlapping intervals are coalesced. Intervals are treated as
    inclusive on both ends, so ``(1, 3)`` and ``(4, 6)`` merge into
    ``(1, 6)``.
    """
    items = []
    for start, end in intervals:
        if start > end:
            raise ValueError(f"interval start must be <= end: ({start}, {end})")
        items.append((start, end))
    items.sort()
    merged: List[Interval] = []
    for start, end in items:
        if merged and start <= merged[-1][1] + 1:
            previous_start, previous_end = merged[-1]
            merged[-1] = (previous_start, max(previous_end, end))
        else:
            merged.append((start, end))
    return merged


def intersect(a: Interval, b: Interval) -> Optional[Interval]:
    """Return the overlap of two inclusive intervals, or ``None`` if none."""
    start = max(a[0], b[0])
    end = min(a[1], b[1])
    return (start, end) if start <= end else None


def length(intervals: Iterable[Interval]) -> int:
    """Total inclusive length covered by ``intervals`` (after merging)."""
    return sum(end - start + 1 for start, end in merge(intervals))

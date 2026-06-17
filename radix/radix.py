"""Least-significant-digit radix sort and counting sort."""
from __future__ import annotations

from typing import List, Sequence


def radix_sort(values: Sequence[int], *, base: int = 256) -> List[int]:
    """Sort ``values`` ascending using LSD radix sort.

    Negative numbers are supported by sorting magnitudes and flipping
    the negative bucket.
    """
    if base < 2:
        raise ValueError("base must be >= 2")
    if not values:
        return []
    positives = [v for v in values if v >= 0]
    negatives = [-v for v in values if v < 0]
    sorted_pos = _radix_sort_nonneg(positives, base)
    sorted_neg = _radix_sort_nonneg(negatives, base)
    return [-n for n in reversed(sorted_neg)] + sorted_pos


def _radix_sort_nonneg(values: List[int], base: int) -> List[int]:
    if not values:
        return []
    largest = max(values)
    place = 1
    result = list(values)
    while place <= largest:
        buckets: List[List[int]] = [[] for _ in range(base)]
        for v in result:
            buckets[(v // place) % base].append(v)
        result = [item for bucket in buckets for item in bucket]
        place *= base
    return result


def counting_sort(values: Sequence[int]) -> List[int]:
    """Sort small-range non-negative integers in O(n + max(values))."""
    if not values:
        return []
    if any(v < 0 for v in values):
        raise ValueError("counting_sort requires non-negative integers")
    largest = max(values)
    counts = [0] * (largest + 1)
    for v in values:
        counts[v] += 1
    result: List[int] = []
    for value, count in enumerate(counts):
        result.extend([value] * count)
    return result

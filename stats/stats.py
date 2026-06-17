"""Descriptive statistics: mean, median, variance, stdev, percentile."""
from __future__ import annotations

import math
from typing import Sequence, Tuple


def mean(values: Sequence[float]) -> float:
    if not values:
        raise ValueError("values must be non-empty")
    return sum(values) / len(values)


def median(values: Sequence[float]) -> float:
    if not values:
        raise ValueError("values must be non-empty")
    ordered = sorted(values)
    n = len(ordered)
    mid = n // 2
    if n % 2:
        return float(ordered[mid])
    return (ordered[mid - 1] + ordered[mid]) / 2


def variance(values: Sequence[float], *, sample: bool = True) -> float:
    if len(values) < (2 if sample else 1):
        raise ValueError(
            "sample variance needs >= 2 values; population variance needs >= 1"
        )
    mu = mean(values)
    total = sum((v - mu) ** 2 for v in values)
    return total / (len(values) - 1 if sample else len(values))


def stdev(values: Sequence[float], *, sample: bool = True) -> float:
    return math.sqrt(variance(values, sample=sample))


def percentile(values: Sequence[float], p: float) -> float:
    """Return the ``p``th percentile via linear interpolation (p in [0, 100])."""
    if not values:
        raise ValueError("values must be non-empty")
    if not 0 <= p <= 100:
        raise ValueError("p must be in [0, 100]")
    ordered = sorted(values)
    if len(ordered) == 1:
        return float(ordered[0])
    rank = (p / 100) * (len(ordered) - 1)
    lo = int(math.floor(rank))
    hi = int(math.ceil(rank))
    if lo == hi:
        return float(ordered[lo])
    fraction = rank - lo
    return ordered[lo] + fraction * (ordered[hi] - ordered[lo])


def quartiles(values: Sequence[float]) -> Tuple[float, float, float]:
    """Return ``(Q1, Q2, Q3)`` -- the 25th, 50th and 75th percentiles."""
    return (
        percentile(values, 25),
        percentile(values, 50),
        percentile(values, 75),
    )

"""0/1 knapsack: maximum value within a weight capacity."""
from __future__ import annotations

from typing import List, Sequence, Tuple


def _check(weights: Sequence[int], values: Sequence[float], capacity: int) -> None:
    if len(weights) != len(values):
        raise ValueError("weights and values must be the same length")
    if capacity < 0:
        raise ValueError("capacity must be non-negative")
    if any(w < 0 for w in weights):
        raise ValueError("weights must be non-negative")


def max_value(
    weights: Sequence[int],
    values: Sequence[float],
    capacity: int,
) -> float:
    """Return the maximum total value that fits within ``capacity``."""
    _check(weights, values, capacity)
    dp = [0.0] * (capacity + 1)
    for weight, value in zip(weights, values):
        if weight > capacity:
            continue
        for c in range(capacity, weight - 1, -1):
            candidate = dp[c - weight] + value
            if candidate > dp[c]:
                dp[c] = candidate
    return dp[capacity]


def chosen_items(
    weights: Sequence[int],
    values: Sequence[float],
    capacity: int,
) -> Tuple[float, List[int]]:
    """Return ``(value, indices)`` where ``indices`` is one optimal subset."""
    _check(weights, values, capacity)
    n = len(weights)
    dp = [[0.0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        weight = weights[i - 1]
        value = values[i - 1]
        for c in range(capacity + 1):
            dp[i][c] = dp[i - 1][c]
            if weight <= c:
                with_item = dp[i - 1][c - weight] + value
                if with_item > dp[i][c]:
                    dp[i][c] = with_item
    picked: List[int] = []
    c = capacity
    for i in range(n, 0, -1):
        if dp[i][c] != dp[i - 1][c]:
            picked.append(i - 1)
            c -= weights[i - 1]
    picked.reverse()
    return dp[n][capacity], picked

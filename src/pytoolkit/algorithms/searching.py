"""Linear and binary search helpers."""
from __future__ import annotations

from typing import List, Optional


def linear_search(values: List[int], target: int) -> Optional[int]:
    for index, value in enumerate(values):
        if value == target:
            return index
    return None


def binary_search(sorted_values: List[int], target: int) -> Optional[int]:
    low, high = 0, len(sorted_values) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_values[mid] == target:
            return mid
        if sorted_values[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return None

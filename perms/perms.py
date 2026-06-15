"""Lexicographic permutations, combinations and power set."""
from __future__ import annotations

from typing import Iterator, List, Sequence, TypeVar

T = TypeVar("T")


def permutations(items: Sequence[T]) -> Iterator[List[T]]:
    """Yield every permutation of ``items`` in lexicographic order."""
    n = len(items)
    indices = list(range(n))
    yield [items[i] for i in indices]
    while True:
        i = n - 2
        while i >= 0 and indices[i] >= indices[i + 1]:
            i -= 1
        if i < 0:
            return
        j = n - 1
        while indices[j] <= indices[i]:
            j -= 1
        indices[i], indices[j] = indices[j], indices[i]
        indices[i + 1:] = reversed(indices[i + 1:])
        yield [items[k] for k in indices]


def combinations(items: Sequence[T], k: int) -> Iterator[List[T]]:
    """Yield every k-element combination of ``items`` in lexicographic order."""
    if k < 0:
        raise ValueError("k must be non-negative")
    n = len(items)
    if k > n:
        return
    indices = list(range(k))
    yield [items[i] for i in indices]
    while True:
        for i in range(k - 1, -1, -1):
            if indices[i] != i + n - k:
                break
        else:
            return
        indices[i] += 1
        for j in range(i + 1, k):
            indices[j] = indices[j - 1] + 1
        yield [items[i] for i in indices]


def power_set(items: Sequence[T]) -> Iterator[List[T]]:
    """Yield every subset of ``items`` from smallest to largest."""
    for size in range(len(items) + 1):
        yield from combinations(items, size)

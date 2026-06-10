"""Damerau-Levenshtein edit distance with adjacent transpositions."""
from __future__ import annotations

from typing import List


def distance(a: str, b: str) -> int:
    """Return the optimal-string-alignment Damerau-Levenshtein distance.

    Counts insertions, deletions, substitutions, and the transposition of
    two adjacent characters as one edit each. This is the OSA variant --
    each pair of characters may participate in at most one transposition.
    """
    if a == b:
        return 0
    if not a:
        return len(b)
    if not b:
        return len(a)
    n, m = len(a), len(b)
    prev2: List[int] = []
    prev1: List[int] = list(range(m + 1))
    for i in range(1, n + 1):
        current = [i] + [0] * m
        for j in range(1, m + 1):
            cost = 0 if a[i - 1] == b[j - 1] else 1
            current[j] = min(
                current[j - 1] + 1,        # insertion
                prev1[j] + 1,              # deletion
                prev1[j - 1] + cost,       # substitution
            )
            if (
                i > 1
                and j > 1
                and a[i - 1] == b[j - 2]
                and a[i - 2] == b[j - 1]
            ):
                current[j] = min(current[j], prev2[j - 2] + 1)
        prev2, prev1 = prev1, current
    return prev1[m]

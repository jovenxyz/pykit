"""Compute the Levenshtein edit distance between two strings."""
from __future__ import annotations


def distance(a: str, b: str) -> int:
    """Return the minimum number of single-character insertions, deletions
    or substitutions required to transform ``a`` into ``b``."""
    if a == b:
        return 0
    if not a:
        return len(b)
    if not b:
        return len(a)
    # Use a rolling 1-D array for O(min(len(a), len(b))) memory.
    if len(a) < len(b):
        a, b = b, a
    previous = list(range(len(b) + 1))
    for i, char_a in enumerate(a, start=1):
        current = [i] + [0] * len(b)
        for j, char_b in enumerate(b, start=1):
            cost = 0 if char_a == char_b else 1
            current[j] = min(
                current[j - 1] + 1,        # insertion
                previous[j] + 1,           # deletion
                previous[j - 1] + cost,    # substitution
            )
        previous = current
    return previous[-1]


def ratio(a: str, b: str) -> float:
    """Return a similarity ratio in ``[0.0, 1.0]`` based on edit distance."""
    longest = max(len(a), len(b))
    if longest == 0:
        return 1.0
    return 1.0 - distance(a, b) / longest

"""Knuth-Morris-Pratt substring search."""
from __future__ import annotations

from typing import List


def build_failure(pattern: str) -> List[int]:
    """Compute the KMP failure (longest proper prefix/suffix) table."""
    table = [0] * len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            table[i] = length
            i += 1
        elif length != 0:
            length = table[length - 1]
        else:
            table[i] = 0
            i += 1
    return table


def find(text: str, pattern: str) -> int:
    """Return the index of the first occurrence of ``pattern`` or ``-1``."""
    if not pattern:
        return 0
    table = build_failure(pattern)
    i = j = 0
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                return i - j
        elif j != 0:
            j = table[j - 1]
        else:
            i += 1
    return -1


def find_all(text: str, pattern: str) -> List[int]:
    """Return all (possibly overlapping) start indices of ``pattern``."""
    if not pattern:
        return list(range(len(text) + 1))
    table = build_failure(pattern)
    matches: List[int] = []
    i = j = 0
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                matches.append(i - j)
                j = table[j - 1]
        elif j != 0:
            j = table[j - 1]
        else:
            i += 1
    return matches

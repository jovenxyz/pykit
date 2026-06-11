"""Boyer-Moore-Horspool substring search."""
from __future__ import annotations

from typing import Dict, List


def _bad_char_skip(pattern: str) -> Dict[str, int]:
    m = len(pattern)
    table: Dict[str, int] = {}
    for i in range(m - 1):
        table[pattern[i]] = m - 1 - i
    return table


def find(text: str, pattern: str) -> int:
    """Return the index of the first occurrence of ``pattern`` or ``-1``."""
    if not pattern:
        return 0
    m = len(pattern)
    n = len(text)
    if m > n:
        return -1
    skip = _bad_char_skip(pattern)
    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1
        if j < 0:
            return i
        i += skip.get(text[i + m - 1], m)
    return -1


def find_all(text: str, pattern: str) -> List[int]:
    """Return all (possibly overlapping) start indices of ``pattern``."""
    if not pattern:
        return list(range(len(text) + 1))
    matches: List[int] = []
    m = len(pattern)
    n = len(text)
    if m > n:
        return matches
    skip = _bad_char_skip(pattern)
    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1
        if j < 0:
            matches.append(i)
            i += 1
        else:
            i += skip.get(text[i + m - 1], m)
    return matches

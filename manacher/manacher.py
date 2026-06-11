"""Manacher's algorithm: longest palindromic substring in linear time."""
from __future__ import annotations

from typing import List


def _radii(text: str) -> List[int]:
    transformed = "^#" + "#".join(text) + "#$"
    n = len(transformed)
    p = [0] * n
    center = right = 0
    for i in range(1, n - 1):
        mirror = 2 * center - i
        if i < right:
            p[i] = min(right - i, p[mirror])
        while transformed[i + p[i] + 1] == transformed[i - p[i] - 1]:
            p[i] += 1
        if i + p[i] > right:
            center, right = i, i + p[i]
    return p


def longest_palindrome(text: str) -> str:
    """Return the longest palindromic substring of ``text``.

    Ties are broken by the earliest position.
    """
    if not text:
        return ""
    p = _radii(text)
    max_radius = max(p)
    max_center = p.index(max_radius)
    start = (max_center - max_radius) // 2
    return text[start:start + max_radius]


def all_palindrome_radii(text: str) -> List[int]:
    """Return, for each position between/around characters of ``text``, the
    radius of the longest palindrome centred there (Manacher's ``p`` array).
    """
    if not text:
        return []
    return _radii(text)[1:-1]

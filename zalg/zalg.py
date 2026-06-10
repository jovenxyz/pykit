"""The Z-algorithm: compute Z-array and find all pattern occurrences."""
from __future__ import annotations

from typing import List


def z_array(text: str) -> List[int]:
    """Return the Z-array of ``text``.

    ``z[i]`` is the length of the longest substring starting at ``i`` that
    matches a prefix of ``text``. By convention ``z[0]`` is the length of
    the whole string.
    """
    n = len(text)
    if n == 0:
        return []
    z = [0] * n
    z[0] = n
    left = right = 0
    for i in range(1, n):
        if i < right:
            z[i] = min(right - i, z[i - left])
        while i + z[i] < n and text[z[i]] == text[i + z[i]]:
            z[i] += 1
        if i + z[i] > right:
            left, right = i, i + z[i]
    return z


def find_all(text: str, pattern: str, *, sep: str = "\x00") -> List[int]:
    """Return all (possibly overlapping) start indices of ``pattern`` in ``text``."""
    if not pattern:
        return list(range(len(text) + 1))
    if sep in pattern or sep in text:
        raise ValueError(f"separator {sep!r} must not appear in input")
    combined = pattern + sep + text
    z = z_array(combined)
    plen = len(pattern)
    return [
        i - plen - 1
        for i in range(plen + 1, len(combined))
        if z[i] >= plen
    ]

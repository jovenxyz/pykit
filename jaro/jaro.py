"""Jaro and Jaro-Winkler string similarity."""
from __future__ import annotations


def jaro_similarity(a: str, b: str) -> float:
    """Return the Jaro similarity of ``a`` and ``b`` (between 0.0 and 1.0)."""
    if a == b:
        return 1.0
    len_a, len_b = len(a), len(b)
    if len_a == 0 or len_b == 0:
        return 0.0

    match_distance = max(0, max(len_a, len_b) // 2 - 1)

    a_matches = [False] * len_a
    b_matches = [False] * len_b
    matches = 0

    for i, char_a in enumerate(a):
        start = max(0, i - match_distance)
        end = min(i + match_distance + 1, len_b)
        for j in range(start, end):
            if b_matches[j] or b[j] != char_a:
                continue
            a_matches[i] = True
            b_matches[j] = True
            matches += 1
            break

    if matches == 0:
        return 0.0

    transpositions = 0
    j = 0
    for i in range(len_a):
        if not a_matches[i]:
            continue
        while not b_matches[j]:
            j += 1
        if a[i] != b[j]:
            transpositions += 1
        j += 1
    transpositions //= 2

    m = float(matches)
    return (m / len_a + m / len_b + (matches - transpositions) / m) / 3


def jaro_winkler_similarity(
    a: str,
    b: str,
    *,
    prefix_scale: float = 0.1,
    max_prefix: int = 4,
) -> float:
    """Return the Jaro-Winkler similarity (Jaro plus a prefix bonus)."""
    if not 0 <= prefix_scale <= 0.25:
        raise ValueError("prefix_scale should be in [0, 0.25]")
    base = jaro_similarity(a, b)
    if base == 0.0 or base == 1.0:
        return base
    prefix = 0
    for i in range(min(len(a), len(b), max_prefix)):
        if a[i] != b[i]:
            break
        prefix += 1
    return base + prefix * prefix_scale * (1 - base)

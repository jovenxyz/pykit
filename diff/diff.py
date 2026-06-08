"""Compute a line-level diff between two text blocks using LCS."""
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Sequence


@dataclass(frozen=True)
class DiffLine:
    tag: str           # " " (context), "+" (added), or "-" (removed)
    text: str


def _lcs_table(a: Sequence[str], b: Sequence[str]) -> List[List[int]]:
    n, m = len(a), len(b)
    table = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if a[i] == b[j]:
                table[i][j] = table[i + 1][j + 1] + 1
            else:
                table[i][j] = max(table[i + 1][j], table[i][j + 1])
    return table


def diff_lines(a: str, b: str) -> List[DiffLine]:
    """Return a line-by-line diff of two text blobs.

    Each :class:`DiffLine` has a ``tag`` of ``" "``, ``"+"``, or ``"-"``.
    Common lines appear as context; lines unique to ``a`` are marked ``"-"``
    and unique to ``b`` as ``"+"``.
    """
    lines_a = a.splitlines()
    lines_b = b.splitlines()
    table = _lcs_table(lines_a, lines_b)
    result: List[DiffLine] = []
    i = j = 0
    while i < len(lines_a) and j < len(lines_b):
        if lines_a[i] == lines_b[j]:
            result.append(DiffLine(" ", lines_a[i]))
            i += 1
            j += 1
        elif table[i + 1][j] >= table[i][j + 1]:
            result.append(DiffLine("-", lines_a[i]))
            i += 1
        else:
            result.append(DiffLine("+", lines_b[j]))
            j += 1
    while i < len(lines_a):
        result.append(DiffLine("-", lines_a[i]))
        i += 1
    while j < len(lines_b):
        result.append(DiffLine("+", lines_b[j]))
        j += 1
    return result


def format_diff(a: str, b: str) -> str:
    """Return the diff formatted as one ``"<tag> <text>"`` line per entry."""
    return "\n".join(f"{line.tag} {line.text}" for line in diff_lines(a, b))

"""Render rows of data as an ASCII table."""
from __future__ import annotations

from typing import Iterable, Optional, Sequence


def render(
    headers: Sequence[str],
    rows: Iterable[Sequence],
    *,
    align: Optional[Sequence[str]] = None,
) -> str:
    """Render ``rows`` as an ASCII table with ``headers``.

    ``align`` is a per-column alignment specifier: ``"l"``, ``"r"`` or
    ``"c"``. Defaults to all left-aligned.
    """
    rows = [tuple(str(cell) for cell in row) for row in rows]
    if any(len(row) != len(headers) for row in rows):
        raise ValueError("every row must have the same number of columns as the header")
    if align is None:
        align = ["l"] * len(headers)
    if len(align) != len(headers):
        raise ValueError("align must match the number of columns")
    for spec in align:
        if spec not in ("l", "r", "c"):
            raise ValueError(f"unknown alignment: {spec!r}")

    widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(cell))

    border = "+" + "+".join("-" * (w + 2) for w in widths) + "+"

    def format_row(cells: Sequence[str]) -> str:
        parts = []
        for cell, width, spec in zip(cells, widths, align):
            if spec == "r":
                parts.append(f" {cell:>{width}} ")
            elif spec == "c":
                parts.append(f" {cell:^{width}} ")
            else:
                parts.append(f" {cell:<{width}} ")
        return "|" + "|".join(parts) + "|"

    lines = [border, format_row(headers), border]
    for row in rows:
        lines.append(format_row(row))
    if rows:
        lines.append(border)
    return "\n".join(lines)

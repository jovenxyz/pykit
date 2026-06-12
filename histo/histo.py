"""Render labelled bar charts and value histograms as ASCII text."""
from __future__ import annotations

from typing import Mapping, Sequence


def bar_chart(
    data: Mapping[str, float],
    *,
    width: int = 40,
    bar: str = "#",
    sort: str = "input",
) -> str:
    """Render ``data`` as a horizontal ASCII bar chart.

    ``width`` is the maximum bar length in characters. ``sort`` controls
    row order: ``"input"`` keeps insertion order, ``"asc"`` / ``"desc"``
    sort by value.
    """
    if width <= 0:
        raise ValueError("width must be positive")
    if sort not in ("input", "asc", "desc"):
        raise ValueError(f"unknown sort: {sort!r}")
    if not data:
        return ""
    items = list(data.items())
    if sort == "asc":
        items.sort(key=lambda item: item[1])
    elif sort == "desc":
        items.sort(key=lambda item: item[1], reverse=True)
    label_width = max(len(label) for label, _ in items)
    largest = max(value for _, value in items)
    scale = width / largest if largest > 0 else 0.0
    lines = []
    for label, value in items:
        bar_length = int(round(value * scale)) if largest > 0 else 0
        lines.append(f"{label:<{label_width}} | {bar * bar_length} {value}")
    return "\n".join(lines)


def histogram(values: Sequence[float], *, bins: int = 10, **kwargs) -> str:
    """Render the distribution of ``values`` as an ASCII histogram."""
    if bins <= 0:
        raise ValueError("bins must be positive")
    if not values:
        return ""
    lo = min(values)
    hi = max(values)
    if hi == lo:
        return bar_chart({f"{lo:g}": len(values)}, **kwargs)
    span = (hi - lo) / bins
    counts = [0] * bins
    for value in values:
        index = min(int((value - lo) / span), bins - 1)
        counts[index] += 1
    labels = [
        f"{lo + i * span:.2f}..{lo + (i + 1) * span:.2f}" for i in range(bins)
    ]
    return bar_chart(dict(zip(labels, counts)), **kwargs)

"""Render a sequence of numbers as a Unicode sparkline."""
from __future__ import annotations

from typing import Optional, Sequence

_BARS = "▁▂▃▄▅▆▇█"   # 8 block-fill glyphs


def sparkline(
    values: Sequence[float],
    *,
    minimum: Optional[float] = None,
    maximum: Optional[float] = None,
) -> str:
    """Return a one-line bar chart of ``values`` using block-fill glyphs."""
    if not values:
        return ""
    lo = minimum if minimum is not None else min(values)
    hi = maximum if maximum is not None else max(values)
    if hi < lo:
        raise ValueError("maximum must be >= minimum")
    span = hi - lo
    last = len(_BARS) - 1
    chars = []
    for v in values:
        if span == 0:
            chars.append(_BARS[0])
            continue
        normalised = (v - lo) / span
        normalised = max(0.0, min(1.0, normalised))
        chars.append(_BARS[int(round(normalised * last))])
    return "".join(chars)

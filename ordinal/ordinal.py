"""Format integers with English ordinal suffixes (1st, 2nd, 22nd, ...)."""
from __future__ import annotations


def ordinal_suffix(number: int) -> str:
    """Return ``"st"``/``"nd"``/``"rd"``/``"th"`` for ``number``."""
    n = abs(number)
    if n % 100 in (11, 12, 13):
        return "th"
    return {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")


def ordinal(number: int) -> str:
    """Return a string like ``"1st"`` or ``"22nd"`` for ``number``."""
    return f"{number}{ordinal_suffix(number)}"

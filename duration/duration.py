"""Format and parse human-readable durations."""
from __future__ import annotations

import re

_UNITS = [("w", 604800), ("d", 86400), ("h", 3600), ("m", 60), ("s", 1)]
_FULL = re.compile(r"^\s*(?:\d+\s*[wdhmsWDHMS]\s*)+$")
_PART = re.compile(r"(\d+)\s*([wdhmsWDHMS])")


def format_duration(seconds: int) -> str:
    """Return a string like ``"1h 30m"`` for the given number of seconds."""
    if seconds < 0:
        raise ValueError("seconds must be non-negative")
    if seconds == 0:
        return "0s"
    parts = []
    remaining = seconds
    for label, size in _UNITS:
        count, remaining = divmod(remaining, size)
        if count:
            parts.append(f"{count}{label}")
    return " ".join(parts)


def parse_duration(text: str) -> int:
    """Parse strings like ``"1h 30m"`` into a number of seconds."""
    if not _FULL.match(text):
        raise ValueError(f"invalid duration: {text!r}")
    sizes = dict(_UNITS)
    return sum(
        int(amount) * sizes[unit.lower()]
        for amount, unit in _PART.findall(text)
    )

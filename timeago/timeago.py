"""Render a past or future duration as a human-readable phrase."""
from __future__ import annotations

from datetime import datetime, timezone
from typing import Optional, Union

_UNITS = [
    (60 * 60 * 24 * 365, "year"),
    (60 * 60 * 24 * 30, "month"),
    (60 * 60 * 24 * 7, "week"),
    (60 * 60 * 24, "day"),
    (60 * 60, "hour"),
    (60, "minute"),
    (1, "second"),
]


def time_ago(
    when: Union[int, float, datetime],
    now: Optional[datetime] = None,
) -> str:
    """Return a string like ``"2 minutes ago"`` or ``"in 3 hours"``."""
    reference = now if now is not None else datetime.now(timezone.utc)
    if isinstance(when, datetime):
        target = when
    else:
        target = datetime.fromtimestamp(float(when), tz=timezone.utc)
    if target.tzinfo is None:
        target = target.replace(tzinfo=timezone.utc)
    if reference.tzinfo is None:
        reference = reference.replace(tzinfo=timezone.utc)
    delta = (reference - target).total_seconds()
    if abs(delta) < 1:
        return "just now"
    direction_past = delta > 0
    seconds = int(abs(delta))
    for size, unit in _UNITS:
        if seconds >= size:
            count = seconds // size
            plural = "" if count == 1 else "s"
            label = f"{count} {unit}{plural}"
            return f"{label} ago" if direction_past else f"in {label}"
    return "just now"

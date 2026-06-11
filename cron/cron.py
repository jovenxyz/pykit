"""Parse cron expressions and check whether a datetime matches."""
from __future__ import annotations

from datetime import datetime
from typing import List

_RANGES = [
    ("minute", 0, 59),
    ("hour", 0, 23),
    ("day", 1, 31),
    ("month", 1, 12),
    ("weekday", 0, 6),    # 0 = Sunday in cron convention
]


class CronError(ValueError):
    """Raised when a cron expression is malformed."""


def parse(expression: str) -> List[List[int]]:
    """Parse a 5-field cron expression into per-field allowed values."""
    fields = expression.split()
    if len(fields) != 5:
        raise CronError(f"expected 5 fields, got {len(fields)}: {expression!r}")
    return [_parse_field(fields[i], _RANGES[i][1], _RANGES[i][2]) for i in range(5)]


def _parse_field(field: str, lo: int, hi: int) -> List[int]:
    values: set = set()
    for chunk in field.split(","):
        step = 1
        if "/" in chunk:
            chunk, step_str = chunk.split("/", 1)
            try:
                step = int(step_str)
            except ValueError as error:
                raise CronError(f"invalid step: {step_str!r}") from error
            if step <= 0:
                raise CronError(f"step must be positive: {step}")
        if chunk == "*":
            start, end = lo, hi
        elif "-" in chunk:
            start_str, end_str = chunk.split("-", 1)
            try:
                start, end = int(start_str), int(end_str)
            except ValueError as error:
                raise CronError(f"invalid range: {chunk!r}") from error
        else:
            try:
                start = end = int(chunk)
            except ValueError as error:
                raise CronError(f"invalid value: {chunk!r}") from error
        if start < lo or end > hi or start > end:
            raise CronError(f"value out of range [{lo}, {hi}]: {chunk!r}")
        values.update(range(start, end + 1, step))
    return sorted(values)


def matches(expression: str, moment: datetime) -> bool:
    """Return ``True`` if ``moment`` would trigger ``expression``."""
    minute, hour, day, month, weekday = parse(expression)
    return (
        moment.minute in minute
        and moment.hour in hour
        and moment.day in day
        and moment.month in month
        and (moment.weekday() + 1) % 7 in weekday   # cron Sunday = 0
    )

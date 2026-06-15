"""Calendar utilities: leap years, weekdays, and days between dates."""
from __future__ import annotations

from typing import Tuple

DAYS_OF_WEEK = (
    "Sunday", "Monday", "Tuesday", "Wednesday",
    "Thursday", "Friday", "Saturday",
)
DAYS_IN_MONTH = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)


def is_leap(year: int) -> bool:
    """Return ``True`` if ``year`` is a Gregorian leap year."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year: int, month: int) -> int:
    """Return the number of days in ``month`` of ``year``."""
    if not 1 <= month <= 12:
        raise ValueError(f"month must be in 1..12: {month}")
    if month == 2 and is_leap(year):
        return 29
    return DAYS_IN_MONTH[month - 1]


def is_valid_date(year: int, month: int, day: int) -> bool:
    """Return ``True`` if the (year, month, day) triple is a valid date."""
    if year < 1:
        return False
    if not 1 <= month <= 12:
        return False
    return 1 <= day <= days_in_month(year, month)


def weekday(year: int, month: int, day: int) -> str:
    """Return the day-of-week name for a Gregorian date (Zeller's congruence)."""
    if not is_valid_date(year, month, day):
        raise ValueError(f"invalid date: {year}-{month:02d}-{day:02d}")
    if month < 3:
        month += 12
        year -= 1
    k = year % 100
    j = year // 100
    h = (day + (13 * (month + 1)) // 5 + k + k // 4 + j // 4 + 5 * j) % 7
    # Zeller: 0 = Saturday, 1 = Sunday, ..., 6 = Friday.
    mapping = (6, 0, 1, 2, 3, 4, 5)
    return DAYS_OF_WEEK[mapping[h]]


def days_between(
    start: Tuple[int, int, int],
    end: Tuple[int, int, int],
) -> int:
    """Return the signed number of days between two ``(year, month, day)`` dates."""
    return _ordinal(*end) - _ordinal(*start)


def _ordinal(year: int, month: int, day: int) -> int:
    if not is_valid_date(year, month, day):
        raise ValueError(f"invalid date: {year}-{month:02d}-{day:02d}")
    days = 0
    for y in range(1, year):
        days += 366 if is_leap(y) else 365
    for m in range(1, month):
        days += days_in_month(year, m)
    days += day - 1
    return days

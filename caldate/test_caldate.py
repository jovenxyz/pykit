import pytest

from caldate import (
    days_between,
    days_in_month,
    is_leap,
    is_valid_date,
    weekday,
)


def test_leap_year():
    assert is_leap(2000)
    assert is_leap(2024)
    assert not is_leap(2023)
    assert not is_leap(1900)        # century not divisible by 400
    assert is_leap(2400)


def test_days_in_month():
    assert days_in_month(2023, 1) == 31
    assert days_in_month(2023, 2) == 28
    assert days_in_month(2024, 2) == 29
    assert days_in_month(2023, 4) == 30
    assert days_in_month(2023, 12) == 31


def test_days_in_month_invalid_raises():
    with pytest.raises(ValueError):
        days_in_month(2023, 13)


def test_is_valid_date():
    assert is_valid_date(2024, 2, 29)
    assert not is_valid_date(2023, 2, 29)
    assert not is_valid_date(2023, 13, 1)
    assert not is_valid_date(0, 1, 1)


def test_weekday_known_dates():
    assert weekday(2026, 6, 15) == "Monday"
    assert weekday(2000, 1, 1) == "Saturday"
    assert weekday(1969, 7, 20) == "Sunday"     # moon landing


def test_weekday_invalid_date_raises():
    with pytest.raises(ValueError):
        weekday(2023, 2, 30)


def test_days_between_same_date():
    assert days_between((2024, 1, 1), (2024, 1, 1)) == 0


def test_days_between_consecutive():
    assert days_between((2024, 1, 1), (2024, 1, 2)) == 1


def test_days_between_across_leap_year():
    # 2023-06-01 -> 2024-06-01 spans Feb 29 2024 -> 366 days.
    assert days_between((2023, 6, 1), (2024, 6, 1)) == 366


def test_days_between_signed():
    assert days_between((2024, 1, 5), (2024, 1, 1)) == -4

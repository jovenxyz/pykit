from datetime import datetime

import pytest

from cron import CronError, matches, parse


def test_parse_wildcard():
    minute, hour, day, month, weekday = parse("* * * * *")
    assert minute == list(range(60))
    assert hour == list(range(24))
    assert day == list(range(1, 32))
    assert month == list(range(1, 13))
    assert weekday == list(range(7))


def test_parse_fixed_value():
    minute, *_ = parse("5 * * * *")
    assert minute == [5]


def test_parse_list_and_range():
    minute, *_ = parse("0,15,30,45 * * * *")
    assert minute == [0, 15, 30, 45]
    _, _, _, _, weekday = parse("* * * * 1-5")
    assert weekday == [1, 2, 3, 4, 5]


def test_parse_step():
    minute, *_ = parse("*/15 * * * *")
    assert minute == [0, 15, 30, 45]


def test_parse_range_with_step():
    minute, *_ = parse("0-30/10 * * * *")
    assert minute == [0, 10, 20, 30]


def test_parse_invalid_field_count():
    with pytest.raises(CronError):
        parse("* * * *")


def test_parse_out_of_range_raises():
    with pytest.raises(CronError):
        parse("60 * * * *")
    with pytest.raises(CronError):
        parse("* 24 * * *")


def test_matches_at_exact_time():
    # 2026-06-15 is a Monday.
    moment = datetime(2026, 6, 15, 9, 0)
    assert matches("0 9 * * 1", moment)
    assert not matches("0 10 * * 1", moment)


def test_matches_with_step():
    assert matches("*/5 * * * *", datetime(2026, 6, 15, 9, 5))
    assert not matches("*/5 * * * *", datetime(2026, 6, 15, 9, 7))


def test_matches_weekday_range():
    monday = datetime(2026, 6, 15, 12, 0)
    saturday = datetime(2026, 6, 20, 12, 0)
    assert matches("* * * * 1-5", monday)
    assert not matches("* * * * 1-5", saturday)

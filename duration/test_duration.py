import pytest

from duration import format_duration, parse_duration


def test_format_basic():
    assert format_duration(0) == "0s"
    assert format_duration(45) == "45s"
    assert format_duration(60) == "1m"
    assert format_duration(90) == "1m 30s"
    assert format_duration(3600) == "1h"
    assert format_duration(3661) == "1h 1m 1s"
    assert format_duration(86400) == "1d"
    assert format_duration(604800 + 3600) == "1w 1h"


def test_format_negative_raises():
    with pytest.raises(ValueError):
        format_duration(-1)


def test_parse_basic():
    assert parse_duration("45s") == 45
    assert parse_duration("1m") == 60
    assert parse_duration("1m 30s") == 90
    assert parse_duration("1h 1m 1s") == 3661
    assert parse_duration("1d") == 86400
    assert parse_duration("1w") == 604800


def test_parse_case_insensitive_and_no_spaces():
    assert parse_duration("1H30M") == 5400
    assert parse_duration("2h15m") == 8100


def test_parse_invalid_raises():
    with pytest.raises(ValueError):
        parse_duration("abc")
    with pytest.raises(ValueError):
        parse_duration("10")
    with pytest.raises(ValueError):
        parse_duration("")


def test_round_trip():
    for seconds in (1, 59, 60, 61, 3661, 86461, 604800 + 86400 + 3661):
        assert parse_duration(format_duration(seconds)) == seconds

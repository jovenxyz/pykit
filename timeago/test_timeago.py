from datetime import datetime, timedelta, timezone

from timeago import time_ago


_NOW = datetime(2026, 6, 1, 12, 0, 0, tzinfo=timezone.utc)


def _ago(seconds):
    return _NOW - timedelta(seconds=seconds)


def _future(seconds):
    return _NOW + timedelta(seconds=seconds)


def test_just_now():
    assert time_ago(_NOW, now=_NOW) == "just now"
    assert time_ago(_NOW - timedelta(milliseconds=500), now=_NOW) == "just now"


def test_seconds_minutes_hours_ago():
    assert time_ago(_ago(5), now=_NOW) == "5 seconds ago"
    assert time_ago(_ago(60), now=_NOW) == "1 minute ago"
    assert time_ago(_ago(120), now=_NOW) == "2 minutes ago"
    assert time_ago(_ago(3600), now=_NOW) == "1 hour ago"
    assert time_ago(_ago(7200), now=_NOW) == "2 hours ago"


def test_days_weeks_months_years_ago():
    assert time_ago(_ago(60 * 60 * 24), now=_NOW) == "1 day ago"
    assert time_ago(_ago(60 * 60 * 24 * 8), now=_NOW) == "1 week ago"
    assert time_ago(_ago(60 * 60 * 24 * 35), now=_NOW) == "1 month ago"
    assert time_ago(_ago(60 * 60 * 24 * 400), now=_NOW) == "1 year ago"


def test_future_phrases():
    assert time_ago(_future(30), now=_NOW) == "in 30 seconds"
    assert time_ago(_future(3600), now=_NOW) == "in 1 hour"
    assert time_ago(_future(60 * 60 * 24 * 400), now=_NOW) == "in 1 year"


def test_unix_timestamp_input():
    target = _ago(120).timestamp()
    assert time_ago(target, now=_NOW) == "2 minutes ago"


def test_naive_datetime_treated_as_utc():
    naive = _NOW.replace(tzinfo=None) - timedelta(seconds=30)
    assert time_ago(naive, now=_NOW) == "30 seconds ago"

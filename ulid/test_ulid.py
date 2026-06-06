import pytest

from ulid import new, timestamp_ms_of


def test_length_is_26():
    assert len(new()) == 26


def test_only_uses_crockford_base32_alphabet():
    allowed = set("0123456789ABCDEFGHJKMNPQRSTVWXYZ")
    assert set(new()) <= allowed


def test_timestamp_round_trip():
    fixed_ms = 1_700_000_000_000
    uid = new(timestamp_ms=fixed_ms, random_func=lambda n: 0)
    assert timestamp_ms_of(uid) == fixed_ms


def test_two_ulids_with_increasing_timestamp_sort_correctly():
    a = new(timestamp_ms=1_000_000_000_000, random_func=lambda n: 0)
    b = new(timestamp_ms=1_000_000_001_000, random_func=lambda n: 0)
    assert a < b


def test_two_ulids_same_timestamp_differ_by_randomness():
    a = new(timestamp_ms=1_000_000_000_000, random_func=lambda n: 1)
    b = new(timestamp_ms=1_000_000_000_000, random_func=lambda n: 2)
    assert a != b
    assert a[:10] == b[:10]


def test_invalid_timestamp_raises():
    with pytest.raises(ValueError):
        new(timestamp_ms=-1)
    with pytest.raises(ValueError):
        new(timestamp_ms=1 << 48)


def test_timestamp_of_invalid_length_raises():
    with pytest.raises(ValueError):
        timestamp_ms_of("short")


def test_timestamp_of_invalid_character_raises():
    bad = "I" * 26    # 'I' is excluded from Crockford base32
    with pytest.raises(ValueError):
        timestamp_ms_of(bad)

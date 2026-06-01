import pytest

from bytesize import format_bytes, parse_size


def test_format_bytes_basic():
    assert format_bytes(0) == "0 B"
    assert format_bytes(512) == "512 B"
    assert format_bytes(1024) == "1.0 KB"
    assert format_bytes(1536) == "1.5 KB"
    assert format_bytes(1024 ** 2) == "1.0 MB"
    assert format_bytes(1024 ** 3) == "1.0 GB"


def test_format_bytes_precision():
    assert format_bytes(1536, precision=2) == "1.50 KB"


def test_format_bytes_negative_raises():
    with pytest.raises(ValueError):
        format_bytes(-1)


def test_parse_size_basic():
    assert parse_size("0") == 0
    assert parse_size("512 B") == 512
    assert parse_size("1 KB") == 1024
    assert parse_size("1.5 KB") == 1536
    assert parse_size("1.5MB") == int(1.5 * 1024 ** 2)


def test_parse_size_case_insensitive():
    assert parse_size("1 kb") == 1024
    assert parse_size("2 Gb") == 2 * 1024 ** 3


def test_parse_size_invalid_raises():
    with pytest.raises(ValueError):
        parse_size("abc")
    with pytest.raises(ValueError):
        parse_size("10 ZB")


def test_round_trip():
    for size in (0, 512, 1024, 1536, 1024 ** 2, 5 * 1024 ** 3):
        assert parse_size(format_bytes(size)) == size

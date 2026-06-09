import pytest

from fnv import fnv1a_32, fnv1a_64, fnv1a_128


def test_fnv32_empty_is_offset_basis():
    assert fnv1a_32(b"") == 0x811C9DC5


@pytest.mark.parametrize("data,expected", [
    (b"a", 0xE40C292C),
    (b"b", 0xE70C2DE5),
    (b"foobar", 0xBF9CF968),
])
def test_fnv32_known_vectors(data, expected):
    assert fnv1a_32(data) == expected


def test_fnv64_empty_is_offset_basis():
    assert fnv1a_64(b"") == 0xCBF29CE484222325


@pytest.mark.parametrize("data,expected", [
    (b"a", 0xAF63DC4C8601EC8C),
    (b"foobar", 0x85944171F73967E8),
])
def test_fnv64_known_vectors(data, expected):
    assert fnv1a_64(data) == expected


def test_fnv128_empty_is_offset_basis():
    assert fnv1a_128(b"") == 0x6C62272E07BB014262B821756295C58D


def test_fnv128_returns_value_in_range():
    h = fnv1a_128(b"hello world")
    assert 0 <= h < (1 << 128)


def test_hash_is_deterministic():
    data = b"the quick brown fox"
    assert fnv1a_32(data) == fnv1a_32(data)
    assert fnv1a_64(data) == fnv1a_64(data)


def test_different_inputs_have_different_hashes():
    assert fnv1a_32(b"abc") != fnv1a_32(b"xyz")
    assert fnv1a_64(b"abc") != fnv1a_64(b"xyz")

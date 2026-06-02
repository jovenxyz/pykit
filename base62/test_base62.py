import pytest

from base62 import decode, encode


def test_encode_basic():
    assert encode(0) == "0"
    assert encode(1) == "1"
    assert encode(10) == "A"
    assert encode(35) == "Z"
    assert encode(36) == "a"
    assert encode(61) == "z"
    assert encode(62) == "10"


def test_decode_basic():
    assert decode("0") == 0
    assert decode("Z") == 35
    assert decode("a") == 36
    assert decode("10") == 62


def test_round_trip():
    for number in (0, 1, 61, 62, 12345, 9999999):
        assert decode(encode(number)) == number


def test_encode_negative_raises():
    with pytest.raises(ValueError):
        encode(-1)


def test_decode_invalid_raises():
    with pytest.raises(ValueError):
        decode("")
    with pytest.raises(ValueError):
        decode("Hello!")

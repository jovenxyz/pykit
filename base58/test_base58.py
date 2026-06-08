import os

import pytest

from base58 import decode, encode


def test_encode_empty_bytes():
    assert encode(b"") == ""


def test_decode_empty_string():
    assert decode("") == b""


def test_encode_known_small_values():
    assert encode(b"\x00") == "1"
    assert encode(b"\x01") == "2"
    assert encode(b"\xff") == "5Q"


def test_round_trip():
    for data in (b"\x00", b"\xff", b"abc", b"hello world", b"\x00\x00\x01"):
        assert decode(encode(data)) == data


def test_leading_zero_bytes_become_leading_ones():
    assert encode(b"\x00\x00\xff") == "115Q"
    assert decode("115Q") == b"\x00\x00\xff"


def test_invalid_character_raises():
    # 0, O, I, l are all excluded from the alphabet.
    with pytest.raises(ValueError):
        decode("0OIl")


def test_non_bytes_or_str_input_raises():
    with pytest.raises(TypeError):
        encode("hello")
    with pytest.raises(TypeError):
        decode(b"hello")


def test_round_trip_random_lengths():
    for length in (1, 4, 16, 64):
        data = os.urandom(length)
        assert decode(encode(data)) == data

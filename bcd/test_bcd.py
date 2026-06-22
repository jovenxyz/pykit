import pytest
from bcd import encode, decode, encode_unpacked, decode_unpacked, byte_to_digits


def test_encode_even_digits():
    assert encode(1234) == bytes([0x12, 0x34])


def test_encode_odd_digits_pads_high_nibble():
    assert encode(123) == bytes([0x01, 0x23])


def test_encode_single_digit():
    assert encode(7) == bytes([0x07])


def test_encode_zero():
    assert encode(0) == bytes([0x00])


def test_decode_roundtrip():
    for n in [0, 1, 9, 10, 99, 100, 1234, 1000000, 9999999999]:
        assert decode(encode(n)) == n


def test_encode_negative_raises():
    with pytest.raises(ValueError):
        encode(-1)


def test_decode_invalid_nibble_raises():
    with pytest.raises(ValueError):
        decode(bytes([0xAB]))


def test_unpacked_roundtrip():
    for n in [0, 5, 42, 99, 12345]:
        assert decode_unpacked(encode_unpacked(n)) == n


def test_unpacked_invalid_digit_raises():
    with pytest.raises(ValueError):
        decode_unpacked(bytes([10]))


def test_unpacked_negative_raises():
    with pytest.raises(ValueError):
        encode_unpacked(-5)


def test_byte_to_digits():
    assert byte_to_digits(0x12) == (1, 2)
    assert byte_to_digits(0x99) == (9, 9)
    assert byte_to_digits(0x00) == (0, 0)


def test_byte_to_digits_invalid():
    with pytest.raises(ValueError):
        byte_to_digits(0xAB)
    with pytest.raises(ValueError):
        byte_to_digits(256)

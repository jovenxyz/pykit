import pytest

from qp import decode, encode


def test_encode_plain_ascii():
    assert encode(b"hello") == "hello"


def test_encode_high_byte():
    assert encode(b"\xe9") == "=E9"


def test_encode_equals_is_escaped():
    assert encode(b"a=b") == "a=3Db"


def test_encode_preserves_space():
    assert encode(b"a b") == "a b"


def test_decode_basic():
    assert decode("hello") == b"hello"
    assert decode("=E9") == b"\xe9"
    assert decode("a=3Db") == b"a=b"


def test_decode_soft_line_break():
    assert decode("foo=\nbar") == b"foobar"
    assert decode("foo=\r\nbar") == b"foobar"


def test_decode_invalid_escape_raises():
    with pytest.raises(ValueError):
        decode("=ZZ")
    with pytest.raises(ValueError):
        decode("=")


def test_round_trip_bytes():
    data = bytes(range(256))
    assert decode(encode(data)) == data


def test_encode_line_wrap_keeps_lines_under_length():
    encoded = encode(b"A" * 200, line_length=20)
    for line in encoded.split("\n"):
        assert len(line) <= 20


def test_invalid_line_length_raises():
    with pytest.raises(ValueError):
        encode(b"abc", line_length=3)

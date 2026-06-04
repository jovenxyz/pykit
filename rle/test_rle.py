import pytest

from rle import decode, decode_string, encode, encode_string


def test_encode_basic():
    assert encode("aaabbc") == [("a", 3), ("b", 2), ("c", 1)]


def test_encode_empty():
    assert encode("") == []


def test_encode_single_run():
    assert encode("zzzz") == [("z", 4)]


def test_decode_basic():
    assert decode([("a", 3), ("b", 2), ("c", 1)]) == "aaabbc"


def test_decode_empty():
    assert decode([]) == ""


def test_decode_invalid_raises():
    with pytest.raises(ValueError):
        decode([("ab", 1)])
    with pytest.raises(ValueError):
        decode([("a", 0)])


def test_round_trip_pairs():
    for text in ("", "a", "abc", "aaabbc", "xxxxx"):
        assert decode(encode(text)) == text


def test_encode_string_compact_form():
    assert encode_string("aaabbc") == "3a2b1c"


def test_decode_string_basic():
    assert decode_string("3a2b1c") == "aaabbc"
    assert decode_string("") == ""


def test_decode_string_multi_digit_count():
    assert decode_string("12a") == "a" * 12


def test_decode_string_invalid_raises():
    with pytest.raises(ValueError):
        decode_string("abc")
    with pytest.raises(ValueError):
        decode_string("3a2")


def test_round_trip_string_form():
    for text in ("a", "abc", "aaabbc", "xxxxx" * 5):
        assert decode_string(encode_string(text)) == text

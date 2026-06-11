import pytest

from lz77 import compress, decompress


def test_round_trip_simple_text():
    data = b"the quick brown fox jumps over the lazy dog"
    assert decompress(compress(data)) == data


def test_round_trip_repetitive():
    data = b"aaaaaaaaaa"
    assert decompress(compress(data)) == data


def test_round_trip_empty():
    assert decompress(compress(b"")) == b""


def test_round_trip_single_byte():
    assert decompress(compress(b"x")) == b"x"


def test_round_trip_binary_data():
    data = bytes(range(256))
    assert decompress(compress(data)) == data


def test_tokens_for_pure_literal_run():
    # No repeats -> every token is a pure literal (offset 0, length 0).
    tokens = compress(b"abcdef")
    assert all(t.offset == 0 and t.length == 0 for t in tokens)


def test_finds_match_for_repeated_sequence():
    tokens = compress(b"abcabc")
    assert any(t.length > 0 for t in tokens)


def test_invalid_window_size_raises():
    with pytest.raises(ValueError):
        compress(b"abc", window_size=0)
    with pytest.raises(ValueError):
        compress(b"abc", lookahead=0)

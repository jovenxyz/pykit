import pytest

from bencode import BencodeError, decode, encode


def test_encode_int():
    assert encode(0) == b"i0e"
    assert encode(42) == b"i42e"
    assert encode(-7) == b"i-7e"


def test_encode_bytes_and_str():
    assert encode(b"spam") == b"4:spam"
    assert encode("spam") == b"4:spam"
    assert encode("") == b"0:"


def test_encode_list():
    assert encode([1, 2, b"x"]) == b"li1ei2e1:xe"


def test_encode_dict_keys_are_sorted():
    assert encode({"b": 2, "a": 1}) == b"d1:ai1e1:bi2ee"


def test_encode_bool_rejected():
    with pytest.raises(BencodeError):
        encode(True)


def test_encode_unsupported_type():
    with pytest.raises(BencodeError):
        encode(1.5)


def test_decode_int():
    assert decode(b"i0e") == 0
    assert decode(b"i42e") == 42
    assert decode(b"i-7e") == -7


def test_decode_string_returns_bytes():
    assert decode(b"4:spam") == b"spam"


def test_decode_list():
    assert decode(b"li1ei2e1:xe") == [1, 2, b"x"]


def test_decode_dict():
    assert decode(b"d1:ai1e1:bi2ee") == {b"a": 1, b"b": 2}


def test_round_trip_canonical():
    samples = [
        0,
        42,
        b"hello",
        [1, b"two", [3]],
        {"name": "alice", "items": [1, 2, 3]},
    ]
    for sample in samples:
        encoded = encode(sample)
        decoded = decode(encoded)
        # Re-encode to confirm canonical equality (str keys become bytes
        # after decode, but the canonical encoding stays the same).
        assert encode(decoded) == encoded


def test_decode_trailing_data_raises():
    with pytest.raises(BencodeError):
        decode(b"i1ei2e")


def test_decode_truncated_string_raises():
    with pytest.raises(BencodeError):
        decode(b"10:short")

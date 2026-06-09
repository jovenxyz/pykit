import zlib

import pytest

from crc import crc32, crc32_hex


def test_empty_input():
    assert crc32(b"") == 0


@pytest.mark.parametrize("data,expected", [
    (b"a", 0xE8B7BE43),
    (b"abc", 0x352441C2),
    (b"123456789", 0xCBF43926),
    (b"The quick brown fox jumps over the lazy dog", 0x414FA339),
])
def test_known_vectors(data, expected):
    assert crc32(data) == expected


def test_matches_zlib():
    for data in (b"", b"a", b"hello world", b"\x00" * 100, b"\xff\x00\x01"):
        assert crc32(data) == zlib.crc32(data)


def test_chunked_extension_matches_single_pass():
    text = b"The quick brown fox jumps over the lazy dog"
    full = crc32(text)
    half = len(text) // 2
    running = crc32(text[:half])
    running = crc32(text[half:], initial=running)
    assert running == full


def test_crc32_hex_format():
    assert crc32_hex(b"") == "00000000"
    assert crc32_hex(b"a") == "e8b7be43"

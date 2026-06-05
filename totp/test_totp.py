import pytest

from totp import from_base32, hotp, totp


# 20-byte ASCII secret from the RFC 4226 / 6238 test vectors.
SECRET = b"12345678901234567890"


@pytest.mark.parametrize("counter,expected", [
    (0, "755224"),
    (1, "287082"),
    (2, "359152"),
    (3, "969429"),
    (4, "338314"),
    (5, "254676"),
    (6, "287922"),
    (7, "162583"),
    (8, "399871"),
    (9, "520489"),
])
def test_hotp_rfc4226_test_vectors(counter, expected):
    assert hotp(SECRET, counter) == expected


def test_totp_maps_time_to_counter():
    # At T=59 s with a 30 s period, counter = 1.
    assert totp(SECRET, timestamp=59) == hotp(SECRET, 1)


def test_totp_rfc6238_8_digit_sha1():
    # RFC 6238 test vector: T=59 s, 8 digits, SHA-1.
    assert totp(SECRET, timestamp=59, digits=8) == "94287082"


def test_totp_injected_time_func():
    assert totp(SECRET, time_func=lambda: 90.0) == hotp(SECRET, 3)


def test_hotp_invalid_digits_raise():
    with pytest.raises(ValueError):
        hotp(SECRET, 0, digits=0)
    with pytest.raises(ValueError):
        hotp(SECRET, 0, digits=11)


def test_totp_period_must_be_positive():
    with pytest.raises(ValueError):
        totp(SECRET, period=0)


def test_from_base32_handles_unpadded_input():
    assert from_base32("JBSWY3DP") == b"Hello"


def test_from_base32_strips_spaces_and_accepts_lowercase():
    assert from_base32("jbswy 3dp") == b"Hello"

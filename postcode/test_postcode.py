import pytest
from postcode import (
    is_us_zip, normalize_us_zip,
    is_uk_postcode, normalize_uk_postcode,
    is_ca_postcode, normalize_ca_postcode,
    detect_country,
)


def test_us_zip_5_digit():
    assert is_us_zip("90210")
    assert normalize_us_zip("90210") == "90210"


def test_us_zip_plus4():
    assert is_us_zip("90210-1234")
    assert normalize_us_zip("90210-1234") == "90210-1234"


def test_us_zip_invalid():
    assert not is_us_zip("9021")
    assert not is_us_zip("ABCDE")
    assert not is_us_zip("90210-12")
    with pytest.raises(ValueError):
        normalize_us_zip("XYZ")


def test_uk_postcode_valid():
    assert is_uk_postcode("SW1A 1AA")
    assert is_uk_postcode("sw1a1aa")
    assert is_uk_postcode("EC1A 1BB")
    assert is_uk_postcode("M1 1AE")


def test_uk_postcode_normalize_uppercases_and_spaces():
    assert normalize_uk_postcode("sw1a1aa") == "SW1A 1AA"
    assert normalize_uk_postcode("  m11ae  ") == "M1 1AE"


def test_uk_postcode_invalid():
    assert not is_uk_postcode("12345")
    assert not is_uk_postcode("SW1A 1A")
    with pytest.raises(ValueError):
        normalize_uk_postcode("nope")


def test_ca_postcode_valid():
    assert is_ca_postcode("K1A 0B1")
    assert is_ca_postcode("k1a0b1")
    assert is_ca_postcode("M5V 3L9")


def test_ca_postcode_normalize():
    assert normalize_ca_postcode("k1a0b1") == "K1A 0B1"


def test_ca_postcode_invalid_letters():
    # D, F, I, O, Q, U, W, Z not allowed in first position
    assert not is_ca_postcode("D1A 1A1")
    assert not is_ca_postcode("F1A 1A1")
    with pytest.raises(ValueError):
        normalize_ca_postcode("ZZZZZZ")


def test_detect_country():
    assert detect_country("90210") == "US"
    assert detect_country("90210-1234") == "US"
    assert detect_country("SW1A 1AA") == "UK"
    assert detect_country("K1A 0B1") == "CA"
    assert detect_country("not a code") is None

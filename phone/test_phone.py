import pytest

from phone import format_e164, format_us, is_valid, normalize


def test_normalize_strips_punctuation():
    assert normalize("(415) 555-1234") == "4155551234"
    assert normalize("+1-415-555-1234") == "+14155551234"
    assert normalize("415.555.1234") == "4155551234"


def test_normalize_empty_raises():
    with pytest.raises(ValueError):
        normalize("")


def test_normalize_misplaced_plus_raises():
    with pytest.raises(ValueError):
        normalize("415+5551234")
    with pytest.raises(ValueError):
        normalize("+1+44")


def test_is_valid_basic():
    assert is_valid("(415) 555-1234")
    assert is_valid("+14155551234")
    assert not is_valid("123")                 # too short
    assert not is_valid("a" * 8)                # all letters -> empty after strip
    assert not is_valid("")
    assert not is_valid("+1234567890123456")    # 16 digits, too long


def test_format_us_with_country_code():
    assert format_us("+1-415-555-1234") == "(415) 555-1234"
    assert format_us("14155551234") == "(415) 555-1234"
    assert format_us("415-555-1234") == "(415) 555-1234"


def test_format_us_wrong_length_raises():
    with pytest.raises(ValueError):
        format_us("123")


def test_format_e164_basic():
    assert format_e164("(415) 555-1234") == "+14155551234"
    assert format_e164("+44 20 7946 0958") == "+442079460958"


def test_format_e164_with_custom_country():
    assert format_e164("020 7946 0958", default_country="44") == "+4402079460958"


def test_format_e164_invalid_country_raises():
    with pytest.raises(ValueError):
        format_e164("123", default_country="X")

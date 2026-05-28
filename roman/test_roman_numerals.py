import pytest

from roman_numerals import from_roman, to_roman


def test_to_roman_examples():
    assert to_roman(1) == "I"
    assert to_roman(4) == "IV"
    assert to_roman(9) == "IX"
    assert to_roman(58) == "LVIII"
    assert to_roman(1994) == "MCMXCIV"


def test_from_roman_examples():
    assert from_roman("IV") == 4
    assert from_roman("LVIII") == 58
    assert from_roman("MCMXCIV") == 1994


def test_round_trip():
    for number in (1, 4, 9, 40, 90, 400, 944, 2023, 3999):
        assert from_roman(to_roman(number)) == number


def test_out_of_range_raises():
    with pytest.raises(ValueError):
        to_roman(0)
    with pytest.raises(ValueError):
        to_roman(4000)


def test_invalid_character_raises():
    with pytest.raises(ValueError):
        from_roman("ABC")

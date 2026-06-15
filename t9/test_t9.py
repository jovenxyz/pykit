import pytest

from t9 import digits_for, iter_letter_combinations, letter_combinations


def test_classic_example():
    assert sorted(letter_combinations("23")) == sorted([
        "ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf",
    ])


def test_single_digit():
    assert sorted(letter_combinations("7")) == ["p", "q", "r", "s"]


def test_empty_input():
    assert letter_combinations("") == []
    assert list(iter_letter_combinations("")) == []


def test_invalid_digit_raises():
    with pytest.raises(ValueError):
        letter_combinations("123")     # 1 is not on the alphabetic keypad
    with pytest.raises(ValueError):
        letter_combinations("0")


def test_iter_matches_list():
    assert list(iter_letter_combinations("23")) == letter_combinations("23")


def test_digits_for_basic():
    assert digits_for("hi") == "44"
    assert digits_for("hello") == "43556"


def test_digits_for_case_insensitive():
    assert digits_for("HELLO") == "43556"


def test_digits_for_invalid_char_raises():
    with pytest.raises(ValueError):
        digits_for("hi!")

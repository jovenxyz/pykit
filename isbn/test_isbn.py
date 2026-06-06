import pytest

from isbn import is_isbn10, is_isbn13, is_valid


VALID_ISBN10 = (
    "0306406152",
    "0-306-40615-2",
    "0 306 40615 2",
    "043942089X",      # ISBN-10 with trailing X check digit
)

VALID_ISBN13 = (
    "9780306406157",
    "978-0-306-40615-7",
    "978 0 306 40615 7",
    "9780201896831",
)


@pytest.mark.parametrize("isbn", VALID_ISBN10)
def test_valid_isbn10(isbn):
    assert is_isbn10(isbn)
    assert is_valid(isbn)


@pytest.mark.parametrize("isbn", VALID_ISBN13)
def test_valid_isbn13(isbn):
    assert is_isbn13(isbn)
    assert is_valid(isbn)


def test_invalid_isbn10_check_digit():
    assert not is_isbn10("0306406153")    # last digit flipped


def test_invalid_isbn13_check_digit():
    assert not is_isbn13("9780306406158")


def test_wrong_length_is_invalid():
    assert not is_isbn10("12345")
    assert not is_isbn13("12345")
    assert not is_valid("12345")


def test_non_numeric_input_is_invalid():
    assert not is_isbn10("ABCDEFGHIJ")
    assert not is_isbn13("ABCDEFGHIJKLM")


def test_isbn10_x_only_at_last_position():
    assert not is_isbn10("X306406152")


def test_is_valid_accepts_either_form():
    assert is_valid("0306406152")
    assert is_valid("9780306406157")

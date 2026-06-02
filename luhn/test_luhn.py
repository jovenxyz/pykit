import pytest

from luhn import check_digit, is_valid, luhn_checksum


def test_known_valid_numbers():
    assert is_valid("79927398713")
    assert is_valid("4532015112830366")
    assert is_valid("4111111111111111")


def test_known_invalid_numbers():
    assert not is_valid("79927398710")
    assert not is_valid("1234567890")


def test_ignores_spaces_and_dashes():
    assert is_valid("4111 1111 1111 1111")
    assert is_valid("4111-1111-1111-1111")


def test_check_digit_completes_number():
    assert check_digit("7992739871") == 3
    partial = "7992739871"
    completed = partial + str(check_digit(partial))
    assert is_valid(completed)


def test_empty_or_non_digit_raises():
    with pytest.raises(ValueError):
        luhn_checksum("")
    with pytest.raises(ValueError):
        luhn_checksum("abc")
    with pytest.raises(ValueError):
        check_digit("")

"""Luhn checksum algorithm for validating identification numbers.

The Luhn algorithm (also known as the modulus-10 algorithm) is used to
validate credit card numbers, IMEIs, and a variety of identification numbers.
Non-digit characters are ignored, so formatted strings like ``"4111 1111
1111 1111"`` work directly.
"""
from __future__ import annotations


def _digits(number: str) -> list:
    digits = [int(ch) for ch in number if ch.isdigit()]
    if not digits:
        raise ValueError("number must contain at least one digit")
    return digits


def luhn_checksum(number: str) -> int:
    """Return the Luhn checksum (0 for a valid number)."""
    digits = _digits(number)
    parity = len(digits) % 2
    total = 0
    for index, digit in enumerate(digits):
        if index % 2 == parity:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit
    return total % 10


def is_valid(number: str) -> bool:
    """Return ``True`` if ``number`` has a valid Luhn check digit."""
    return luhn_checksum(number) == 0


def check_digit(partial: str) -> int:
    """Return the digit to append to ``partial`` to make it Luhn-valid."""
    digits = _digits(partial)
    parity = (len(digits) + 1) % 2
    total = 0
    for index, digit in enumerate(digits):
        if index % 2 == parity:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit
    return (10 - total % 10) % 10

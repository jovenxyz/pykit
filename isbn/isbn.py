"""Validate ISBN-10 and ISBN-13 numbers using their check digits."""
from __future__ import annotations


def _digits(isbn: str, allow_x: bool) -> str:
    cleaned = "".join(ch for ch in isbn if ch.isalnum())
    return cleaned.upper() if allow_x else cleaned


def is_isbn10(isbn: str) -> bool:
    """Return ``True`` if ``isbn`` is a valid ISBN-10 check sequence."""
    digits = _digits(isbn, allow_x=True)
    if len(digits) != 10:
        return False
    total = 0
    for index, char in enumerate(digits):
        if char == "X":
            if index != 9:
                return False
            value = 10
        elif char.isdigit():
            value = int(char)
        else:
            return False
        total += value * (10 - index)
    return total % 11 == 0


def is_isbn13(isbn: str) -> bool:
    """Return ``True`` if ``isbn`` is a valid ISBN-13 check sequence."""
    digits = _digits(isbn, allow_x=False)
    if len(digits) != 13 or not digits.isdigit():
        return False
    total = sum(
        int(char) * (1 if index % 2 == 0 else 3)
        for index, char in enumerate(digits)
    )
    return total % 10 == 0


def is_valid(isbn: str) -> bool:
    """Return ``True`` if ``isbn`` is either a valid ISBN-10 or ISBN-13."""
    return is_isbn10(isbn) or is_isbn13(isbn)

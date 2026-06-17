"""Phone number formatting and validation helpers."""
from __future__ import annotations

import re


def normalize(number: str) -> str:
    """Strip every character that isn't a digit or a leading ``+``."""
    if not number:
        raise ValueError("number must be non-empty")
    digits = re.sub(r"[^0-9+]", "", number)
    if digits.count("+") > 1:
        raise ValueError(f"too many '+' characters: {number!r}")
    if "+" in digits and not digits.startswith("+"):
        raise ValueError(f"'+' must be at the start: {number!r}")
    return digits


def is_valid(number: str, *, min_length: int = 7, max_length: int = 15) -> bool:
    """Return ``True`` if the digit count falls inside ``[min_length, max_length]``."""
    try:
        cleaned = normalize(number)
    except ValueError:
        return False
    digits = cleaned.lstrip("+")
    return min_length <= len(digits) <= max_length and digits.isdigit()


def format_us(number: str) -> str:
    """Format a US-style 10-digit number as ``(NNN) NNN-NNNN``."""
    cleaned = normalize(number).lstrip("+")
    if cleaned.startswith("1") and len(cleaned) == 11:
        cleaned = cleaned[1:]
    if len(cleaned) != 10:
        raise ValueError(f"US number must have 10 digits: {number!r}")
    return f"({cleaned[:3]}) {cleaned[3:6]}-{cleaned[6:]}"


def format_e164(number: str, *, default_country: str = "1") -> str:
    """Return the number in E.164 form (``+`` followed by digits only)."""
    cleaned = normalize(number)
    if cleaned.startswith("+"):
        return cleaned
    if not default_country.isdigit():
        raise ValueError(f"default_country must be digits: {default_country!r}")
    return f"+{default_country}{cleaned}"

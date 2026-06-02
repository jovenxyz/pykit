"""Encode integers as compact base62 strings and decode them back."""
from __future__ import annotations

_ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
_INDEX = {ch: i for i, ch in enumerate(_ALPHABET)}
_BASE = len(_ALPHABET)


def encode(number: int) -> str:
    """Return a base62 string for the non-negative integer ``number``."""
    if number < 0:
        raise ValueError("number must be non-negative")
    if number == 0:
        return _ALPHABET[0]
    chars = []
    while number:
        number, remainder = divmod(number, _BASE)
        chars.append(_ALPHABET[remainder])
    return "".join(reversed(chars))


def decode(text: str) -> int:
    """Decode a base62 string back into an integer."""
    if not text:
        raise ValueError("text must contain at least one character")
    number = 0
    for char in text:
        if char not in _INDEX:
            raise ValueError(f"invalid base62 character: {char!r}")
        number = number * _BASE + _INDEX[char]
    return number

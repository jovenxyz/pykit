"""Vigenere cipher -- a polyalphabetic shift cipher with a keyword."""
from __future__ import annotations

from typing import List


def _shift(char: str, amount: int) -> str:
    if "a" <= char <= "z":
        base = ord("a")
    elif "A" <= char <= "Z":
        base = ord("A")
    else:
        return char
    return chr((ord(char) - base + amount) % 26 + base)


def _key_shifts(key: str) -> List[int]:
    cleaned = [ch for ch in key if ch.isalpha()]
    if not cleaned:
        raise ValueError("key must contain at least one letter")
    return [ord(ch.lower()) - ord("a") for ch in cleaned]


def encrypt(text: str, key: str) -> str:
    """Encrypt ``text`` with the Vigenere cipher under ``key``."""
    shifts = _key_shifts(key)
    result = []
    index = 0
    for char in text:
        if char.isalpha():
            result.append(_shift(char, shifts[index % len(shifts)]))
            index += 1
        else:
            result.append(char)
    return "".join(result)


def decrypt(text: str, key: str) -> str:
    """Decrypt ``text`` produced by :func:`encrypt` under the same ``key``."""
    shifts = _key_shifts(key)
    result = []
    index = 0
    for char in text:
        if char.isalpha():
            result.append(_shift(char, -shifts[index % len(shifts)]))
            index += 1
        else:
            result.append(char)
    return "".join(result)

"""Caesar cipher: shift each ASCII letter by ``n`` positions."""
from __future__ import annotations


def caesar(text: str, shift: int) -> str:
    """Return ``text`` with every ASCII letter shifted by ``shift`` positions."""
    result = []
    for char in text:
        if "a" <= char <= "z":
            result.append(chr((ord(char) - ord("a") + shift) % 26 + ord("a")))
        elif "A" <= char <= "Z":
            result.append(chr((ord(char) - ord("A") + shift) % 26 + ord("A")))
        else:
            result.append(char)
    return "".join(result)


def rot13(text: str) -> str:
    """Apply the classic ROT13 substitution (Caesar cipher with shift 13)."""
    return caesar(text, 13)

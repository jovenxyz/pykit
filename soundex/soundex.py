"""Soundex phonetic algorithm -- encode names by sound."""
from __future__ import annotations

_CODES = {
    "B": "1", "F": "1", "P": "1", "V": "1",
    "C": "2", "G": "2", "J": "2", "K": "2", "Q": "2", "S": "2", "X": "2", "Z": "2",
    "D": "3", "T": "3",
    "L": "4",
    "M": "5", "N": "5",
    "R": "6",
}
_TRANSPARENT = {"H", "W"}


def soundex(name: str) -> str:
    """Return the 4-character American Soundex code for ``name``."""
    cleaned = [ch for ch in name.upper() if ch.isalpha()]
    if not cleaned:
        return "0000"
    digits = [_CODES.get(ch, "") for ch in cleaned]
    result = [cleaned[0]]
    previous = digits[0]
    for ch, code in zip(cleaned[1:], digits[1:]):
        if code:
            if code != previous:
                result.append(code)
                previous = code
            # else collapse adjacent duplicate
        elif ch in _TRANSPARENT:
            # H and W are transparent -- they do not break adjacency.
            pass
        else:
            # Vowels and Y break adjacency.
            previous = ""
        if len(result) == 4:
            break
    return ("".join(result) + "000")[:4]

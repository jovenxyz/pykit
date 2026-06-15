"""T9 / phone-keypad letter combinations from digit sequences."""
from __future__ import annotations

from typing import Iterator, List

_KEYPAD = {
    "2": "abc", "3": "def", "4": "ghi",
    "5": "jkl", "6": "mno", "7": "pqrs",
    "8": "tuv", "9": "wxyz",
}


def letter_combinations(digits: str) -> List[str]:
    """Return every letter combination encoded by ``digits`` (T9 keypad)."""
    if digits == "":
        return []
    if any(d not in _KEYPAD for d in digits):
        raise ValueError(f"only digits 2-9 are allowed: {digits!r}")
    results = [""]
    for digit in digits:
        results = [prefix + letter for prefix in results for letter in _KEYPAD[digit]]
    return results


def iter_letter_combinations(digits: str) -> Iterator[str]:
    """Yield each letter combination one at a time (memory-friendly)."""
    if digits == "":
        return
    if any(d not in _KEYPAD for d in digits):
        raise ValueError(f"only digits 2-9 are allowed: {digits!r}")

    def _recurse(prefix: str, index: int) -> Iterator[str]:
        if index == len(digits):
            yield prefix
            return
        for letter in _KEYPAD[digits[index]]:
            yield from _recurse(prefix + letter, index + 1)

    yield from _recurse("", 0)


def digits_for(text: str) -> str:
    """Encode ASCII ``text`` back into a T9 digit sequence."""
    reverse = {ch: digit for digit, letters in _KEYPAD.items() for ch in letters}
    out = []
    for char in text:
        key = char.lower()
        if key not in reverse:
            raise ValueError(f"character not on keypad: {char!r}")
        out.append(reverse[key])
    return "".join(out)

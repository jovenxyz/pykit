"""Convert between integers and Roman numerals (1..3999)."""
from __future__ import annotations

_NUMERALS = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
]

_VALUES = {symbol: value for value, symbol in _NUMERALS}


def to_roman(number: int) -> str:
    if not 1 <= number <= 3999:
        raise ValueError("number must be between 1 and 3999")
    parts = []
    for value, symbol in _NUMERALS:
        count, number = divmod(number, value)
        parts.append(symbol * count)
    return "".join(parts)


def from_roman(numeral: str) -> int:
    total = 0
    previous = 0
    for char in reversed(numeral.upper()):
        if char not in _VALUES:
            raise ValueError(f"invalid Roman numeral character: {char!r}")
        value = _VALUES[char]
        if value < previous:
            total -= value
        else:
            total += value
            previous = value
    return total

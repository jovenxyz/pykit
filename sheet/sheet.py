"""Convert between spreadsheet column letters and 1-based indices."""
from __future__ import annotations


def column_to_index(column: str) -> int:
    """Convert ``"A"`` -> 1, ``"Z"`` -> 26, ``"AA"`` -> 27, ``"AZ"`` -> 52, ..."""
    if not column or not column.isalpha():
        raise ValueError(
            f"column must be a non-empty alphabetic string: {column!r}"
        )
    result = 0
    for char in column.upper():
        result = result * 26 + (ord(char) - ord("A") + 1)
    return result


def index_to_column(index: int) -> str:
    """Convert ``1`` -> ``"A"``, ``27`` -> ``"AA"``, etc."""
    if index < 1:
        raise ValueError(f"index must be >= 1: {index}")
    chars = []
    while index > 0:
        index -= 1
        chars.append(chr(index % 26 + ord("A")))
        index //= 26
    return "".join(reversed(chars))

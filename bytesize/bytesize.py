"""Format and parse human-readable byte sizes."""
from __future__ import annotations

import re

_UNITS = ["B", "KB", "MB", "GB", "TB", "PB"]
_PARSE = re.compile(r"^\s*([0-9]+(?:\.[0-9]+)?)\s*([a-zA-Z]*)\s*$")
_FACTORS = {
    "": 1,
    "B": 1,
    "K": 1024, "KB": 1024,
    "M": 1024 ** 2, "MB": 1024 ** 2,
    "G": 1024 ** 3, "GB": 1024 ** 3,
    "T": 1024 ** 4, "TB": 1024 ** 4,
    "P": 1024 ** 5, "PB": 1024 ** 5,
}


def format_bytes(size: int, precision: int = 1) -> str:
    """Return a human-readable representation of ``size`` bytes."""
    if size < 0:
        raise ValueError("size must be non-negative")
    value = float(size)
    for unit in _UNITS:
        if value < 1024 or unit == _UNITS[-1]:
            if unit == "B":
                return f"{int(value)} {unit}"
            return f"{value:.{precision}f} {unit}"
        value /= 1024
    return f"{value:.{precision}f} {_UNITS[-1]}"


def parse_size(text: str) -> int:
    """Parse strings like '1.5 MB' into a number of bytes."""
    match = _PARSE.match(text)
    if not match:
        raise ValueError(f"invalid size: {text!r}")
    number, unit = match.groups()
    unit = unit.upper()
    if unit not in _FACTORS:
        raise ValueError(f"unknown unit: {unit!r}")
    return int(float(number) * _FACTORS[unit])

"""Gray-code conversions and enumeration."""
from __future__ import annotations

from typing import List


def to_gray(value: int) -> int:
    """Convert a non-negative integer to its reflected binary Gray code."""
    if value < 0:
        raise ValueError("value must be non-negative")
    return value ^ (value >> 1)


def from_gray(gray: int) -> int:
    """Convert a Gray-code integer back to its standard binary value."""
    if gray < 0:
        raise ValueError("gray must be non-negative")
    value = gray
    shift = 1
    while gray >> shift:
        value ^= gray >> shift
        shift += 1
    return value


def sequence(bits: int) -> List[int]:
    """Return all ``2**bits`` Gray-code values in order (0..2**bits-1)."""
    if bits < 0:
        raise ValueError("bits must be non-negative")
    return [to_gray(i) for i in range(1 << bits)]

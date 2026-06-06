"""Generate ULID-like sortable short identifiers."""
from __future__ import annotations

import secrets
import time
from typing import Callable, Optional


# Crockford's Base32 (excludes I, L, O, U) -- the standard ULID alphabet.
_ALPHABET = "0123456789ABCDEFGHJKMNPQRSTVWXYZ"
_INDEX = {ch: i for i, ch in enumerate(_ALPHABET)}


def _encode(value: int, length: int) -> str:
    if value < 0:
        raise ValueError("value must be non-negative")
    chars = []
    for _ in range(length):
        value, remainder = divmod(value, 32)
        chars.append(_ALPHABET[remainder])
    if value:
        raise ValueError(f"value does not fit in {length} base32 characters")
    return "".join(reversed(chars))


def new(
    *,
    timestamp_ms: Optional[int] = None,
    time_func: Callable[[], float] = time.time,
    random_func: Callable[[int], int] = lambda n: secrets.randbits(n),
) -> str:
    """Return a new 26-character ULID-like identifier.

    Composed of a 48-bit millisecond timestamp (10 base32 chars) and an
    80-bit random tail (16 base32 chars).
    """
    if timestamp_ms is None:
        timestamp_ms = int(time_func() * 1000)
    if timestamp_ms < 0 or timestamp_ms >= 1 << 48:
        raise ValueError("timestamp_ms must fit in 48 bits")
    randomness = random_func(80)
    return _encode(timestamp_ms, 10) + _encode(randomness, 16)


def timestamp_ms_of(ulid: str) -> int:
    """Return the millisecond timestamp embedded in a ULID."""
    if len(ulid) != 26:
        raise ValueError("ULID must be 26 characters long")
    value = 0
    for char in ulid[:10]:
        if char not in _INDEX:
            raise ValueError(f"invalid ULID character: {char!r}")
        value = value * 32 + _INDEX[char]
    return value

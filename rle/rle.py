"""Run-length encoding and decoding of strings."""
from __future__ import annotations

import re
from typing import Iterable, List, Tuple


def encode(text: str) -> List[Tuple[str, int]]:
    """Return a list of ``(character, run_length)`` pairs."""
    if not text:
        return []
    pairs: List[Tuple[str, int]] = []
    previous = text[0]
    count = 1
    for char in text[1:]:
        if char == previous:
            count += 1
        else:
            pairs.append((previous, count))
            previous = char
            count = 1
    pairs.append((previous, count))
    return pairs


def decode(pairs: Iterable[Tuple[str, int]]) -> str:
    """Decode a sequence of ``(character, run_length)`` pairs back to text."""
    parts = []
    for char, count in pairs:
        if len(char) != 1:
            raise ValueError(f"each entry must be a single character: {char!r}")
        if count < 1:
            raise ValueError(f"run length must be positive: {count}")
        parts.append(char * count)
    return "".join(parts)


_TOKEN = re.compile(r"(\d+)(.)")
_FULL = re.compile(r"(\d+.)+")


def encode_string(text: str) -> str:
    """Return a compact string form like ``"3a2b1c"``."""
    return "".join(f"{count}{char}" for char, count in encode(text))


def decode_string(encoded: str) -> str:
    """Inverse of :func:`encode_string`."""
    if not encoded:
        return ""
    if not _FULL.fullmatch(encoded):
        raise ValueError(f"invalid run-length encoding: {encoded!r}")
    return "".join(char * int(count) for count, char in _TOKEN.findall(encoded))

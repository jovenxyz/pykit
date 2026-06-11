"""LZ77 sliding-window compression and decompression."""
from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Token:
    offset: int       # how far back to look (0 for a pure literal)
    length: int       # match length (0 for a pure literal)
    next_byte: int    # next literal byte (0..255)


def compress(
    data: bytes,
    *,
    window_size: int = 4096,
    lookahead: int = 18,
) -> List[Token]:
    """Compress ``data`` into a list of ``(offset, length, next_byte)`` tokens."""
    if window_size <= 0 or lookahead <= 0:
        raise ValueError("window_size and lookahead must be positive")
    tokens: List[Token] = []
    i = 0
    n = len(data)
    while i < n:
        match_offset = 0
        match_length = 0
        start = max(0, i - window_size)
        # Reserve one byte at the end of the lookahead for ``next_byte``.
        max_len = min(lookahead, n - i - 1)
        for j in range(start, i):
            length = 0
            while length < max_len and data[j + length] == data[i + length]:
                length += 1
            if length > match_length:
                match_length = length
                match_offset = i - j
        next_index = i + match_length
        next_byte = data[next_index] if next_index < n else 0
        tokens.append(Token(match_offset, match_length, next_byte))
        i = next_index + 1
    return tokens


def decompress(tokens: List[Token]) -> bytes:
    """Reverse :func:`compress` and return the original byte string."""
    output = bytearray()
    for token in tokens:
        if token.offset:
            start = len(output) - token.offset
            for k in range(token.length):
                output.append(output[start + k])
        output.append(token.next_byte)
    return bytes(output)

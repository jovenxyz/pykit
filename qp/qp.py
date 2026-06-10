"""Quoted-printable encoding and decoding (RFC 2045)."""
from __future__ import annotations


_SAFE = {chr(c) for c in range(33, 127) if c != ord("=")}


def encode(data: bytes, *, line_length: int = 76) -> str:
    """Encode ``data`` as quoted-printable text.

    Printable ASCII (except ``=``) and spaces / tabs pass through; all
    other bytes become ``=XX`` hex escapes. Lines are softly wrapped at
    ``line_length`` columns using ``=\\n`` continuations.
    """
    if line_length <= 3:
        raise ValueError("line_length must be > 3")
    tokens = []
    for byte in data:
        char = chr(byte)
        if char in _SAFE or char in (" ", "\t"):
            tokens.append(char)
        else:
            tokens.append(f"={byte:02X}")
    lines = []
    line = ""
    for token in tokens:
        if len(line) + len(token) > line_length - 1:
            lines.append(line + "=")
            line = ""
        line += token
    lines.append(line)
    return "\n".join(lines)


def decode(text: str) -> bytes:
    """Decode quoted-printable text back into bytes."""
    result = bytearray()
    i = 0
    while i < len(text):
        char = text[i]
        if char == "=":
            if i + 1 < len(text) and text[i + 1] == "\n":
                i += 2
                continue
            if i + 2 < len(text) and text[i + 1] == "\r" and text[i + 2] == "\n":
                i += 3
                continue
            if i + 2 >= len(text):
                raise ValueError(f"truncated escape at position {i}")
            hex_digits = text[i + 1:i + 3]
            try:
                result.append(int(hex_digits, 16))
            except ValueError as error:
                raise ValueError(f"invalid escape =\"{hex_digits}\"") from error
            i += 3
            continue
        result.append(ord(char))
        i += 1
    return bytes(result)

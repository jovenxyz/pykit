"""Base58 encoder and decoder (Bitcoin / IPFS alphabet)."""
from __future__ import annotations

_ALPHABET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
_INDEX = {ch: i for i, ch in enumerate(_ALPHABET)}
_BASE = len(_ALPHABET)


def encode(data: bytes) -> str:
    """Encode ``data`` as a base58 string."""
    if not isinstance(data, (bytes, bytearray)):
        raise TypeError("data must be bytes")
    # Count leading zero bytes; they become leading '1' characters.
    leading_zeros = 0
    for byte in data:
        if byte == 0:
            leading_zeros += 1
        else:
            break
    number = int.from_bytes(data, "big")
    chars = []
    while number:
        number, remainder = divmod(number, _BASE)
        chars.append(_ALPHABET[remainder])
    return _ALPHABET[0] * leading_zeros + "".join(reversed(chars))


def decode(text: str) -> bytes:
    """Decode a base58 string back into bytes."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    leading_ones = 0
    for char in text:
        if char == _ALPHABET[0]:
            leading_ones += 1
        else:
            break
    number = 0
    for char in text:
        if char not in _INDEX:
            raise ValueError(f"invalid base58 character: {char!r}")
        number = number * _BASE + _INDEX[char]
    if number:
        encoded = number.to_bytes((number.bit_length() + 7) // 8, "big")
    else:
        encoded = b""
    return b"\x00" * leading_ones + encoded

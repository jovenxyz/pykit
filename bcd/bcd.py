"""Binary-Coded Decimal (BCD) encoding / decoding.

Packed BCD stores two decimal digits per byte (high nibble = first digit).
For odd-length numbers the leading nibble is zero-padded.
"""
from __future__ import annotations


def encode(n: int) -> bytes:
    """Encode a non-negative integer as packed BCD bytes."""
    if n < 0:
        raise ValueError("BCD encoding requires non-negative integer")
    digits = str(n)
    if len(digits) % 2 == 1:
        digits = "0" + digits
    out = bytearray()
    for i in range(0, len(digits), 2):
        hi = int(digits[i])
        lo = int(digits[i + 1])
        out.append((hi << 4) | lo)
    return bytes(out)


def decode(data: bytes) -> int:
    """Decode packed BCD bytes back to an integer."""
    digits = []
    for b in data:
        hi = (b >> 4) & 0x0F
        lo = b & 0x0F
        if hi > 9 or lo > 9:
            raise ValueError(f"invalid BCD nibble in byte 0x{b:02x}")
        digits.append(str(hi))
        digits.append(str(lo))
    s = "".join(digits).lstrip("0")
    return int(s) if s else 0


def encode_unpacked(n: int) -> bytes:
    """Encode each decimal digit in its own byte (unpacked BCD)."""
    if n < 0:
        raise ValueError("BCD encoding requires non-negative integer")
    return bytes(int(d) for d in str(n))


def decode_unpacked(data: bytes) -> int:
    digits = []
    for b in data:
        if b > 9:
            raise ValueError(f"invalid unpacked BCD digit 0x{b:02x}")
        digits.append(str(b))
    s = "".join(digits).lstrip("0")
    return int(s) if s else 0


def byte_to_digits(b: int) -> tuple[int, int]:
    """Split a packed BCD byte into its (high, low) decimal digits."""
    if not 0 <= b <= 0xFF:
        raise ValueError("byte must be 0..255")
    hi = (b >> 4) & 0x0F
    lo = b & 0x0F
    if hi > 9 or lo > 9:
        raise ValueError("byte is not valid BCD")
    return hi, lo

"""Convert IPv4 addresses between dotted-quad strings and 32-bit integers."""
from __future__ import annotations


def ip_to_int(address: str) -> int:
    """Convert ``"192.168.1.1"`` into a 32-bit unsigned integer."""
    parts = address.strip().split(".")
    if len(parts) != 4:
        raise ValueError(f"invalid IPv4 address: {address!r}")
    result = 0
    for part in parts:
        if not part.isdigit():
            raise ValueError(f"invalid IPv4 address: {address!r}")
        octet = int(part)
        if not 0 <= octet <= 255:
            raise ValueError(f"octet out of range 0-255: {octet}")
        result = (result << 8) | octet
    return result


def int_to_ip(number: int) -> str:
    """Convert a 32-bit unsigned integer back into a dotted-quad string."""
    if not 0 <= number <= 0xFFFFFFFF:
        raise ValueError("number must fit in 32 bits (0 - 4294967295)")
    return "{}.{}.{}.{}".format(
        (number >> 24) & 0xFF,
        (number >> 16) & 0xFF,
        (number >> 8) & 0xFF,
        number & 0xFF,
    )

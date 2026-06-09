"""CRC-32 (IEEE 802.3 polynomial) implemented from first principles."""
from __future__ import annotations

from typing import List

# Reflected IEEE 802.3 polynomial; matches ZIP, PNG and zlib.crc32.
_POLY = 0xEDB88320
_MASK = 0xFFFFFFFF


def _build_table() -> List[int]:
    table = []
    for byte in range(256):
        value = byte
        for _ in range(8):
            value = (value >> 1) ^ _POLY if value & 1 else value >> 1
        table.append(value)
    return table


_TABLE = _build_table()


def crc32(data: bytes, *, initial: int = 0) -> int:
    """Return the IEEE 802.3 CRC-32 of ``data``.

    Matches ``zlib.crc32``. Pass ``initial=`` (a previous result) to extend
    a running checksum across multiple chunks of data.
    """
    crc = (~initial) & _MASK
    for byte in data:
        crc = (crc >> 8) ^ _TABLE[(crc ^ byte) & 0xFF]
    return (~crc) & _MASK


def crc32_hex(data: bytes) -> str:
    """Return ``crc32(data)`` as an 8-character lowercase hex string."""
    return f"{crc32(data):08x}"

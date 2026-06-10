"""Bit-level read/write streams over bytes (MSB-first)."""
from __future__ import annotations


class BitWriter:
    """Append individual bits to an in-memory byte buffer."""

    def __init__(self) -> None:
        self._bytes = bytearray()
        self._current = 0
        self._bit_count = 0

    def write_bit(self, bit: int) -> None:
        if bit not in (0, 1):
            raise ValueError(f"bit must be 0 or 1, got {bit!r}")
        self._current = (self._current << 1) | bit
        self._bit_count += 1
        if self._bit_count == 8:
            self._bytes.append(self._current)
            self._current = 0
            self._bit_count = 0

    def write_bits(self, value: int, width: int) -> None:
        if width < 0:
            raise ValueError("width must be non-negative")
        if value < 0 or value >= 1 << width:
            raise ValueError(f"value {value} does not fit in {width} bits")
        for shift in range(width - 1, -1, -1):
            self.write_bit((value >> shift) & 1)

    def to_bytes(self) -> bytes:
        """Return all written bits as bytes; the last byte is zero-padded."""
        if self._bit_count == 0:
            return bytes(self._bytes)
        padding = 8 - self._bit_count
        return bytes(self._bytes) + bytes([self._current << padding])

    @property
    def total_bits(self) -> int:
        return len(self._bytes) * 8 + self._bit_count


class BitReader:
    """Read individual bits from a byte buffer."""

    def __init__(self, data: bytes) -> None:
        self._data = data
        self._position = 0          # bit position; 0 = MSB of byte 0

    def read_bit(self) -> int:
        if self._position >= len(self._data) * 8:
            raise EOFError("no more bits to read")
        byte_index, bit_index = divmod(self._position, 8)
        bit = (self._data[byte_index] >> (7 - bit_index)) & 1
        self._position += 1
        return bit

    def read_bits(self, width: int) -> int:
        if width < 0:
            raise ValueError("width must be non-negative")
        value = 0
        for _ in range(width):
            value = (value << 1) | self.read_bit()
        return value

    @property
    def bits_remaining(self) -> int:
        return len(self._data) * 8 - self._position

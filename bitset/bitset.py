"""A compact bit set supporting basic set operations."""
from __future__ import annotations

from typing import Iterator


class BitSet:
    """Fixed-size mutable set of bit indices in ``[0, size)``."""

    def __init__(self, size: int) -> None:
        if size < 0:
            raise ValueError("size must be non-negative")
        self._size = size
        self._words = bytearray((size + 7) // 8)

    @property
    def size(self) -> int:
        return self._size

    def _check(self, index: int) -> None:
        if not 0 <= index < self._size:
            raise IndexError(f"bit {index} out of range for size {self._size}")

    def set(self, index: int, value: bool = True) -> None:
        self._check(index)
        word, bit = divmod(index, 8)
        mask = 1 << bit
        if value:
            self._words[word] |= mask
        else:
            self._words[word] &= 0xFF ^ mask

    def clear(self, index: int) -> None:
        self.set(index, False)

    def get(self, index: int) -> bool:
        self._check(index)
        word, bit = divmod(index, 8)
        return bool(self._words[word] & (1 << bit))

    def toggle(self, index: int) -> None:
        self._check(index)
        word, bit = divmod(index, 8)
        self._words[word] ^= 1 << bit

    def count(self) -> int:
        return sum(bin(b).count("1") for b in self._words)

    def union(self, other: "BitSet") -> "BitSet":
        self._same_size(other)
        result = BitSet(self._size)
        result._words = bytearray(a | b for a, b in zip(self._words, other._words))
        return result

    def intersect(self, other: "BitSet") -> "BitSet":
        self._same_size(other)
        result = BitSet(self._size)
        result._words = bytearray(a & b for a, b in zip(self._words, other._words))
        return result

    def difference(self, other: "BitSet") -> "BitSet":
        self._same_size(other)
        result = BitSet(self._size)
        result._words = bytearray(a & (0xFF ^ b) for a, b in zip(self._words, other._words))
        return result

    def _same_size(self, other: "BitSet") -> None:
        if other._size != self._size:
            raise ValueError("bitsets must be the same size")

    def __getitem__(self, index: int) -> bool:
        return self.get(index)

    def __setitem__(self, index: int, value: bool) -> None:
        self.set(index, value)

    def __contains__(self, index: int) -> bool:
        if not 0 <= index < self._size:
            return False
        return self.get(index)

    def __len__(self) -> int:
        return self.count()

    def __iter__(self) -> Iterator[int]:
        for i in range(self._size):
            if self.get(i):
                yield i

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, BitSet):
            return NotImplemented
        return self._size == other._size and self._words == other._words

    def __repr__(self) -> str:
        return f"BitSet({self._size}, set={list(self)})"

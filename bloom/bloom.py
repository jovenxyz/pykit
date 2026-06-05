"""A simple Bloom filter -- a probabilistic set with no false negatives."""
from __future__ import annotations

import hashlib
import math


class BloomFilter:
    """Approximate set membership with a tunable false-positive rate."""

    def __init__(
        self,
        expected_items: int,
        false_positive_rate: float = 0.01,
    ) -> None:
        if expected_items <= 0:
            raise ValueError("expected_items must be positive")
        if not 0 < false_positive_rate < 1:
            raise ValueError("false_positive_rate must be between 0 and 1")
        self._size = self._optimal_size(expected_items, false_positive_rate)
        self._hash_count = self._optimal_hashes(self._size, expected_items)
        self._bits = bytearray((self._size + 7) // 8)
        self._added = 0

    @staticmethod
    def _optimal_size(n: int, p: float) -> int:
        return max(1, int(math.ceil(-n * math.log(p) / (math.log(2) ** 2))))

    @staticmethod
    def _optimal_hashes(m: int, n: int) -> int:
        return max(1, int(round((m / n) * math.log(2))))

    def _positions(self, item: object):
        encoded = repr(item).encode("utf-8")
        digest = hashlib.sha256(encoded).digest()
        # Treat the digest as two 8-byte halves and use double-hashing to
        # generate ``hash_count`` independent positions.
        h1 = int.from_bytes(digest[:8], "big")
        h2 = int.from_bytes(digest[8:16], "big") or 1
        for i in range(self._hash_count):
            yield (h1 + i * h2) % self._size

    def add(self, item: object) -> None:
        for position in self._positions(item):
            self._bits[position // 8] |= 1 << (position % 8)
        self._added += 1

    def __contains__(self, item: object) -> bool:
        for position in self._positions(item):
            if not (self._bits[position // 8] >> (position % 8)) & 1:
                return False
        return True

    def __len__(self) -> int:
        return self._added

    @property
    def bit_size(self) -> int:
        return self._size

    @property
    def hash_count(self) -> int:
        return self._hash_count

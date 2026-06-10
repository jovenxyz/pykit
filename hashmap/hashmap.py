"""A tiny chained hash table built from scratch."""
from __future__ import annotations

from typing import Any, Hashable, Iterator, List, Tuple


class HashMap:
    """Separate-chaining hash map with dynamic resizing."""

    def __init__(
        self,
        *,
        initial_capacity: int = 8,
        load_factor: float = 0.75,
    ) -> None:
        if initial_capacity < 1:
            raise ValueError("initial_capacity must be >= 1")
        if not 0 < load_factor < 1:
            raise ValueError("load_factor must be in (0, 1)")
        self._capacity = initial_capacity
        self._load_factor = load_factor
        self._buckets: List[List[Tuple[Hashable, Any]]] = [
            [] for _ in range(initial_capacity)
        ]
        self._size = 0

    def _bucket_for(self, key: Hashable) -> List[Tuple[Hashable, Any]]:
        return self._buckets[hash(key) % self._capacity]

    def _resize(self, new_capacity: int) -> None:
        old_buckets = self._buckets
        self._capacity = new_capacity
        self._buckets = [[] for _ in range(new_capacity)]
        for bucket in old_buckets:
            for key, value in bucket:
                self._buckets[hash(key) % new_capacity].append((key, value))

    def __setitem__(self, key: Hashable, value: Any) -> None:
        bucket = self._bucket_for(key)
        for i, (existing, _) in enumerate(bucket):
            if existing == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self._size += 1
        if self._size / self._capacity > self._load_factor:
            self._resize(self._capacity * 2)

    def __getitem__(self, key: Hashable) -> Any:
        for existing, value in self._bucket_for(key):
            if existing == key:
                return value
        raise KeyError(key)

    def __delitem__(self, key: Hashable) -> None:
        bucket = self._bucket_for(key)
        for i, (existing, _) in enumerate(bucket):
            if existing == key:
                del bucket[i]
                self._size -= 1
                return
        raise KeyError(key)

    def __contains__(self, key: Hashable) -> bool:
        return any(existing == key for existing, _ in self._bucket_for(key))

    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> Iterator[Hashable]:
        for bucket in self._buckets:
            for key, _ in bucket:
                yield key

    def get(self, key: Hashable, default: Any = None) -> Any:
        for existing, value in self._bucket_for(key):
            if existing == key:
                return value
        return default

    def items(self) -> List[Tuple[Hashable, Any]]:
        return [(k, v) for bucket in self._buckets for (k, v) in bucket]

    @property
    def capacity(self) -> int:
        return self._capacity

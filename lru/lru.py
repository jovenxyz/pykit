"""A bounded least-recently-used (LRU) cache."""
from __future__ import annotations

from collections import OrderedDict
from typing import Any, Hashable

_MISSING = object()


class LRUCache:
    """Mapping that evicts the least-recently-used key when full."""

    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self._capacity = capacity
        self._data: OrderedDict = OrderedDict()
        self._hits = 0
        self._misses = 0

    def get(self, key: Hashable, default: Any = None) -> Any:
        """Return the value for ``key``; mark it as most recently used."""
        if key not in self._data:
            self._misses += 1
            return default
        self._hits += 1
        self._data.move_to_end(key)
        return self._data[key]

    def set(self, key: Hashable, value: Any) -> None:
        """Insert or replace ``key`` and mark it as most recently used."""
        if key in self._data:
            self._data.move_to_end(key)
        self._data[key] = value
        if len(self._data) > self._capacity:
            self._data.popitem(last=False)

    def __getitem__(self, key: Hashable) -> Any:
        value = self.get(key, _MISSING)
        if value is _MISSING:
            raise KeyError(key)
        return value

    def __setitem__(self, key: Hashable, value: Any) -> None:
        self.set(key, value)

    def __contains__(self, key: Hashable) -> bool:
        return key in self._data

    def __len__(self) -> int:
        return len(self._data)

    @property
    def stats(self) -> dict:
        return {
            "hits": self._hits,
            "misses": self._misses,
            "size": len(self._data),
        }

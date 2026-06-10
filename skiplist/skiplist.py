"""A probabilistic skip list -- sorted set with O(log n) expected operations."""
from __future__ import annotations

import random
from typing import Any, List, Optional


class _Node:
    __slots__ = ("value", "forward")

    def __init__(self, value: Any, level: int) -> None:
        self.value = value
        self.forward: List[Optional["_Node"]] = [None] * (level + 1)


class SkipList:
    """Sorted set supporting O(log n) expected insert / contains / remove."""

    def __init__(
        self,
        *,
        max_level: int = 16,
        p: float = 0.5,
        rng: Optional[random.Random] = None,
    ) -> None:
        if max_level < 1:
            raise ValueError("max_level must be >= 1")
        if not 0 < p < 1:
            raise ValueError("p must be in (0, 1)")
        self._max_level = max_level
        self._p = p
        self._rng = rng if rng is not None else random
        self._head = _Node(value=None, level=max_level)
        self._level = 0
        self._size = 0

    def _random_level(self) -> int:
        level = 0
        while level < self._max_level and self._rng.random() < self._p:
            level += 1
        return level

    def insert(self, value: Any) -> bool:
        """Insert ``value``; return ``True`` if added, ``False`` if duplicate."""
        update = [self._head] * (self._max_level + 1)
        current = self._head
        for i in range(self._level, -1, -1):
            while current.forward[i] is not None and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current
        nxt = current.forward[0]
        if nxt is not None and nxt.value == value:
            return False
        level = self._random_level()
        if level > self._level:
            for i in range(self._level + 1, level + 1):
                update[i] = self._head
            self._level = level
        node = _Node(value, level)
        for i in range(level + 1):
            node.forward[i] = update[i].forward[i]
            update[i].forward[i] = node
        self._size += 1
        return True

    def contains(self, value: Any) -> bool:
        current = self._head
        for i in range(self._level, -1, -1):
            while current.forward[i] is not None and current.forward[i].value < value:
                current = current.forward[i]
        nxt = current.forward[0]
        return nxt is not None and nxt.value == value

    def remove(self, value: Any) -> bool:
        """Remove ``value``; return ``True`` if found, ``False`` otherwise."""
        update = [self._head] * (self._max_level + 1)
        current = self._head
        for i in range(self._level, -1, -1):
            while current.forward[i] is not None and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current
        target = current.forward[0]
        if target is None or target.value != value:
            return False
        for i in range(self._level + 1):
            if update[i].forward[i] is not target:
                break
            update[i].forward[i] = target.forward[i]
        while self._level > 0 and self._head.forward[self._level] is None:
            self._level -= 1
        self._size -= 1
        return True

    def __iter__(self):
        current = self._head.forward[0]
        while current is not None:
            yield current.value
            current = current.forward[0]

    def __len__(self) -> int:
        return self._size

    def __contains__(self, value: Any) -> bool:
        return self.contains(value)

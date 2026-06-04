"""A simple in-memory trie (prefix tree)."""
from __future__ import annotations

from typing import Dict, Iterator, List


_TERMINAL = "$"


class Trie:
    """Set of strings supporting prefix queries."""

    def __init__(self) -> None:
        self._root: Dict = {}
        self._size = 0

    def insert(self, word: str) -> None:
        node = self._root
        for char in word:
            node = node.setdefault(char, {})
        if not node.get(_TERMINAL, False):
            node[_TERMINAL] = True
            self._size += 1

    def contains(self, word: str) -> bool:
        node = self._root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return bool(node.get(_TERMINAL, False))

    def starts_with(self, prefix: str) -> bool:
        node = self._root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True

    def with_prefix(self, prefix: str) -> List[str]:
        node = self._root
        for char in prefix:
            if char not in node:
                return []
            node = node[char]
        return [prefix + suffix for suffix in self._walk(node)]

    def _walk(self, node: Dict) -> Iterator[str]:
        if node.get(_TERMINAL, False):
            yield ""
        for char, child in node.items():
            if char == _TERMINAL:
                continue
            for suffix in self._walk(child):
                yield char + suffix

    def __len__(self) -> int:
        return self._size

    def __contains__(self, word: str) -> bool:
        return self.contains(word)

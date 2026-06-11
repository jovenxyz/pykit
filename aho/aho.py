"""Aho-Corasick multi-pattern string search.

Build a finite-state machine from a set of patterns and find every
occurrence of every pattern in a single linear-time pass over the text.
"""
from __future__ import annotations

from collections import deque
from typing import Dict, Iterable, List, Tuple


class AhoCorasick:
    """Match every pattern in a single pass over the text."""

    def __init__(self, patterns: Iterable[str]) -> None:
        self._goto: List[Dict[str, int]] = [{}]
        self._fail: List[int] = [0]
        self._output: List[List[int]] = [[]]
        self._patterns: List[str] = []
        for pattern in patterns:
            self._add(pattern)
        self._build_failure()

    def _add(self, pattern: str) -> None:
        if not pattern:
            raise ValueError("patterns must be non-empty")
        node = 0
        for char in pattern:
            if char in self._goto[node]:
                node = self._goto[node][char]
            else:
                new_node = len(self._goto)
                self._goto.append({})
                self._fail.append(0)
                self._output.append([])
                self._goto[node][char] = new_node
                node = new_node
        self._output[node].append(len(self._patterns))
        self._patterns.append(pattern)

    def _build_failure(self) -> None:
        queue: deque = deque()
        for child in self._goto[0].values():
            self._fail[child] = 0
            queue.append(child)
        while queue:
            node = queue.popleft()
            for char, child in self._goto[node].items():
                queue.append(child)
                f = self._fail[node]
                while f != 0 and char not in self._goto[f]:
                    f = self._fail[f]
                if char in self._goto[f] and self._goto[f][char] != child:
                    self._fail[child] = self._goto[f][char]
                else:
                    self._fail[child] = 0
                self._output[child].extend(self._output[self._fail[child]])

    def find(self, text: str) -> List[Tuple[int, str]]:
        """Return ``(start_index, pattern)`` for every match in ``text``."""
        results: List[Tuple[int, str]] = []
        node = 0
        for i, char in enumerate(text):
            while node and char not in self._goto[node]:
                node = self._fail[node]
            node = self._goto[node].get(char, 0)
            for pattern_index in self._output[node]:
                pattern = self._patterns[pattern_index]
                results.append((i - len(pattern) + 1, pattern))
        return results

    @property
    def patterns(self) -> List[str]:
        return list(self._patterns)

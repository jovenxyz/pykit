"""A binary min-heap implemented on a list."""
from __future__ import annotations

from typing import List


class MinHeap:
    """Priority queue returning the smallest element first."""

    def __init__(self) -> None:
        self._data: List[int] = []

    def push(self, value: int) -> None:
        self._data.append(value)
        self._sift_up(len(self._data) - 1)

    def pop(self) -> int:
        if not self._data:
            raise IndexError("pop from empty heap")
        last = len(self._data) - 1
        self._data[0], self._data[last] = self._data[last], self._data[0]
        smallest = self._data.pop()
        if self._data:
            self._sift_down(0)
        return smallest

    def peek(self) -> int:
        if not self._data:
            raise IndexError("peek from empty heap")
        return self._data[0]

    def _sift_up(self, index: int) -> None:
        while index > 0:
            parent = (index - 1) // 2
            if self._data[index] >= self._data[parent]:
                break
            self._data[index], self._data[parent] = (
                self._data[parent],
                self._data[index],
            )
            index = parent

    def _sift_down(self, index: int) -> None:
        size = len(self._data)
        while True:
            left, right = 2 * index + 1, 2 * index + 2
            smallest = index
            if left < size and self._data[left] < self._data[smallest]:
                smallest = left
            if right < size and self._data[right] < self._data[smallest]:
                smallest = right
            if smallest == index:
                break
            self._data[index], self._data[smallest] = (
                self._data[smallest],
                self._data[index],
            )
            index = smallest

    def __len__(self) -> int:
        return len(self._data)

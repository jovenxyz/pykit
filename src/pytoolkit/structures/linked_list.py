"""A minimal singly linked list."""
from __future__ import annotations

from typing import Generic, Iterator, Optional, TypeVar

T = TypeVar("T")


class _Node(Generic[T]):
    __slots__ = ("value", "next")

    def __init__(self, value: T) -> None:
        self.value = value
        self.next: Optional["_Node[T]"] = None


class LinkedList(Generic[T]):
    """Singly linked list with append and search."""

    def __init__(self) -> None:
        self._head: Optional[_Node[T]] = None
        self._size = 0

    def append(self, value: T) -> None:
        node = _Node(value)
        if self._head is None:
            self._head = node
        else:
            current = self._head
            while current.next is not None:
                current = current.next
            current.next = node
        self._size += 1

    def find(self, value: T) -> bool:
        current = self._head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def __iter__(self) -> Iterator[T]:
        current = self._head
        while current is not None:
            yield current.value
            current = current.next

    def __len__(self) -> int:
        return self._size

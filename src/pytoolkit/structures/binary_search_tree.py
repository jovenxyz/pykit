"""An unbalanced binary search tree of integers."""
from __future__ import annotations

from typing import List, Optional


class _Node:
    __slots__ = ("key", "left", "right")

    def __init__(self, key: int) -> None:
        self.key = key
        self.left: Optional["_Node"] = None
        self.right: Optional["_Node"] = None


class BinarySearchTree:
    """Ordered set of integers."""

    def __init__(self) -> None:
        self._root: Optional[_Node] = None

    def insert(self, key: int) -> None:
        self._root = self._insert(self._root, key)

    def _insert(self, node: Optional[_Node], key: int) -> _Node:
        if node is None:
            return _Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node

    def contains(self, key: int) -> bool:
        node = self._root
        while node is not None:
            if key == node.key:
                return True
            node = node.left if key < node.key else node.right
        return False

    def inorder(self) -> List[int]:
        result: List[int] = []
        self._inorder(self._root, result)
        return result

    def _inorder(self, node: Optional[_Node], out: List[int]) -> None:
        if node is None:
            return
        self._inorder(node.left, out)
        out.append(node.key)
        self._inorder(node.right, out)

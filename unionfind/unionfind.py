"""Union-Find (Disjoint Set Union) with path compression and union by rank."""
from __future__ import annotations

from typing import Dict, Hashable


class UnionFind:
    """Track equivalence classes under union operations."""

    def __init__(self) -> None:
        self._parent: Dict[Hashable, Hashable] = {}
        self._rank: Dict[Hashable, int] = {}
        self._size: Dict[Hashable, int] = {}
        self._components = 0

    def add(self, item: Hashable) -> None:
        """Register ``item`` as a new singleton component (no-op if already)."""
        if item in self._parent:
            return
        self._parent[item] = item
        self._rank[item] = 0
        self._size[item] = 1
        self._components += 1

    def find(self, item: Hashable) -> Hashable:
        """Return the representative of ``item``'s component."""
        if item not in self._parent:
            self.add(item)
            return item
        root = item
        while self._parent[root] != root:
            root = self._parent[root]
        # Path compression: point every node on the walk directly at root.
        while self._parent[item] != root:
            self._parent[item], item = root, self._parent[item]
        return root

    def union(self, a: Hashable, b: Hashable) -> bool:
        """Merge the components containing ``a`` and ``b``.

        Returns ``True`` if a merge happened, ``False`` if they were already
        in the same component.
        """
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return False
        # Union by rank.
        if self._rank[root_a] < self._rank[root_b]:
            root_a, root_b = root_b, root_a
        self._parent[root_b] = root_a
        self._size[root_a] += self._size[root_b]
        if self._rank[root_a] == self._rank[root_b]:
            self._rank[root_a] += 1
        self._components -= 1
        return True

    def connected(self, a: Hashable, b: Hashable) -> bool:
        """Return ``True`` if ``a`` and ``b`` are in the same component."""
        return self.find(a) == self.find(b)

    def size(self, item: Hashable) -> int:
        """Return the size of ``item``'s component."""
        return self._size[self.find(item)]

    @property
    def components(self) -> int:
        """Number of distinct components."""
        return self._components

    def __len__(self) -> int:
        return len(self._parent)

    def __contains__(self, item: Hashable) -> bool:
        return item in self._parent

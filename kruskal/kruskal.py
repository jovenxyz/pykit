"""Kruskal's algorithm for minimum spanning tree (or forest)."""
from __future__ import annotations

from typing import Dict, Hashable, List, Sequence, Tuple

Edge = Tuple[Hashable, Hashable, float]


def minimum_spanning_tree(
    nodes: Sequence[Hashable],
    edges: Sequence[Edge],
) -> List[Edge]:
    """Return a list of edges forming a minimum spanning tree.

    The graph is treated as undirected. If the graph is disconnected the
    result is the union of MSTs of each component (a minimum spanning
    forest).
    """
    parent: Dict[Hashable, Hashable] = {n: n for n in nodes}
    rank: Dict[Hashable, int] = {n: 0 for n in nodes}

    def find(x: Hashable) -> Hashable:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a: Hashable, b: Hashable) -> bool:
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        if rank[ra] < rank[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        if rank[ra] == rank[rb]:
            rank[ra] += 1
        return True

    tree: List[Edge] = []
    for source, target, weight in sorted(edges, key=lambda e: e[2]):
        if source not in parent or target not in parent:
            raise ValueError(f"edge references unknown node: ({source}, {target})")
        if union(source, target):
            tree.append((source, target, weight))
    return tree


def total_weight(tree: Sequence[Edge]) -> float:
    """Return the sum of edge weights in ``tree``."""
    return sum(weight for _, _, weight in tree)

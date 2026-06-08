"""Topological ordering of a directed acyclic graph (Kahn's algorithm)."""
from __future__ import annotations

from collections import defaultdict, deque
from typing import Dict, Hashable, Iterable, List, Tuple

Edge = Tuple[Hashable, Hashable]


class CycleError(ValueError):
    """Raised when the input graph contains a cycle."""


def topological_sort(
    edges: Iterable[Edge],
    nodes: Iterable[Hashable] = (),
) -> List[Hashable]:
    """Return a topological ordering of nodes using Kahn's algorithm.

    ``edges`` is an iterable of ``(source, target)`` pairs. ``nodes`` lets
    you include isolated vertices that don't appear in any edge.
    """
    indegree: Dict[Hashable, int] = {}
    out_edges: Dict[Hashable, List[Hashable]] = defaultdict(list)
    insertion_order: List[Hashable] = []

    def register(node: Hashable) -> None:
        if node not in indegree:
            indegree[node] = 0
            insertion_order.append(node)

    for node in nodes:
        register(node)
    for source, target in edges:
        register(source)
        register(target)
        out_edges[source].append(target)
        indegree[target] += 1

    queue: deque = deque(n for n in insertion_order if indegree[n] == 0)
    ordering: List[Hashable] = []
    while queue:
        node = queue.popleft()
        ordering.append(node)
        for neighbour in out_edges[node]:
            indegree[neighbour] -= 1
            if indegree[neighbour] == 0:
                queue.append(neighbour)

    if len(ordering) != len(indegree):
        placed = set(ordering)
        remaining = [n for n in indegree if n not in placed]
        raise CycleError(f"graph contains a cycle involving {remaining!r}")
    return ordering

"""Breadth-first and depth-first traversals over an adjacency map."""
from __future__ import annotations

from collections import deque
from typing import Dict, List, Set

Graph = Dict[int, List[int]]


def bfs(graph: Graph, start: int) -> List[int]:
    visited: Set[int] = {start}
    order: List[int] = []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    return order


def dfs(graph: Graph, start: int) -> List[int]:
    visited: Set[int] = set()
    order: List[int] = []

    def _visit(node: int) -> None:
        visited.add(node)
        order.append(node)
        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                _visit(neighbour)

    _visit(start)
    return order

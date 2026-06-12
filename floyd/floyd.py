"""Floyd-Warshall all-pairs shortest paths."""
from __future__ import annotations

import math
from typing import Dict, Hashable, Sequence, Tuple

Edge = Tuple[Hashable, Hashable, float]


def shortest_paths(
    nodes: Sequence[Hashable],
    edges: Sequence[Edge],
) -> Dict[Hashable, Dict[Hashable, float]]:
    """Return the matrix of shortest distances between every pair of nodes.

    Edges may have negative weights. Raises ``ValueError`` when a
    negative-weight cycle is detected.
    """
    node_list = list(nodes)
    index = {n: i for i, n in enumerate(node_list)}
    if len(index) != len(node_list):
        raise ValueError("duplicate node labels")
    n = len(node_list)
    dist = [[math.inf] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for source, target, weight in edges:
        i, j = index[source], index[target]
        if weight < dist[i][j]:
            dist[i][j] = weight
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    for i in range(n):
        if dist[i][i] < 0:
            raise ValueError("graph contains a negative-weight cycle")
    return {
        node_list[i]: {node_list[j]: dist[i][j] for j in range(n)}
        for i in range(n)
    }

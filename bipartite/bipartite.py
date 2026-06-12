"""Bipartite graph check and 2-colouring."""
from __future__ import annotations

from collections import deque
from typing import Dict, Hashable, Iterable, Optional, Sequence, Tuple


def two_colour(
    nodes: Sequence[Hashable],
    edges: Iterable[Tuple[Hashable, Hashable]],
) -> Optional[Dict[Hashable, int]]:
    """Return a 2-colouring of the undirected graph or ``None`` if not bipartite.

    Colours are ``0`` and ``1``; adjacent nodes always differ.
    """
    adjacency: Dict[Hashable, list] = {n: [] for n in nodes}
    for source, target in edges:
        if source not in adjacency or target not in adjacency:
            raise ValueError(f"edge references unknown node: ({source}, {target})")
        adjacency[source].append(target)
        adjacency[target].append(source)

    colour: Dict[Hashable, int] = {}
    for start in nodes:
        if start in colour:
            continue
        colour[start] = 0
        queue = deque([start])
        while queue:
            node = queue.popleft()
            for neighbour in adjacency[node]:
                if neighbour not in colour:
                    colour[neighbour] = 1 - colour[node]
                    queue.append(neighbour)
                elif colour[neighbour] == colour[node]:
                    return None
    return colour


def is_bipartite(
    nodes: Sequence[Hashable],
    edges: Iterable[Tuple[Hashable, Hashable]],
) -> bool:
    """Return ``True`` if the graph admits a 2-colouring."""
    return two_colour(nodes, edges) is not None

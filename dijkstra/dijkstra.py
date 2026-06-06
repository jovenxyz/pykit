"""Dijkstra's shortest-path algorithm on a weighted graph."""
from __future__ import annotations

import heapq
import math
from typing import Dict, Hashable, List, Optional, Tuple

Graph = Dict[Hashable, Dict[Hashable, float]]


def shortest_distances(graph: Graph, source: Hashable) -> Dict[Hashable, float]:
    """Return the shortest distance from ``source`` to every reachable node."""
    distances: Dict[Hashable, float] = {source: 0.0}
    queue: List[Tuple[float, int, Hashable]] = [(0.0, 0, source)]
    counter = 1
    while queue:
        distance, _, node = heapq.heappop(queue)
        if distance > distances.get(node, math.inf):
            continue
        for neighbour, weight in graph.get(node, {}).items():
            if weight < 0:
                raise ValueError("Dijkstra requires non-negative edge weights")
            new_distance = distance + weight
            if new_distance < distances.get(neighbour, math.inf):
                distances[neighbour] = new_distance
                heapq.heappush(queue, (new_distance, counter, neighbour))
                counter += 1
    return distances


def shortest_path(
    graph: Graph,
    source: Hashable,
    target: Hashable,
) -> Optional[List[Hashable]]:
    """Return the shortest path from ``source`` to ``target`` as a node list.

    Returns ``None`` if no path exists.
    """
    distances: Dict[Hashable, float] = {source: 0.0}
    previous: Dict[Hashable, Hashable] = {}
    queue: List[Tuple[float, int, Hashable]] = [(0.0, 0, source)]
    counter = 1
    while queue:
        distance, _, node = heapq.heappop(queue)
        if node == target:
            break
        if distance > distances.get(node, math.inf):
            continue
        for neighbour, weight in graph.get(node, {}).items():
            if weight < 0:
                raise ValueError("Dijkstra requires non-negative edge weights")
            new_distance = distance + weight
            if new_distance < distances.get(neighbour, math.inf):
                distances[neighbour] = new_distance
                previous[neighbour] = node
                heapq.heappush(queue, (new_distance, counter, neighbour))
                counter += 1
    if target not in distances:
        return None
    path = [target]
    while path[-1] != source:
        if path[-1] not in previous:
            return None
        path.append(previous[path[-1]])
    path.reverse()
    return path

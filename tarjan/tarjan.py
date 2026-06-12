"""Tarjan's strongly-connected-components algorithm."""
from __future__ import annotations

from typing import Dict, Hashable, Iterable, List, Sequence, Tuple


def strongly_connected_components(
    nodes: Sequence[Hashable],
    edges: Iterable[Tuple[Hashable, Hashable]],
) -> List[List[Hashable]]:
    """Return the SCCs of a directed graph in reverse topological order.

    Components nearer the sinks of the condensation DAG come first.
    """
    graph: Dict[Hashable, List[Hashable]] = {n: [] for n in nodes}
    for source, target in edges:
        if source not in graph or target not in graph:
            raise ValueError(f"edge references unknown node: ({source}, {target})")
        graph[source].append(target)

    index_counter = [0]
    stack: List[Hashable] = []
    on_stack: Dict[Hashable, bool] = {}
    index: Dict[Hashable, int] = {}
    lowlink: Dict[Hashable, int] = {}
    components: List[List[Hashable]] = []

    def strong_connect(node: Hashable) -> None:
        index[node] = index_counter[0]
        lowlink[node] = index_counter[0]
        index_counter[0] += 1
        stack.append(node)
        on_stack[node] = True
        for neighbour in graph[node]:
            if neighbour not in index:
                strong_connect(neighbour)
                lowlink[node] = min(lowlink[node], lowlink[neighbour])
            elif on_stack.get(neighbour, False):
                lowlink[node] = min(lowlink[node], index[neighbour])
        if lowlink[node] == index[node]:
            component: List[Hashable] = []
            while True:
                top = stack.pop()
                on_stack[top] = False
                component.append(top)
                if top == node:
                    break
            components.append(component)

    for node in nodes:
        if node not in index:
            strong_connect(node)
    return components

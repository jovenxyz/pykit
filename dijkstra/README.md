# dijkstra

A tiny, dependency-free implementation of **Dijkstra's shortest-path
algorithm** on a weighted directed graph with non-negative edge weights.

## Usage

```python
from dijkstra import shortest_distances, shortest_path

graph = {
    "A": {"B": 1, "C": 4},
    "B": {"C": 2, "D": 5},
    "C": {"D": 1},
    "D": {},
}

assert shortest_distances(graph, "A") == {"A": 0, "B": 1, "C": 3, "D": 4}
assert shortest_path(graph, "A", "D") == ["A", "B", "C", "D"]
```

Nodes may be any hashable value. Edge weights must be non-negative -- a
``ValueError`` is raised otherwise. ``shortest_path`` returns ``None`` when
the target is unreachable.

## Tests

```bash
cd dijkstra
pytest
```

# kruskal

A tiny, dependency-free implementation of **Kruskal's algorithm** for the
minimum spanning tree of an undirected weighted graph. Disconnected
graphs return the minimum spanning forest.

## Usage

```python
from kruskal import minimum_spanning_tree, total_weight

nodes = ["A", "B", "C", "D", "E"]
edges = [
    ("A", "B", 1), ("A", "C", 7),
    ("B", "C", 5), ("B", "D", 4),
    ("C", "D", 6), ("C", "E", 3),
    ("D", "E", 2),
]

tree = minimum_spanning_tree(nodes, edges)
assert total_weight(tree) == 10        # 1 + 2 + 3 + 4
```

Uses a union-find with path compression and union-by-rank under the
hood, so the cost is dominated by the edge sort -- ``O(E log E)``.

## Tests

```bash
cd kruskal
pytest
```

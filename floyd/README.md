# floyd

A tiny, dependency-free implementation of the **Floyd-Warshall**
all-pairs shortest paths algorithm. Handles negative edge weights and
detects negative-weight cycles.

## Usage

```python
from floyd import shortest_paths

nodes = ["A", "B", "C"]
edges = [("A", "B", 1), ("B", "C", 2), ("A", "C", 10)]

dist = shortest_paths(nodes, edges)
assert dist["A"]["C"] == 3       # A -> B -> C is cheaper than A -> C
```

Unreachable pairs come back as ``math.inf``. A graph containing a
negative-weight cycle raises ``ValueError``.

## Tests

```bash
cd floyd
pytest
```

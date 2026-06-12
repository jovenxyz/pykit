# tarjan

A tiny, dependency-free implementation of **Tarjan's algorithm** for
strongly-connected components of a directed graph. Returns components in
reverse topological order (sinks first), which is convenient for
condensing the graph into a DAG.

## Usage

```python
from tarjan import strongly_connected_components

nodes = ["A", "B", "C", "D", "E"]
edges = [
    ("A", "B"), ("B", "C"), ("C", "A"),    # cycle
    ("C", "D"),
    ("D", "E"), ("E", "D"),                  # cycle
]

for component in strongly_connected_components(nodes, edges):
    print(sorted(component))
# ['D', 'E']
# ['A', 'B', 'C']
```

Each component is a list of nodes (internal order is not specified).
Single nodes without a self-loop form their own SCC.

## Tests

```bash
cd tarjan
pytest
```

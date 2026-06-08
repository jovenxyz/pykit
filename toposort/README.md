# toposort

A tiny, dependency-free **topological sort** for directed acyclic graphs,
implemented via Kahn's algorithm.

## Usage

```python
from toposort import topological_sort

edges = [("compile", "link"), ("test", "package"), ("link", "package")]
print(topological_sort(edges))
# e.g. ['compile', 'test', 'link', 'package']
```

Nodes may be any hashable value. ``CycleError`` is raised if the input
graph contains a cycle. Pass ``nodes=`` to include isolated vertices that
don't appear in any edge.

## Tests

```bash
cd toposort
pytest
```

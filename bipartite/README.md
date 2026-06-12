# bipartite

A tiny, dependency-free check for whether an undirected graph is
**bipartite** -- can the nodes be split into two groups so that every
edge crosses between them? Equivalent to a valid 2-colouring.

## Usage

```python
from bipartite import is_bipartite, two_colour

# Even cycle: bipartite.
assert is_bipartite([0, 1, 2, 3], [(0, 1), (1, 2), (2, 3), (3, 0)])

# Triangle: odd cycle, not bipartite.
assert not is_bipartite([0, 1, 2], [(0, 1), (1, 2), (2, 0)])

# Get the colouring itself:
colours = two_colour(["A", "B", "C"], [("A", "B"), ("B", "C")])
# {'A': 0, 'B': 1, 'C': 0}
```

Disconnected components are handled. Edges referencing unknown nodes
raise ``ValueError``.

## Tests

```bash
cd bipartite
pytest
```

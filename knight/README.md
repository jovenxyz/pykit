# knight

A tiny, dependency-free solver for the **Knight's tour** problem on an
``n``-by-``n`` chess board. Uses **Warnsdorff's rule** -- always step to
the square with the fewest onward moves -- which usually finds an open
tour without backtracking.

## Usage

```python
from knight import find_tour

tour = find_tour(8, start=(0, 0))
assert tour is not None
assert len(tour) == 64                # visits every square
assert tour[0] == (0, 0)
```

Returns ``None`` when no tour is found (e.g. for boards smaller than
5x5, which have no knight's tour at all).

## Tests

```bash
cd knight
pytest
```

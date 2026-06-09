# maze

A tiny, dependency-free **maze generator** that produces perfect mazes
(exactly one path between any two cells) via iterative randomised
depth-first search.

## Usage

```python
import random

from maze import generate, render

grid = generate(width=20, height=10, rng=random.Random(42))
print(render(grid))
```

The grid is returned as a list of rows of cell dictionaries, where each
cell has four wall keys ``"N"``, ``"E"``, ``"S"`` and ``"W"`` (``True`` =
wall intact). Pass ``rng=`` to make generation deterministic in tests.

## Tests

```bash
cd maze
pytest
```

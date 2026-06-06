# life

A tiny, dependency-free implementation of **Conway's Game of Life** on an
unbounded grid. The board is represented as a set of ``(x, y)`` live cells,
so the playing field is effectively infinite.

## Usage

```python
from life import run, step

blinker = {(0, 0), (1, 0), (2, 0)}
assert step(blinker) == {(1, -1), (1, 0), (1, 1)}

glider = {(1, 0), (2, 1), (0, 2), (1, 2), (2, 2)}
moved = run(glider, generations=4)
assert moved == {(x + 1, y + 1) for (x, y) in glider}
```

Standard Life rules: live cells survive with 2 or 3 live neighbours; empty
cells become alive with exactly 3 live neighbours.

## Tests

```bash
cd life
pytest
```

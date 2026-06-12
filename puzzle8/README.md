# puzzle8

A tiny, dependency-free **8-puzzle** solver. Uses A* with the
Manhattan-distance heuristic to find an optimal sequence of moves from
any start state to the goal.

## Usage

```python
from puzzle8 import GOAL, is_solvable, solve

start = (1, 2, 3,
         4, 5, 6,
         0, 7, 8)

assert is_solvable(start)
path = solve(start)
print(len(path) - 1, "moves")           # 2
assert path[-1] == GOAL
```

The board is a 9-tuple read row-major; ``0`` marks the blank tile.
Unsolvable boards (odd inversion parity) return ``None``.

## Tests

```bash
cd puzzle8
pytest
```

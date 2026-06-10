# astar

A tiny, dependency-free **A\* pathfinder** on a 2D grid. Returns the
shortest path from start to goal around obstacles.

## Usage

```python
from astar import euclidean, find_path

grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
]

path = find_path(grid, start=(0, 0), goal=(4, 4))
print(path)

# Allow diagonal moves and switch the heuristic:
diag = find_path(grid, (0, 0), (4, 4), heuristic=euclidean, diagonal=True)
```

Cells with truthy values are obstacles. Manhattan distance is the default
heuristic; pass ``heuristic=euclidean`` (or your own callable) to swap it.

## Tests

```bash
cd astar
pytest
```

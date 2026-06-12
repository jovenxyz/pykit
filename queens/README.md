# queens

A tiny, dependency-free **N-queens** solver. Count the number of distinct
ways to place ``n`` non-attacking queens on an ``n``-by-``n`` board, or
enumerate the placements themselves.

## Usage

```python
from queens import count_solutions, first_solution, solutions

assert count_solutions(8) == 92        # OEIS A000170

placement = first_solution(8)
print(placement)                       # e.g. [0, 4, 7, 5, 2, 6, 1, 3]

for sol in solutions(5):
    print(sol)
```

Each solution is a list of length ``n`` where ``placement[row]`` gives the
queen's column in that row. Implementation uses the standard column /
diagonal bitmask trick for fast pruning.

## Tests

```bash
cd queens
pytest
```

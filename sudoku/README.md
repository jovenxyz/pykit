# sudoku

A tiny, dependency-free helper that **validates Sudoku boards** -- both
partially filled puzzles and fully solved grids. Checks rows, columns and
the nine 3x3 boxes for duplicates.

## Usage

```python
from sudoku import is_complete, is_valid

board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    # ... 8 more rows of nine ints (0 = empty cell)
]

assert is_valid(board)        # no rule conflicts so far
assert not is_complete(board)
```

Empty cells are represented by ``0``; other values must be integers in
``1..9``. The board must be exactly 9 rows of 9 cells.

## Tests

```bash
cd sudoku
pytest
```

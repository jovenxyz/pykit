# intervals

A tiny, dependency-free helper for working with **closed integer intervals**:
merge overlapping or adjacent ranges, intersect a pair, and measure the
total covered length.

## Usage

```python
from intervals import intersect, length, merge

assert merge([(1, 3), (2, 5), (7, 9)]) == [(1, 5), (7, 9)]
assert merge([(1, 3), (4, 6)]) == [(1, 6)]          # adjacent coalesce
assert intersect((1, 5), (3, 7)) == (3, 5)
assert length([(1, 3), (5, 6)]) == 5
```

Intervals are treated as inclusive on both ends, so ``(1, 3)`` and ``(4, 6)``
are considered adjacent and merge into ``(1, 6)``.

## Tests

```bash
cd intervals
pytest
```

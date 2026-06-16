# fenwick

A tiny, dependency-free **Fenwick tree** (Binary Indexed Tree) for
prefix-sum queries and point updates. Smaller and simpler than a full
segment tree, with O(log n) update and query.

## Usage

```python
from fenwick import Fenwick

bit = Fenwick([1, 2, 3, 4, 5])
assert bit.prefix_sum(5) == 15        # sum of values in [0, 5)
assert bit.range_sum(1, 4) == 9       # 2 + 3 + 4

bit.add(2, 7)                          # values become [1, 2, 10, 4, 5]
assert bit.range_sum(0, 5) == 22
```

Construct an empty tree with ``Fenwick(size)`` or seed it from a
sequence -- the latter runs in O(n).

## Tests

```bash
cd fenwick
pytest
```

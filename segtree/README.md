# segtree

A tiny, dependency-free **segment tree** for prefix-sum-style range
queries with point updates. Any sub-range sum in O(log n); a single
element update in O(log n).

## Usage

```python
from segtree import SegmentTree

st = SegmentTree([1, 2, 3, 4, 5])
assert st.query(0, 5) == 15        # sum over [0, 5)
assert st.query(1, 4) == 9         # 2 + 3 + 4

st.update(2, 10)                    # values become [1, 2, 10, 4, 5]
assert st.query(0, 5) == 22
```

Ranges are half-open: ``query(lo, hi)`` includes ``lo`` and excludes
``hi``. Item access via ``st[i]`` and assignment ``st[i] = v`` are
supported.

## Tests

```bash
cd segtree
pytest
```

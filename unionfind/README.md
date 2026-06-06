# unionfind

A tiny, dependency-free **Union-Find** (Disjoint Set Union) data structure
with **path compression** and **union by rank**, giving near-constant
amortized cost per operation.

## Usage

```python
from unionfind import UnionFind

uf = UnionFind()
for edge in (("a", "b"), ("b", "c"), ("d", "e")):
    uf.union(*edge)

assert uf.connected("a", "c")
assert not uf.connected("a", "d")
assert uf.components == 2
assert uf.size("a") == 3
```

Items may be any hashable value. ``find`` / ``union`` implicitly add
unknown items, so you can build a graph incrementally without bookkeeping.

## Tests

```bash
cd unionfind
pytest
```

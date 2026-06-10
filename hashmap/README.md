# hashmap

A tiny, dependency-free **hash table** built with separate chaining and
dynamic resizing -- a from-scratch alternative to ``dict`` that exposes
its load factor and capacity.

## Usage

```python
from hashmap import HashMap

h = HashMap(initial_capacity=8, load_factor=0.75)
h["alpha"] = 1
h["beta"] = 2
assert h["alpha"] == 1
assert len(h) == 2

del h["beta"]
assert "beta" not in h
```

When inserts push the load factor above the threshold, the table doubles
its capacity and rehashes. Supports ``[]`` access, ``in``, ``len``,
``del``, ``get``, ``items`` and iteration over keys.

## Tests

```bash
cd hashmap
pytest
```

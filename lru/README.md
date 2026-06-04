# lru

A tiny, dependency-free **least-recently-used (LRU) cache** built on
``collections.OrderedDict``. Useful as a bounded map with eviction.

## Usage

```python
from lru import LRUCache

cache = LRUCache(capacity=2)
cache["a"] = 1
cache["b"] = 2
cache.get("a")        # marks "a" as most recent
cache["c"] = 3        # evicts "b"
assert "b" not in cache
assert cache.stats["size"] == 2
```

``stats`` returns the cumulative ``hits``, ``misses`` and current ``size``
for quick introspection.

## Tests

```bash
cd lru
pytest
```

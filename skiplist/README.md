# skiplist

A tiny, dependency-free **skip list** -- a probabilistic sorted set with
O(log n) expected insert, contains, and remove operations.

## Usage

```python
from skiplist import SkipList

sl = SkipList()
for v in (42, 7, 19, 3, 28):
    sl.insert(v)

assert 19 in sl
assert sl.remove(7) is True
print(list(sl))    # [3, 19, 28, 42] -- iteration yields sorted order
```

Pass ``rng=`` to make level assignment deterministic in tests. Tweak
``max_level`` and ``p`` to balance expected height against memory.

## Tests

```bash
cd skiplist
pytest
```

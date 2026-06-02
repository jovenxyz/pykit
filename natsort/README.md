# natsort

A tiny, dependency-free **natural-order sort key** so ``"file10"`` sorts after
``"file2"`` rather than before. Use it as the ``key=`` argument to
``sorted`` / ``list.sort``.

## Usage

```python
from natsort import natural_key

items = ["file10", "file2", "file1"]
assert sorted(items, key=natural_key) == ["file1", "file2", "file10"]
```

Comparison is case-insensitive: ``"File2"`` and ``"file2"`` produce the same
key.

## Tests

```bash
cd natsort
pytest
```

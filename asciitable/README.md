# asciitable

A tiny, dependency-free helper to render rows of data as a tidy **ASCII
table** with optional per-column alignment.

## Usage

```python
from asciitable import render

print(render(
    headers=["name", "age"],
    rows=[("alice", 30), ("bob", 25)],
))
# +-------+-----+
# | name  | age |
# +-------+-----+
# | alice | 30  |
# | bob   | 25  |
# +-------+-----+

# Right-align the numeric column:
print(render(
    headers=["item", "price"],
    rows=[("apple", 1.5), ("banana", 0.25)],
    align=["l", "r"],
))
```

Columns auto-size to the widest cell. ``align`` accepts ``"l"``, ``"r"``
or ``"c"`` per column. Cell values are coerced with ``str``.

## Tests

```bash
cd asciitable
pytest
```

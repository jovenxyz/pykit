# humanlist

A tiny, dependency-free helper to join a sequence of items into an
English-language list with an optional Oxford comma.

## Usage

```python
from humanlist import humanlist

assert humanlist(["a", "b", "c"]) == "a, b, and c"
assert humanlist(["a", "b", "c"], oxford=False) == "a, b and c"
assert humanlist(["red", "blue"], conjunction="or") == "red or blue"
assert humanlist([]) == ""
```

Items are coerced with ``str``, so any iterable of values works.

## Tests

```bash
cd humanlist
pytest
```

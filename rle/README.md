# rle

A tiny, dependency-free **run-length encoder** and decoder. Useful for
quick compression of strings with long runs of repeating characters.

## Usage

```python
from rle import encode, decode, encode_string, decode_string

# Pair form
assert encode("aaabbc") == [("a", 3), ("b", 2), ("c", 1)]
assert decode([("a", 3), ("b", 2), ("c", 1)]) == "aaabbc"

# Compact string form
assert encode_string("aaabbc") == "3a2b1c"
assert decode_string("3a2b1c") == "aaabbc"
```

The compact string form supports multi-digit counts: ``"12a"`` decodes to
12 ``a``s.

## Tests

```bash
cd rle
pytest
```

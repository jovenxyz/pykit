# base62

A tiny, dependency-free encoder/decoder for **base62** integers — compact
strings useful for short URLs and identifiers.

The alphabet is ``0-9A-Za-z`` (case-sensitive), giving 62 symbols.

## Usage

```python
from base62 import decode, encode

assert encode(62) == "10"
assert decode("zz") == 61 * 62 + 61
assert decode(encode(123456789)) == 123456789
```

## Tests

```bash
cd base62
pytest
```

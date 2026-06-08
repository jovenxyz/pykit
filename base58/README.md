# base58

A tiny, dependency-free **base58** encoder / decoder using the Bitcoin /
IPFS alphabet (no ``0``, ``O``, ``I``, or ``l`` so values are easy to read
aloud).

## Usage

```python
from base58 import decode, encode

assert encode(b"\xff") == "5Q"
assert decode("5Q") == b"\xff"
assert encode(b"\x00\x00\xff") == "115Q"   # leading zero bytes -> leading '1's
```

Leading zero bytes are preserved on round-trip (each leading zero byte
becomes a leading ``1`` character).

## Tests

```bash
cd base58
pytest
```

# bencode

A tiny, dependency-free implementation of **bencode** -- the simple
serialization format used by BitTorrent. Supports integers, byte strings,
lists, and string-keyed dictionaries.

## Usage

```python
from bencode import decode, encode

assert encode({"name": "alice", "items": [1, 2, 3]}) == (
    b"d5:itemsli1ei2ei3ee4:name5:alicee"
)
assert decode(b"i42e") == 42
assert decode(b"li1ei2ee") == [1, 2]
```

Encoded dict keys are sorted to produce canonical output (the BitTorrent
requirement). On decode, byte strings stay as ``bytes`` so binary payloads
survive a round-trip.

## Tests

```bash
cd bencode
pytest
```

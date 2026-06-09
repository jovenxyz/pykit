# crc

A tiny, dependency-free implementation of **CRC-32** (IEEE 802.3 / ZIP /
PNG polynomial) computed from first principles. The output matches
``zlib.crc32``.

## Usage

```python
from crc import crc32, crc32_hex

assert crc32(b"") == 0
assert crc32(b"123456789") == 0xCBF43926
assert crc32_hex(b"a") == "e8b7be43"
```

Pass ``initial=`` (a previous result) to extend a running checksum across
multiple chunks of data.

## Tests

```bash
cd crc
pytest
```

# bitstream

A tiny, dependency-free pair of **bit-level reader and writer** for
packing and unpacking sub-byte fields. Bits are processed MSB-first.

## Usage

```python
from bitstream import BitReader, BitWriter

w = BitWriter()
w.write_bits(0b1010, 4)
w.write_bits(0b1111, 4)
data = w.to_bytes()                # b"\\xaf"

r = BitReader(data)
assert r.read_bits(4) == 0b1010
assert r.read_bits(4) == 0b1111
```

The writer zero-pads the final byte. The reader raises ``EOFError`` once
the bit stream is exhausted.

## Tests

```bash
cd bitstream
pytest
```

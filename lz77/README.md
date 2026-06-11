# lz77

A tiny, dependency-free **LZ77** sliding-window compressor and
decompressor. Produces a stream of ``(offset, length, next_byte)`` tokens
suitable for further entropy coding.

## Usage

```python
from lz77 import compress, decompress

data = b"abracadabra" * 4
tokens = compress(data)
assert decompress(tokens) == data
```

Tune ``window_size`` (default 4096) and ``lookahead`` (default 18) to
trade compression ratio against encoder speed.

## Tests

```bash
cd lz77
pytest
```

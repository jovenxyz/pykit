# bytesize

A tiny, dependency-free helper for human-readable byte sizes.

## Usage

```python
from bytesize import format_bytes, parse_size

assert format_bytes(1536) == "1.5 KB"
assert parse_size("1.5 MB") == int(1.5 * 1024 ** 2)
```

Units are powers of 1024 (B, KB, MB, GB, TB, PB) and parsing is
case-insensitive.

## Tests

```bash
cd bytesize
pytest
```

# fnv

A tiny, dependency-free implementation of the **FNV-1a** non-cryptographic
hash in 32-bit, 64-bit and 128-bit variants. FNV is small, fast, and well
suited to hashing keys for in-memory tables.

## Usage

```python
from fnv import fnv1a_32, fnv1a_64

assert fnv1a_32(b"") == 0x811C9DC5            # offset basis
assert fnv1a_32(b"foobar") == 0xBF9CF968
assert fnv1a_64(b"foobar") == 0x85944171F73967E8
```

Constants and test vectors come from the [FNV reference][ref] by Glenn
Fowler, Landon Curt Noll and Phong Vo.

[ref]: http://www.isthe.com/chongo/tech/comp/fnv/

## Tests

```bash
cd fnv
pytest
```

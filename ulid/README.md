# ulid

A tiny, dependency-free **ULID** generator: 26-character, lexicographically
sortable identifiers combining a millisecond timestamp with cryptographic
randomness. Uses [Crockford's Base32][crockford] alphabet (no I, L, O, U).

[crockford]: https://www.crockford.com/base32.html

## Usage

```python
from ulid import new, timestamp_ms_of

uid = new()
assert len(uid) == 26

# The embedded timestamp is recoverable:
ts = timestamp_ms_of(uid)
```

ULIDs generated within the same millisecond sort by their random tail, and
across milliseconds they sort by time -- handy for use as primary keys.
Inject ``time_func`` / ``random_func`` to make generation deterministic in
tests.

## Tests

```bash
cd ulid
pytest
```

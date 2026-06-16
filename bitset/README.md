# bitset

A tiny, dependency-free **bit set** -- a fixed-size mutable set of
integer indices packed into bytes for compact storage. Supports union,
intersection, difference and the usual ``[]`` / ``in`` / ``len``
mappings.

## Usage

```python
from bitset import BitSet

primes = BitSet(20)
for p in (2, 3, 5, 7, 11, 13, 17, 19):
    primes[p] = True

assert primes[7] and not primes[8]
assert list(primes) == [2, 3, 5, 7, 11, 13, 17, 19]

odds = BitSet(20)
for i in range(1, 20, 2):
    odds[i] = True

odd_primes = primes.intersect(odds)
assert 2 not in odd_primes
```

Union, intersection and difference produce a new ``BitSet`` of the same
size. Bitsets of differing sizes can't be combined.

## Tests

```bash
cd bitset
pytest
```

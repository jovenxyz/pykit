# totient

A tiny, dependency-free implementation of **Euler's totient function**
``phi(n)`` -- the count of integers in ``[1, n]`` coprime to ``n`` --
plus a linear-time sieve and helpers for ``gcd`` / coprimality.

## Usage

```python
from totient import coprimes_up_to, gcd, totient, totient_sieve

assert totient(10) == 4                # 1, 3, 7, 9 are coprime to 10
assert totient(101) == 100             # phi(p) = p - 1 for prime p

# Bulk computation:
assert totient_sieve(20) == [
    0, 1, 1, 2, 2, 4, 2, 6, 4, 6, 4,
    10, 4, 12, 6, 8, 8, 16, 6, 18, 8,
]

assert list(coprimes_up_to(10)) == [1, 3, 7, 9]
```

``totient(n)`` uses trial division (good up to roughly ``10**12``);
``totient_sieve(limit)`` precomputes every value at once.

## Tests

```bash
cd totient
pytest
```

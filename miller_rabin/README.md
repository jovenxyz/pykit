# miller_rabin

A tiny, dependency-free **Miller-Rabin primality test**. Deterministic
for any number below ``3.317 * 10**24`` (a well-known sufficient witness
set covers that range) and probabilistic above that, with a
false-positive rate below ``4 ** -rounds``.

## Usage

```python
from miller_rabin import is_prime, next_prime

assert is_prime(982451653)               # 50 millionth prime
assert not is_prime(561)                 # smallest Carmichael number
assert next_prime(100) == 101
```

The test is fast even on huge inputs -- modular exponentiation runs in
``O(log n)`` arithmetic operations on arbitrary-precision integers.

## Tests

```bash
cd miller_rabin
pytest
```

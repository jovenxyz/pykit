# modular

A tiny, dependency-free pack of **modular arithmetic** helpers:
extended Euclidean algorithm, modular multiplicative inverse, fast
modular exponentiation, and the Chinese Remainder Theorem.

## Usage

```python
from modular import crt, extended_gcd, mod_inverse, mod_pow

g, x, y = extended_gcd(30, 12)
assert 30 * x + 12 * y == g

assert mod_inverse(3, 11) == 4
assert mod_pow(2, 100, 1009) == pow(2, 100, 1009)

# Classic CRT example:
assert crt([2, 3, 2], [3, 5, 7]) == 23
```

``mod_pow`` accepts negative exponents (using the inverse). ``crt``
requires pairwise-coprime moduli and raises ``ValueError`` otherwise.

## Tests

```bash
cd modular
pytest
```

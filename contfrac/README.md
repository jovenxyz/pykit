# contfrac

A tiny, dependency-free helper for **continued fractions**: expand
rationals and floats into their continued-fraction coefficients, and
reconstruct the original value (or any partial convergent) from those
coefficients.

## Usage

```python
import math

from contfrac import convergent, convergents, expand_rational, expand_real

assert expand_rational(415, 93) == [4, 2, 6, 7]
assert convergent([4, 2, 6, 7]).numerator == 415

# Best rational approximations of pi:
print(convergents(expand_real(math.pi, terms=4)))
# [Fraction(3, 1), Fraction(22, 7), Fraction(333, 106), Fraction(355, 113)]
```

The reconstructed convergent is exact for rationals; for floats it
approximates the target up to ``terms`` coefficients.

## Tests

```bash
cd contfrac
pytest
```

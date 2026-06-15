# quad

A tiny, dependency-free implementation of **numerical quadrature** -- the
composite trapezoidal rule and composite Simpson's rule for definite
integrals.

## Usage

```python
import math

from quad import simpson, trapezoidal

# integral of sin from 0 to pi = 2
assert round(trapezoidal(math.sin, 0, math.pi, n=1000), 4) == 2.0
assert round(simpson(math.sin, 0, math.pi, n=100), 8) == 2.0
```

Trapezoidal is exact for linear functions; Simpson's rule is exact for
polynomials up to degree 3 and converges much faster for smooth
integrands. Simpson requires an even number of intervals.

## Tests

```bash
cd quad
pytest
```

# polynomial

A tiny, dependency-free helper for **polynomial** evaluation,
differentiation, and root-finding via Horner's method and Newton's method.

Polynomials are represented as coefficient lists in **ascending** order:
``[a0, a1, a2, ...]`` stands for ``a0 + a1*x + a2*x^2 + ...``.

## Usage

```python
from polynomial import derivative, evaluate, newton_root

# 1 + 2x + 3x^2 evaluated at x = 2:
assert evaluate([1, 2, 3], 2) == 17

# Derivative of the same polynomial:
assert derivative([1, 2, 3]) == [2, 6]

# Find a root of x^2 - 4 near x = 1.5:
root = newton_root([-4, 0, 1], initial=1.5)
assert round(root, 9) == 2
```

Horner's method evaluates an n-th degree polynomial in O(n) multiplications
without ``pow``. Newton's method converges fast when started near a root --
``ValueError`` is raised if it does not converge within ``max_iterations``.

## Tests

```bash
cd polynomial
pytest
```

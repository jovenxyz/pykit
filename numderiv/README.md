# numderiv

Numerical differentiation via finite differences — pure Python, no NumPy.

## API

- `forward(f, x, h=1e-5)` — forward difference, O(h) error
- `backward(f, x, h=1e-5)` — backward difference, O(h) error
- `central(f, x, h=1e-5)` — central difference, O(h²) error (good default)
- `five_point(f, x, h=1e-4)` — five-point stencil, O(h⁴) error
- `second(f, x, h=1e-4)` — second derivative, O(h²) error
- `partial(f, point, index, h=1e-5)` — partial derivative of a multivariate `f`
- `gradient(f, point, h=1e-5)` — gradient vector

## Example

```python
import math
from numderiv import central, gradient

central(math.sin, 0.0)                  # ≈ 1.0   (= cos 0)
gradient(lambda x, y: x*x + 2*y, (3, 4))  # ≈ (6.0, 2.0)
```

## Test

```bash
python -m pytest
```

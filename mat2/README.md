# mat2

2×2 matrix algebra — addition, multiplication, determinant, inverse,
transpose, eigenvalues, plus rotation and scale constructors.

## API

- `Mat2(a, b, c, d)` — frozen dataclass `[[a, b], [c, d]]`
- Arithmetic: `+`, `-`, scalar `*`, matrix `*`
- `apply(v)` — transform a 2D vector
- `transpose()`, `det()`, `trace()`, `inverse()`
- `eigenvalues()` — real or complex pair via the characteristic polynomial
- `identity()`, `rotation(angle)`, `scale(sx, sy=None)`

## Example

```python
from mat2 import Mat2, rotation
import math

r = rotation(math.pi / 2)
r.apply((1, 0))            # ≈ (0, 1)
Mat2(4, 7, 2, 6).inverse() # solve a 2×2 system
```

## Test

```bash
python -m pytest
```

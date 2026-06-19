# quaternion

Quaternion arithmetic for 3D rotations.

## Features

- `Quaternion(w, x, y, z)` — frozen dataclass
- Arithmetic: `+`, `-`, scalar `*`, Hamilton product `q1 * q2`
- `conjugate()`, `norm()`, `norm_squared()`, `normalize()`, `inverse()`
- `from_axis_angle(axis, angle)` — build a unit rotation quaternion
- `rotate_vector(q, v)` — apply rotation to a 3D vector

## Example

```python
import math
from quaternion import from_axis_angle, rotate_vector

q = from_axis_angle((0, 0, 1), math.pi / 2)
rotate_vector(q, (1, 0, 0))  # ≈ (0, 1, 0)
```

## Test

```bash
python -m pytest
```

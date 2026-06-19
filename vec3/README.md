# vec3

A tiny, dependency-free **3D vector** with the usual operators and the
helpers you usually want next: dot, cross, length, normalize, distance,
lerp, and the angle between two vectors.

## Usage

```python
import math

from vec3 import Vec3, angle_between, lerp

i = Vec3(1, 0, 0)
j = Vec3(0, 1, 0)

assert i.cross(j) == Vec3(0, 0, 1)               # i x j = k
assert angle_between(i, j) == math.pi / 2
assert Vec3(2, 3, 6).length() == 7
assert lerp(Vec3(0, 0, 0), Vec3(10, 20, 30), 0.5) == Vec3(5, 10, 15)
```

``Vec3`` is a frozen dataclass, so equality and hashing work out of the
box. Operators ``+ - *`` and unary ``-`` are supported; scalar
multiplication works on either side.

## Tests

```bash
cd vec3
pytest
```

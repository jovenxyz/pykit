# vec2

A tiny, dependency-free **2D vector** with the usual operators and a
handful of geometry helpers (length, normalize, dot, cross, rotate,
angle, distance, lerp).

## Usage

```python
import math

from vec2 import Vec2, distance, lerp

a = Vec2(1, 2)
b = Vec2(3, 4)

assert (a + b) == Vec2(4, 6)
assert (b - a).length() == math.sqrt(8)
assert Vec2(3, 4).normalize().length() == 1.0
assert Vec2(1, 0).rotate(math.pi / 2).y == 1.0
assert lerp(Vec2(0, 0), Vec2(10, 20), 0.5) == Vec2(5, 10)
```

``Vec2`` is a frozen dataclass, so equality and hashing work out of the
box. Operators ``+ - *`` and unary ``-`` are supported; scalar
multiplication works on either side.

## Tests

```bash
cd vec2
pytest
```

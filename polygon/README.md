# polygon

A tiny, dependency-free helper for **simple 2-D polygons**:
point-in-polygon (ray casting), axis-aligned bounding box, and the
signed shoelace area.

## Usage

```python
from polygon import bounding_box, point_in_polygon, signed_area

square = [(0, 0), (4, 0), (4, 4), (0, 4)]

assert point_in_polygon((2, 2), square)
assert not point_in_polygon((5, 5), square)
assert bounding_box(square) == ((0, 0), (4, 4))
assert signed_area(square) == 16.0
```

The signed area is positive for counter-clockwise polygons and negative
for clockwise ones -- convenient for orientation tests.

## Tests

```bash
cd polygon
pytest
```

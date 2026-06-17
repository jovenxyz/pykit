# convex_hull

A tiny, dependency-free **2D convex hull** via Andrew's monotone chain
algorithm, plus a shoelace polygon-area helper.

## Usage

```python
from convex_hull import convex_hull, polygon_area

points = [(0, 0), (4, 0), (4, 4), (0, 4), (2, 2)]
hull = convex_hull(points)
assert hull == [(0, 0), (4, 0), (4, 4), (0, 4)]    # CCW; (2, 2) dropped

assert polygon_area(hull) == 16.0
```

The hull is returned counter-clockwise starting from the
lexicographically smallest point. Collinear and duplicate points on the
hull edges are excluded.

## Tests

```bash
cd convex_hull
pytest
```

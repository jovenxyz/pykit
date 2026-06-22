# triangle

Triangle geometry: validation, Heron's-formula area, classification, angles, centroid.

## API

- `is_triangle(a, b, c)` — triangle-inequality check
- `perimeter(a, b, c)`
- `area(a, b, c)` — Heron's formula
- `classify_by_sides(a, b, c)` → `"equilateral" | "isosceles" | "scalene"`
- `classify_by_angles(a, b, c)` → `"right" | "acute" | "obtuse"`
- `angles(a, b, c)` — interior angles (radians) via law of cosines
- `Point(x, y)`, `centroid(p1, p2, p3)`, `area_from_points(p1, p2, p3)` (shoelace)

## Example

```python
from triangle import area, classify_by_angles

area(3, 4, 5)               # 6.0
classify_by_angles(3, 4, 5) # "right"
```

## Test

```bash
python -m pytest
```

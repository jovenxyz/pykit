# bresenham

A tiny, dependency-free implementation of **Bresenham's line and
circle** rasterization algorithms. Returns every integer pixel on a
line segment or a discrete circle.

## Usage

```python
from bresenham import circle, line

assert line(0, 0, 4, 0) == [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]
assert line(0, 0, 3, 3) == [(0, 0), (1, 1), (2, 2), (3, 3)]

# Pixels on a radius-3 circle centred at the origin:
print(sorted(circle(0, 0, 3)))
```

Both routines work in either direction and produce 8-connected pixel
sets -- handy for ASCII art, tile-grid pathing, and low-level graphics.

## Tests

```bash
cd bresenham
pytest
```

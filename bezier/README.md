# bezier

A tiny, dependency-free **Bezier curve** evaluator: quadratic and cubic
shortcuts, a uniform sampler, and the general De Casteljau algorithm
that works for any degree.

## Usage

```python
from bezier import cubic, de_casteljau, quadratic, sample

# Quadratic curve at the midpoint.
assert quadratic((0, 0), (10, 10), (20, 0), 0.5) == (10, 5)

# Sample a cubic for plotting.
points = sample([(0, 0), (0, 10), (10, 10), (10, 0)], steps=32)
assert points[0] == (0, 0)
assert points[-1] == (10, 0)

# De Casteljau works for arbitrary control-point counts.
assert de_casteljau([(0, 0), (5, 5), (10, 0)], 0.5) == (5.0, 2.5)
```

All evaluation points use ``t`` in ``[0, 1]``; values outside that
range raise ``ValueError``.

## Tests

```bash
cd bezier
pytest
```

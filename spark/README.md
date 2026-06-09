# spark

A tiny, dependency-free **sparkline** renderer -- turn a sequence of
numbers into a one-line Unicode bar chart using the eight block-fill
glyphs ``▁▂▃▄▅▆▇█``.

## Usage

```python
from spark import sparkline

print(sparkline([1, 5, 22, 13, 53, 28, 28, 44, 75]))
# A short bar chart string, one glyph per value.

# Pin the scale to a known range:
print(sparkline([0, 25, 50, 75, 100], minimum=0, maximum=100))
```

Without ``minimum`` / ``maximum`` the range is taken from the values
themselves. Values outside the explicit range are clamped to the endpoint
glyphs.

## Tests

```bash
cd spark
pytest
```

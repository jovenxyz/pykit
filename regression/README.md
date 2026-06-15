# regression

A tiny, dependency-free **least-squares linear regression** with
``slope``, ``intercept``, ``r_squared`` and a ``predict`` method, plus
the Pearson correlation coefficient.

## Usage

```python
from regression import correlation, fit

line = fit([1, 2, 3, 4], [3, 5, 7, 9])   # y = 2x + 1
assert line.slope == 2 and line.intercept == 1
assert line.r_squared == 1.0
assert line.predict(10) == 21

assert correlation([1, 2, 3], [2, 4, 6]) == 1.0
```

Raises ``ValueError`` on length mismatches, fewer than two points, or
zero-variance series.

## Tests

```bash
cd regression
pytest
```

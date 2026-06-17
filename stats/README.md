# stats

A tiny, dependency-free pack of **descriptive statistics**: mean,
median, variance, standard deviation, percentile (with linear
interpolation), and the three quartiles.

## Usage

```python
from stats import mean, median, percentile, quartiles, stdev, variance

data = [2, 4, 4, 4, 5, 5, 7, 9]

assert mean(data) == 5
assert median(data) == 4.5
assert round(stdev(data), 4) == 2.1381

assert percentile([1, 2, 3, 4, 5], 25) == 2
assert quartiles([1, 2, 3, 4, 5]) == (2, 3, 4)
```

``variance`` and ``stdev`` default to the **sample** estimator (divide
by ``n - 1``); pass ``sample=False`` for the population variant.

## Tests

```bash
cd stats
pytest
```

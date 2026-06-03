# dice

A tiny, dependency-free parser and evaluator for tabletop **dice notation**
like ``"2d6+3"``.

## Usage

```python
from dice import parse, minimum, maximum, average, roll

d = parse("2d6+3")
assert (d.count, d.sides, d.modifier) == (2, 6, 3)
assert minimum(d) == 5
assert maximum(d) == 15
assert average(d) == 10.0

total, rolls = roll(d)
```

Only the common ``NdS±M`` form (a single dice term plus an optional flat
modifier) is supported; case and whitespace are tolerated.

## Tests

```bash
cd dice
pytest
```

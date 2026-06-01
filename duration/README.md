# duration

A tiny, dependency-free helper for human-readable durations.

## Usage

```python
from duration import format_duration, parse_duration

assert format_duration(3661) == "1h 1m 1s"
assert parse_duration("1h 30m") == 5400
```

Units: ``w`` (weeks), ``d`` (days), ``h`` (hours), ``m`` (minutes), ``s``
(seconds). Parsing is case-insensitive.

## Tests

```bash
cd duration
pytest
```

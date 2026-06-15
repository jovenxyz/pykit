# caldate

A tiny, dependency-free helper for **Gregorian calendar** maths:
leap-year detection, days-in-month, weekday-of-date (via Zeller's
congruence) and the signed number of days between two dates.

## Usage

```python
from caldate import days_between, is_leap, weekday

assert is_leap(2024)
assert not is_leap(1900)

assert weekday(2026, 6, 15) == "Monday"
assert days_between((2023, 6, 1), (2024, 6, 1)) == 366    # leap year inside
```

Dates are validated against the calendar -- ``29 February`` is rejected
in non-leap years.

## Tests

```bash
cd caldate
pytest
```

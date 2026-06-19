# money

A tiny, dependency-free helper for **money formatting and parsing**:
render a number with a currency symbol and thousands grouping in either
the English or European convention, parse formatted strings back into
floats, and round amounts using the "half away from zero" rule.

## Usage

```python
from money import format_amount, parse_amount, round_half_up

assert format_amount(1234.5) == "$1,234.50"
assert format_amount(
    1234.5,
    symbol="€",
    thousands=".",
    decimal_point=",",
    symbol_after=True,
) == "1.234,50 €"

assert parse_amount("$1,234.50") == 1234.5
assert parse_amount("1.234,50 €", thousands=".", decimal_point=",") == 1234.5

assert round_half_up(2.5, 0) == 3
```

``round_half_up`` rounds ``.5`` away from zero (the accounting
convention), unlike Python's built-in banker's rounding.

## Tests

```bash
cd money
pytest
```

# finance

A tiny, dependency-free pack of **financial math helpers**: compound
interest, present and future values of cash flows, level annuity
payments, and the effective annual rate.

## Usage

```python
from finance import (
    annuity_payment,
    compound,
    effective_annual_rate,
    future_value,
    present_value,
)

# Future value of $1,000 at 5% for 10 years.
assert round(compound(1000, 0.05, 10), 2) == 1628.89

# Mortgage payment: $100,000 at 5% over 30 years (annual payments).
assert round(annuity_payment(100_000, 0.05, 30), 2) == 6505.14

# 12% nominal monthly -> 12.683% effective.
assert round(effective_annual_rate(0.12, 12), 5) == 0.12683
```

Rates are quoted per period (matched to ``periods`` or the supplied
nominal frequency). Negative principal / years raises ``ValueError``.

## Tests

```bash
cd finance
pytest
```

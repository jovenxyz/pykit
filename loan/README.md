# loan

A tiny, dependency-free helper for **loan amortization**: compute the fixed
monthly payment, the full per-period schedule, and the total interest paid
over the life of a loan.

## Usage

```python
from loan import amortization_schedule, monthly_payment, total_interest

# $100,000 at 5% APR over 30 years
assert round(monthly_payment(100_000, 0.05, 30), 2) == 536.82

schedule = amortization_schedule(100_000, 0.05, 30)
assert len(schedule) == 360
assert schedule[-1].balance == 0.0

print(f"total interest: ${total_interest(100_000, 0.05, 30):.2f}")
```

Each row of the schedule is a frozen ``Payment`` with ``period``,
``payment``, ``principal``, ``interest`` and ``balance``. The final period
absorbs floating-point drift so the loan always finishes at zero.

## Tests

```bash
cd loan
pytest
```

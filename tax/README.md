# tax

A tiny, dependency-free helper for **sales-tax / VAT** calculations:
add or strip tax from an amount, isolate the tax component, and break
down a bill into net, tax and tip.

## Usage

```python
from tax import add_tax, remove_tax, split_total, tax_amount

assert add_tax(100, 0.2) == 120                       # net -> gross
assert remove_tax(120, 0.2) == 100                    # gross -> net
assert tax_amount(120, 0.2, inclusive=True) == 20     # tax inside 120
assert split_total(100, tax_rate=0.1, tip_rate=0.2) == {
    "net": 100, "tax": 10.0, "tip": 22.0, "total": 132.0,
}
```

Tip is calculated on the post-tax subtotal, matching standard practice
in many restaurants.

## Tests

```bash
cd tax
pytest
```

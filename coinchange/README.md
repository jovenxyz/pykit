# coinchange

A tiny, dependency-free **coin-change** solver: find the minimum number
of coins needed to make a target amount, the number of distinct
combinations that work, and one concrete breakdown.

## Usage

```python
from coinchange import coin_breakdown, min_coins, ways

assert min_coins(11, [1, 2, 5]) == 3
assert ways(5, [1, 2, 5]) == 4
assert sum(coin_breakdown(11, [1, 2, 5])) == 11
```

Denominations must be positive. ``min_coins`` and ``coin_breakdown``
return ``None`` when the amount cannot be made exactly.

## Tests

```bash
cd coinchange
pytest
```

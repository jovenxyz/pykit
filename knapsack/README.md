# knapsack

A tiny, dependency-free solver for the **0/1 knapsack problem** -- given
items with weights and values, pick the subset with the maximum total
value that fits inside a weight capacity.

## Usage

```python
from knapsack import chosen_items, max_value

weights = [2, 3, 4, 5]
values  = [3, 4, 5, 6]

assert max_value(weights, values, 5) == 7

value, picked = chosen_items(weights, values, 5)
assert value == 7
assert picked == [0, 1]      # indices into the original lists
```

The classic dynamic-programming formulation. ``max_value`` runs in
O(n * capacity); ``chosen_items`` also takes O(n * capacity) memory to
reconstruct one optimal subset.

## Tests

```bash
cd knapsack
pytest
```

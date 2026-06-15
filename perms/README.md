# perms

A tiny, dependency-free generator for **permutations**, **combinations**
and the **power set** of a sequence, all in lexicographic order.

## Usage

```python
from perms import combinations, permutations, power_set

list(permutations([1, 2, 3]))
# [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

list(combinations([1, 2, 3, 4], 2))
# [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]

list(power_set([1, 2, 3]))
# [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
```

All three generators yield fresh lists in lexicographic order.
``power_set`` emits subsets ordered first by size, then lexicographically
within size.

## Tests

```bash
cd perms
pytest
```

# radix

A tiny, dependency-free pair of **non-comparison sorts**: least-
significant-digit radix sort (with any base) and counting sort.

## Usage

```python
from radix import counting_sort, radix_sort

assert radix_sort([170, 45, 75, 90, 802, 24, 2, 66]) == [
    2, 24, 45, 66, 75, 90, 170, 802,
]

# Negatives are handled by sorting magnitudes then flipping:
assert radix_sort([3, -1, 4, -1, 5, -9, 2, 6]) == [-9, -1, -1, 2, 3, 4, 5, 6]

# Counting sort is fastest for small non-negative ranges:
assert counting_sort([4, 2, 2, 8, 3, 3, 1]) == [1, 2, 2, 3, 3, 4, 8]
```

Radix sort runs in O(d * (n + base)) for ``d`` digits. Counting sort
runs in O(n + max(values)) and requires non-negative integers.

## Tests

```bash
cd radix
pytest
```

# karatsuba

A tiny, dependency-free implementation of **Karatsuba's divide-and-
conquer multiplication** algorithm for integers of arbitrary size.

## Usage

```python
from karatsuba import karatsuba

assert karatsuba(1234, 5678) == 1234 * 5678

# Works on arbitrarily large numbers (Python ints are unbounded):
a = (1 << 1024) + 1
b = (1 << 1024) - 1
assert karatsuba(a, b) == a * b
```

Karatsuba runs in roughly ``O(n ** 1.585)`` compared to the schoolbook
``O(n ** 2)``. The implementation falls back to ordinary multiplication
once a factor fits in ``cutoff`` bits (default 64); below that the
recursion overhead dominates.

## Tests

```bash
cd karatsuba
pytest
```

# pascal

A tiny, dependency-free helper for **Pascal's triangle** and binomial
coefficients. Compute a single row in O(n), the first few rows of the
triangle, or any ``n choose k`` directly without intermediate factorials.

## Usage

```python
from pascal import binomial, row, triangle

assert row(4) == [1, 4, 6, 4, 1]
assert binomial(20, 10) == 184756
assert triangle(3) == [[1], [1, 1], [1, 2, 1]]
```

``binomial(n, k)`` runs in O(min(k, n-k)) multiplications and divisions,
so it stays fast even for large ``n``.

## Tests

```bash
cd pascal
pytest
```

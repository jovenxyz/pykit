# reservoir

A tiny, dependency-free implementation of **reservoir sampling**
(Algorithm R): pick a uniform random sample of ``k`` items from a stream
of unknown length in a single pass with O(k) memory.

## Usage

```python
from reservoir import sample

with open("huge.log") as fh:
    picked = sample(fh, k=100)        # 100 random lines, one pass
```

Each item in the stream has equal probability of appearing in the result,
regardless of total length. Pass ``rng=`` to make sampling deterministic in
tests.

## Tests

```bash
cd reservoir
pytest
```

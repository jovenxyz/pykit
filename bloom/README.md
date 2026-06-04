# bloom

A tiny, dependency-free **Bloom filter**: a probabilistic set supporting
fast membership tests with no false negatives, at the cost of a tunable
false-positive rate.

## Usage

```python
from bloom import BloomFilter

bf = BloomFilter(expected_items=1000, false_positive_rate=0.01)
for word in ("apple", "banana", "cherry"):
    bf.add(word)

assert "apple" in bf
assert "missing" not in bf       # extremely likely (1% expected FP)
```

The filter chooses an optimal bit-array size and hash count from the
expected item count and target false-positive rate. ``len(bf)`` returns the
number of ``add()`` operations performed (including duplicates).

## Tests

```bash
cd bloom
pytest
```

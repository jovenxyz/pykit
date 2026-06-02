# levenshtein

A tiny, dependency-free implementation of the **Levenshtein edit distance**:
the minimum number of single-character insertions, deletions or substitutions
required to transform one string into another.

## Usage

```python
from levenshtein import distance, ratio

assert distance("kitten", "sitting") == 3
assert ratio("kitten", "sitting") == 1 - 3 / 7
```

The implementation uses an O(min(len(a), len(b))) rolling array, so it stays
efficient on long strings.

## Tests

```bash
cd levenshtein
pytest
```

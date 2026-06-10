# damerau

A tiny, dependency-free implementation of the **Damerau-Levenshtein
distance** -- the minimum number of insertions, deletions, substitutions
or transpositions of adjacent characters needed to transform one string
into another.

## Usage

```python
from damerau import distance

assert distance("ab", "ba") == 1            # transposition counts as one edit
assert distance("teh", "the") == 1          # typical typo
assert distance("kitten", "sitting") == 3
```

This is the optimal-string-alignment (OSA) variant: each pair of
characters may take part in at most one transposition. Pure Levenshtein
distance can be recovered by ignoring the transposition term.

## Tests

```bash
cd damerau
pytest
```

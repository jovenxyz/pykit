# kmp

A tiny, dependency-free implementation of the **Knuth-Morris-Pratt**
substring search. Linear-time in the length of the text plus the length of
the pattern, with no worst-case quadratic blow-up.

## Usage

```python
from kmp import find, find_all

assert find("hello world", "world") == 6
assert find("hello world", "missing") == -1

# Overlapping matches are reported:
assert find_all("AAAAAA", "AAAA") == [0, 1, 2]
```

The ``build_failure`` helper exposes the failure (longest-proper-prefix-
suffix) table for educational use.

## Tests

```bash
cd kmp
pytest
```

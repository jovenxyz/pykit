# horspool

A tiny, dependency-free implementation of the **Boyer-Moore-Horspool**
substring search. Uses the bad-character heuristic to skip ahead through
the text in (typically) sub-linear time.

## Usage

```python
from horspool import find, find_all

assert find("hello world", "world") == 6
assert find("ABAAABCD", "ABC") == 4

# Overlapping matches are reported:
assert find_all("AAAAAA", "AAAA") == [0, 1, 2]
assert find_all("ababababab", "abab") == [0, 2, 4, 6]
```

Returns ``-1`` (``find``) or ``[]`` (``find_all``) when nothing matches.

## Tests

```bash
cd horspool
pytest
```

# zalg

A tiny, dependency-free implementation of the **Z-algorithm**, a
linear-time string-matching technique. The ``z_array`` is also useful for
many other string problems (period detection, palindrome counting, ...).

## Usage

```python
from zalg import find_all, z_array

# z[i] = length of the longest prefix of the string starting at i.
assert z_array("aaaa") == [4, 3, 2, 1]

# Find all (overlapping) matches of a pattern.
assert find_all("AAAAAA", "AAAA") == [0, 1, 2]
assert find_all("ababababab", "abab") == [0, 2, 4, 6]
```

``find_all`` runs the Z-algorithm on ``pattern + sep + text`` where
``sep`` is a character that does not appear in either string (default
``"\x00"``).

## Tests

```bash
cd zalg
pytest
```

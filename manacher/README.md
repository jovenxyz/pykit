# manacher

A tiny, dependency-free implementation of **Manacher's algorithm** for
finding the longest palindromic substring of a string in O(n) time.

## Usage

```python
from manacher import longest_palindrome

assert longest_palindrome("racecar") == "racecar"
assert longest_palindrome("forgeeksskeegfor") == "geeksskeeg"
assert longest_palindrome("cbbd") == "bb"
```

Use ``all_palindrome_radii`` to get the radius of the longest palindrome
centred at each position (the classic Manacher ``p`` array).

## Tests

```bash
cd manacher
pytest
```

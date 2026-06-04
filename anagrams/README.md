# anagrams

A tiny, dependency-free helper for **anagram** detection and grouping. Two
strings are anagrams when they share the same multiset of characters.

## Usage

```python
from anagrams import are_anagrams, group_anagrams, signature

assert are_anagrams("listen", "silent")
assert are_anagrams("Triangle", "Integral")

groups = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
assert groups == [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

assert signature("listen") == signature("silent")
```

Comparison is case-insensitive by default; pass ``case_insensitive=False``
to make ``"AB"`` and ``"ab"`` distinct.

## Tests

```bash
cd anagrams
pytest
```

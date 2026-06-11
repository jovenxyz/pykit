# aho

A tiny, dependency-free implementation of **Aho-Corasick** multi-pattern
string matching. Given any set of patterns, find every occurrence of
every pattern in a single linear-time pass over the text.

## Usage

```python
from aho import AhoCorasick

ac = AhoCorasick(["he", "she", "his", "hers"])
print(ac.find("ushers"))
# [(1, 'she'), (2, 'he'), (2, 'hers')]
```

Returns ``(start_index, pattern)`` for every match, including overlapping
ones (``"aa"`` in ``"aaaa"`` yields three matches).

## Tests

```bash
cd aho
pytest
```

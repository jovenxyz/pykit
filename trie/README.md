# trie

A tiny, dependency-free implementation of a **trie** (prefix tree): a set
of strings supporting fast membership tests, prefix queries, and listing all
words starting with a given prefix.

## Usage

```python
from trie import Trie

trie = Trie()
for word in ("cat", "car", "cart", "dog"):
    trie.insert(word)

assert "cat" in trie
assert trie.starts_with("ca")
assert sorted(trie.with_prefix("ca")) == ["car", "cart", "cat"]
assert len(trie) == 4
```

Inserts of duplicate words are no-ops.

## Tests

```bash
cd trie
pytest
```

# words

A tiny, dependency-free helper to **tokenize** text and surface its
most-common words. Built on ``collections.Counter`` with a default English
stop-word list.

## Usage

```python
from words import count_words, top_n, tokenize

text = "The quick brown fox jumps over the lazy dog and the cat."

assert tokenize("Hello, World!") == ["hello", "world"]
counts = count_words(text)            # default stop words excluded
assert counts["fox"] == 1
assert top_n(text, 3)[0][1] == 1
```

Pass ``stop_words=set()`` to disable filtering, or supply a custom set.

## Tests

```bash
cd words
pytest
```

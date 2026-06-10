# reflow

A tiny, dependency-free **word-wrap / text reflow** helper. Break a long
paragraph into lines that fit a maximum width.

## Usage

```python
from reflow import fill, wrap

print(fill("the quick brown fox jumps over the lazy dog", width=20))
# the quick brown fox
# jumps over the lazy
# dog

assert wrap("hello   world", 20) == ["hello world"]   # whitespace collapses
```

Runs of whitespace (including tabs and newlines) collapse to a single
space. Words longer than ``width`` are emitted on their own line as-is.

## Tests

```bash
cd reflow
pytest
```

# miniregex

A tiny, dependency-free **regex engine** supporting a small but useful
subset of patterns: literal characters, ``.`` (any char), the ``*``,
``+`` and ``?`` quantifiers, and the ``^`` / ``$`` anchors.

## Usage

```python
from miniregex import match

assert match("a.c", "abc")
assert match("^a+b*c?$", "aaabbb")
assert not match("^abc$", "abcd")
```

A pattern matches anywhere in the text unless anchored with ``^``
(start) or ``$`` (end). The engine uses greedy quantifiers with
backtracking and is deliberately small -- character classes and
alternation are not supported.

## Tests

```bash
cd miniregex
pytest
```

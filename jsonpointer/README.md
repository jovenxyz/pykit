# jsonpointer

A tiny, dependency-free implementation of [JSON Pointer (RFC 6901)][rfc]
for navigating nested ``dict`` / ``list`` structures.

[rfc]: https://datatracker.ietf.org/doc/html/rfc6901

## Usage

```python
from jsonpointer import resolve

doc = {"foo": ["bar", "baz"], "a/b": 1}

assert resolve(doc, "") == doc
assert resolve(doc, "/foo") == ["bar", "baz"]
assert resolve(doc, "/foo/0") == "bar"
assert resolve(doc, "/a~1b") == 1                    # "/" -> "~1"
assert resolve(doc, "/missing", default=None) is None
```

Pass ``default=`` to suppress ``KeyError`` and return a fallback when the
pointer doesn't resolve.

## Tests

```bash
cd jsonpointer
pytest
```

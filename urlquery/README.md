# urlquery

A tiny helper to parse and build URL query strings. Repeated keys are
preserved, ``+`` and percent-escapes are decoded on parse, and values are
percent-encoded on build.

## Usage

```python
from urlquery import build_query, parse_query

assert parse_query("?a=1&b=2&a=3") == {"a": ["1", "3"], "b": ["2"]}
assert build_query({"name": "Hello World"}) == "name=Hello%20World"
assert build_query({"tags": ["py", "test"]}) == "tags=py&tags=test"
```

The implementation only uses ``urllib.parse.quote``/``unquote`` from the
standard library for percent-encoding.

## Tests

```bash
cd urlquery
pytest
```

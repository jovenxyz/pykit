# minijson

A tiny, dependency-free **JSON parser** built as a recursive-descent
implementation of the [JSON spec][spec]. Useful as a learning reference or
when the standard library's ``json`` module is unavailable.

[spec]: https://www.json.org/

## Usage

```python
from minijson import loads

assert loads("42") == 42
assert loads('"hello"') == "hello"
assert loads("[1, 2, 3]") == [1, 2, 3]
assert loads('{"x": [1, {"y": null}]}') == {"x": [1, {"y": None}]}
```

Numbers without a decimal point or exponent decode to ``int`` (preserving
arbitrary precision); decimal or exponential numbers decode to ``float``.
Strings recognise ``\\n``, ``\\t``, ``\\u00e9`` and other JSON escapes.

Malformed input raises ``JSONDecodeError``.

## Tests

```bash
cd minijson
pytest
```

# slugify

A tiny, dependency-free helper to convert arbitrary text into URL-safe slugs.
Unicode accents are stripped, runs of non-alphanumerics collapse, and the
result is lowercase.

## Usage

```python
from slugify import slugify

assert slugify("Hello, World!") == "hello-world"
assert slugify("Cafe Creme") == "cafe-creme"
assert slugify("Hello World", separator="_") == "hello_world"
```

## Tests

```bash
cd slug
pytest
```

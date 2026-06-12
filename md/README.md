# md

A tiny, dependency-free **Markdown to plain text** stripper. Removes
common Markdown formatting (headers, emphasis, code spans, links,
images, lists, blockquotes, horizontal rules) and returns the underlying
text.

## Usage

```python
from md import to_plain_text

assert to_plain_text("# Title") == "Title"
assert to_plain_text("see [docs](https://example.com)") == "see docs"
assert to_plain_text("use `print()` to debug") == "use print() to debug"
assert to_plain_text("**bold** and *italic*") == "bold and italic"
```

This is a lightweight stripper, not a full CommonMark parser -- deeply
nested or unusual inline emphasis may slip through.

## Tests

```bash
cd md
pytest
```

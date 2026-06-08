# diff

A tiny, dependency-free **line-level diff** between two text blocks,
computed via the longest-common-subsequence algorithm. Each output line
is tagged as context (``" "``), removed (``"-"``), or added (``"+"``).

## Usage

```python
from diff import diff_lines, format_diff

before = "foo\nbar\nbaz"
after = "foo\nqux\nbaz"

print(format_diff(before, after))
#   foo
# - bar
# + qux
#   baz
```

``diff_lines`` returns a list of ``DiffLine(tag, text)`` records;
``format_diff`` renders them as a tagged text block.

## Tests

```bash
cd diff
pytest
```

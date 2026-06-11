# sheet

A tiny, dependency-free helper to convert between **spreadsheet column
letters** and 1-based indices: ``A = 1``, ``Z = 26``, ``AA = 27``,
``AZ = 52``, ``BA = 53``, ``AAA = 703``, ...

## Usage

```python
from sheet import column_to_index, index_to_column

assert column_to_index("A") == 1
assert column_to_index("AA") == 27
assert column_to_index("ZZ") == 702

assert index_to_column(1) == "A"
assert index_to_column(27) == "AA"
assert index_to_column(703) == "AAA"
```

Input to ``column_to_index`` is case-insensitive.

## Tests

```bash
cd sheet
pytest
```

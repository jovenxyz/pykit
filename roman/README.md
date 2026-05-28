# roman_numerals

A tiny, dependency-free helper to convert between integers (1-3999) and Roman
numerals.

## Usage

```python
from roman_numerals import to_roman, from_roman

assert to_roman(1994) == "MCMXCIV"
assert from_roman("MCMXCIV") == 1994
```

## Tests

```bash
cd roman
pytest
```

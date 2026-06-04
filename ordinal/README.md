# ordinal

A tiny, dependency-free helper that formats integers with English ordinal
suffixes (``1st``, ``2nd``, ``3rd``, ``4th``, ...). Handles the ``11th``/
``12th``/``13th`` exceptions correctly.

## Usage

```python
from ordinal import ordinal, ordinal_suffix

assert ordinal(1) == "1st"
assert ordinal(22) == "22nd"
assert ordinal(113) == "113th"
assert ordinal_suffix(21) == "st"
```

Negative numbers keep their sign; the suffix is chosen from the absolute
value.

## Tests

```bash
cd ordinal
pytest
```

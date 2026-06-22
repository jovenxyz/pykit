# postcode

Postal-code validation and normalization for US, UK, and Canadian formats.

## API

- `is_us_zip(s)` / `normalize_us_zip(s)` — accepts `12345` or `12345-6789`
- `is_uk_postcode(s)` / `normalize_uk_postcode(s)` — e.g. `SW1A 1AA`, `M1 1AE`
- `is_ca_postcode(s)` / `normalize_ca_postcode(s)` — e.g. `K1A 0B1` (rejects forbidden letters DFIOQUWZ in the first position)
- `detect_country(s)` → `"US" | "UK" | "CA" | None`

Normalizers raise `ValueError` on invalid input and otherwise return the canonical uppercase / spaced form.

## Example

```python
from postcode import normalize_uk_postcode, detect_country

normalize_uk_postcode("sw1a1aa")  # "SW1A 1AA"
detect_country("K1A 0B1")         # "CA"
```

## Test

```bash
python -m pytest
```

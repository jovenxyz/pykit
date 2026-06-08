# iban

A tiny, dependency-free **IBAN validator** (ISO 13616). Performs the
mod-97 check and verifies the country-specific length against a built-in
table.

## Usage

```python
from iban import country_of, is_valid

assert is_valid("GB82 WEST 1234 5698 7654 32")
assert is_valid("DE89370400440532013000")
assert country_of("FR1420041010050500013M02606") == "FR"
```

Whitespace and lowercase letters in the input are normalised before
checking. Unknown country codes skip the length check; the mod-97 step is
still applied, so most random strings still fail.

## Tests

```bash
cd iban
pytest
```

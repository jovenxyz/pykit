# luhn

A tiny, dependency-free implementation of the **Luhn checksum algorithm**
(modulus-10), used to validate credit card numbers, IMEIs, and a variety of
identification numbers.

## Usage

```python
from luhn import is_valid, check_digit

assert is_valid("4111 1111 1111 1111")
assert check_digit("7992739871") == 3
```

Non-digit characters (spaces, dashes) are ignored, so formatted card numbers
work directly.

## Tests

```bash
cd luhn
pytest
```

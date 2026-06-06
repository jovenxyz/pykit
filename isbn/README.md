# isbn

A tiny, dependency-free **ISBN** validator. Verifies the check digit of
both **ISBN-10** (10 digits, optional trailing ``X``) and **ISBN-13** (13
digits) book identifiers. Hyphens and spaces in the input are ignored.

## Usage

```python
from isbn import is_isbn10, is_isbn13, is_valid

assert is_isbn10("0-306-40615-2")
assert is_isbn13("978-0-306-40615-7")
assert is_valid("043942089X")            # accepts either form
```

The check confirms the trailing digit matches the rest of the number; it
does NOT verify the registration group or publisher prefix.

## Tests

```bash
cd isbn
pytest
```

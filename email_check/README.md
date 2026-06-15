# email_check

A tiny, dependency-free **email-address validator**. Filters out typos
in everyday forms by checking the local part, domain structure, label
shape, and length limits.

## Usage

```python
from email_check import is_valid, normalize

assert is_valid("user@example.com")
assert is_valid("first.last+tag@sub.example.co.uk")
assert not is_valid("user..name@example.com")

assert normalize("User@Example.COM") == "User@example.com"
```

This is a pragmatic subset of RFC 5321/5322 -- enough to catch common
mistakes, not a complete grammar.

## Tests

```bash
cd email_check
pytest
```

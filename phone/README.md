# phone

A tiny, dependency-free helper for **phone number** formatting and
validation. Strip punctuation, format US numbers as ``(NNN) NNN-NNNN``,
or render any number in E.164 form.

## Usage

```python
from phone import format_e164, format_us, is_valid, normalize

assert normalize("(415) 555-1234") == "4155551234"
assert is_valid("+1-415-555-1234")

assert format_us("+1-415-555-1234") == "(415) 555-1234"
assert format_e164("(415) 555-1234") == "+14155551234"
```

Pass ``default_country="44"`` (or any digit string) to ``format_e164`` to
prepend that country code when the input lacks ``+``.

## Tests

```bash
cd phone
pytest
```

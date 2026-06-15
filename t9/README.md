# t9

A tiny, dependency-free helper for the classic **T9 phone keypad**:
expand digit sequences into every possible letter combination, and
encode words back into their digit form.

## Usage

```python
from t9 import digits_for, letter_combinations

# Every word that "23" could spell:
print(letter_combinations("23"))
# ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']

# Encode a word into keys (case-insensitive):
assert digits_for("hello") == "43556"
```

Only the alphabetic keys (2-9) are supported -- characters outside the
keypad raise ``ValueError``.

## Tests

```bash
cd t9
pytest
```

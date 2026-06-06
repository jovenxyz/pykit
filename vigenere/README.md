# vigenere

A tiny, dependency-free implementation of the **Vigenere cipher** -- a
polyalphabetic substitution cipher driven by a keyword. The cipher was
considered unbreakable for centuries (hence "le chiffre indechiffrable").

## Usage

```python
from vigenere import decrypt, encrypt

assert encrypt("ATTACKATDAWN", "LEMON") == "LXFOPVEFRNHR"
assert decrypt("LXFOPVEFRNHR", "LEMON") == "ATTACKATDAWN"
```

Non-letter characters pass through unchanged, case is preserved, and the
key cycles through its letters as the text advances.

## Tests

```bash
cd vigenere
pytest
```

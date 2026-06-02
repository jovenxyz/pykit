# caesar

A tiny, dependency-free implementation of the **Caesar cipher** (a shift
substitution cipher) and the classic **ROT13** transform.

## Usage

```python
from caesar import caesar, rot13

assert caesar("Hello, World!", 5) == "Mjqqt, Btwqi!"
assert rot13("Hello, World!") == "Uryyb, Jbeyq!"
assert rot13(rot13("anything")) == "anything"
```

Non-letter characters pass through unchanged. Shifts may be any integer
(negative shifts decrypt, large shifts wrap automatically).

## Tests

```bash
cd caesar
pytest
```

# gray

A tiny, dependency-free helper for **Gray-code** conversions: binary
<-> reflected-binary Gray code, plus a generator for the full Gray
sequence of ``2**n`` codes where consecutive entries differ by exactly
one bit.

## Usage

```python
from gray import from_gray, sequence, to_gray

assert to_gray(5) == 0b111      # 5 -> 7 in Gray code
assert from_gray(0b111) == 5    # round-trip

# 3-bit Gray sequence (8 codes, each differing by one bit):
print(sequence(3))
# [0, 1, 3, 2, 6, 7, 5, 4]
```

Gray codes are useful for rotary encoders, finite-state minimisation,
genetic algorithms, and any place where consecutive numbers should
differ in only one bit position.

## Tests

```bash
cd gray
pytest
```

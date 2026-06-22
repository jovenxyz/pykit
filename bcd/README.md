# bcd

Binary-Coded Decimal (BCD) encoding and decoding — packed and unpacked.

## API

- `encode(n)` — packed BCD bytes (two digits per byte)
- `decode(data)` — inverse of `encode`
- `encode_unpacked(n)` — one digit per byte
- `decode_unpacked(data)` — inverse of `encode_unpacked`
- `byte_to_digits(b)` — split a packed byte into its `(hi, lo)` digits

## Example

```python
from bcd import encode, decode

encode(1234)         # b'\x12\x34'
decode(b'\x12\x34')  # 1234
encode(123)          # b'\x01\x23'  (odd → zero-padded)
```

## Test

```bash
python -m pytest
```

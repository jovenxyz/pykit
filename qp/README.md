# qp

A tiny, dependency-free **quoted-printable** encoder and decoder (RFC
2045). Quoted-printable is the encoding used for non-ASCII text in email
bodies and MIME headers.

## Usage

```python
from qp import decode, encode

assert encode(b"a=b") == "a=3Db"
assert encode(b"caf\xe9") == "caf=E9"
assert decode("caf=E9") == b"caf\xe9"
```

Lines are softly wrapped with ``=\\n`` continuations at ``line_length``
columns (default 76, the RFC maximum).

## Tests

```bash
cd qp
pytest
```

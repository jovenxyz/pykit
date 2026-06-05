# totp

A tiny, dependency-free implementation of **HOTP (RFC 4226)** and **TOTP
(RFC 6238)** one-time passwords. Built on ``hmac`` and ``hashlib`` from the
standard library.

## Usage

```python
from totp import from_base32, hotp, totp

secret = from_base32("JBSWY3DPEHPK3PXP")    # the form QR codes use
print(totp(secret))                          # current 6-digit code

# Reproducible for tests:
assert totp(secret, timestamp=59) == hotp(secret, 1)
```

Pass ``timestamp=`` or ``time_func=`` to make TOTP deterministic in tests.
``digits`` and ``algorithm`` ("sha1"/"sha256"/"sha512") can be tuned.

## Tests

```bash
cd totp
pytest
```

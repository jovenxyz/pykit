"""HOTP and TOTP one-time passwords (RFC 4226 and RFC 6238)."""
from __future__ import annotations

import base64
import hashlib
import hmac
import struct
import time
from typing import Callable, Optional


def hotp(
    secret: bytes,
    counter: int,
    digits: int = 6,
    algorithm: str = "sha1",
) -> str:
    """Generate an HOTP code (RFC 4226) for ``counter`` from ``secret``."""
    if digits < 1 or digits > 10:
        raise ValueError("digits must be between 1 and 10")
    counter_bytes = struct.pack(">Q", counter)
    digest = hmac.new(secret, counter_bytes, getattr(hashlib, algorithm)).digest()
    offset = digest[-1] & 0x0F
    binary = (
        (digest[offset] & 0x7F) << 24
        | (digest[offset + 1] & 0xFF) << 16
        | (digest[offset + 2] & 0xFF) << 8
        | (digest[offset + 3] & 0xFF)
    )
    return str(binary % (10 ** digits)).zfill(digits)


def totp(
    secret: bytes,
    *,
    period: int = 30,
    digits: int = 6,
    algorithm: str = "sha1",
    timestamp: Optional[float] = None,
    time_func: Callable[[], float] = time.time,
) -> str:
    """Generate a TOTP code (RFC 6238) for the current (or given) time."""
    if period <= 0:
        raise ValueError("period must be positive")
    now = timestamp if timestamp is not None else time_func()
    counter = int(now // period)
    return hotp(secret, counter, digits=digits, algorithm=algorithm)


def from_base32(encoded: str) -> bytes:
    """Decode a base32 secret (the form shown in QR codes); pad as needed."""
    cleaned = encoded.replace(" ", "").upper()
    padding = (-len(cleaned)) % 8
    return base64.b32decode(cleaned + "=" * padding)

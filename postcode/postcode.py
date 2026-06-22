"""Postal code validation and normalization for several countries."""
from __future__ import annotations
import re


_US_ZIP = re.compile(r"^(\d{5})(?:-(\d{4}))?$")
_UK = re.compile(
    r"^([A-Z]{1,2}\d[A-Z\d]?)\s*(\d[A-Z]{2})$",
    re.IGNORECASE,
)
_CA = re.compile(
    r"^([ABCEGHJKLMNPRSTVXY]\d[ABCEGHJKLMNPRSTVWXYZ])\s*(\d[ABCEGHJKLMNPRSTVWXYZ]\d)$",
    re.IGNORECASE,
)


def is_us_zip(s: str) -> bool:
    return _US_ZIP.match(s.strip()) is not None


def normalize_us_zip(s: str) -> str:
    m = _US_ZIP.match(s.strip())
    if not m:
        raise ValueError(f"invalid US ZIP: {s!r}")
    five, four = m.group(1), m.group(2)
    return f"{five}-{four}" if four else five


def is_uk_postcode(s: str) -> bool:
    return _UK.match(s.strip()) is not None


def normalize_uk_postcode(s: str) -> str:
    m = _UK.match(s.strip())
    if not m:
        raise ValueError(f"invalid UK postcode: {s!r}")
    return f"{m.group(1).upper()} {m.group(2).upper()}"


def is_ca_postcode(s: str) -> bool:
    return _CA.match(s.strip()) is not None


def normalize_ca_postcode(s: str) -> str:
    m = _CA.match(s.strip())
    if not m:
        raise ValueError(f"invalid Canadian postcode: {s!r}")
    return f"{m.group(1).upper()} {m.group(2).upper()}"


def detect_country(s: str) -> str | None:
    """Best-effort country detection. Returns 'US' | 'UK' | 'CA' | None."""
    s = s.strip()
    if is_us_zip(s):
        return "US"
    if is_ca_postcode(s):
        return "CA"
    if is_uk_postcode(s):
        return "UK"
    return None

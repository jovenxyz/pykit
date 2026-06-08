"""Validate International Bank Account Numbers (IBAN, ISO 13616)."""
from __future__ import annotations

# Country-specific IBAN lengths (full reference at https://www.iban.com/).
_LENGTHS = {
    "AD": 24, "AE": 23, "AL": 28, "AT": 20, "AZ": 28, "BA": 20, "BE": 16,
    "BG": 22, "BH": 22, "BR": 29, "BY": 28, "CH": 21, "CR": 22, "CY": 28,
    "CZ": 24, "DE": 22, "DK": 18, "DO": 28, "EE": 20, "EG": 29, "ES": 24,
    "FI": 18, "FO": 18, "FR": 27, "GB": 22, "GE": 22, "GI": 23, "GL": 18,
    "GR": 27, "GT": 28, "HR": 21, "HU": 28, "IE": 22, "IL": 23, "IQ": 23,
    "IS": 26, "IT": 27, "JO": 30, "KW": 30, "KZ": 20, "LB": 28, "LC": 32,
    "LI": 21, "LT": 20, "LU": 20, "LV": 21, "MC": 27, "MD": 24, "ME": 22,
    "MK": 19, "MR": 27, "MT": 31, "MU": 30, "NL": 18, "NO": 15, "PK": 24,
    "PL": 28, "PS": 29, "PT": 25, "QA": 29, "RO": 24, "RS": 22, "SA": 24,
    "SC": 31, "SE": 24, "SI": 19, "SK": 24, "SM": 27, "ST": 25, "SV": 28,
    "TL": 23, "TN": 24, "TR": 26, "UA": 29, "VA": 22, "VG": 24, "XK": 20,
}


def normalize(iban: str) -> str:
    """Strip whitespace and uppercase an IBAN string."""
    return "".join(iban.split()).upper()


def _digits_for(char: str) -> str:
    if char.isdigit():
        return char
    return str(ord(char) - ord("A") + 10)


def is_valid(iban: str) -> bool:
    """Return ``True`` if ``iban`` passes the ISO 13616 mod-97 check."""
    candidate = normalize(iban)
    if (
        len(candidate) < 5
        or not candidate[:2].isalpha()
        or not candidate[2:4].isdigit()
    ):
        return False
    expected = _LENGTHS.get(candidate[:2])
    if expected is not None and len(candidate) != expected:
        return False
    rearranged = candidate[4:] + candidate[:4]
    if not all(ch.isalnum() for ch in rearranged):
        return False
    numeric = "".join(_digits_for(ch) for ch in rearranged)
    return int(numeric) % 97 == 1


def country_of(iban: str) -> str:
    """Return the ISO 3166-1 alpha-2 country code from an IBAN."""
    candidate = normalize(iban)
    if len(candidate) < 2 or not candidate[:2].isalpha():
        raise ValueError(f"IBAN missing country code: {iban!r}")
    return candidate[:2]

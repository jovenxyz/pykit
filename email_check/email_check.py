"""Practical email-address validator.

Implements a sensible subset of RFC 5321/5322 -- enough to filter out
typos in everyday forms, but not a full RFC parser.
"""
from __future__ import annotations

import re

# Local part: letters, digits, and a limited set of punctuation, with no
# leading/trailing dot and no consecutive dots.
_LOCAL = re.compile(r"^(?!\.)(?!.*\.\.)[A-Za-z0-9._%+\-]+(?<!\.)$")

# Domain label: alphanumeric with internal hyphens, 1..63 chars.
_LABEL = re.compile(r"^[A-Za-z0-9](?:[A-Za-z0-9\-]{0,61}[A-Za-z0-9])?$")


def is_valid(address: str) -> bool:
    """Return ``True`` if ``address`` looks like a deliverable email address."""
    if not address or "@" not in address:
        return False
    local, _, domain = address.rpartition("@")
    if not local or not domain:
        return False
    if len(local) > 64 or len(address) > 254:
        return False
    if not _LOCAL.match(local):
        return False
    labels = domain.split(".")
    if len(labels) < 2:
        return False
    if any(not _LABEL.match(label) for label in labels):
        return False
    if labels[-1].isdigit():
        return False
    return True


def normalize(address: str) -> str:
    """Lower-case the domain portion of ``address`` (RFC-compliant)."""
    if "@" not in address:
        raise ValueError(f"not an email address: {address!r}")
    local, _, domain = address.rpartition("@")
    return f"{local}@{domain.lower()}"

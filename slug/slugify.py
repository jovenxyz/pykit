"""Convert arbitrary text into URL-safe slugs."""
from __future__ import annotations

import re
import unicodedata

_NON_ALNUM = re.compile(r"[^a-z0-9]+")
_TRIM = re.compile(r"^-+|-+$")


def slugify(text: str, separator: str = "-") -> str:
    """Return a lowercase, ASCII-only slug for ``text``.

    Unicode accents are stripped, runs of non-alphanumerics collapse to a
    single separator, and leading/trailing separators are removed.
    """
    normalised = unicodedata.normalize("NFKD", text)
    ascii_text = normalised.encode("ascii", "ignore").decode("ascii").lower()
    slug = _NON_ALNUM.sub("-", ascii_text)
    slug = _TRIM.sub("", slug)
    if separator != "-":
        slug = slug.replace("-", separator)
    return slug

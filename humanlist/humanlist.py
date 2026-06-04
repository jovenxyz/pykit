"""Join a sequence of items into an English-language list."""
from __future__ import annotations

from typing import Iterable


def humanlist(
    items: Iterable,
    conjunction: str = "and",
    oxford: bool = True,
) -> str:
    """Join ``items`` into a list like ``"a, b, and c"``.

    Parameters
    ----------
    items:
        Iterable of values; each is coerced with ``str``.
    conjunction:
        The word placed before the last item ("and", "or", ...).
    oxford:
        Whether to include the serial comma before ``conjunction`` for
        three-or-more items.
    """
    values = [str(item) for item in items]
    if not values:
        return ""
    if len(values) == 1:
        return values[0]
    if len(values) == 2:
        return f"{values[0]} {conjunction} {values[1]}"
    head = ", ".join(values[:-1])
    separator = f", {conjunction} " if oxford else f" {conjunction} "
    return f"{head}{separator}{values[-1]}"

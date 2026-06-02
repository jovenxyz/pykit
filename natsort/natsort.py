"""A natural-order sort key so ``"file10"`` sorts after ``"file2"``."""
from __future__ import annotations

import re
from typing import List, Tuple, Union

_NUMBER = re.compile(r"(\d+)")


def natural_key(text: str) -> List[Tuple[int, Union[int, str]]]:
    """Return a sort key for ``text`` that orders numeric runs by value."""
    key: List[Tuple[int, Union[int, str]]] = []
    for part in _NUMBER.split(text.casefold()):
        if not part:
            continue
        if part.isdigit():
            key.append((0, int(part)))
        else:
            key.append((1, part))
    return key

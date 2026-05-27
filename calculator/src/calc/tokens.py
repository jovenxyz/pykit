"""Token definitions for the calculator."""
from __future__ import annotations

import enum
from dataclasses import dataclass
from typing import Optional


class TokenType(enum.Enum):
    NUMBER = "NUMBER"
    PLUS = "+"
    MINUS = "-"
    STAR = "*"
    SLASH = "/"
    PERCENT = "%"
    CARET = "**"
    LPAREN = "("
    RPAREN = ")"
    EOF = "EOF"


@dataclass(frozen=True)
class Token:
    type: TokenType
    value: Optional[float] = None

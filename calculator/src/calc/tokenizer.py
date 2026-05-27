"""Convert a source string into a list of tokens."""
from __future__ import annotations

from typing import List

from calc.errors import TokenizeError
from calc.tokens import Token, TokenType

_SINGLE = {
    "+": TokenType.PLUS,
    "-": TokenType.MINUS,
    "/": TokenType.SLASH,
    "%": TokenType.PERCENT,
    "(": TokenType.LPAREN,
    ")": TokenType.RPAREN,
}


def tokenize(source: str) -> List[Token]:
    tokens: List[Token] = []
    i = 0
    length = len(source)
    while i < length:
        char = source[i]
        if char.isspace():
            i += 1
            continue
        if char.isdigit() or char == ".":
            start = i
            seen_dot = char == "."
            i += 1
            while i < length and (
                source[i].isdigit() or (source[i] == "." and not seen_dot)
            ):
                if source[i] == ".":
                    seen_dot = True
                i += 1
            tokens.append(Token(TokenType.NUMBER, float(source[start:i])))
            continue
        if char == "*":
            if i + 1 < length and source[i + 1] == "*":
                tokens.append(Token(TokenType.CARET))
                i += 2
            else:
                tokens.append(Token(TokenType.STAR))
                i += 1
            continue
        token_type = _SINGLE.get(char)
        if token_type is None:
            raise TokenizeError(f"unexpected character {char!r}")
        tokens.append(Token(token_type))
        i += 1
    tokens.append(Token(TokenType.EOF))
    return tokens

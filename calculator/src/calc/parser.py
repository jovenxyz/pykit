"""A recursive-descent parser producing an AST.

Grammar (lowest to highest precedence)::

    expr  := term (("+" | "-") term)*
    term  := power (("*" | "/" | "%") power)*
    power := unary ("**" power)?
    unary := ("+" | "-") unary | atom
    atom  := NUMBER | "(" expr ")"
"""
from __future__ import annotations

from typing import List

from calc.ast_nodes import BinaryOp, Node, Number, UnaryOp
from calc.errors import ParseError
from calc.tokens import Token, TokenType


class Parser:
    def __init__(self, tokens: List[Token]) -> None:
        self._tokens = tokens
        self._pos = 0

    def parse(self) -> Node:
        node = self._expr()
        self._expect(TokenType.EOF)
        return node

    @property
    def _current(self) -> Token:
        return self._tokens[self._pos]

    def _advance(self) -> Token:
        token = self._tokens[self._pos]
        self._pos += 1
        return token

    def _expect(self, token_type: TokenType) -> Token:
        if self._current.type is not token_type:
            raise ParseError(
                f"expected {token_type.value}, got {self._current.type.value}"
            )
        return self._advance()

    def _expr(self) -> Node:
        node = self._term()
        while self._current.type in (TokenType.PLUS, TokenType.MINUS):
            op = "+" if self._advance().type is TokenType.PLUS else "-"
            node = BinaryOp(op, node, self._term())
        return node

    def _term(self) -> Node:
        node = self._power()
        ops = {
            TokenType.STAR: "*",
            TokenType.SLASH: "/",
            TokenType.PERCENT: "%",
        }
        while self._current.type in ops:
            op = ops[self._advance().type]
            node = BinaryOp(op, node, self._power())
        return node

    def _power(self) -> Node:
        base = self._unary()
        if self._current.type is TokenType.CARET:
            self._advance()
            return BinaryOp("**", base, self._power())
        return base

    def _unary(self) -> Node:
        if self._current.type in (TokenType.PLUS, TokenType.MINUS):
            op = "+" if self._advance().type is TokenType.PLUS else "-"
            return UnaryOp(op, self._unary())
        return self._atom()

    def _atom(self) -> Node:
        token = self._current
        if token.type is TokenType.NUMBER:
            self._advance()
            return Number(token.value)
        if token.type is TokenType.LPAREN:
            self._advance()
            node = self._expr()
            self._expect(TokenType.RPAREN)
            return node
        raise ParseError(f"unexpected token {token.type.value}")

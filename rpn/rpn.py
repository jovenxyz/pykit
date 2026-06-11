"""Reverse Polish Notation (postfix) evaluator and infix-to-RPN converter."""
from __future__ import annotations

import operator
from typing import Callable, Dict, List

_OPERATORS: Dict[str, Callable[[float, float], float]] = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "%": operator.mod,
    "**": operator.pow,
}

_PRECEDENCE = {"+": 1, "-": 1, "*": 2, "/": 2, "%": 2, "**": 3}
_RIGHT_ASSOC = {"**"}


def evaluate(expression: str) -> float:
    """Evaluate a whitespace-separated RPN expression."""
    stack: List[float] = []
    for token in expression.split():
        if token in _OPERATORS:
            if len(stack) < 2:
                raise ValueError(f"not enough operands for {token!r}")
            b = stack.pop()
            a = stack.pop()
            if token == "/" and b == 0:
                raise ZeroDivisionError("division by zero")
            if token == "%" and b == 0:
                raise ZeroDivisionError("modulo by zero")
            stack.append(_OPERATORS[token](a, b))
            continue
        try:
            value = int(token)
        except ValueError:
            try:
                value = float(token)
            except ValueError as error:
                raise ValueError(f"unknown token: {token!r}") from error
        stack.append(value)
    if len(stack) != 1:
        raise ValueError(f"expression did not reduce to a single value: {stack}")
    return stack[0]


def infix_to_rpn(expression: str) -> str:
    """Convert an infix expression to RPN via the shunting-yard algorithm."""
    output: List[str] = []
    ops: List[str] = []
    for token in _tokenize_infix(expression):
        if token in _OPERATORS:
            while ops and ops[-1] != "(":
                top = ops[-1]
                if top in _OPERATORS and (
                    _PRECEDENCE[top] > _PRECEDENCE[token]
                    or (
                        _PRECEDENCE[top] == _PRECEDENCE[token]
                        and token not in _RIGHT_ASSOC
                    )
                ):
                    output.append(ops.pop())
                else:
                    break
            ops.append(token)
        elif token == "(":
            ops.append(token)
        elif token == ")":
            while ops and ops[-1] != "(":
                output.append(ops.pop())
            if not ops:
                raise ValueError("mismatched parentheses")
            ops.pop()
        else:
            output.append(token)
    while ops:
        top = ops.pop()
        if top in ("(", ")"):
            raise ValueError("mismatched parentheses")
        output.append(top)
    return " ".join(output)


def _tokenize_infix(expression: str) -> List[str]:
    tokens: List[str] = []
    i = 0
    while i < len(expression):
        ch = expression[i]
        if ch.isspace():
            i += 1
            continue
        if ch.isdigit() or ch == ".":
            j = i + 1
            while j < len(expression) and (
                expression[j].isdigit() or expression[j] == "."
            ):
                j += 1
            tokens.append(expression[i:j])
            i = j
            continue
        if ch == "*" and i + 1 < len(expression) and expression[i + 1] == "*":
            tokens.append("**")
            i += 2
            continue
        if ch in "+-*/%()":
            tokens.append(ch)
            i += 1
            continue
        raise ValueError(f"unexpected character {ch!r} at position {i}")
    return tokens

"""Evaluate an AST to a numeric result."""
from __future__ import annotations

from calc.ast_nodes import BinaryOp, Node, Number, UnaryOp
from calc.errors import EvaluationError


def evaluate_node(node: Node) -> float:
    if isinstance(node, Number):
        return node.value
    if isinstance(node, UnaryOp):
        value = evaluate_node(node.operand)
        return value if node.op == "+" else -value
    if isinstance(node, BinaryOp):
        left = evaluate_node(node.left)
        right = evaluate_node(node.right)
        return _apply(node.op, left, right)
    raise EvaluationError(f"unknown node: {node!r}")


def _apply(op: str, left: float, right: float) -> float:
    if op == "+":
        return left + right
    if op == "-":
        return left - right
    if op == "*":
        return left * right
    if op == "/":
        if right == 0:
            raise EvaluationError("division by zero")
        return left / right
    if op == "%":
        if right == 0:
            raise EvaluationError("modulo by zero")
        return left % right
    if op == "**":
        return left ** right
    raise EvaluationError(f"unknown operator: {op}")

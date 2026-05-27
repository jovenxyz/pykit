"""AST node definitions."""
from __future__ import annotations

from dataclasses import dataclass


class Node:
    """Base class for expression nodes."""


@dataclass(frozen=True)
class Number(Node):
    value: float


@dataclass(frozen=True)
class UnaryOp(Node):
    op: str
    operand: Node


@dataclass(frozen=True)
class BinaryOp(Node):
    op: str
    left: Node
    right: Node

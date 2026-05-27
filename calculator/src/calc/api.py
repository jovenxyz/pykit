"""High-level convenience API."""
from __future__ import annotations

from calc.evaluator import evaluate_node
from calc.parser import Parser
from calc.tokenizer import tokenize


def evaluate(expression: str) -> float:
    """Tokenize, parse and evaluate ``expression``."""
    tokens = tokenize(expression)
    tree = Parser(tokens).parse()
    return evaluate_node(tree)

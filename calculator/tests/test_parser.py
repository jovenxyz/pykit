from calc.ast_nodes import BinaryOp, Number
from calc.parser import Parser
from calc.tokenizer import tokenize


def _parse(source):
    return Parser(tokenize(source)).parse()


def test_precedence_builds_correct_tree():
    tree = _parse("1 + 2 * 3")
    assert isinstance(tree, BinaryOp)
    assert tree.op == "+"
    assert isinstance(tree.left, Number)
    assert isinstance(tree.right, BinaryOp)
    assert tree.right.op == "*"


def test_parentheses_override_precedence():
    tree = _parse("(1 + 2) * 3")
    assert tree.op == "*"
    assert tree.left.op == "+"


def test_trailing_operator_raises():
    import pytest

    from calc.errors import ParseError

    with pytest.raises(ParseError):
        _parse("1 +")

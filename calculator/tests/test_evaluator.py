from calc.evaluator import evaluate_node
from calc.parser import Parser
from calc.tokenizer import tokenize


def _eval(source):
    return evaluate_node(Parser(tokenize(source)).parse())


def test_basic_arithmetic():
    assert _eval("1 + 2 * 3") == 7
    assert _eval("(1 + 2) * 3") == 9
    assert _eval("10 - 4 - 3") == 3


def test_unary_minus():
    assert _eval("-3 + 5") == 2


def test_modulo():
    assert _eval("7 % 3") == 1


def test_power_is_right_associative():
    assert _eval("2 ** 3 ** 2") == 512

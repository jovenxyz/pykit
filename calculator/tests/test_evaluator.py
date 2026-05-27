from calc.evaluator import evaluate_node
from calc.parser import Parser
from calc.tokenizer import tokenize


def _eval(source):
    return evaluate_node(Parser(tokenize(source)).parse())


def test_basic_arithmetic():
    assert _eval("1 + 2 * 3") == 7
    assert _eval("(1 + 2) * 3") == 9
    assert _eval("10 - 4 - 3") == 3

import pytest

from rpn import evaluate, infix_to_rpn


def test_basic_arithmetic():
    assert evaluate("3 4 +") == 7
    assert evaluate("10 3 -") == 7
    assert evaluate("3 4 *") == 12
    assert evaluate("8 2 /") == 4


def test_complex_expression():
    # (3 + 4) * 5 in RPN: 3 4 + 5 *
    assert evaluate("3 4 + 5 *") == 35


def test_negative_numbers():
    assert evaluate("-3 4 +") == 1
    assert evaluate("3 -4 *") == -12


def test_floating_point():
    assert evaluate("1.5 2.5 +") == 4.0


def test_division_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        evaluate("1 0 /")


def test_too_few_operands_raises():
    with pytest.raises(ValueError):
        evaluate("+")
    with pytest.raises(ValueError):
        evaluate("1 +")


def test_extra_operands_raise():
    with pytest.raises(ValueError):
        evaluate("1 2 3")


def test_infix_to_rpn_basic():
    assert infix_to_rpn("3 + 4") == "3 4 +"
    assert infix_to_rpn("3 + 4 * 5") == "3 4 5 * +"


def test_infix_to_rpn_parentheses():
    assert infix_to_rpn("(3 + 4) * 5") == "3 4 + 5 *"


def test_infix_to_rpn_right_associative_power():
    assert infix_to_rpn("2 ** 3 ** 2") == "2 3 2 ** **"
    assert evaluate(infix_to_rpn("2 ** 3 ** 2")) == 512


def test_infix_to_rpn_then_evaluate():
    assert evaluate(infix_to_rpn("(3 + 4) * 5")) == 35
    assert evaluate(infix_to_rpn("10 - 2 * 3")) == 4


def test_mismatched_parentheses_raise():
    with pytest.raises(ValueError):
        infix_to_rpn("(3 + 4")
    with pytest.raises(ValueError):
        infix_to_rpn("3 + 4)")

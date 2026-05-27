import pytest

from calc import evaluate
from calc.errors import CalcError


def test_evaluate_end_to_end():
    assert evaluate("2 + 3 * 4") == 14
    assert evaluate("2 ** 10") == 1024


def test_evaluate_raises_calc_error():
    with pytest.raises(CalcError):
        evaluate("2 +")

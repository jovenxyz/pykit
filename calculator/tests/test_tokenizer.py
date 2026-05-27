from calc.tokenizer import tokenize
from calc.tokens import TokenType


def _types(source):
    return [token.type for token in tokenize(source)]


def test_numbers_and_operators():
    assert _types("1 + 2 * 3") == [
        TokenType.NUMBER,
        TokenType.PLUS,
        TokenType.NUMBER,
        TokenType.STAR,
        TokenType.NUMBER,
        TokenType.EOF,
    ]


def test_power_token():
    assert _types("2 ** 3") == [
        TokenType.NUMBER,
        TokenType.CARET,
        TokenType.NUMBER,
        TokenType.EOF,
    ]


def test_decimal_value():
    assert tokenize("3.5")[0].value == 3.5


def test_unexpected_character_raises():
    import pytest

    from calc.errors import TokenizeError

    with pytest.raises(TokenizeError):
        tokenize("1 $ 2")

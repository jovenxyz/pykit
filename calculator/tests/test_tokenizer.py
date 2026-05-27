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

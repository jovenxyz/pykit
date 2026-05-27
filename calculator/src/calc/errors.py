"""Exception types raised by the calculator."""


class CalcError(Exception):
    """Base class for all calculator errors."""


class TokenizeError(CalcError):
    """Raised when the input contains an unexpected character."""


class ParseError(CalcError):
    """Raised when the token stream is not a valid expression."""


class EvaluationError(CalcError):
    """Raised when a valid expression cannot be evaluated."""

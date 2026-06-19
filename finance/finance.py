"""Compound interest and present/future value financial helpers."""
from __future__ import annotations


def compound(principal: float, rate: float, years: float, *, periods: int = 1) -> float:
    """Future value of ``principal`` under compound interest."""
    if principal < 0 or years < 0:
        raise ValueError("principal and years must be non-negative")
    if rate < -1:
        raise ValueError("rate must be > -1")
    if periods <= 0:
        raise ValueError("periods must be positive")
    return principal * (1 + rate / periods) ** (periods * years)


def future_value(payment: float, rate: float, periods: int) -> float:
    """Future value of an ordinary annuity (payment at end of each period)."""
    if periods < 0:
        raise ValueError("periods must be non-negative")
    if rate == 0:
        return payment * periods
    return payment * (((1 + rate) ** periods - 1) / rate)


def present_value(future: float, rate: float, periods: int) -> float:
    """Return the present value of a future cash flow."""
    if periods < 0:
        raise ValueError("periods must be non-negative")
    return future / ((1 + rate) ** periods)


def annuity_payment(present_value: float, rate: float, periods: int) -> float:
    """Level payment that retires ``present_value`` over ``periods``."""
    if periods <= 0:
        raise ValueError("periods must be positive")
    if rate == 0:
        return present_value / periods
    return present_value * rate / (1 - (1 + rate) ** -periods)


def effective_annual_rate(nominal_rate: float, periods: int) -> float:
    """Convert a nominal annual rate (with ``periods`` compoundings) to EAR."""
    if periods <= 0:
        raise ValueError("periods must be positive")
    return (1 + nominal_rate / periods) ** periods - 1

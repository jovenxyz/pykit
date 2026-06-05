"""Loan amortization helpers: monthly payment and full schedule."""
from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Payment:
    period: int
    payment: float
    principal: float
    interest: float
    balance: float


def monthly_payment(principal: float, annual_rate: float, years: float) -> float:
    """Return the fixed monthly payment for a fully amortized loan.

    ``annual_rate`` is the nominal annual interest rate (0.05 = 5%).
    Zero-interest loans are supported.
    """
    if principal <= 0:
        raise ValueError("principal must be positive")
    if years <= 0:
        raise ValueError("years must be positive")
    if annual_rate < 0:
        raise ValueError("annual_rate must be non-negative")
    months = int(round(years * 12))
    if annual_rate == 0:
        return principal / months
    monthly_rate = annual_rate / 12
    factor = (1 + monthly_rate) ** months
    return principal * monthly_rate * factor / (factor - 1)


def amortization_schedule(
    principal: float,
    annual_rate: float,
    years: float,
) -> List[Payment]:
    """Return the per-period :class:`Payment` schedule for the loan."""
    months = int(round(years * 12))
    payment = monthly_payment(principal, annual_rate, years)
    monthly_rate = annual_rate / 12
    balance = principal
    schedule: List[Payment] = []
    for period in range(1, months + 1):
        interest = balance * monthly_rate
        principal_part = payment - interest
        balance -= principal_part
        # Absorb floating-point drift so the final balance is exactly zero.
        if period == months:
            principal_part += balance
            balance = 0.0
        schedule.append(
            Payment(
                period=period,
                payment=round(payment, 2),
                principal=round(principal_part, 2),
                interest=round(interest, 2),
                balance=round(balance, 2),
            )
        )
    return schedule


def total_interest(principal: float, annual_rate: float, years: float) -> float:
    """Total interest paid over the life of the loan."""
    return sum(
        payment.interest
        for payment in amortization_schedule(principal, annual_rate, years)
    )

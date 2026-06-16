"""Sales tax / VAT helpers."""
from __future__ import annotations


def add_tax(amount: float, rate: float) -> float:
    """Return ``amount`` increased by ``rate`` (e.g. ``0.2`` for 20%)."""
    if amount < 0:
        raise ValueError("amount must be non-negative")
    if rate < 0:
        raise ValueError("rate must be non-negative")
    return amount * (1 + rate)


def remove_tax(gross: float, rate: float) -> float:
    """Return the net amount before ``rate`` has been added."""
    if gross < 0:
        raise ValueError("gross must be non-negative")
    if rate < 0:
        raise ValueError("rate must be non-negative")
    return gross / (1 + rate)


def tax_amount(amount: float, rate: float, *, inclusive: bool = False) -> float:
    """Return the tax component of ``amount``.

    If ``inclusive=True``, treat ``amount`` as the gross (tax-included)
    figure; otherwise as the net (pre-tax) figure.
    """
    if amount < 0:
        raise ValueError("amount must be non-negative")
    if rate < 0:
        raise ValueError("rate must be non-negative")
    if inclusive:
        return amount - amount / (1 + rate)
    return amount * rate


def split_total(total: float, *, tax_rate: float, tip_rate: float = 0.0) -> dict:
    """Break down a total bill into ``net``, ``tax``, ``tip`` and ``total``."""
    if total < 0:
        raise ValueError("total must be non-negative")
    if tax_rate < 0 or tip_rate < 0:
        raise ValueError("rates must be non-negative")
    net = total
    tax = net * tax_rate
    tip = (net + tax) * tip_rate
    return {
        "net": net,
        "tax": tax,
        "tip": tip,
        "total": net + tax + tip,
    }

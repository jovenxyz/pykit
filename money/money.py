"""Money / currency formatting and parsing helpers."""
from __future__ import annotations


def format_amount(
    amount: float,
    *,
    symbol: str = "$",
    decimals: int = 2,
    thousands: str = ",",
    decimal_point: str = ".",
    symbol_after: bool = False,
) -> str:
    """Format ``amount`` with a currency symbol and thousands grouping."""
    if decimals < 0:
        raise ValueError("decimals must be non-negative")
    sign = "-" if amount < 0 else ""
    amount = abs(amount)
    integer_part, _, fraction_part = f"{amount:.{decimals}f}".partition(".")
    grouped = []
    for i, ch in enumerate(reversed(integer_part)):
        if i and i % 3 == 0:
            grouped.append(thousands)
        grouped.append(ch)
    integer_grouped = "".join(reversed(grouped))
    body = integer_grouped + (decimal_point + fraction_part if decimals else "")
    if symbol_after:
        return f"{sign}{body} {symbol}"
    return f"{sign}{symbol}{body}"


def parse_amount(text: str, *, thousands: str = ",", decimal_point: str = ".") -> float:
    """Parse a formatted money string back into a float."""
    cleaned = text.strip()
    if cleaned.startswith("-"):
        sign = -1
        cleaned = cleaned[1:].lstrip()
    else:
        sign = 1
    out = []
    for ch in cleaned:
        if ch.isdigit():
            out.append(ch)
        elif ch == decimal_point:
            out.append(".")
        elif ch == thousands or ch.isspace():
            continue
        # otherwise (currency symbol or letter) -> ignore
    raw = "".join(out)
    if not raw:
        raise ValueError(f"could not parse money string: {text!r}")
    return sign * float(raw)


def round_half_up(amount: float, decimals: int = 2) -> float:
    """Round ``amount`` to ``decimals`` places using half-away-from-zero rounding."""
    if decimals < 0:
        raise ValueError("decimals must be non-negative")
    factor = 10 ** decimals
    if amount >= 0:
        return int(amount * factor + 0.5) / factor
    return -int(-amount * factor + 0.5) / factor

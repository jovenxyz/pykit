import pytest

from finance import (
    annuity_payment,
    compound,
    effective_annual_rate,
    future_value,
    present_value,
)


def test_compound_annual():
    assert compound(1000, 0.05, 10) == pytest.approx(1628.8946, abs=0.01)


def test_compound_monthly():
    assert compound(1000, 0.05, 10, periods=12) == pytest.approx(1647.01, abs=0.01)


def test_compound_zero_rate():
    assert compound(1000, 0, 10) == 1000


def test_compound_invalid_raises():
    with pytest.raises(ValueError):
        compound(-1, 0.05, 10)
    with pytest.raises(ValueError):
        compound(1000, 0.05, -1)
    with pytest.raises(ValueError):
        compound(1000, 0.05, 10, periods=0)


def test_future_value_ordinary_annuity():
    assert future_value(100, 0.05, 10) == pytest.approx(1257.789, abs=0.01)


def test_future_value_zero_rate():
    assert future_value(100, 0, 10) == 1000


def test_present_value_basic():
    assert present_value(1000, 0.05, 5) == pytest.approx(783.5262, abs=0.01)


def test_annuity_payment_known_value():
    assert annuity_payment(100_000, 0.05, 30) == pytest.approx(6505.1435, abs=0.01)


def test_annuity_payment_zero_rate():
    assert annuity_payment(1200, 0, 12) == 100


def test_effective_annual_rate():
    assert effective_annual_rate(0.12, 12) == pytest.approx(0.12683, abs=1e-4)


def test_effective_rate_matches_compound():
    nominal, p = 0.08, 4
    ear = effective_annual_rate(nominal, p)
    assert (1 + ear) == pytest.approx((1 + nominal / p) ** p)

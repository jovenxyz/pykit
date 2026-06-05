import pytest

from loan import amortization_schedule, monthly_payment, total_interest


def test_monthly_payment_known_value():
    # $100,000 at 5% APR over 30 years -> $536.82/mo (standard mortgage example).
    assert monthly_payment(100_000, 0.05, 30) == pytest.approx(536.82, abs=0.01)


def test_monthly_payment_zero_interest():
    # $1,200 at 0% over 1 year -> $100/mo exactly.
    assert monthly_payment(1200, 0.0, 1) == pytest.approx(100.0)


def test_monthly_payment_invalid_raises():
    with pytest.raises(ValueError):
        monthly_payment(0, 0.05, 30)
    with pytest.raises(ValueError):
        monthly_payment(100, -0.05, 30)
    with pytest.raises(ValueError):
        monthly_payment(100, 0.05, 0)


def test_amortization_schedule_length():
    schedule = amortization_schedule(1200, 0.0, 1)
    assert len(schedule) == 12


def test_amortization_zero_interest_schedule():
    schedule = amortization_schedule(1200, 0.0, 1)
    assert all(p.interest == 0.0 for p in schedule)
    assert all(p.principal == pytest.approx(100.0) for p in schedule)
    assert schedule[-1].balance == 0.0


def test_amortization_final_balance_is_zero():
    schedule = amortization_schedule(100_000, 0.05, 30)
    assert schedule[-1].balance == 0.0


def test_total_interest_is_positive_for_interest_loan():
    assert total_interest(100_000, 0.05, 30) > 0


def test_total_interest_is_zero_for_zero_rate():
    assert total_interest(1200, 0.0, 1) == 0.0

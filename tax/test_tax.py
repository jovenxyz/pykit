import pytest

from tax import add_tax, remove_tax, split_total, tax_amount


def test_add_tax_basic():
    assert add_tax(100, 0.2) == pytest.approx(120.0)
    assert add_tax(100, 0.0) == 100.0


def test_remove_tax_inverse():
    assert remove_tax(120, 0.2) == pytest.approx(100.0)


def test_round_trip():
    for amount in (10, 100, 999.99, 0):
        assert remove_tax(add_tax(amount, 0.15), 0.15) == pytest.approx(amount)


def test_tax_amount_exclusive():
    assert tax_amount(100, 0.2) == pytest.approx(20.0)


def test_tax_amount_inclusive():
    assert tax_amount(120, 0.2, inclusive=True) == pytest.approx(20.0)


def test_split_total_with_tip():
    breakdown = split_total(100, tax_rate=0.1, tip_rate=0.2)
    assert breakdown["net"] == 100
    assert breakdown["tax"] == pytest.approx(10.0)
    assert breakdown["tip"] == pytest.approx(22.0)        # 20% of 110
    assert breakdown["total"] == pytest.approx(132.0)


def test_split_total_no_tip():
    breakdown = split_total(50, tax_rate=0.05)
    assert breakdown["tip"] == 0.0
    assert breakdown["total"] == pytest.approx(52.5)


def test_negative_inputs_raise():
    with pytest.raises(ValueError):
        add_tax(-1, 0.1)
    with pytest.raises(ValueError):
        add_tax(100, -0.1)
    with pytest.raises(ValueError):
        remove_tax(-1, 0.1)
    with pytest.raises(ValueError):
        tax_amount(-1, 0.1)
    with pytest.raises(ValueError):
        split_total(-1, tax_rate=0.1)

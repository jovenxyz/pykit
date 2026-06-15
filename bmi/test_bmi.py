import pytest

from bmi import bmi, category, from_imperial


def test_bmi_basic():
    # 70 kg, 1.75 m -> BMI ~ 22.86
    assert bmi(70, 1.75) == pytest.approx(22.857, abs=0.01)


def test_bmi_invalid_raises():
    with pytest.raises(ValueError):
        bmi(0, 1.75)
    with pytest.raises(ValueError):
        bmi(70, 0)
    with pytest.raises(ValueError):
        bmi(-1, 1.75)


def test_category_thresholds():
    assert category(17) == "underweight"
    assert category(22) == "normal"
    assert category(27) == "overweight"
    assert category(32) == "obese class I"
    assert category(37) == "obese class II"
    assert category(45) == "obese class III"


def test_category_invalid_raises():
    with pytest.raises(ValueError):
        category(0)
    with pytest.raises(ValueError):
        category(-5)


def test_from_imperial():
    # 154 lb, 69 in -> roughly 22.74 BMI.
    assert from_imperial(154, 69) == pytest.approx(22.74, abs=0.05)


def test_from_imperial_matches_metric():
    metric = bmi(70, 1.75)
    imperial = from_imperial(70 * 2.20462, 1.75 * 39.3701)
    assert metric == pytest.approx(imperial, abs=0.05)


def test_from_imperial_invalid_raises():
    with pytest.raises(ValueError):
        from_imperial(0, 69)
    with pytest.raises(ValueError):
        from_imperial(150, 0)

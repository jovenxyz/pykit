import pytest

from knapsack import chosen_items, max_value


def test_classic_example():
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    # Capacity 5: pick items 0 and 1 -> value 7.
    assert max_value(weights, values, 5) == 7


def test_pick_single_best():
    assert max_value([4], [10], 5) == 10
    assert max_value([4], [10], 3) == 0


def test_no_items():
    assert max_value([], [], 10) == 0


def test_zero_capacity():
    assert max_value([1, 2, 3], [10, 20, 30], 0) == 0


def test_chosen_items_basic():
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    value, items = chosen_items(weights, values, 5)
    assert value == 7
    assert sorted(items) == [0, 1]
    assert sum(weights[i] for i in items) <= 5


def test_chosen_items_picks_nothing_when_too_heavy():
    value, items = chosen_items([10, 20], [5, 6], 5)
    assert value == 0
    assert items == []


def test_chosen_items_full_capacity():
    value, items = chosen_items([1, 2, 3], [10, 15, 40], 6)
    assert value == 65            # 10 + 15 + 40
    assert sorted(items) == [0, 1, 2]


def test_mismatched_lengths_raise():
    with pytest.raises(ValueError):
        max_value([1, 2], [10], 5)


def test_negative_capacity_raises():
    with pytest.raises(ValueError):
        max_value([1], [10], -1)


def test_negative_weight_raises():
    with pytest.raises(ValueError):
        max_value([-1, 2], [10, 20], 5)

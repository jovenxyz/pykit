import pytest

from coinchange import coin_breakdown, min_coins, ways


def test_min_coins_basic():
    # 11 with [1, 2, 5] -> 5+5+1 = 3 coins.
    assert min_coins(11, [1, 2, 5]) == 3


def test_min_coins_exact_match():
    assert min_coins(5, [1, 2, 5]) == 1


def test_min_coins_zero():
    assert min_coins(0, [1, 2, 5]) == 0


def test_min_coins_impossible():
    assert min_coins(3, [2]) is None


def test_min_coins_negative_amount_raises():
    with pytest.raises(ValueError):
        min_coins(-1, [1])


def test_min_coins_non_positive_denomination_raises():
    with pytest.raises(ValueError):
        min_coins(5, [0, 1])
    with pytest.raises(ValueError):
        min_coins(5, [1, -2])


def test_ways_classic_example():
    # 5 with [1, 2, 5] -> {5}, {2+2+1}, {2+1+1+1}, {1*5} = 4 ways.
    assert ways(5, [1, 2, 5]) == 4


def test_ways_zero_amount_is_one():
    assert ways(0, [1, 2, 5]) == 1


def test_ways_impossible():
    assert ways(3, [2]) == 0


def test_coin_breakdown_basic():
    coins = coin_breakdown(11, [1, 2, 5])
    assert coins is not None
    assert sum(coins) == 11
    assert len(coins) == 3


def test_coin_breakdown_impossible():
    assert coin_breakdown(3, [2]) is None

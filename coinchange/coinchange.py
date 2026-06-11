"""Coin-change problem: minimum coins and number of ways via DP."""
from __future__ import annotations

from typing import List, Optional, Sequence


def _check(amount: int, denominations: Sequence[int]) -> None:
    if amount < 0:
        raise ValueError("amount must be non-negative")
    if any(d <= 0 for d in denominations):
        raise ValueError("denominations must be positive")


def min_coins(amount: int, denominations: Sequence[int]) -> Optional[int]:
    """Return the minimum number of coins to make ``amount`` or ``None``."""
    _check(amount, denominations)
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in denominations:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
    return dp[amount] if dp[amount] <= amount else None


def ways(amount: int, denominations: Sequence[int]) -> int:
    """Return the number of distinct combinations summing to ``amount``."""
    _check(amount, denominations)
    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in denominations:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
    return dp[amount]


def coin_breakdown(
    amount: int,
    denominations: Sequence[int],
) -> Optional[List[int]]:
    """Return one minimum-coin breakdown for ``amount`` or ``None``."""
    _check(amount, denominations)
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    used = [0] * (amount + 1)
    for i in range(1, amount + 1):
        for coin in denominations:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                used[i] = coin
    if dp[amount] > amount:
        return None
    coins: List[int] = []
    while amount > 0:
        coin = used[amount]
        coins.append(coin)
        amount -= coin
    coins.sort(reverse=True)
    return coins

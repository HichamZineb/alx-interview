#!/usr/bin/python3
"""
Module for makeChange function.
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list): List of coin denominations.
        total (int): Total amount to be met.

    Returns:
        int: Fewest number of coins needed to meet the total.

    """
    if total < 1:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1


if __name__ == "__main__":
    coins1 = [1, 2, 25]
    total1 = 37
    print(makeChange(coins1, total1))  # Output: 7

    coins2 = [1256, 54, 48, 16, 102]
    total2 = 1453
    print(makeChange(coins2, total2))  # Output: -1
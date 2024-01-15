#!/usr/bin/python3
"""
Module documentation - 0-minoperations

This module contains a method 'minOperations' that calculates
the fewest number of operations needed to result in exactly n H
characters in the file using Copy All and Paste operations.

"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in
    exactly n H characters in the file using Copy All and Paste operations.

    Args:
        n (int): Target number of H characters.

    Returns:
        int: Fewest number of operations.

    """
    if n <= 1:
        return 0

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i + minOperations(n // i)

    return n

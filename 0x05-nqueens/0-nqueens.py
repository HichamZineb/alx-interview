#!/usr/bin/python3
"""
N queens puzzle
"""

import sys


def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]"""
    for i in range(col):
        if board[i] == row or \
           board[i] - i == row - col or \
           board[i] + i == row + col:
            return False
    return True


def solve(board, col):
    """Recursively solve the N queens problem"""
    if col >= N:
        print(board)
        return
    for i in range(N):
        if is_safe(board, i, col):
            board[col] = i
            solve(board, col + 1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1 for _ in range(N)]
    solve(board, 0)

#!/usr/bin/python3
import sys


def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


def print_solution(board):
    solution = []
    for row, col in enumerate(board):
        solution.append([row, col])
    return solution


def solve_n_queens(size):
    if size < 4:
        print("N must be at least 4", file=sys.stderr)
        sys.exit(1)

    board = [-1] * size

    def place_queen(row):
        if row == size:
            solutions.append(print_solution(board))
            return
        for col in range(size):
            if is_safe(board, row, col):
                board[row] = col
                place_queen(row + 1)
    solutions = [] 
    place_queen(0)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N", file=sys.stderr)
        sys.exit(1)

    try:
        size = int(sys.argv[1])
        if size < 4:
            raise ValueError
    except ValueError:
        print("N must be a positive integer", file=sys.stderr)
        sys.exit(1)

    solve_n_queens(size)

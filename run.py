import random

"""
Constants
"""
MIN_BOARD_SIZE = 4
MAX_BOARD_SIZE = 8
EMPTY = ' '
SHIP_SIZES = [2, 2, 3, 4]
DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

"""
Special symbols representing different ship sizes
"""
SHIP_SYMBOLS = ['@', '■', '∆']


def create_board(size):
    return [[EMPTY] * size for _ in range(size)]


def place_ships(board):
    for size in SHIP_SIZES:
        while True:
            x = random.randint(0, len(board) - 1)
            y = random.randint(0, len(board) - 1)
            direction = random.choice(DIRECTIONS)

        """
        Check if ship fits in the board in the chosen direction
        """
        fits = True
        for i in range(size):
            new_x = x + direction[0] * i
            new_y = y + direction[1] * i
            if not (0 <= new_x < len(board) and 0 <= new_y < len(board)) or \
                    board[new_x][new_y] != EMPTY:
                fits = False
                break

        
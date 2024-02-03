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
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

        if fits:
            """
            Place ships and record its size
            """
            for i in range(size):
                new_x = x + direction[0] * i
                new_y = y + direction[1] * i
                board[new_x][new_y] = SHIP_SYMBOLS[size - 2]
            break

def print_board(board,size, hide_ships=True)
    column_width = len(str(size - 1))
    print("  " + " ".join(f"{i:>{column_width}}" for i in range(size)))  
    for i, row in enumerate(board):
        row_display = [cell if cell != EMPTY else '.' for cell in row]
        print(f"{i:>{column_width}} {' '.join(row_display)}")
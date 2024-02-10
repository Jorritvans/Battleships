import random

"""
Variables
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

def print_board(board, size, hide_ships=True):
    column_width = len(str(size - 1))
    print("  " + " ".join(f"{i:>{column_width}}" for i in range(size)))  
    for i, row in enumerate(board):
        row_display = [cell if cell != EMPTY else '.' for cell in row]
        print(f"{i:>{column_width}} {' '.join(row_display)}")

def get_board_size():
    while True:
        try:
            size = int(input(f"Enter board size ({MIN_BOARD_SIZE}-{MAX_BOARD_SIZE}): "))
            if MIN_BOARD_SIZE <= size <= MAX_BOARD_SIZE:
                return size
            else:
                print(f"Invalid input. Please enter a number between {MIN_BOARD_SIZE} and {MAX_BOARD_SIZE}.")
        except ValueError:
            print("Invalid input. Please enter a number between 4-8.")


def get_guess(board_size, guesses_board):
    while True:
        try:
            x = int(input(f"Enter row (0-{board_size - 1}): "))
            y = int(input(f"Enter column (0-{board_size - 1}): "))
            if 0 <= x < board_size and 0 <= y < board_size and guesses_board[x][y] == EMPTY:
                return x, y
            else:
                print(f"Invalid input. Please enter a number between 0 and {board_size - 1}.")
        except ValueError:
            print("Invalid input. Please enter a number.")



def get_player_name():
    return input("Enter your name: ")


def get_play_again():
    while True:
        answer = input("Do you want to play again? (y/n): ").lower()
        if answer in ['y', 'n']:
            return answer == 'y'
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")

def update_board(board, x, y, result):
    if result == 'Hit':
        board[x][y] = '!'
    elif result == 'Miss':
        board[x][y] = 'X'

def check_ship_sunk(board, x, y):
    ship_symbol = board[x][y]
    if ship_symbol in SHIP_SYMBOLS:
        ship_size = SHIP_SYMBOLS.index(ship_symbol) + 2
        directions = DIRECTIONS
        for dx, dy in directions:
            count = 1
            for i in range(1, ship_size):
                nx, ny = x + dx * i, y + dy * i
                if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] == ship_symbol:
                    count += 1
                else:
                    break
            if count == ship_size:
                return True
    return False

def main():
    print("Welcome to Battleships!")
    player_name = get_player_name()

    while True:
        print(f"Welcome, {player_name}!")

        board_size = get_board_size()
        player_board = create_board(board_size)
        computer_board = create_board(board_size)
        player_guesses_board = create_board(board_size)
        computer_guesses = set()

        """
        Place ships
        """
        place_ships(player_board)
        place_ships(computer_board)

        """ 
        Game loop
        """
        while True:
            """
            Display boards
            """
            print("\nYour board:")
            print_board(player_board, board_size, hide_ships=False)
            print("\nYour guesses:")
            print_board(player_guesses_board, board_size)

            """
            Players turn
            """
            print("\nYour turn:")
            x, y = get_guess(board_size, player_guesses_board)
            if computer_board[x][y] != EMPTY:
                print("You have hit a ship!")
                update_board(player_guesses_board, x, y, 'Hit')
                update_board(computer_board, x, y, 'Hit')
                if all(all(cell not in SHIP_SYMBOLS for cell in row) for row in computer_board):
                    print("Congratulations! You sank all the enemy ships!")
                    break
            else:
                print("You have missed!")
                update_board(player_guesses_board, x, y, 'Miss')

            """
            Check if a ship has been sunk
            """
            if check_ship_sunk(computer_board, x, y):
                print(f"You sank a {SHIP_SYMBOLS[SHIP_SIZES.index(len(computer_board[x][y]))]}!")

            """
            Check if all symbols '@', '■', '∆' have been eliminated from the computer's board
            """
            if all(cell not in SHIP_SYMBOLS for row in computer_board for cell in row):
                print("Congratulations! You've eliminated all the enemy ships!")
                break
        
            """
            Computers turn
            """
            print("\nComputer's turn:")
            while True:
                x, y = random.randint(0, board_size - 1), random.randint(0, board_size - 1)
                if (x, y) not in computer_guesses:
                    computer_guesses.add((x, y)) 
                    break
            if player_board[x][y] != EMPTY:
                print("The computer hit your ship at", x, y)
                update_board(player_board, x, y, 'Hit')
                if all(all(cell not in SHIP_SYMBOLS for cell in row) for row in player_board):
                    print("Game Over! The computer sank all your ships!")
                    break
                
            else:
                print("The computer missed at", x, y)
                update_board(player_board, x, y, 'Miss')

            """
            Check if all symbols '@', '■', '∆' have been eliminated from the player's board
            """
            if all(cell not in SHIP_SYMBOLS for row in player_board for cell in row):
                print("Game Over! You've eliminated all the enemy ships!")
                break

        if not get_play_again():
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
def print_board(board):
    """Prints the current board."""
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

def check_winner(board, player):
    """Checks if the given player has won."""
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # columns
        [0, 4, 8], [2, 4, 6]             # diagonals
    ]
    for cond in win_conditions:
        if board[cond[0]] == board[cond[1]] == board[cond[2]] == player:
            return True
    return False

def is_draw(board):
    """Checks if the game is a draw."""
    return all(spot in ['X', 'O'] for spot in board)

def get_player_move(board, player):
    """Asks the human player for their move."""
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if move >= 0 and move <= 8 and board[move] not in ['X', 'O']:
                return move
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Please enter a number from 1 to 9.")

def get_ai_move(board):
    """Simple AI picks the first available move."""
    for i in range(9):
        if board[i] not in ['X', 'O']:
            return i
    return None

def play_game():
    """Main function to play the game."""
    board = list("123456789")  # Initial board positions
    current_player = 'X'  # Human starts as X

    print("Welcome to Tic-Tac-Toe!")
    print("You are playing as X. The AI plays as O.")
    print_board(board)

    while True:
        if current_player == 'X':
            move = get_player_move(board, current_player)
        else:
            move = get_ai_move(board)
            print(f"AI ({current_player}) chose position {move + 1}")

        board[move] = current_player
        print_board(board)

        if check_winner(board, current_player):
            print(f"Player {current_player} wins! 🎉")
            break
        elif is_draw(board):
            print("It's a draw!")
            break

        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'

# Run the game
if __name__ == "__main__":
    play_game()
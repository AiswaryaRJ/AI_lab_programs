"""
Tic-Tac-Toe Game

This program implements a simple two-player Tic-Tac-Toe game where two human players take turns
entering their moves. The game checks for wins or draws after each move.

The game board is a 3x3 grid. Players enter row and column numbers (0-2) to place their marks.
Player X goes first, followed by Player O.

Rules:
- Players alternate turns.
- A player wins by getting three of their marks in a row, column, or diagonal.
- If the board is full and no one has won, it's a draw.
"""

def print_board(board):
    """
    Prints the current state of the Tic-Tac-Toe board.

    Args:
    board (list of lists): 3x3 grid representing the board.
    """
    print("\nCurrent board:")
    for row in board:
        print(' | '.join(row))
    print()

def is_winner(board, player):
    """
    Checks if a player has won the game.

    Args:
    board (list of lists): 3x3 grid representing the board.
    player (str): 'X' or 'O', the player's mark.

    Returns:
    bool: True if the player has won, False otherwise.
    """
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    """
    Checks if the board is full (no empty spaces).

    Args:
    board (list of lists): 3x3 grid representing the board.

    Returns:
    bool: True if the board is full, False otherwise.
    """
    return all(cell != ' ' for row in board for cell in row)

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    moves = [(0, 0), (0, 1), (1, 1), (2, 2), (0, 2)]  # Pre-defined moves for demonstration
    
    turn = 0
    for row, col in moves:
        print_board(board)
        current_player = players[turn]
        board[row][col] = current_player
        
        if is_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif is_full(board):
            print_board(board)
            print("Draw!")
            break
        
        turn = 1 - turn

if __name__ == "__main__":
    main()

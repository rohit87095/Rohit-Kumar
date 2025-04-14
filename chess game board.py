import pandas as pd

# Initialize the chess board
def initialize_chess_board():
    # Create an 8x8 DataFrame filled with empty strings
    board = pd.DataFrame([[' ' for _ in range(8)] for _ in range(8)], 
                         index=[8, 7, 6, 5, 4, 3, 2, 1], 
                         columns=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
    
    # Place the pieces on the board
    board.at[8, 'a'] = '♖'  # Rook
    board.at[8, 'b'] = '♘'  # Knight
    board.at[8, 'c'] = '♗'  # Bishop
    board.at[8, 'd'] = '♕'  # Queen
    board.at[8, 'e'] = '♔'  # King
    board.at[8, 'f'] = '♗'  # Bishop
    board.at[8, 'g'] = '♘'  # Knight
    board.at[8, 'h'] = '♖'  # Rook
    
    for col in 'abcdefgh':
        board.at[7, col] = '♟'  # Pawns

    # Place black pieces
    board.at[1, 'a'] = '♖'  # Rook
    board.at[1, 'b'] = '♘'  # Knight
    board.at[1, 'c'] = '♗'  # Bishop
    board.at[1, 'd'] = '♕'  # Queen
    board.at[1, 'e'] = '♔'  # King
    board.at[1, 'f'] = '♗'  # Bishop
    board.at[1, 'g'] = '♘'  # Knight
    board.at[1, 'h'] = '♖'  # Rook
    
    for col in 'abcdefgh':
        board.at[2, col] = '♙'  # Pawns

    return board

# Display the chess board
def display_chess_board(board):
    print(board)

if __name__ == "__main__":
    chess_board = initialize_chess_board()
    display_chess_board(chess_board)
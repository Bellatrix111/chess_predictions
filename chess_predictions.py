# Module 1 - Practical Project - A Chess Question

# dictionary to map letters to their corresponding column indices on the chess board
chess_coordinates_letter_to_index = {
    "a" : 0,
    "b" : 1,
    "c" : 2,
    "d" : 3,
    "e" : 4,
    "f" : 5,
    "g" : 6,
    "h" : 7
}

# dictionary to map coloumn indices to their corresponding letters on the chess board
chess_coordinates_index_to_letter = {
    0 : "a",
    1 : "b",
    2 : "c",
    3 : "d",
    4 : "e",
    5 : "f",
    6 : "g",
    7 : "h"
}

def is_valid_coordinate(position: str) -> bool:
    """
    Check if the given position is a valid coordinate on the chess board.

    Parameters:
        position (str): The position to be validated, represented as a string of the form "a3" or "h6".

    Returns:
        bool: True if the position is valid, False otherwise.
    """

    if len(position) != 2:
        return False

    column, row = position
    return column in chess_coordinates_letter_to_index and 1 <= int(row) <= 8


# i = row and j = col
# pawn attacks one square in front diagonal left or right
# pawn attack rules: (i + 1, j - 1) , (i + 1, j + 1)

def get_piece_attacks(position: str, piece_type: str) -> list:
    """
    This function takes a position on the chess board and a piece type as input
    and returns a list of all possible attacks for that piece at the given position.

    Parameters:
        position (str): The position of the piece on the chess board, represented as a string of the form "a3" or "h6".
        piece_type (str): The type of the piece, either "pawn" or "rook".

    Returns:
        list: A list of all possible attacks for the given piece at the given position, represented as strings of the form "a2" or "h5".
    """
    column, row = list(position)
    row = int(row) - 1
    column = chess_coordinates_letter_to_index[column]
    
    i, j = row, column
    solution_moves = []

    if piece_type == "pawn":
        try:
            if 0 <= i + 1 < 8 and 0 <= j - 1 < 8:
                solution_moves.append((i + 1, j - 1))
        except IndexError:
            pass
        try:
            if 0 <= i + 1 < 8 and 0 <= j + 1 < 8:
                solution_moves.append((i + 1, j + 1))
        except IndexError:
            pass
    elif piece_type == "rook":
        # Compute the moves in Row
        for col in range(8):
            if col != column:
                solution_moves.append((row, col))

        # Compute the moves in column
        for row_index in range(8):
            if row_index != row:
                solution_moves.append((row_index, column))

    # Filter out moves outside the board
    solution_moves = [(r, c) for r, c in solution_moves if 0 <= r < 8 and 0 <= c < 8]

    all_possible_moves = [
        "".join([chess_coordinates_index_to_letter[c], str(r + 1)])
        for r, c in solution_moves
    ]
    all_possible_moves.sort()
    return all_possible_moves


# Ask user to pick one piece 
chosen_white_piece = input("Please choose either pawn or rook: ").strip().lower()

# Ask user to pick a piece type 
while chosen_white_piece not in ["pawn", "rook"]:
    print("Invalid choice. Please choose either 'pawn' or 'rook'.")
    chosen_white_piece = input("Please choose either pawn or rook: ").strip().lower()

# Ask user to place the piece on the board
position = input(f"Please enter the position to place {chosen_white_piece} on the board (e.g., d4): ").strip().lower()
print(f"{chosen_white_piece.capitalize()} is now positioned at {position}")

if chosen_white_piece in ["pawn", "rook"]:
    attack_moves = get_piece_attacks(position, chosen_white_piece)
else:
    print("Invalid choice for a white piece. Please choose either 'pawn' or 'rook.'")

# Ask the user to place the black pieces on the board
# Use the same format as the white piece
# User needs to add at least 1 black piece or 16 at most 
# User can finish by writing "done" after placing at least one black piece on the board
    
black_piece_positions = []
black_piece = ""

while black_piece.lower() != "done" and len(black_piece_positions) < 16:
    black_piece = input("Enter a black piece position (or type 'done' if you are finished): ").strip().lower()

    if black_piece.lower() == "done" and not black_piece_positions:
        print("You must enter at least one valid coordinate before finishing with 'done'.")
    elif black_piece.lower() == "done":
        break  
    elif not is_valid_coordinate(black_piece):
        print("Invalid coordinate. Please enter a valid position on the chess board.")
    elif black_piece in black_piece_positions:
        print("Position already taken, please enter a different coordinate.")
    else:
        black_piece_positions.append(black_piece)
        print(f"Added black piece at {black_piece} positioned")


available_attacks = [i for i in attack_moves if i in black_piece_positions]

if available_attacks:
    print("You can attack:", ", ".join(available_attacks))
else:
    print("There are no attacks available, sorry!")

# With more time I would have liked to:
# - add all other white chess pieces including their moves and randomly select two pieces 




def create_empty_board() -> list:
    """
    Returns a game board with three rows and three colums in which all fields are set to empty, i.e., ' '.
    Returns:
        list:           Empty 3x3 game board.
    """
    return [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
    # alternative: return [[" " for row in range(3)] for col in range(3)]

    # alternative 2 with variable size:
    # outer_lst = list()

    # for r in range(rows):
    #     inner_lst = list()
    #     for c in range(columns):
    #         inner_lst.append(" ")
    #     outer_lst.append( inner_lst )
    # return outer_lst

def get_token(board: list, x: int, y: int) -> str:
    """
    Returns the game token at position x, y on the board or None if position is invalid.
    Parameters:
        board (list):   The board to get the token from.
        x (int):        The x-position.
        y (int):        The y-position.
    Returns:
        str:            The player token ('X' or '0') or ' ', if the field is empty.
    """
    if not (0 <= x < 3 and 0 <= y < 3): return None # out of bounds
    return board[y][x] 

def drop_token(board: list, player: str, x: int, y: int) -> bool:
    """
    Place the player token onto the board at the position x, y.
    Parameters:
        board (list):   The board to place the token onto.
        player (str):   The player token ('X' or '0')
        x (int):        The x-position of the drop.
        y (int):        The y-position of the drop.
    Returns:
        bool:           True, if the token was successfully dropped, False otherwise.
    """
    if not (0 <= x < 3 and 0 <= y < 3): return False # out of bounds
    if get_token(board, x,y) != " ": return False # field not empty
    if not player in ["X", "0", " "]: return False # not a valid player 
    board[y][x] = player
    return True

def print_board(board: list) -> None:
    """
    Prints a user friendly representation of the game board.
    Parameters:
        board (list):   The board to print.
    """
    assert isinstance(board, list), "board mus be a list!"
    assert len(board)==3, "Board must have 3 rows."    
    assert len(board[0])==3, "Board must have 3 columns."
    print("    0   1   2")
    print("  +---+---+---+")
    for i, row in enumerate(board):
        print(f"{i} |", end="")
        for elem in row:
            print(f" {elem} ", end="|")
        print("\n  +---+---+---+")
    print() # newline at eand of board


def is_board_full(board: list) -> bool:
    """
    Retruns True if the given game board is full (i.e., all fields are not ' '), False otherwise.
    Parameters:
        board (list):   The board to check.
    Returns:
        bool:           True if the board is full, False otherwise.
    """
    count = 0
    for row in board:
        count += row.count(" ")
    return count == 0


def check_winner(board: list) -> str:
    """
    Checks the board for a winner and returns the winner's player token ('X' or '0'), otherwise returns None.
    Parameters:
        board (list):   The board to check.
    Returns:
        str:            The player token if there is a winner, otherwise None.
    """
    for player in ["X", "0"]: # for both players check ...
        # check rows (horizontally)
        for row in board: # check all rows (left to right ---)
            if row.count(player) == 3: return player
        # check columns (vertically)
        for x in range(3): # check every column (down |)
            if board[0][x] == board[1][x] == board[2][x] == player: return player
            # alternative:
            # column_list = [row[x] for row in board] # create list with tokens from one column 
            # if column_list.count(player) == 3: return player # check if that list contains 3 player tokens
        # check diagonals
        if board[0][0] == board[1][1] == board[2][2] == player: return player # diagonally down \
        if board[2][0] == board[1][1] == board[0][2] == player: return player # diagonally up /
    if is_board_full(board): return "draw" # nobody won and board full => draw
    return None; # nobody won but board not yet full => still undecided

def play_turn() -> tuple:
    """
    Asks the user to imput a x,y position and retruns that position as a tupe. 
    Returns:
        tuple:          The position input by the user.
    """
    str = input("Enter x and y speparated by space: ")
    words = str.split()
    x, y = int(words[0]), int(words[1])
    return (x, y)

def main() -> None:
    """
    Plays a game ot TicTacToe.
    """
    board = create_empty_board()
    print_board(board) # draw initially empty board

    players = ("X", "0") # our two players
    current_player = 0 # index of current player, i.e., players[current_player]

    while True:
        move_pending=True # have not completed the current move
        while move_pending:
            print(f"It's player {players[current_player]}'s turn!")
            x,y = play_turn() # ask the player to enter their turn
            drop_ok = drop_token(board, players[current_player], x, y) # drop token into the board
            if not drop_ok: print("Error: invalid position, try again!")
            else: move_pending=False # move succesfully completed
            print_board(board) # print the board after the last move

        winner = check_winner(board)
        if winner != None:
            print(f"*** We have a winner: '{winner}'! ***")
            return            
        if is_board_full(board):
            print("Game ended in a draw!")
            return
        current_player = (current_player + 1) % len(players) # next players turn
        # end of while loop: next players move

if __name__ == "__main__":
    main()
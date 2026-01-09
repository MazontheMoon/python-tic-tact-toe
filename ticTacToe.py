# A Tic-Tac-Toe game in Python

# Define Variables

board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print("+-------+-------+-------+")
    for row in board:
        print("|       |       |       |")
        print("|   {}   |   {}   |   {}   |".format(row[0], row[1], row[2])) #extra spaces needed for alignment when printed
        print("|       |       |       |")
        print("+-------+-------+-------+")


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if move < 1 or move > 9:
                print("Invalid move.")
                continue

            for row in range(3):
                for col in range(3):
                    if board[row][col] == move:
                        board[row][col] = 'O'
                        return

            print("That square is already taken.")

        except ValueError:
            print("Please enter a number.")

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields = []

    for row in range(3):
        for col in range(3):
            if isinstance(board[row][col], int):
                free_fields.append((row, col))

    return free_fields

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    
    # Rows
    for row in board:
        if row == [sign, sign, sign]:
            return True

    # Columns
    for col in range(3):
        if board[0][col] == sign and board[1][col] == sign and board[2][col] == sign:
            return True

    # Diagonals
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True

    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True

    return False

def draw_move(board):
# The function draws the computer's move and updates the board.
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        row, col = random.choice(free_fields)
        board[row][col] = 'X'

#display_board(board)

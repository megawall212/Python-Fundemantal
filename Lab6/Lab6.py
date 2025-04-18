# Take in the 2D character list for the board and print the board.
def print_board(board):
    # Loop through each row in the board
    for row_value in board:
        # Loop through each column in the row and print the value followed by a space
        for col_value in row_value:
            print(col_value, end=" ")
        # Move to the next line after printing a row
        print()

# This will take in the num_row and num_cols from user input and
# set each spot in the list to "-".
# A 2D character list with each spot set to "-" will be returned.
def initialize_board(num_rows, num_cols):
    # Initialize an empty list to hold the rows
    board = []

    # Loop through the number of rows
    for _ in range(num_rows):
        # Create a list (row) filled with "-" for each column
        row = ["-"] * num_cols
        # Append the row to the board
        board.append(row)

    # Return the filled 2D board
    return board


# This will take in the 2D character list for the board. This function places the token
# ("x" or "o" as "chip_type") in the column that the user has chosen.
# Will find the next available spot in that column if there are already tokens there.
# The row that the token is placed in is returned.
def insert_chip(board, col, chip_type):
    row = len(board) - 1  # Start from the bottom row
    # Loop until an empty spot is found
    while board[row][col] == "o" or board[row][col] == "x":
        row -= 1
    # Place the chip in the empty spot
    board[row][col] = chip_type
    # Return the updated board and the row where the chip was placed
    return board, row


# This will take in the 2D character list for the board.
# After a token is added, checks whether the token in this location of the specified chip type
# creates four in a row. Will return True if someone won, and False otherwise.
def check_if_winner(board, col, row, chip_type):
    if_win = False  # Initialize the win flag to False
    matching_nums_in_row = 0  # Variable to track consecutive matches

    # Check horizontal locations
    for c in range(len(board[0])):  # Loop through each column
        if board[row][c] == chip_type:
            matching_nums_in_row += 1
        else:
            matching_nums_in_row = 0  # Reset if a different token is found
        if matching_nums_in_row == 4:
            if_win = True

    # Check vertical locations
    matching_nums_in_row = 0  # Reset for vertical check
    for r in range(len(board)):  # Loop through each row
        if board[r][col] == chip_type:
            matching_nums_in_row += 1
        else:
            matching_nums_in_row = 0
        if matching_nums_in_row == 4:
            if_win = True

    return if_win  # Return the result of the check


# Main function and ask for input here:
if __name__ == "__main__":
    # Ask for input to define game board dimensions.
    print("What would you like the height of the board to be?", end=" ")
    height = int(input())  # number of rows
    print("What would you like the length of the board to be?", end=" ")
    length = int(input())  # number of columns

    # Game setup
    game_board = initialize_board(height, length)  # Create a blank game board
    print_board(game_board)  # Display the board
    print("\nPlayer 1: x \nPlayer 2: o\n")  # Indicate player symbols

    # Variables for loop
    game_over = False  # Game end condition
    count = 0  # Keep track of the number of moves

    # Loop for playing game
    while not game_over:
        # First player playing
        print("Player 1: Which column would you like to choose?", end=" ")
        column = int(input())  # Get column input from Player 1
        game_board, row_num = insert_chip(game_board, column, "x")  # Insert Player 1's chip
        print_board(game_board)  # Display the updated board
        print()
        win = check_if_winner(game_board, column, row_num, "x")  # Check if Player 1 has won
        if win is True:
            print("Player 1 won the game!")
            game_over = True  # End the game if Player 1 wins
            continue

        # If board is full
        count += 1  # Increment move counter
        if count >= (height * length):  # Check if all slots are filled
            print("Draw. Nobody wins.")  # Declare draw
            game_over = True
            continue

        # Second player playing
        print("Player 2: Which column would you like to choose?", end=" ")
        column = int(input())  # Get column input from Player 2
        game_board, row_num = insert_chip(game_board, column, "o")  # Insert Player 2's chip
        print_board(game_board)  # Display the updated board
        print()
        win = check_if_winner(game_board, column, row_num, "o")  # Check if Player 2 has won
        if win is True:
            print("Player 2 won the game!")
            game_over = True  # End the game if Player 2 wins
            continue

        # If board is full
        count += 1  # Increment move counter
        if count >= (height * length):
            print("Draw. Nobody wins.")  # Declare draw if board is full, and nobody should win
            game_over = True

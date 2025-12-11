import random

# Create the board
board = [" " for _ in range(9)]

def display_board():
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def make_move(position, player):
    if board[position] == " ":
        board[position] = player
        return True
    else:
        print("That spot is already taken!")
        return False

def get_player_input(player):
    while True:
        try:
            position = int(input(f"Player {player}, choose a position (0-8): "))
            if position >= 0 and position <= 8:
                return position
            else:
                print("Please enter a number between 0 and 8.")
        except ValueError:
            print("Invalid input! Please enter a number.")

def check_winning_move(player):
    """Check if player can win on next move, return that position"""
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    
    for combo in win_combinations:
        positions = [board[combo[0]], board[combo[1]], board[combo[2]]]
        # Check if player has 2 in a row and the third spot is empty
        if positions.count(player) == 2 and positions.count(" ") == 1:
            # Find the empty spot
            for pos in combo:
                if board[pos] == " ":
                    return pos
    return None

def get_computer_move():
    """Smart computer move - blocks player from winning"""
    # First, check if computer can win
    winning_move = check_winning_move("O")
    if winning_move is not None:
        print(f"Computer chose position {winning_move} (going for the win!)")
        return winning_move
    
    # Second, check if player is about to win and block them
    blocking_move = check_winning_move("X")
    if blocking_move is not None:
        print(f"Computer chose position {blocking_move} (blocking you!)")
        return blocking_move
    
    # Otherwise, pick a random empty spot
    empty_spots = [i for i in range(9) if board[i] == " "]
    if empty_spots:
        position = random.choice(empty_spots)
        print(f"Computer chose position {position}")
        return position
    return None

def check_winner():
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return board[combo[0]]
    return None

def check_tie():
    return " " not in board

def play_game():
    """Main game loop with computer opponent"""
    current_player = "X"
    print("Welcome to Tic-Tac-Toe!")
    print("You are X, Computer is O")
    print("Positions are numbered 0-8, starting from top-left")
    
    while True:
        display_board()
        
        # Get move based on who's turn it is
        if current_player == "X":
            position = get_player_input(current_player)
        else:
            position = get_computer_move()
        
        if not make_move(position, current_player):
            continue
        
        # Check for winner
        winner = check_winner()
        if winner:
            display_board()
            if winner == "X":
                print(f"You win! 🎉")
            else:
                print(f"Computer wins! 🤖")
            break
        
        # Check for tie
        if check_tie():
            display_board()
            print("It's a tie! 🤝")
            break
        
        # Switch player
        current_player = "O" if current_player == "X" else "X"

# Start the game!
play_game()
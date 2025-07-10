# Initialize empty board
board = [" " for _ in range(9)]

def print_board():
    print("\n")
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("-" * 5)
    print("\n")

def check_winner(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8], # rows
        [0,3,6], [1,4,7], [2,5,8], # cols
        [0,4,8], [2,4,6]           # diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def is_draw():
    return " " not in board

def play_game(turn):
    print_board()
    current_player = "X" if turn % 2 == 0 else "O"
    
    print(f"Player {current_player}, enter a move (1-9):")
    move = input()
    
    # Check if input is a number
    if move.isdigit():
        move = int(move) - 1
        if 0 <= move <= 8:
            if board[move] == " ":
                board[move] = current_player
                if check_winner(current_player):
                    print_board()
                    print(f"🎉 Player {current_player} wins!")
                    return
                elif is_draw():
                    print_board()
                    print("😐 It's a draw!")
                    return
                else:
                    play_game(turn + 1)
            else:
                print("❌ That spot is already taken. Try again.")
                play_game(turn)
        else:
            print("❌ Invalid number. Please enter 1 to 9.")
            play_game(turn)
    else:
        print("❌ Invalid input. Please enter a number.")
        play_game(turn)

# Start game
print("🎮 Welcome to Tic-Tac-Toe!")
print("🧩 Cell Numbers:\n1 | 2 | 3\n4 | 5 | 6\n7 | 8 | 9")
play_game(0)

import math

# The board has 9 positions
board = [" " for _ in range(9)]


def print_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def check_winner(board):
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]

    if " " not in board:
        return "draw"

    return None


def minimax(board, maximizing):
    result = check_winner(board)

    if result == "O":
        return 1

    if result == "X":
        return -1

    if result == "draw":
        return 0

    if maximizing:
        best_score = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"

                score = minimax(board, False)

                board[i] = " "

                best_score = max(best_score, score)

        return best_score

    else:
        best_score = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"

                score = minimax(board, True)

                board[i] = " "

                best_score = min(best_score, score)

        return best_score


def ai_move():
    best_score = -math.inf
    best_move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"

            score = minimax(board, False)

            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = "O"


def player_move():
    while True:
        try:
            position = int(input("Choose a position (1-9): ")) - 1

            if position < 0 or position > 8:
                print("Please choose a number from 1 to 9.")
            elif board[position] != " ":
                print("That position is already taken.")
            else:
                board[position] = "X"
                break

        except ValueError:
            print("Please enter a number.")


def main():
    print("TIC-TAC-TOE")
    print("You are X. The AI is O.")

    while True:
        print_board()

        # Player's turn
        player_move()

        winner = check_winner(board)

        if winner:
            print_board()

            if winner == "X":
                print("You win!")
            else:
                print("It's a draw!")

            break

        # AI's turn
        print("AI is thinking...")
        ai_move()

        winner = check_winner(board)

        if winner:
            print_board()

            if winner == "O":
                print("AI wins!")
            else:
                print("It's a draw!")

            break


if __name__ == "__main__":
    main()

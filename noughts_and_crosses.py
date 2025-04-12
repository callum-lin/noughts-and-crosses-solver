from math import inf
from random import randint, choice


def get_all_child_moves(board):
    for row in range(3):
        for column in range(3):
            if board[row][column] == " ":
                yield row, column


def crosses_to_move(board):
    noughts = 0
    crosses = 0
    for i in board:
        for j in i:
            match j:
                case "O":
                    noughts += 1
                case "X":
                    crosses += 1
    return crosses == noughts
    """Note that the above is significantly faster than doing
    noughts = sum(row.count("O") for row in board)
    crosses = sum(row.count("X") for row in board)
    """


def is_there_three_in_a_row(board, symbol):
    for row in board:
        if row[0] == row[1] == row[2] == symbol:
            return True
    for column in range(len(board)):
        if board[0][column] == board[1][column] == board[2][column] == symbol:
            return True
    if board[0][0] == board[1][1] == board[2][2] == symbol:
        return True
    if board[0][2] == board[1][1] == board[2][0] == symbol:
        return True
    return False


def have_noughts_won(board):
    return is_there_three_in_a_row(board, "O")


def have_crosses_won(board):
    return is_there_three_in_a_row(board, "X")


def is_draw(board):
    if have_crosses_won(board) or have_noughts_won(board):
        return False
    for row in board:
        if " " in row:
            return False
    return True


def game_ended(board):
    if have_crosses_won(board) or have_noughts_won(board) or is_draw(board):
        return True
    return False


def evaluate(board):
    multiplier = 1 if crosses_to_move(board) else -1
    if game_ended(board):
        if have_crosses_won(board):
            return 1 * multiplier
        elif have_noughts_won(board):
            return -1 * multiplier
        else:
            return 0
    raise TypeError("Only call this function when the game has ended.")


def make_move(board, move):
    side_to_move = "X" if crosses_to_move(board) else "O"
    move_row, move_column = move
    board[move_row][move_column] = side_to_move


def unmake_move(board, move):
    move_row, move_column = move
    board[move_row][move_column] = " "


def negamax(board, starting=True):
    if game_ended(board):
        return evaluate(board)
    side_to_move = "X" if crosses_to_move(board) else "O"
    max_score = -inf
    best_move = None
    for move in get_all_child_moves(board):
        make_move(board, move)
        score = -negamax(board, starting=False)
        unmake_move(board, move)
        if score > max_score:
            max_score = score
            best_move = move
    if starting:
        return best_move
    return max_score


def is_move_valid(board, move):
    return board[move[0]][move[1]] == " "


def return_list_of_won_squares(board):
    if not game_ended(board):
        return []
    if is_draw(board):
        return []
    for i, row in enumerate(board):
        if row[0] == row[1] == row[2]:
            return [(i, 0), (i, 1), (i, 2)]
    for i in range(len(board)):
        if board[0][i] == board[1][i] == board[2][i]:
            return [(0, i), (1, i), (2, i)]
    if board[0][0] == board[1][1] == board[2][2]:
        return [(0, 0), (1, 1), (2, 2)]
    if board[0][2] == board[1][1] == board[2][0]:
        return [(0, 2), (1, 1), (2, 0)]
    return False


def generate_random_move(board):
    possible_moves = []
    for i in range(3):
        for j in range(3):
            move = (i, j)
            if is_move_valid(board, move):
                possible_moves.append(move)
    return choice(possible_moves)

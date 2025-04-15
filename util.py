from random import randint, choice
from noughts_and_crosses import is_draw, game_ended


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

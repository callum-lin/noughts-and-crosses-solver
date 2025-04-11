from noughts_and_crosses import (
    get_all_child_moves,
    evaluate,
    make_move,
    unmake_move,
    crosses_to_move,
    have_crosses_won,
    have_noughts_won,
    game_ended,
    negamax,
    is_move_valid
)

import signal
from sys import exit
from string import ascii_uppercase
from time import sleep
from random import randint


def clear_screen():
    print("\x1Bc")


def print_board(board):
    print("     A   B   C")
    print("    -----------")
    for i, row in enumerate(board):
        print(i + 1, " |", " | ".join(row), "|")
    print("    -----------")


def user_input_helper():
    user_input = input("Enter a move or type EXIT to exit: ")
    user_input = user_input.upper()
    if user_input == "EXIT":
        clear_screen()
        disable_alternate_text_buffer()
        exit()
    move_column = ascii_uppercase.find(user_input[0])
    move_row = int(user_input[1]) - 1
    return (move_row, move_column)


def get_user_input(board):
    while True:
        move = user_input_helper()
        if is_move_valid(board, move):
            return move
        print("That was an invalid move")
        sleep(1)
        clear_screen()
        print_board(board)


def game_loop(board):
    print_board(board)
    while not game_ended(board):
        user_move = get_user_input(board)
        make_move(board, user_move)

        clear_screen()
        print_board(board)   
        print("The AI is thinking...")
        best_move = negamax(board)
        make_move(board, best_move)
        clear_screen()
        print_board(board)
        if game_ended(board):
            return


def show_message(board):
    if not game_ended(board):
        print("The game is still ongoing.")
        return
    if have_crosses_won(board):
        print("Crosses have won!")
    elif have_noughts_won(board):
        print("Noughts have won!")
    else:
        print("The game ended in a draw.")


def enable_alternate_text_buffer():
    print("\x1B[?1049h")


def disable_alternate_text_buffer():
    print("\x1B[?1049l")


def main():
    board = [[" ", " ", " "] for i in range(3)]
    board[randint(0,2)][randint(0,2)] = "X"
    enable_alternate_text_buffer()
    game_loop(board)
    show_message(board)
    sleep(4)
    clear_screen()
    disable_alternate_text_buffer()


def signal_handler(sig, frame):
    print("Program shutting down.")
    print("Restoring original environment...")
    clear_screen()
    disable_alternate_text_buffer()
    exit()


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    main()

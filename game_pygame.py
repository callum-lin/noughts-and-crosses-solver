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
    is_move_valid,
    return_list_of_won_squares,
    generate_random_move,
)
import pygame

WIDTH = 720
HEIGHT = 720
LINE_THICKNESS = 2
FPS = 30
FONT_SIZE = 150


def draw_symbol_on_grid(window, center, symbol):
    font = pygame.font.SysFont("monospace", FONT_SIZE)
    COLOR = "RED" if symbol == "X" else "BLUE"
    label = font.render(symbol, True, COLOR)
    screen.blit(label, (center))


def draw_and_update_grid(window, board):
    CELL_WIDTH = WIDTH // 3
    CELL_HEIGHT = HEIGHT // 3
    rects = [[" ", " ", " "] for i in range(3)]
    for row in range(3):
        for column in range(3):
            rect = pygame.Rect(
                column * CELL_WIDTH, row * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT
            )
            rects[row][column] = rect
            if (
                rect.collidepoint(pygame.mouse.get_pos())
                and board[column][row] == " "
                and not game_ended(board)
            ) or ((column, row) in return_list_of_won_squares(board)):
                pygame.draw.rect(window, "grey", rect)
            else:
                pygame.draw.rect(window, "white", rect)
            pygame.draw.rect(window, "black", rect, LINE_THICKNESS)
    for i in range(3):
        for j in range(3):
            center_x = i * CELL_WIDTH + CELL_WIDTH // 2
            center_y = j * CELL_HEIGHT + CELL_HEIGHT // 2
            symbol = board[i][j]
            draw_symbol_on_grid(
                window, (center_x - FONT_SIZE // 3.5, center_y - FONT_SIZE // 2), symbol
            )
    return rects


def game_loop(screen, clock, board):
    screen.fill("white")
    rects = draw_and_update_grid(screen, board)
    pygame.display.flip()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            for i, row in enumerate(rects):
                for j, rect in enumerate(row):
                    if rect.collidepoint(pos):
                        move = j, i
            if is_move_valid(board, move) and not game_ended(board):
                make_move(board, move)
    if crosses_to_move(board) and not game_ended(board):
        best_move = negamax(board)
        make_move(board, best_move)


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    board = [[" ", " ", " "] for i in range(3)]
    move = generate_random_move(board)
    make_move(board, move)
    while True:
        game_loop(screen, clock, board)
    pygame.quit()

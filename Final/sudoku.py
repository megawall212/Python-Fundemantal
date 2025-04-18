import pygame
import sys
from Board import Board
from sudoku_generator import generate_sudoku


def main(difficulty=None):
    pygame.init()
    screen = pygame.display.set_mode((540, 600))
    pygame.display.set_caption("Sudoku")
    clock = pygame.time.Clock()

    if difficulty is None:
        # Display the welcome screen
        difficulty = welcome_screen(screen, clock)

    # Generate a Sudoku puzzle based on selected difficulty
    if difficulty == "easy":
        num_clues = 30  # Easy: More clues
    elif difficulty == "medium":
        num_clues = 40  # Medium: Moderate clues
    elif difficulty == "hard":
        num_clues = 50  # Hard: Fewer clues
    else:
        num_clues = 30  # Default: Medium clues

    sudoku_puzzle = generate_sudoku(9, num_clues)
    sudoku_screen = Board(540, 540, screen, sudoku_puzzle)

    # Define button rectangles
    exit_button_rect = pygame.Rect(440, 560, 80, 30)
    reset_button_rect = pygame.Rect(220, 560, 80, 30)
    restart_button_rect = pygame.Rect(10, 560, 80, 30)

    game_won = False  # Flag to track if the game is won

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Handle mouse clicks
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                click_result = sudoku_screen.click(pos[0], pos[1])
                if click_result:
                    row, col = click_result
                    sudoku_screen.select(row, col)

                if exit_button_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

                if reset_button_rect.collidepoint(event.pos):
                    sudoku_screen.reset_to_original()
                    game_won = False  # Reset the game won flag

                if restart_button_rect.collidepoint(event.pos):
                    main()

            # Handle keyboard input
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_1, pygame.K_KP1]:
                    sudoku_screen.sketch(1)
                elif event.key in [pygame.K_2, pygame.K_KP2]:
                    sudoku_screen.sketch(2)
                elif event.key in [pygame.K_3, pygame.K_KP3]:
                    sudoku_screen.sketch(3)
                elif event.key in [pygame.K_4, pygame.K_KP4]:
                    sudoku_screen.sketch(4)
                elif event.key in [pygame.K_5, pygame.K_KP5]:
                    sudoku_screen.sketch(5)
                elif event.key in [pygame.K_6, pygame.K_KP6]:
                    sudoku_screen.sketch(6)
                elif event.key in [pygame.K_7, pygame.K_KP7]:
                    sudoku_screen.sketch(7)
                elif event.key in [pygame.K_8, pygame.K_KP8]:
                    sudoku_screen.sketch(8)
                elif event.key in [pygame.K_9, pygame.K_KP9]:
                    sudoku_screen.sketch(9)
                elif event.key == pygame.K_BACKSPACE:
                    sudoku_screen.clear()
                elif event.key == pygame.K_RETURN:
                    sudoku_screen.place_number()

        # Check if the game is won (call from Board.py)
                # if not game_won and sudoku_screen.check_board():
                    # game_won = True

        # Screen
        screen.fill((255, 255, 255))
        if sudoku_screen.check_board() ==1:
            # You Won Display
            font = pygame.font.SysFont("arial", 50)
            text = font.render("Congratulations! You Won!", True, (0, 200, 0))
            screen.blit(text, (50, 250))
        elif sudoku_screen.check_board() == -1:
            font = pygame.font.SysFont("arial", 50)
            text = font.render("You lose!", True, (200, 0, 0))
            screen.blit(text, (50, 250))


        else:
            sudoku_screen.draw()

        # Draw buttons
        pygame.draw.rect(screen, (200, 200, 200), exit_button_rect)
        pygame.draw.rect(screen, (200, 200, 200), reset_button_rect)
        pygame.draw.rect(screen, (200, 200, 200), restart_button_rect)

        # Buttons Text :)
        font = pygame.font.SysFont("arial", 20)
        screen.blit(font.render("Exit", True, (0, 0, 0)), (450, 565))
        screen.blit(font.render("Reset", True, (0, 0, 0)), (230, 565))
        screen.blit(font.render("Restart", True, (0, 0, 0)), (20, 565))

        pygame.display.flip()
        clock.tick(30)


def welcome_screen(screen, clock):
    easy_button = pygame.Rect(170, 200, 200, 50)
    medium_button = pygame.Rect(170, 300, 200, 50)
    hard_button = pygame.Rect(170, 400, 200, 50)

    running = True
    while running:
        screen.fill((255, 255, 255))

        # Title
        font = pygame.font.SysFont("arial", 50)
        title = font.render("Welcome to Sudoku", True, (0, 0, 0))
        screen.blit(title, (80, 100))

        # Buttons
        pygame.draw.rect(screen, (200, 200, 200), easy_button)
        pygame.draw.rect(screen, (200, 200, 200), medium_button)
        pygame.draw.rect(screen, (200, 200, 200), hard_button)

        # Text Buttons
        font = pygame.font.SysFont("arial", 30)
        screen.blit(font.render("Easy", True, (0, 0, 0)), (230, 210))
        screen.blit(font.render("Medium", True, (0, 0, 0)), (210, 310))
        screen.blit(font.render("Hard", True, (0, 0, 0)), (230, 410))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_button.collidepoint(event.pos):
                    return "easy"
                elif medium_button.collidepoint(event.pos):
                    return "medium"
                elif hard_button.collidepoint(event.pos):
                    return "hard"

        clock.tick(30)


if __name__ == "__main__":
    main()
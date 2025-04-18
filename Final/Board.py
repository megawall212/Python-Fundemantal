import pygame


class Board:
    def __init__(self, width, height, screen, puzzle):
        self.width = width
        self.height = height
        self.screen = screen
        self.puzzle = puzzle
        self.original_puzzle = [row[:] for row in puzzle]  # original puzzle
        self.selected = None  # selected cell
        self.temp_values = [[0 for _ in range(9)] for _ in range(9)]  # Temporary values

    def click(self, x, y):
        """
        Given (x,y) bounds
        """
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return None  # Click is out of bounds

        row = y // (self.height // 9)  # Calculate the row
        col = x // (self.width // 9)   # Calculate the column
        return row, col

    def select(self, row, col):
        """
        Select Cell
        """
        if 0 <= row < 9 and 0 <= col < 9:  # Ensure selection is within bounds
            self.selected = (row, col)

    def clear(self):
        """
        Clears Value
        """
        if self.selected:
            row, col = self.selected
            if self.original_puzzle[row][col] == 0:  # Only clear cells not in the original puzzle
                self.puzzle[row][col] = 0
                self.temp_values[row][col] = 0

    def sketch(self, value):
        """
        Temp Number
        """
        if self.selected:
            row, col = self.selected
            if self.original_puzzle[row][col] == 0:  # Only sketch in cells not in the original puzzle
                self.temp_values[row][col] = value

    def place_number(self):
        """
        Perm Value/Clear Sketch
        """
        if self.selected:
            row, col = self.selected
            if self.original_puzzle[row][col] == 0:  # Only place values in editable cells
                if self.temp_values[row][col] != 0:  # Place only non-zero values
                    self.puzzle[row][col] = self.temp_values[row][col]
                    self.temp_values[row][col] = 0


    def reset_to_original(self):
        """
        Resets the board to its original state.
        """
        self.puzzle = [row[:] for row in self.original_puzzle]
        self.temp_values = [[0 for _ in range(9)] for _ in range(9)]
        self.selected = None

    def draw(self):
        """
        Draw the board and highlight the selected cell if any.
        """
        cell_width = self.width // 9
        cell_height = self.height // 9

        # Draw grid lines
        for i in range(10):
            line_width = 3 if i % 3 == 0 else 1
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * cell_height), (self.width, i * cell_height), line_width)
            pygame.draw.line(self.screen, (0, 0, 0), (i * cell_width, 0), (i * cell_width, self.height), line_width)

        # Highlight selected cell
        if self.selected:
            row, col = self.selected
            pygame.draw.rect(
                self.screen, (255, 0, 0),
                (col * cell_width, row * cell_height, cell_width, cell_height), 3
            )

        # Draw numbers and sketches
        font = pygame.font.SysFont("arial", 35)
        small_font = pygame.font.SysFont("arial", 20)
        for row in range(9):
            for col in range(9):
                num = self.puzzle[row][col]
                temp = self.temp_values[row][col]
                x = col * cell_width + cell_width // 2
                y = row * cell_height + cell_height // 2

                # Draw permanent numbers
                if num != 0:
                    text = font.render(str(num), True, (0, 0, 0))
                    text_rect = text.get_rect(center=(x, y))
                    self.screen.blit(text, text_rect)

                # Draw temporary (sketched) numbers
                elif temp != 0:
                    text = small_font.render(str(temp), True, (128, 128, 128))
                    text_rect = text.get_rect(center=(x, y))
                    self.screen.blit(text, text_rect)

    def check_board(self):
        """
        checks if the Sudoku board is solved correctly.

        Returns:
            bool: True/False
        """
        # Check if all cells are filled
        for row in self.puzzle:
            if 0 in row: # the board is incomplete
                return 0

        # Check rows
        for row in self.puzzle:
            if not self._check_line(row):
                return -1

        # Check columns
        for col in zip(*self.puzzle):
            if not self._check_line(col):
                return -1

        # Check sub-grids
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                sub_grid = [row[j:j + 3] for row in self.puzzle[i:i + 3]]
                flat_grid = sum(sub_grid, [])
                if not self._check_line(flat_grid):
                    return -1

        #  checks passed, board is solved
        return 1

    def _check_line(self, line):
        # Remove zeros (empty cells) from the line
        line = [x for x in line if x != 0]
        return len(set(line)) == len(line) and 1 <= min(line) <= 9

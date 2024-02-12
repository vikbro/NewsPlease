from typing import List, Tuple

import pygame


class GridUI:
    """
    I don't know if this class is used since there is grid.py
    """

    def __init__(self, grid: List[List[Tuple[int, int]]]) -> None:
        # has a relationship
        self.grid = grid
        # pygame window surface
        self.display_surf = pygame.display.get_surface()

    def display(self) -> None:

        for row in self.grid.coordGrid:
            for col in row:
                pygame.draw.rect(self.display_surf, (255, 0, 0),
                                 (col[0], col[1], self.grid.cell_size, self.grid.cell_size), 1)

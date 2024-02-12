from typing import List, Tuple


class Grid:
    """
    Class to contain the grid dimentions and cell size
    """
    def __init__(self, pos: Tuple[int, int], dimensions: Tuple[int, int], cell_size: int) -> None:


        self.pos = pos
        self.rows = dimensions[0]
        self.cols = dimensions[1]
        self.cell_size = cell_size

        self.coord_grid: List[List[Tuple[int, int]]] = []

        self.create_grid()
        # self.display()

    def create_grid(self) -> None:
        """
        Creates the grid positions
        @return:
        """
        start_x = self.pos[0]
        start_y = self.pos[1]
        # self.coord_grid = []
        for row in range(self.rows):
            row_x = []
            for col in range(self.cols):
                row_x.append((start_x, start_y))
                start_x += self.cell_size
            self.coord_grid.append(row_x)
            start_x = self.pos[0]
            start_y += self.cell_size
        # print(self.coord_grid)

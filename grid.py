from cell import Cell

class Grid:

    def __init__(self, width, height) -> None:
        self.cells = [[Cell(x, y) for x in range(width)] for y in range(height)]

    def draw(self, canvas) -> None:
        for row in self.cells:
            for cell in row:
                cell.draw()


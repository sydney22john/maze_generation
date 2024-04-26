from cell import Cell
import random as rand

class Grid:

    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.cells = [[Cell(y, x) for x in range(width)] for y in range(height)]

    def draw(self, canvas) -> None:
        for row in self.cells:
            for cell in row:
                cell.draw(canvas, 25)

    def getRandomCell(self) -> Cell:
        rand_x = rand.randint(0, self.width - 1)
        rand_y = rand.randint(0, self.height - 1)

        return self.cells[rand_y][rand_x]

    def getCellNeighbors(self, cell: Cell) -> list[Cell]:
        l = [
            self.getCell(cell.x, cell.y - 1),
            self.getCell(cell.x + 1, cell.y),
            self.getCell(cell.x, cell.y + 1),
            self.getCell(cell.x - 1, cell.y),
        ]
        # ran into type 'errors' when trying to use built-in filter function
        # using filter_nones to fix the typing problem. More verbose but gets the job done
        def filter_nones(l) -> list[Cell]:
            new_l = []
            for e in l:
                if e is not None:
                    new_l.append(e)
            return new_l
        return filter_nones(l)

    def getCell(self, x, y) -> Cell | None:
        if x < 0 or x >= len(self.cells[0]) \
            or y < 0 or y >= len(self.cells):
            return None
        return self.cells[x][y]

    def nextRandomNeighbor(self, cell: Cell) -> Cell | None:
        unvisisted_neighbor = list(filter(lambda c: not c.visited, self.getCellNeighbors(cell)))
        if len(unvisisted_neighbor) == 0:
            return None

        return rand.choice(unvisisted_neighbor)

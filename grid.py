from cell import Cell
import random as rand

"""
The data structure the manipulates the cells based on the maze generation algorithm
"""
class Grid:

    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.cells = [[Cell(x, y) for x in range(width)] for y in range(height)]

    def reset(self):
        self.cells = [[Cell(x, y) for x in range(self.width)] for y in range(self.height)]

    def draw(self, canvas, length, padding) -> None:
        for row in self.cells:
            for cell in row:
                cell.draw(canvas, length, padding)

    def getRandomCell(self) -> Cell:
        rand_x = rand.randint(0, self.width - 1)
        rand_y = rand.randint(0, self.height - 1)

        return self.cells[rand_y][rand_x]

    """
    returns all neighboring cells. Filters out cells that are outside the bounds of the cells array
    """
    def getCellNeighbors(self, cell: Cell) -> list[Cell]:
        # NOTE: getCell could return None if the coordinates passed in are outside the bounds of the cells array
        # NOTE: that is why we filter l later
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

    # returns a cell within the grid. If the x, y positions are outside the bounds of the cell array then None is returned
    def getCell(self, x, y) -> Cell | None:
        if x < 0 or x >= len(self.cells[0]) \
            or y < 0 or y >= len(self.cells):
            return None
        return self.cells[y][x]

    # returns a random cell that neighbors the cell passed in 
    def getRandomNeighbor(self, cell: Cell) -> Cell | None:
        unvisisted_neighbor = list(filter(lambda c: not c.visited, self.getCellNeighbors(cell)))
        if len(unvisisted_neighbor) == 0:
            return None

        return rand.choice(unvisisted_neighbor)

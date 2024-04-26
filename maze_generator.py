from abc import ABC, abstractmethod
from grid import Grid
from cell import break_wall

class MazeGenerator(ABC):

    @abstractmethod
    def generate(self, grid: Grid):
        pass

class DepthFirstGenerator(MazeGenerator):

    """
    pseudocode:
    pick random start cell
    add to stack
    while stack is not empty
        c = top of stack
        n = choose nextRandomCell (cell that isn't visited)
        if n is null
            pop stack
            continue
        break wall between c & n
        mark n as visited
        add n to stack
    """

    def generate(self, grid: Grid):
        current_cell = grid.getRandomCell()
        stack = [current_cell]

        while len(stack) != 0:
            # top of the stack
            current_cell = stack[-1]
            neighbor = grid.nextRandomNeighbor(current_cell)
            if neighbor is None:
                stack.pop()
                continue
            break_wall(current_cell, neighbor)
            neighbor.visited = True
            stack.append(neighbor)
            
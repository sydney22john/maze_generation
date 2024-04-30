from abc import ABC, abstractmethod
from cell import break_wall
from grid import Grid

# abstract MazeGenerator class
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
        mark c as visited
        n = choose nextRandomCell (cell that isn't visited)
        if n is null
            pop stack
            continue
        break wall between c & n
        add n to stack
    """
    def generate(self, grid: Grid) -> None:
        current_cell = grid.getRandomCell()
        stack = [current_cell]

        while len(stack) != 0:
            # top of the stack
            current_cell = stack[-1]
            current_cell.visited = True
            neighbor = grid.nextRandomNeighbor(current_cell)
            if neighbor is None:
                stack.pop()
                continue
            break_wall(current_cell, neighbor)
            stack.append(neighbor)

name_to_algo_map = {
    "recursive": DepthFirstGenerator,
}


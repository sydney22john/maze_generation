from abc import ABC, abstractmethod
import random as rand
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
            neighbor = grid.getRandomNeighbor(current_cell)
            if neighbor is None:
                stack.pop()
                continue
            break_wall(current_cell, neighbor)
            stack.append(neighbor)

class RandomizedPrimGenerator(MazeGenerator):
    """
    pseudocode:

    initialize the maze stack with a random cell
    while stack is not empty: 
        choose a random cell from the stack
        mark it as visited
    """
    def generate(self, grid: Grid):
        # algorithm initialization
        current_cell = grid.getRandomCell()
        current_cell.visited = True
        to_evaluate = grid.getCellNeighbors(current_cell)

        while len(to_evaluate) != 0:
            # top of stack
            rand_cell_idx = rand.randint(0, len(to_evaluate) - 1)
            current_cell = to_evaluate.pop(rand_cell_idx)
            if current_cell.visited:
                continue
            current_cell.visited = True

            neighbors = grid.getCellNeighbors(current_cell)
            # append unvisited neighbors
            to_evaluate = to_evaluate + list(filter(lambda c: not c.visited, neighbors)) 

            # break wall with current_cell and another cell that is part of the maze already
            visited_neighbors = list(filter(lambda c: c.visited, neighbors))
            break_wall(current_cell, rand.choice(visited_neighbors))
            

name_to_algo_map = {
    "recursive": DepthFirstGenerator,
    "randomized prim": RandomizedPrimGenerator,
}


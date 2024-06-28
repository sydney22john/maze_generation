
import maze_generator as gen

from grid import Grid
from maze_view import DEFAULT_ALGO, MIN_HEIGHT, MIN_WIDTH
from maze_generator import name_to_algo_map

class MazeModel:
    
    def __init__(self, width=MIN_WIDTH, height=MIN_HEIGHT) -> None:
        self.grid = Grid(width, height)
        self.generator = name_to_algo_map[DEFAULT_ALGO]()

    def setGenerator(self, generator: gen.MazeGenerator) -> None:
        self.generator = generator

    # updates the view
    def draw(self, canvas, length, padding) -> None:
        self.grid.draw(canvas, length, padding)

    # resets the maze data structure which is held in grid
    def reset(self) -> None:
        self.grid.reset()

    def generate(self) -> None:
        self.generator.generate(self.grid)

    def setWidth(self, width) -> None:
        self.grid = Grid(width, self.grid.height)

    def setHeight(self, height) -> None:
        self.grid = Grid(self.grid.width, height)

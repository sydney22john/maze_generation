
import maze_generator as gen

from grid import Grid
from maze_view import MIN_HEIGHT, MIN_WIDTH

class MazeModel:
    
    def __init__(self, width=MIN_WIDTH, height=MIN_HEIGHT) -> None:
        self.grid = Grid(width, height)
        self.generator = gen.DepthFirstGenerator()

    def setGenerator(self, generator: gen.MazeGenerator) -> None:
        self.generator = generator

    def draw(self, canvas, length, padding) -> None:
        self.grid.draw(canvas, length, padding)

    def reset(self) -> None:
        self.grid.reset()

    def start(self) -> None:
        self.generator.generate(self.grid)

    def setWidth(self, width) -> None:
        self.grid = Grid(width, self.grid.height)

    def setHeight(self, height) -> None:
        self.grid = Grid(self.grid.width, height)

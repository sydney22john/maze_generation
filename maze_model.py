
import maze_generator as gen

from grid import Grid

class MazeModel:
    
    def __init__(self, width=5, height=5):
        self.grid = Grid(width, height)
        self.generator = gen.DepthFirstGenerator()

    def setGenerator(self, generator: gen.MazeGenerator):
        self.generator = generator

    def draw(self, canvas) -> None:
        self.grid.draw(canvas)

    def reset(self):
        self.grid.reset()

    def start(self):
        self.generator.generate(self.grid)

    def setWidth(self, width):
        self.grid = Grid(width, self.grid.height)

    def setHeight(self, height):
        self.grid = Grid(self.grid.width, height)

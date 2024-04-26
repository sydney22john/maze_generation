
from grid import Grid
from maze_generator import MazeGenerator

class GridController:

    def __init__(self, canvas, x, y) -> None:
        self.canvas = canvas
        self.x = x
        self.y = y
        self.grid = Grid(self.x, self.y)

    def setGenerator(self, generator: MazeGenerator):
        self.generator = generator

    def reset(self):
        self.grid = Grid(self.x, self.y)
        self.canvas.delete("all")
        self.grid.draw(self.canvas)

    def start(self):
        self.generator.generate(self.grid)
        self.canvas.delete("all")
        self.grid.draw(self.canvas)

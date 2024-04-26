
from maze_generator import MazeGenerator

class GridController:

    def __init__(self, grid) -> None:
        self.grid = grid
        self.generator = None

    def setGenerator(self, generator: MazeGenerator):
        self.generator = generator



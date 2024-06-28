
import tkinter as tk
from maze_model import MazeModel
from maze_view import CANVAS_WIDTH, MazeView
from maze_generator import name_to_algo_map


class MazeControl:
    MIN_PADDING = 10

    def __init__(self, model: MazeModel, view: MazeView) -> None:
        # giving the control references to the model and view
        # the controller communicates to the model and view based on user input
        self.view = view
        self.view.setControl(self)

        self.model = model

        # initial rendering of the maze on the screen
        self.reset(self.view.canvas.canvas)

    """
    starts the maze generation algorithm
    this function is called by the view
    """
    def start(self, canvas):
        self.model.generate()
        canvas.delete('all')
        length, padding = self.calcDrawingParams()
        self.model.draw(canvas, length, padding)

    # not implemented 
    def stop(self):
        print("stop")

    """
    resets the maze 
    this function is called by the view
    """
    def reset(self, canvas):
        self.model.reset()
        canvas.delete('all')
        length, padding = self.calcDrawingParams()
        self.model.draw(canvas, length, padding)

    # not implemented 
    def export(self):
        print("export")

    def setWidth(self, width):
        self.model.setWidth(width)
        self.reset(self.view.canvas.canvas)

    def setHeight(self, height):
        self.model.setHeight(height)
        self.reset(self.view.canvas.canvas)

    """
    Helper function to determine the size of each cell in order to properly fit within the UI
    """
    def calcDrawingParams(self):
        max_cells = max(self.model.grid.width, self.model.grid.height)
        length = (CANVAS_WIDTH - self.MIN_PADDING * 2) / max_cells
        return length, self.MIN_PADDING

    def setAlgo(self, event: tk.Event):
        algo = event.widget.get()
        if algo not in name_to_algo_map:
            print("Error: couldn't find algorithm")
            return
        self.model.setGenerator(name_to_algo_map[algo]())


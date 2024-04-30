
import tkinter as tk
from maze_model import MazeModel
from maze_view import CANVAS_WIDTH, MazeView
from maze_generator import name_to_algo_map


class MazeControl:

    def __init__(self, model: MazeModel, view: MazeView) -> None:
        self.view = view
        self.view.setControl(self)

        self.model = model

        self.reset(self.view.canvas.canvas)

    def start(self, canvas):
        self.model.start()
        canvas.delete('all')
        length, padding = self.calcDrawingParams()
        self.model.draw(canvas, length, padding)

    def stop(self):
        print("stop")

    def reset(self, canvas):
        self.model.reset()
        canvas.delete('all')
        length, padding = self.calcDrawingParams()
        self.model.draw(canvas, length, padding)

    def export(self):
        print("export")

    def setWidth(self, width):
        self.model.setWidth(width)
        self.reset(self.view.canvas.canvas)

    def setHeight(self, height):
        self.model.setHeight(height)
        self.reset(self.view.canvas.canvas)

    def calcDrawingParams(self):
        min_padding = 10
        max_cells = max(self.model.grid.width, self.model.grid.height)
        length = (CANVAS_WIDTH - min_padding * 2) / max_cells
        return length, min_padding

    def setAlgo(self, event: tk.Event):
        algo = event.widget.get()
        if algo not in name_to_algo_map:
            print("Error: couldn't find algorithm")
            return
        self.model.setGenerator(name_to_algo_map[algo]())


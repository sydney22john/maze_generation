
from maze_view import CANVAS_WIDTH


class MazeControl:

    def __init__(self, model, view) -> None:
        self.view = view
        self.view.setControl(self)

        self.model = model

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


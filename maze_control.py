
class MazeControl:

    def __init__(self, model, view) -> None:
        self.view = view
        self.view.setControl(self)

        self.model = model

    def start(self, canvas):
        self.model.start(canvas)

    def stop(self):
        print("stop")

    def reset(self, canvas):
        self.model.reset(canvas)

    def export(self):
        print("export")

    def setWidth(self, width):
        self.model.setWidth(width)

    def setHeight(self, height):
        self.model.setHeight(height)


class MazeControl:

    def __init__(self, model, view) -> None:
        self.view = view
        self.view.setControl(self)

        self.model = model

    def start(self):
        print("start")

    def stop(self):
        print("stop")

    def reset(self):
        print("reset")

    def export(self):
        print("export")

    def setWidth(self, width):
        print(width)

    def setHeight(self, height):
        print(height)

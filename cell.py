TOP = 0
RIGHT = 1
LEFT = 2
BOTTOM = 3

class Cell:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.walls = [True, True, True, True]

    def draw(self, canvas, length) -> None:
        if self.walls[TOP]:
            canvas.create_line([(self.x * length, self.y * length), (self.x * length + length, self.y * length)], width=2)
        if self.walls[RIGHT]:
            canvas.create_line([(self.x * length + length, self.y * length), (self.x * length + length, self.y * length + length)], width=2)
        if self.walls[BOTTOM]:
            canvas.create_line([(self.x * length, self.y * length + length), (self.x * length + length, self.y * length + length)], width=2)
        if self.walls[LEFT]:
            canvas.create_line([(self.x * length, self.y * length), (self.x * length, self.y * length + length)], width=2)

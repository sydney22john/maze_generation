from directions import Direction

class Cell:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.visited = False
        self.walls = [True, True, True, True]

    def draw(self, canvas, length, padding) -> None:
        if self.walls[Direction.TOP]:
            canvas.create_line([(self.x * length + padding, self.y * length + padding), (self.x * length + padding + length, self.y * length + padding)], width=2)
        if self.walls[Direction.RIGHT]:
            canvas.create_line([(self.x * length + padding + length, self.y * length + padding), (self.x * length + padding + length, self.y * length + padding + length)], width=2)
        if self.walls[Direction.BOTTOM]:
            canvas.create_line([(self.x * length + padding, self.y * length + padding + length), (self.x * length + padding + length, self.y * length + padding + length)], width=2)
        if self.walls[Direction.LEFT]:
            canvas.create_line([(self.x * length + padding, self.y * length + padding), (self.x * length + padding, self.y * length + padding + length)], width=2)

"""
Removes the walls between two neighboring cells
"""
def break_wall(a: Cell, b: Cell):
    match (a.x - b.x, a.y - b.y):
        # a is above b
        case (0, -1):
            a.walls[Direction.BOTTOM] = False
            b.walls[Direction.TOP] = False
        # a is blow b
        case (0, 1):
            a.walls[Direction.TOP] = False
            b.walls[Direction.BOTTOM] = False
        # a is to the right of b
        case (1, 0):
            a.walls[Direction.LEFT] = False
            b.walls[Direction.RIGHT] = False
        # a is to the left of b
        case (-1, 0):
            a.walls[Direction.RIGHT] = False
            b.walls[Direction.LEFT] = False
        
        # default catch all case
        case _:
            print(f"Error: cell at ({a.x}, {a.y}) and cell at ({b.x}, {b.y}) aren't neighbors")

from tkinter import Canvas

class CCanvas:

    def __init__(self, master, width, height) -> None:
        self.width = width
        self.height = height
        self.canvas = Canvas(master=master, width=width, height=height)

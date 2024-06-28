
import tkinter as tk
from tkinter.ttk import Spinbox, Checkbutton, Combobox, Button
from maze_generator import name_to_algo_map

MIN_WIDTH = 3
MIN_HEIGHT = 3
MAX_WIDTH = 30
MAX_HEIGHT = 30

CANVAS_WIDTH = 600
CANVAS_HEIGHT = 600

DEFAULT_ALGO = "recursive"


"""
Creates all the buttons and scrollwheels at the top of the UI
"""
class Header(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.cmb_algorithm = Combobox(self, values=list(name_to_algo_map.keys()))
        self.btn_animate = Checkbutton(self, text="Animate")
        self.scl_size_w = Spinbox(self, from_=MIN_WIDTH, to=MAX_WIDTH, increment=1.0, command=self.setWidth)
        self.scl_size_h = Spinbox(self, from_=MIN_HEIGHT, to=MAX_HEIGHT, increment=1.0, command=self.setHeight)

        self.scl_size_w.set(MIN_WIDTH)
        self.scl_size_h.set(MIN_HEIGHT)

        self.cmb_algorithm.pack(side=tk.LEFT)
        self.btn_animate.pack(side=tk.LEFT)
        self.scl_size_w.pack(side=tk.LEFT)
        self.scl_size_h.pack(side=tk.LEFT)

        self.cmb_algorithm.bind("<<ComboboxSelected>>", self.setAlgo)
        self.cmb_algorithm.set(DEFAULT_ALGO)


    # CALLBACKS 
    # the following functions are callbacks that will execute when their respective button is clicked
    # NOTE: self.master is refering to the MazeView class. master is an attribute of the tk.Tk class which MazeView inherits from 
    # NOTE: I haven't found a way to get the self.master.control error to go away but all works fine 
    def setWidth(self):
        self.master.control.setWidth(int(self.scl_size_w.get()))

    def setHeight(self):
        self.master.control.setHeight(int(self.scl_size_h.get()))

    def setAlgo(self, event):
        self.master.control.setAlgo(event)


"""
This class is responsible for the middle part of the UI. The canvas is what the 
maze is drawn on top of
"""
class Canvas(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.canvas = tk.Canvas(self, bg="lightblue", height=CANVAS_HEIGHT, width=CANVAS_WIDTH)

        self.canvas.pack(side=tk.LEFT)

"""
Basically the same functionality as the Header class but for the 
buttons on the bottom of the UI
"""
class Footer(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.btn_start = Button(self, text="Start", command=self.start)
        self.btn_stop = Button(self, text="Stop", command=self.stop)
        self.btn_reset = Button(self, text="Reset", command=self.reset)
        self.btn_export = Button(self, text="Export", command=self.export)

        self.btn_start.pack(side=tk.LEFT)
        self.btn_stop.pack(side=tk.LEFT)
        self.btn_reset.pack(side=tk.LEFT)
        self.btn_export.pack(side=tk.LEFT)

    # CALLBACKS 
    # the following functions are callbacks that will execute when their respective button is clicked
    def start(self):
        self.master.control.start(self.master.canvas.canvas)
        self.master
        
    def stop(self):
        self.master.control.stop()

    def reset(self):
        self.master.control.reset(self.master.canvas.canvas)

    def export(self):
        self.master.control.export()
        

"""
Main application window and is the call that will communicate with the controller.
This class creates the header, canvas, and footer sections of the UI
"""
class MazeView(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.header = Header(self)
        self.canvas = Canvas(self)
        self.footer = Footer(self)

        self.header.pack()
        self.canvas.pack()
        self.footer.pack()

        self.control = None

    def setControl(self, control):
        self.control = control

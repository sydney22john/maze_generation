
import tkinter as tk
from tkinter.ttk import Spinbox, Checkbutton, Combobox, Button

class Header(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.cmb_algorithm = Combobox(self, values=["test1", "test2"])
        self.btn_animate = Checkbutton(self, text="Animate")
        self.scl_size_w = Spinbox(self, from_=10.0, to=50.0, increment=1.0, command=self.setWidth)
        self.scl_size_h = Spinbox(self, from_=10.0, to=50.0, increment=1.0, command=self.setHeight)

        self.scl_size_w.set(10)
        self.scl_size_h.set(10)

        self.cmb_algorithm.pack(side=tk.LEFT)
        self.btn_animate.pack(side=tk.LEFT)
        self.scl_size_w.pack(side=tk.LEFT)
        self.scl_size_h.pack(side=tk.LEFT)

    def setWidth(self):
        self.master.control.setWidth(int(self.scl_size_w.get()))

    def setHeight(self):
        self.master.control.setHeight(int(self.scl_size_h.get()))


class Canvas(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.canvas = tk.Canvas(self, bg="lightblue", height=500, width=550)

        self.canvas.pack(side=tk.LEFT)

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

    def start(self):
        self.master.control.start()
        
    def stop(self):
        self.master.control.stop()

    def reset(self):
        self.master.control.reset()

    def export(self):
        self.master.control.export()
        

class MazeView(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.header = Header(self)
        self.canvas = Canvas(self)
        self.footer = Footer(self)

        self.header.pack()
        self.canvas.pack()
        self.footer.pack()

    def setControl(self, control):
        self.control = control

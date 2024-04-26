"""
Goals of this application.
- Ability to step through maze generation algorithm
- auto play maze generation
- specify the size of the maze (with restrictions)
- disable/enable maze generation visualization
- specify the algorithm
- color legend (in a separate help tab or legend tab??)
- reset, play, stop buttons
- animation speed

Other features:
- specify the color scheme
- solve the maze option
"""

"""
Design:

-----------------------------------------
| <algo> | <size> | <animate> | <h> |   |
-----------------------------------------
|                                   | l |
|                                   | e |
|                                   | g |
|         <maze generation>         | e |
|                                   | n |
|                                   | d |
|                                   | ? |
-----------------------------------------
| <start> | <stop> | <reset> | <export> |
-----------------------------------------
| <speed> |                             |
-----------------------------------------

"""

import tkinter as tk
from tkinter.ttk import Frame, Spinbox, Checkbutton, Combobox, Button

from grid_controller import GridController
from maze_generator import DepthFirstGenerator

if __name__ == "__main__":
    window = tk.Tk()

    # START header
    frm_header = Frame(master=window)

    cmb_algorithm = Combobox(master=frm_header, values=["recursive", "breadth first"])
    cmb_algorithm.pack(side=tk.LEFT)

    btn_yes_no = Checkbutton(master=frm_header, text="Animate")
    btn_yes_no.pack(side=tk.LEFT)

    scl_size_w = Spinbox(master=frm_header, from_=10.0, to=50.0, increment=1.0)
    scl_size_w.set(10)
    scl_size_w.pack(side=tk.LEFT)

    scl_size_h = Spinbox(master=frm_header, from_=10.0, to=50.0, increment=1.0)
    scl_size_h.set(10)
    scl_size_h.pack(side=tk.LEFT)
    # END header

    # START body
    frm_body = Frame(master=window)
    canvas = tk.Canvas(master=frm_body, bg="lightblue", height=300, width=450)
    canvas.pack()

    grid_ctrl = GridController(canvas, 10, 10)
    grid_ctrl.setGenerator(DepthFirstGenerator())
    # END body

    # START footer
    frm_footer = Frame(master=window)

    btn_start = Button(master=frm_footer, text="Start", command=grid_ctrl.start)
    btn_start.pack(side=tk.LEFT)

    btn_stop = Button(master=frm_footer, text="Stop")
    btn_stop.pack(side=tk.LEFT)

    btn_reset = Button(master=frm_footer, text="Reset", command=grid_ctrl.reset)
    btn_reset.pack(side=tk.LEFT)

    btn_export = Button(master=frm_footer, text="Export")
    btn_export.pack(side=tk.LEFT)

    scl_speed = Spinbox(master=frm_footer)
    scl_speed.pack(side=tk.BOTTOM)
    # END footer

    frm_header.pack()
    frm_body.pack()
    frm_footer.pack()

    window.mainloop()

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

from maze_control import MazeControl
from maze_view import View
from grid import Grid

def main():
    control = MazeControl(Grid(5, 5), View())
    control.view.mainloop()

if __name__ == "__main__":
    main()

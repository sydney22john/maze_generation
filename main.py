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

"""
This project uses the model, view, controller architecture pattern. 
https://developer.mozilla.org/en-US/docs/Glossary/MVC

In short:
The view is the UI our user sees and it communicates user actions (mouse clicks, key presses, etc.) 
to the Controller
The model is the data itself. In my case, the state of the maze. The model could have the ability to update the view
The controller takes user input from the view and manipulates the model. The controller
can also tell the view to update its display.

an example flow of communication in my application would look something like this:
- user clicks the start button
- the view tells the controller the start button was clicked
- the controller manipulates the model by calling one of the models methods/functions
- once the model has finished its manipulations it will update the view
"""
from maze_control import MazeControl
from maze_view import MazeView
from maze_model import MazeModel

def main():
    control = MazeControl(MazeModel(), MazeView())

    # tkinter mainloop. It keeps the application window open
    control.view.mainloop()

if __name__ == "__main__":
    main()

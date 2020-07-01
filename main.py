from Window import Window
from shapes import *

win = Window(500, 500)
Rect.Rect(win, 10, 10, 100, 100, (255, 0, 0))
Ellipse.Ellipse(win, 150, 150, 100, 100, (0, 255, 0))
Rect.Rect(win, 250, 50, 150, 60, (255, 255, 0))
Rect.Rect(win, 35, 200, 75, 60, (0, 255, 255))
Line.Line(win, 225, 300, 350, 175, (255, 0, 255))

win.loop()

from shapes.BaseShape import BaseShape
from misc import *
from Vec2D import Vec2D


class Line(BaseShape):
    def __init__(self, master, x, y, x2, y2, colour=(0, 0, 0)):
        super().__init__(master, x, y, 0, 0, colour)
        self.y2 = y2
        self.x2 = x2

    def draw(self):
        self.master.drawLine(self.x, self.y, self.x2, self.y2, self.colour)

    def distance(self, x, y):
        angle = Vec2D(self.x, self.y).angle((self.x2, self.y2))
        offset = Vec2D(self.x, self.y)
        newEnd = (Vec2D(self.x2, self.y2) - offset).rotate(angle)
        newPoint = (Vec2D(x, y) - offset).rotate(angle)
        pointY = max(min(newPoint[1], newEnd[1]),0)
        return pythag(0, pointY, *newPoint)

from shapes.BaseShape import BaseShape
from misc import *


class Rect(BaseShape):
    def __init__(self, master, x, y, w, h, colour=(0, 0, 0)):
        super().__init__(master, x, y, w, h, colour)

    def draw(self):
        self.master.drawRect(self.x, self.y, self.w, self.h, self.colour)

    def distance(self, x, y):
        pointX = self.x + max(min(x-self.x, self.w), 0)
        pointY = self.y + max(min(y - self.y, self.h), 0)
        return pythag(x, y, pointX, pointY)

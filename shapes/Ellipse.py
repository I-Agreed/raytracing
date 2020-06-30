from shapes.BaseShape import BaseShape
from misc import *


class Ellipse(BaseShape):
    def __init__(self, master, x, y, w, h, colour=(0, 0, 0)):
        super().__init__(master, x, y, w, h, colour)

    def draw(self):
        self.master.drawEllipse(self.x, self.y, self.w, self.h, self.colour)

    def distance(self, x, y):
        if self.w == self.h:
            return pythag(x, y, self.x + self.w / 2, self.y + self.w / 2) - self.w / 2

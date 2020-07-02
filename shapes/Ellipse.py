from shapes.BaseShape import BaseShape
from misc import *
from math import *
from Vec2D import Vec2D


class Ellipse(BaseShape):
    def __init__(self, master, x, y, w, h, colour=(0, 0, 0)):
        super().__init__(master, x, y, w, h, colour)

    def draw(self):
        self.master.drawEllipse(self.x, self.y, self.w, self.h, self.colour)

    def distance(self, x, y, a=False):
        if self.w == self.h:
            return pythag(x, y, self.x + self.w / 2, self.y + self.w / 2) - self.w / 2
        else:
            fociDistance = (max((self.w / 2) ** 2, (self.h / 2) ** 2) - min((self.w / 2) ** 2,
                                                                            (self.h / 2) ** 2)) ** 0.5
            # length = fociDistance*2+self.w-(fociDistance*2)
            
            angle = -Vec2D(self.x+self.w/2, self.y+self.h/2).angle((x, y))
            l = sqrt(1 / ((sin(radians(angle)) / self.w*2) ** 2 + (cos(radians(angle)) / self.h*2) ** 2))
            lx = self.x+self.w/2 + l * sin(radians(angle))
            ly = self.y+self.h/2 + l * cos(radians(angle))
            if a:
                self.master.drawLine(lx, ly, x, y, (255,255,255))
            return pythag(lx, ly, x, y)

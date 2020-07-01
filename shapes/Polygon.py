from shapes.BaseShape import BaseShape
from Vec2D import Vec2D
from misc import *


class Polygon(BaseShape):
    def __init__(self, master, colour, *points):
        super().__init__(master, points[0][0], points[0][1], 0, 0, colour)
        self.points = points

    def draw(self):
        self.master.drawPolygon(self.colour, self.points)

    def lineDistance(self, x1, y1, x2, y2, pointX, pointY):
        angle = Vec2D(x1, y1).angle((x2, y2))
        offset = Vec2D(x1, y1)
        newEnd = (Vec2D(x2, y2) - offset).rotate(angle)
        newPoint = (Vec2D(pointX, pointY) - offset).rotate(angle)
        pointY = max(min(newPoint[1], newEnd[1]), 0)
        return pythag(0, pointY, *newPoint)

    def distance(self, x, y):
        distances = []
        lastPoint = self.points[-1]
        for i in self.points:
            distances.append(self.lineDistance(*i, *lastPoint, x, y))
        return min(distances)

from shapes.BaseShape import BaseShape


class Polygon(BaseShape):
    def __init__(self, master, colour, *points):
        super().__init__(master, points[0][0], points[0][1], 0, 0, colour)
        self.points = points

    def draw(self):
        self.master.drawPolygon(self.colour, self.points)

from shapes.BaseShape import BaseShape


class Ellipse(BaseShape):
    def __init__(self, master, x, y, w, h, colour=(0, 0, 0)):
        super().__init__(master, x, y, w, h, colour)

    def draw(self):
        self.master.drawEllipse(self.x, self.y, self.w, self.h, self.colour)

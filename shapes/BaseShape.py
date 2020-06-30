class BaseShape:
    def __init__(self, master, x, y, w, h, colour):
        self.master = master
        self.colour = colour
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.master.shapes.append(self)

    def draw(self):
        pass

    def distance(self, x, y):
        pass

    def center(self):
        return self.x + self.w / 2, self.y + self.h / 2

from Vec2D import Vec2D


class Ray:
    def __init__(self, window, x, y, angle):
        self.window = window
        self.x = x
        self.y = y
        self.angle = angle

    def move(self, x, y, angle=None):
        self.x = x
        self.y = y
        self.angle = angle if angle is not None else self.angle

    def cast(self, minError=1, maxError=500):
        offset = Vec2D(self.x, self.y)
        pos = Vec2D(0, 0)
        distance = self.window.closest(*(offset + pos.rotate(self.angle)))
        while maxError > distance[0] > minError:
            pos += Vec2D(0, distance[0])
            distance = self.window.closest(*(offset + pos.rotate(self.angle)))
        return offset + pos.rotate(self.angle)

import pygame
from misc import *
import ctypes
import sys

class Window():
    def __init__(self, w=320, h=240):
        super().__init__()
        try:
            ctypes.windll.shcore.SetProcessDpiAwareness(True)
        except:
            pass
        pygame.init()
        self.screen = pygame.display.set_mode((w, h))
        self.shapes = []

    def frame(self):


        for i in self.shapes:
            i.draw()

        pygame.display.flip()

    def mouseEvent(self, x, y):
        closest = None
        for i in self.shapes:
            point = i.distance(x, y)
            if point is not None:
                if closest is None:
                    closest = point
                elif closest > point:
                    closest = point
        if closest > 0:
            self.drawEllipse(x-closest, y-closest, closest*2, closest*2, (0, 0, 255))

    def drawEllipse(self, x, y, w, h, colour):
        pygame.draw.ellipse(self.screen, colour, (x, y, w, h))

    def drawPolygon(self, colour, *points):
        pygame.draw.polygon(self.screen, colour, points)

    def drawRect(self, x, y, w, h, colour):
        pygame.draw.rect(self.screen, colour, (x, y, w, h))

    def drawLine(self, x1, x2, y1, y2, colour):
        pygame.draw.line(self.screen, colour, (x1, y1), (x2, y2))

    def events(self):
        return pygame.event.get()

    def loop(self):
        while 1:
            self.screen.fill((0, 0, 0))
            for event in self.events():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.mouseEvent(*pygame.mouse.get_pos())
            self.frame()

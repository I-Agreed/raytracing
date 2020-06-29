import pygame

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
        self.screen.fill((0, 0, 0))

        for i in self.shapes:
            i.draw()

        pygame.display.flip()

    def drawEllipse(self, x, y, w, h, colour):
        pygame.draw.ellipse(self.screen, colour, (x, y, w, h))

    def drawPolygon(self, colour, *points):
        pygame.draw.polygon(self.screen, colour, points)

    def drawRect(self, x, y, w, h, colour):
        pygame.draw.rect(self.screen, colour, (x, y, w, h))

    def events(self):
        return pygame.event.get()

    def loop(self):
        while 1:
            for event in self.events():
                if event.type == pygame.QUIT: sys.exit()

            self.frame()

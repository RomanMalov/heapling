import pygame as pg


class View():

    def __init__(self, display : pg.Surface):
        self.display = display

    def draw_circle(self, x, y, r, color):
        pg.draw.circle(self.display, color, (round(x),round(y)), round(r), 1)

    def draw_line(self, x0, y0, x1, y1, color):
        pg.draw.line(self.display, color, (round(x0), round(y0)), (round(x1), round(y1)))

    def fill_circle(self, x, y, r, color):
        pg.draw.circle(self.display, color, (round(x),round(y)), r, 0) #if width is zero - it fill the circle

    def draw_rect(self, x0, y0, x1, y1, color):
        pg.draw.rect(self.display, color, pg.Rect((round(x0), round(y0)), (round(x1), round(y1))))

    def update(self):
        pg.display.flip()
        self.display.fill((255,255,255))

    def erase(self):
        pass
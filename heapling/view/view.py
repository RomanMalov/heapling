import pygame as pg


class View():

    def __init__(self, display : pg.Surface):
        self.display = display

    def draw_circle(self, x, y, r, color):
        pg.draw.circle(self.display, color, (x,y), r, 1)

    def draw_line(self, x0, y0, x1, y1, color):
        pg.draw.line(self.display, color, (x0, y0), (x1, y1))

    def fill_circle(self, x, y, r, color):
        pg.draw.circle(self.display, color, (x,y), r, 0) #if width is zero - it fill the circle


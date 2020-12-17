import pygame as pg
from utility.vector import Vector

POSITIONS = {
    "top left":         [0,   0],
    "top middle":       [-1,  0],
    "top right":        [-2,  0],
    "middle left":      [0,  -1],
    "center":           [-1, -1],
    "middle right":     [-2, -1],
    "bottom left":      [0,  -2],
    "bottom middle":    [-1, -2],
    "bottom right":     [-2, -2],
}


class View:

    window : pg.Surface
    screen_size = (800, 600) # filler values
    resolution = (800, 600)
    is_init = False

    @staticmethod
    def init( width=None, height=None ):
        if View.is_init:
            return 0
        View.is_init = True

        pg.mixer.pre_init(44100, -16, 2, 512)
        pg.mixer.init()
        pg.init()

        infoObject = pg.display.Info()
        View.screen_size = (infoObject.current_w, infoObject.current_h)

        if (width is None) and (height is None):
            View.resolution = View.screen_size
        else:
            View.resolution = (width, height)

        View.window = pg.display.set_mode(View.resolution, pg.RESIZABLE)

    @staticmethod
    def draw_circle(surf: pg.Surface,  pos:Vector, r, color, width=0):
        pg.draw.circle(surf, color, (round(pos.x),round(pos.y)), round(r), width) #if width is zero - it fills the circle

    @staticmethod
    def draw_line(surf: pg.Surface, r1:Vector, r2:Vector, color):
        pg.draw.line(surf, color, (round(r1.x), round(r1.y)), (round(r2.x), round(r2.y)))

    @staticmethod
    def draw_rect(surf: pg.Surface, r1:Vector, r2:Vector, color):
        pg.draw.rect(surf, color, pg.Rect((round(r1.x), round(r1.y)), (round(r2.x-r1.x), round(r2.y-r2.y))))

    @staticmethod
    def blit(surf_to: pg.Surface, surf_from: pg.Surface, position: Vector, position_type="top left"):
        """

        """
        surf_to.blit(surf_from,
                     (
                         round(position.x + POSITIONS[position_type][0]*surf_from.get_width()/2),
                         round(position.y + POSITIONS[position_type][1]*surf_from.get_height()/2)
                     ),)

    @staticmethod
    def update():
        pg.display.update()

    @staticmethod
    def toggle_fullscreen():
        if View.window.get_flags() & pg.FULLSCREEN:
            pg.display.set_mode(View.resolution)
        else:
            pg.display.set_mode(View.screen_size, pg.FULLSCREEN)

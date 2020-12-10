from controller import Controller
from event import Event

from model.dot import Dot
from model.heap import Heap
from model.wall import Wall

import pygame as pg

WHITE = (255, 255, 255)

WIDTH = 1200
HEIGHT = 800

FPS = 30

class TestController(Controller):

    def __init__(self):
        pg.init()
        screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()

        self.onclick = Event()
        self.onkey   = Event()

        self.view = View(screen)

        self.dots = [Dot(400, 600, 10), Dot(450, 450, 20), Dot(550, 450, 30), Dot(500, 550, 25)]

        self.player = Heap(self.dots, 500, 500, 1000, 0.5, 100)
        self.wall = Wall([Dot(200, 600, 0), Dot(300, 500, 0)])

        self.gameObjects = [*self.dots, self.player, self.wall]

        self.running = True

    def on_init(self)->bool:
        self.view.draw_rect(0, 0, 794, 1123, WHITE)
        return True

    def on_loop(self):
        self.player.step(0.00005 * FPS)

    def on_render(self):
        for elem in self.gameObjects:
            elem.display()
        self.view.update()

    def execute(self):

        if self.on_init() == False:
            self.running = False

        while (self.running):
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
            self.on_render()
            self.on_loop()

if __name__ == "__main__":

    app = TestController()
    app.execute()






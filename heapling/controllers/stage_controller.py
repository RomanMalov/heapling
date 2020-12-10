from controllers.controller import Controller

from model.scene import Scene

from view.view import View
import pygame as pg

from utility.vector import Vector


class StageController(Controller):

	scene: Scene

	def __init__(self):
		self.clock = pg.time.Clock()
		self.FPS = 30

		self.game_objects = []
		self.running = False


	def on_init(self):
		self.scene = Scene(Vector(0, 0), Vector(70,0), View.resolution[0], View.resolution[1])
		return True

	def on_render(self):
		View.blit(View.window, self.scene.display(), Vector(0,0), "top left")
		View.update()

	def on_loop(self):
		self.scene.step(0.001 * self.FPS)

	def run(self):
		self.running = True

		if not (self.on_init()):
			self.running = False

		while self.running:
			self.clock.tick(self.FPS)

			self.on_render()

			for event in pg.event.get():

				if event.type == pg.KEYDOWN:
					if event.key == pg.K_F10:
						View.toggle_fullscreen()

					if event.key == pg.K_SPACE:
						self.scene.heap_jump()

				if event.type == pg.QUIT:
					self.running = False


if __name__ == "__main__":
	pass
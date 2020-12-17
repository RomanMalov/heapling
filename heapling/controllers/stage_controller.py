from controllers.controller import Controller
from controllers.event import Event

from model.gui.image import Image
from model.scene import Scene
from model.gameobject import GameObject

from view.view import View
import pygame as pg

from utility.vector import Vector
from typing import List

import os

SOUND_ROOT = os.path.join("resources", "sounds")

class StageController(Controller):

	scene: Scene
	GAMEOVER_EVENT = pg.USEREVENT
	game_objects = List[GameObject]

	def __init__(self):
		self.clock = pg.time.Clock()
		self.FPS = 30

		self.game_objects = []
		self.running = False
		
		self.gameover_event = Event()


	def on_init(self):
		self.scene = Scene(Vector(0, 0), Vector(70,0), View.resolution[0], View.resolution[1])
		self.scene.start()
		self.game_objects.append(self.scene)

		gameover_image = Image(Vector(View.resolution)/2, "gameover.png", 0.5)
		sound = pg.mixer.Sound(os.path.join(SOUND_ROOT, "gameover.wav"))

		that = self
		def on_gameover_set():
			sound.play()
			self.game_objects.append(gameover_image)
			pg.time.set_timer(that.GAMEOVER_EVENT, 2000)
			that.scene.on_die = lambda : None
			pass

		def on_gameover_end():
			pg.time.set_timer(that.GAMEOVER_EVENT, 0)
			self.running = False

		self.gameover_event.addHandler(on_gameover_end)

		self.scene.on_die = on_gameover_set

		return True

	def on_render(self):
		for obj in self.game_objects:
			View.blit(View.window, obj.display(), obj.get_cords(), "top left")
		View.update()

	def on_loop(self):
		self.scene.step(1/self.FPS)

	def run(self):
		self.running = True

		if not (self.on_init()):
			self.running = False

		jump_sound = pg.mixer.Sound(os.path.join(SOUND_ROOT, "jump.wav"))

		while self.running:
			self.clock.tick(self.FPS)

			self.on_render()
			self.on_loop()

			for event in pg.event.get():

				if event.type == self.GAMEOVER_EVENT:
					self.gameover_event.throw()

				if event.type == pg.KEYDOWN:
					if event.key == pg.K_SPACE:
						jump_sound.play()
						self.scene.heap_jump()

					if event.key == pg.K_F10:
						View.toggle_fullscreen()

					if event.key == pg.K_ESCAPE:
						self.running = False

				if event.type == pg.QUIT:
					self.running = False


if __name__ == "__main__":
	pass
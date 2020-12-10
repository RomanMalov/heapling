from controllers.controller import Controller
from controllers.event import Event
from controllers.stage_controller import StageController

from model.gui.button import Button
from model.gui.image import Image

from view.view import View
import pygame as pg

from utility.vector import Vector

F10_KEY = 291


class StartController(Controller):

	def __init__(self, width=None, height=None):

		View.init(width, height)

		self.stage_controller = StageController()

		self.clock = pg.time.Clock()
		self.FPS = 30

		self.game_objects = []
		self.running = False

		self.click_event = Event()

	def on_init(self):

		self.game_objects.append((
			Image("title.png", 0.25),
			Vector(View.window.get_width() / 2, 200)
		))

		style = {"font-family": "SpaceInvaders", "font-size": 20}
		that = self

		pos1 = Vector(View.window.get_width() / 2, View.window.get_height() / 2 - 100)
		play_button = Button("Play the game", pos1, style)
		self.game_objects.append((play_button, pos1))

		def play_button_func(pos: Vector):
			if play_button.is_inside(pos):
				self.stage_controller.run()
				that.running = False

		self.click_event.addHandler(play_button_func)

		pos2 = Vector(View.window.get_width() / 2, View.window.get_height() / 2 + 100)
		self.game_objects.append((Button("Options", pos2, style), pos2))

		pos3 = Vector(View.window.get_width() / 2, View.window.get_height() / 2 + 300)
		quit_button = Button("Quit your hopeless actions", pos3, style)
		self.game_objects.append((quit_button, pos3))

		def quit_button_func(pos: Vector):
			if quit_button.is_inside(pos):
				that.running = False

		self.click_event.addHandler(quit_button_func)

		return True

	def on_loop(self):
		pass

	def on_render(self):
		View.update()
		View.window.fill(pg.Color("#FFFFFF"))
		for obj in self.game_objects:
			surface, position = obj[0].display(), obj[1]
			View.blit(View.window, surface, position, "center")

	def run(self):
		self.running = True

		if not(self.on_init()):
			self.running = False

		while self.running:
			self.clock.tick(self.FPS)

			self.on_render()
			self.on_loop()

			for event in pg.event.get():

				if event.type == pg.KEYDOWN:
					if event.key == F10_KEY:
						View.toggle_fullscreen()

				if event.type == pg.QUIT:
					self.running = False

				if event.type == pg.MOUSEBUTTONDOWN:
					self.click_event.throw((Vector(event.pos)))

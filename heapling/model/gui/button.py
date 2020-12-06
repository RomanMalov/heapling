from model.gameobject import GameObject
from utility.vector import Vector

import pygame as pg

import os


STYLE = {
	"font-size": 20,
	"font-family": "Arial",

	"color": "#000000",  # Black
	"background-color": "#FFFFFF",  # White

	"border": 2,  # px
	"border-color": "#000000",  # Black

	"padding": 5,
}


def font(font_family: str, font_size: int):
	try:
		print(os.path.join("resources", "fonts", font_family + ".ttf"))
		_font = pg.font.Font(os.path.join("resources", "fonts", font_family + ".ttf"), font_size)
		print("Found", font_family, font_size)
		return _font, font_family, font_size
	except FileNotFoundError:
		return pg.font.SysFont(STYLE["font-family"], font_size), STYLE["font-family"], font_size


class Button(GameObject):

	text: str
	position: Vector

	font: pg.font.Font

	style: dict

	def __init__(self, text: str, pos: Vector, style: dict):
		self.text = text
		self.position = pos

		self.style = STYLE.copy()
		for key in STYLE:
			if key in style:
				self.style[key] = style[key]

		self.font, self.style["font-family"], self.style["font-size"] = \
			font(self.style["font-family"], self.style["font-size"])

		self.surface = self.display()[0]

	def is_inside(self, pos: Vector) -> bool:
		dr = pos - self.position
		if (dr.x > 0) and (dr.y > 0) and (dr.x < self.surface.get_width()) and (dr.y < self.surface.get_height()):
			return True
		return False

	def on_click(self, pos: Vector):
		pass

	def display(self):
		print(pg.color.Color(self.style["color"]))
		text_surface = \
			self.font.render(self.text, True, pg.color.Color(self.style["color"]), pg.color.Color(self.style["background-color"]))
		box_surface = pg.Surface((
			text_surface.get_width() + 2 * self.style["border"] + 2 * self.style["padding"],
			text_surface.get_height() + 2 * self.style["border"] + 2 * self.style["padding"]
		))
		box_surface.fill(pg.color.Color(self.style["border-color"]))
		pg.draw.rect(
			box_surface,
			pg.color.Color(self.style["background-color"]),
			(self.style["border"], self.style["border"],
			box_surface.get_width() - 2 * self.style["border"],
			box_surface.get_height() - 2 * self.style["border"]
		))
		box_surface.blit(
			text_surface,
			(self.style["border"] + self.style["padding"], self.style["border"] + self.style["padding"]
		))
		return box_surface, self.position


if __name__ == "__main__":
	pg.font.init()

	font = font("SpaceInvaders", 20)
	print(font)
	print("Hm")

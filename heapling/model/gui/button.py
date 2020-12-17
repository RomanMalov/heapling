from model.gameobject import GameObject
from model.gui.text import Text

from utility.vector import Vector

import pygame as pg

from typing import Union, List, Tuple


STYLE = {
	"font-size": 20,
	"font-family": "Arial",

	"color": "#000000",  # Black
	"background-color": "#FFFFFF",  # White

	"border": 2,  # px
	"border-color": "#000000",  # Black

	"padding": 5,


}

SPACE_STYLE = {"font-family": "SpaceInvaders", "font-size": 20}

class Button(GameObject):

	text: Text
	position: Vector

	font: pg.font.Font

	style: dict

	def __init__(self, text: Union[str,Text], pos: Vector, style: dict):

		if isinstance(text,Text):
			self.text = text
		else:
			self.text = Text(text, Vector(0,0), style)

		self.position = pos

		self.style = STYLE.copy()
		for key in STYLE:
			if key in style:
				self.style[key] = style[key]

		self.surface = self._make_surface()

	def is_inside(self, pos: Vector) -> bool:
		dr = pos - self.position + Vector(self.surface.get_size())/2
		if (dr.x > 0) and (dr.y > 0) and (dr.x < self.surface.get_width()) and (dr.y < self.surface.get_height()):
			return True
		return False

	def on_click(self, pos: Vector):
		pass

	def get_cords(self) -> Vector:
		# print(Vector(self.surface.get_size))
		return self.position - Vector(self.surface.get_size())/2

	def display(self):
		return self._make_surface()

	# Private methods

	def _make_surface(self):

		text_surface = self.text.display()

		box_surface = pg.Surface((
			text_surface.get_width() + 2 * self.style["border"] + 2 * self.style["padding"],
			text_surface.get_height() + 2 * self.style["border"] + 2 * self.style["padding"]
		))

		box_surface.fill(pg.color.Color(self.style["border-color"]))

		pg.draw.rect(
			box_surface,
			pg.color.Color(self.style["background-color"]),
			(
				self.style["border"], self.style["border"],
				box_surface.get_width() - 2 * self.style["border"],
				box_surface.get_height() - 2 * self.style["border"]
			)
		)

		box_surface.blit(
			text_surface,
			(self.style["border"] + self.style["padding"], self.style["border"] + self.style["padding"])
		)

		return box_surface






if __name__ == "__main__":
	pg.font.init()

	font = font("SpaceInvaders", 20)
	print(font)
	print("Hm")

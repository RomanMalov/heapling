from model.gameobject import GameObject

from utility.vector import Vector

import pygame as pg
import os


class Text(GameObject):

	STYLE = {
		"font-size": 20,
		"font-family": "Arial",

		"color": "#000000",  # Black
		"background-color": "#FFFFFF",  # White
	}

	_style = STYLE.copy()

	# Поверхность, на которой находится текст
	_surface: pg.Surface
	_text: str
	_font: pg.font.Font

	def __init__(self, text, pos: Vector, style: dict):
		self._text = text
		self._position = pos

		for key in Text.STYLE:
			if key in style:
				self._style[key] = style[key]

		self._font = self._get_font()
		self._surface = self._make_surface()

	# Public methods

	def get_cords(self) -> Vector:
		return self._position - Vector(self._surface.get_size())/2

	def display(self) -> pg.Surface:
		return self._surface

	def set_text(self, text: str):
		self._text = text
		self._surface = self._make_surface()

	def set_style(self, style: dict):
		for key in style:
			if key in Text.STYLE:
				self._style[key] = style[key]
		self._surface = self._make_surface()

	# Private methods

	def _get_font(self):
		font_family, font_size = self._style["font-family"], self._style["font-size"]
		try:
			_font = pg.font.Font(os.path.join("resources", "fonts", font_family + ".ttf"), font_size)
			return _font
		except FileNotFoundError:
			return pg.font.SysFont(Text.STYLE["font-family"], font_size), Text.STYLE["font-family"], font_size

	def _make_surface(self) -> pg.Surface:
		return self._font.render(
			self._text, True,
			pg.color.Color(self._style["color"]),
			pg.color.Color(self._style["background-color"])
		)

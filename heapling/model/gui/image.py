from model.gameobject import GameObject
import pygame as pg
import os

from utility.vector import Vector

IMAGE_ROOT = os.path.join("resources", "images")



class Image(GameObject):

	image: pg.Surface

	def __init__(self, cords: Vector, path, size=None):
		"""
		cords : Position of center of the image
		"""
		self.image = pg.image.load(os.path.join(IMAGE_ROOT, path))
		if size is not None:
			if isinstance(size, float):
				self.image = pg.transform.scale(
					self.image, (
						round(self.image.get_width()  * size),
						round(self.image.get_height() * size),
					)
				)
			else:
				self.image = pg.transform.scale(self.image, size)
		self._coords = cords - Vector(self.image.get_size())/2

	def get_cords(self) -> Vector:
		return self._coords

	def display(self):
		return self.image

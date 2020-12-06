from model.gameobject import GameObject
import pygame as pg
import os


IMAGE_ROOT = os.path.join("resources", "images")



class Image(GameObject):

	image: pg.Surface

	def __init__(self, path, size=None):
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

	def display(self):
		return self.image

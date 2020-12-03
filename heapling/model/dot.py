import math, pygame
from model.physicalobject import PhysicalObject
from utility.vector import Vector


KEY = (0, 0, 0)
BLACK = (0, 0, 1)


class Dot(PhysicalObject):

	cords: Vector

	def __init__(self, cords: Vector, r):
		self.cords = cords
		self.r = r

	def display(self):
		surf = pygame.Surface((2 * self.r, 2 * self.r))
		surf.set_colorkey(KEY)
		pygame.draw.circle(surf, BLACK, (round(self.r), round(self.r)), round(self.r))
		return surf

	def dist(self, cords: Vector):
		return abs(self.cords - cords)

	def get_cords(self) -> Vector:
		return self.cords

	def get_r(self) -> float:
		return self.r

	def set_cords(self, cords: Vector):
		self.cords = cords

	def get_m(self):
		return self.r*self.r

	def get_I(self):
		return 1/2*self.get_m()*self.r**2

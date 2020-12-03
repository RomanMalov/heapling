import math, pygame
from model.physicalobject import PhysicalObject

KEY = (0, 0, 0)
BLACK = (0, 0, 1)
class Dot(PhysicalObject):
	def __init__(self, cords, r):
		self.cords = cords
		self.r = r

	def display(self):
		surf = pygame.Surface((2 * self.r, 2 * self.r))
		surf.set_colorkey(KEY)
		pygame.draw.circle(surf, BLACK, (round(self.r),round(self.r)), round(self.r))
		return surf

	def dist(self, cords):
		dx = self.cords[0] - cords[0]
		dy = self.cords[1] - cords[1]
		dist = math.pow(dx*dx+dy*dy, 1/2)
		return dist

	def get_cords(self):
		return self.cords

	def get_r(self):
		return self.r

	def set_cords(self, cords):
		self.cords = cords

	def get_m(self):
		return self.r*self.r

	def get_I(self):
		return 1/2*self.get_m()*self.r**2

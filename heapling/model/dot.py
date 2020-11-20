import math
from model.physicalobject import PhysicalObject

BLACK = (0, 0, 0)
class Dot(PhysicalObject):
	def __init__(self, x, y, r):
		self.x = x
		self.y = y
		self.r = r

	def display(self, view):
		view.fill_circle(self.x, self.y, self.r, BLACK)

	def r(self, x, y):
		dx = self.x - x
		dy = self.y - y
		return math.pow(dx*dx+dy*dy, 1/2)

#The main player class
import math
from model.physicalobject import PhysicalObject

class Heap(PhysicalObject):
	def __init__(self, dots, x, y, v, alpha, w):
		self.dots = dots
		self.x = x
		self.y = y
		self.v = v
		self.alpha = alpha
		self.w = w

	def display(self, view):
		for dot in self.dots:
			dot.display(view)

	def step(self, dt):
		self.x += dt*self.v*math.cos(self.alpha)
		self.y += dt*self.v*math.sin(self.alpha)
		for dot in self.dots:
			dot.x += dt*self.v*math.cos(self.alpha)
			dot.y += dt*self.v*math.sin(self.alpha)
			dot.x += dt*self.w*(dot.y - self.y)
			dot.y += dt*-self.w*(dot.x - self.x)

	def append(self, dot):
		self.dots.append(dot)

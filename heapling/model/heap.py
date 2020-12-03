#The main player class
import math, pygame
from model.physicalobject import PhysicalObject
from model.dot import Dot
from model.wall import Wall
from array import array

KEY = (0, 0, 0)
GRAV_ACCELERATION = 140
V_JUMP = (120, -200)
K = 0.994

class Heap(PhysicalObject):
	def __init__(self, dot, v, w):
		self.dots = [dot]
		self.cords = dot.get_cords()
		self.v = v
		self.w = w
		self.m = dot.get_r()**2

	def display(self):
		surf = pygame.Surface((2 * 500, 2 * 500))
		surf.set_colorkey(KEY)
		for dot in self.dots:
			dx = dot.get_cords()[0] - self.cords[0]
			dy = dot.get_cords()[1] - self.cords[1]
			surf.blit(dot.display(), (dx + surf.get_width()/2 - dot.r, dy+ surf.get_height()/2 - dot.r))
		return surf

	def jump(self):
		self.v = V_JUMP

	def step(self, DT):
		x = self.cords[0]; y = self.cords[1]

		x += self.v[0]*DT
		y += self.v[1]*DT
		self.w *= K

		for dot in self.dots:
			dot_x = dot.get_cords()[0]; dot_y = dot.get_cords()[1]

			dot_x += self.v[0]*DT
			dot_y += self.v[1]*DT
			dot_x += DT*self.w*(dot_y - y)
			dot_y += DT*-self.w*(dot_x - x)
			dot.set_cords((dot_x, dot_y))

		self.cords = (x, y)
		self.v = (self.v[0]*K, self.v[1]*K+DT*GRAV_ACCELERATION)

	def intersect(self, dot : Dot):
		for my_dot in self.dots:
			r = my_dot.get_r() + dot.get_r()
			if my_dot.dist(dot.get_cords()) < r - 5:
				self.append(dot)
				return True
		return False

	def collide(self, wall : Wall):
		points = wall.get_dots()
		for point in points:
			for dot in self.dots:
				if dot.dist(point) < dot.get_r():
					pass #текст

	def append(self, dot):
		dot_m = dot.get_m()
		x = (self.m*self.cords[0] + dot.get_m()*dot.get_cords()[0]) / (self.m+dot.get_m())
		y = (self.m*self.cords[1] + dot.get_m()*dot.get_cords()[1]) / (self.m+dot.get_m())

		self.cords = (x, y)
		P = (self.m * self.v[0], self.m * self.v[1])
		L = self.get_I()*self.w + dot.get_m()*(self.v[0]*(self.cords[1] - dot.get_cords()[1]) - self.v[1]*(self.cords[0] - dot.get_cords()[0]))
		self.dots.append(dot)
		self.m = self.m+dot.get_m()
		I = self.get_I()

		self.v = (P[0]/self.m, P[1]/self.m)
		self.w = L/I

	def get_cords(self):
		return self.cords

	def dist(self, cords):
		return self.dots[0].dist(cords)

	def get_I(self):
		I = 0
		for dot in self.dots:
			I += dot.get_m()*self.dist(dot.get_cords())**2+dot.get_I()
		return I
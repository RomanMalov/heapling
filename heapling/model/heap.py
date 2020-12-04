#The main player class
import math, pygame
from model.physicalobject import PhysicalObject
from model.dot import Dot
from model.wall import Wall
from array import array
from utility.vector import Vector

KEY = (0, 0, 0)
GRAV_ACCELERATION = 140
V_JUMP = Vector(120, -200)
K = 0.99


class Heap(PhysicalObject):

	v: Vector
	cords: Vector

	def __init__(self, dot: Dot, v: Vector, w):
		self.dots = [dot]
		self.cords = dot.get_cords()
		self.v = v
		self.w = w
		self.m = dot.get_r()**2

	def display(self):
		surf = pygame.Surface((2 * 500, 2 * 500))
		surf.set_colorkey(KEY)
		for dot in self.dots:
			dr = dot.get_cords() - self.cords
			surf.blit(dot.display(), (dr.x + surf.get_width()/2 - dot.r, dr.y+ surf.get_height()/2 - dot.r))
		return surf

	def jump(self):
		self.v = V_JUMP

	def step(self, dt):
		pos = self.cords + self.v * dt
		self.w *= K

		for dot in self.dots:

			dot_pos = dot.get_cords()
			dot_pos += self.v*dt

			dot_pos += Vector(dot_pos.y - pos.y, pos.x - dot_pos.x)*dt*self.w

			dot.set_cords(dot_pos)

		self.cords = pos
		self.v = self.v*K + Vector(0, GRAV_ACCELERATION)*dt

	def intersect(self, dot : Dot):
		for my_dot in self.dots:
			r = my_dot.get_r() + dot.get_r()
			if abs(my_dot.get_cords() - dot.get_cords()) < (r - 5):
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

		self.cords = (self.cords*self.m + dot.get_cords()*dot.get_m()) / float(self.m + dot.get_m())

		P = self.v * self.m
		L = self.get_I()*self.w + dot.get_m()*self.v.cross(self.cords-dot.get_cords())

		self.dots.append(dot)
		self.m += dot.get_m()
		I = self.get_I()

		self.v = P/self.m
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
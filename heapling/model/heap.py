#The main player class
import math, pygame
from model.physicalobject import PhysicalObject
from model.dot import Dot
from model.wall import Wall
from array import array
from utility.vector import Vector

KEY = (0, 0, 0)
GRAV_ACCELERATION = 200
V_JUMP = Vector(150, -200)
K = 0.99
MU = 0.9

FORCE_CONSTANT = 35e4
class Heap(PhysicalObject):

	v: Vector
	cords: Vector

	def __init__(self, dot: Dot, v: Vector, w):
		self.dots = [dot]
		self.cords = dot.get_cords()
		self.v = v
		self.w = w
		self.m = dot.get_r()**2
		self.r = dot.get_r()

	def display(self):
		surf = pygame.Surface((3 * self.r, 3 * self.r))
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
			dot_pos = Vector(pos.x + (dot_pos.x - pos.x)*math.cos(dt*self.w) - (dot_pos.y - pos.y)*math.sin(dt*self.w),
							 pos.y + (dot_pos.x - pos.x)*math.sin(dt*self.w) + (dot_pos.y - pos.y)*math.cos(dt*self.w))
			dot_pos += self.v*dt

			dot.set_cords(dot_pos)

		self.cords = pos
		self.v = self.v*K + Vector(0, GRAV_ACCELERATION)*dt

	def intersect(self, dot : Dot):
		if abs(dot.get_cords() - self.get_cords()) > self.r + dot.get_r():
			return False

		for my_dot in self.dots:
			r = my_dot.get_r() + dot.get_r()
			if abs(my_dot.get_cords() - dot.get_cords()) < (r - 5):
				self.append(dot)
				return True
		return False

	def collide(self, wall : Wall, dt):
		points = wall.get_dots()
		glob_moment = 0; glob_force = Vector(0,0)

		for point in points:
			if abs(point - self.get_cords()) > self.r:
				continue

			for dot in self.dots:

				dot_coords = dot.get_cords(); dot_force = Vector(0,0)
				l_2 = (point.x - dot_coords.x)**2 + (point.y - dot_coords.y)**2 + 0.01 #because of division by zero

				if l_2 < dot.get_r()**2:
					dot_force += FORCE_CONSTANT * (dot.get_r() - math.sqrt(l_2))/abs(dot_coords-point)*(dot_coords-point)

				dot_moment = (dot_coords - self.get_cords()).cross(dot_force)

				glob_force += dot_force
				glob_moment += dot_moment

		beta = glob_moment/self.get_I()
		a = glob_force/self.m
		self.v += a * dt
		self.w += beta * dt

	def append(self, dot):
		dot_m = dot.get_m()

		self.cords = (self.cords*self.m + dot.get_cords()*dot.get_m()) / float(self.m + dot.get_m())

		P = self.v * self.m
		L = self.get_I()*self.w + dot.get_m()*self.v.cross(self.cords-dot.get_cords())

		self.dots.append(dot)
		self.m += dot.get_m()
		I = self.get_I()
		max = 0
		for dot in self.dots:
			if abs(dot.get_cords() - self.cords) + dot.get_r() > max:
				max = abs(dot.get_cords() - self.cords) + dot.get_r()
		self.r = max

		self.v = P/self.m
		self.w = L/I

	def get_cords(self):
		return self.cords

	def get_r(self):
		return self.r

	def dist(self, cords):
		return self.dots[0].dist(cords)

	def get_I(self):
		I = 0
		for dot in self.dots:
			I += dot.get_m()*self.dist(dot.get_cords())**2+dot.get_I()
		return I
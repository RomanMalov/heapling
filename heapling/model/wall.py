from model.physicalobject import PhysicalObject
import random
from math import *
import pygame
KEY = (0, 0, 0)
BLACK = (0, 0, 1)
def plane_angle_and_length(a, b):
	'''
	it finds all I need for my program please DON'T TOUCH
	:param a:
	:param b:
	:return:
	'''
	if a!=b:
		x = b[0] - a[0]
		y = b[1] - a[1]
		l = sqrt(x ** 2 + y ** 2)
		return [(asin(y / l) if x >= 0 else (pi - asin(y / l))), l]
	else:
		return 0, 0
def iter(coord1, coord2, angle_and_length_list, full_length):
	'''
	creates new iteration between two points
	:param coord1:
	:param coord2:
	:param angle_and_length_list:
	:param full_length:
	:return:
	'''
	new_list = [coord1]
	angle0, length0 = plane_angle_and_length(coord1, coord2)
	for angle, length in angle_and_length_list:
		old_x, old_y = new_list[-1]
		new_length = length * (length0 / full_length)
		new_x = old_x + cos(angle + angle0) * new_length
		new_y = old_y + sin(angle + angle0) * new_length
		new_list.append([new_x, new_y])
	return new_list[:-1]

class Wall(PhysicalObject):
	def __init__(self, x, y, first_coords, last_coords, depth, number_dots):
		'''

		:param first_coords: coordinates of first point
		:param last_coords: coordinates of last point
		:param depth: number of fractal iterations
		:param number_dots: number of inner points of original poligonal chain
		'''

		self.first_coords = first_coords
		self.last_coords = last_coords
		self.number_dots = number_dots
		self.depth = depth
		self.variation1 = random.random()
		self.variation2 = random.random()

		self.time = 0
		self.dots = [[0,0]]
		self.x = x
		self.y = y
		self.width = abs(self.first_coords[0] - self.last_coords[0])
		self.height = abs(self.first_coords[0] - self.last_coords[0])

	def step(self, dt):
		self.time += dt
		iter_number = self.depth
		time = self.time
		initial_list = [[0, 0]]
		frequency = 2
		variation1 = self.variation1
		variation2 = self.variation2
		length = self.last_coords[0]-self.first_coords[0]
		vertex_number = self.number_dots
		l0 = length / (vertex_number + 1)
		for i in range(vertex_number):
			x = (l0) * sin(time * frequency) * cos(
				frequency * time * (variation1 * cos(sin(i * 2))) + i * 2 * pi / vertex_number) + l0 * (i + 1)
			y = (l0) * sin(frequency * time * (variation2 * cos(i + 3)) + i * 2 * pi / vertex_number)
			initial_list.append([x, y])
		initial_list.append([length, 0])
		initial_angle_and_length_list = []
		for i in range(vertex_number + 1):
			initial_angle_and_length_list.append(plane_angle_and_length(initial_list[i], initial_list[i + 1]))
		previous_list = initial_list
		for i in range(iter_number):
			new_list = []
			for k in range(len(previous_list) - 1):
				new_dots = iter(previous_list[k], previous_list[k + 1], initial_angle_and_length_list, length)
				for j in new_dots:
					new_list.append(j)
			previous_list = new_list
			previous_list.append([length, 0])
		self.dots = []
		for dots in previous_list:
			self.dots.append([dots[0]+self.first_coords[0], dots[1]+self.first_coords[1]])
		return previous_list

	def display(self):
		surf = pygame.Surface((4 * self.width, 4 * self.height))
		surf.set_colorkey(KEY)
		for i in range(len(self.dots) - 1):
			pygame.draw.line(surf, BLACK, (self.dots[i][0]+2*self.width, self.dots[i][1]+2*self.height), (self.dots[i + 1][0]+2*self.width, self.dots[i + 1][1]+2*self.height))
		return surf

	def get_dots(self): #КОСТЫЛЬ переделать
		return self.dots

	def get_cords(self):
		return (self.x, self.y)

if __name__ == '__main__':
	pass

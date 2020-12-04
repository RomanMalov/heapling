import pygame 
from random import randint, random
from model.gameobject import GameObject
from model.dot import Dot
from model.wall import Wall
from model.heap import Heap
from utility.vector import Vector

from typing import List

WHITE = (255, 255, 255)
WALLS_COUNT = 3
UPPER_WALL_Y = 250
LOWER_WALL_Y = 650
AMPLITUDE = 120


class Scene(GameObject):

	view_point: Vector
	objects: List[GameObject]

	def __init__(self, view_point: Vector, v: Vector, width, height):
		self.cords = Vector(0, 0)
		self.view_point = view_point
		self.v = v
		self.width = width
		self.height = height
		self.objects = []

	def append(self, object: GameObject):
		self.objects.append(object)

	def remove(self, object: GameObject):
		self.objects.remove(object)

	def step(self, dt):
		self.view_point = self.view_point + self.v * dt
		screen = pygame.Surface((self.width, self.height))
		pygame.draw.rect(screen, WHITE, (0, 0, 1500, 1000))
		heap = self.heap

		for object in self.objects:

			if isinstance(object, Dot):
				dot = object
				if heap.intersect(dot):
					self.remove(dot)
					self.append(self.gen_rnd_dot())

				if dot.get_cords().x<self.view_point.x-dot.get_r():
					self.remove(dot)
					self.append(self.gen_rnd_dot())

			if isinstance(object, Wall):
				wall = object
				heap_x_l = heap.get_cords().x - heap.get_r()
				heap_x_r = heap.get_cords().x + heap.get_r()
				wall_x_l = wall.get_cords().x
				wall_x_r = wall.get_cords().x + wall.width
				if 	(heap_x_l - wall_x_l) * (heap_x_l - wall_x_r) < 0 or (heap_x_r - wall_x_l) * (heap_x_r - wall_x_r) < 0 or heap_x_l - wall_x_l < 0 and heap_x_r - wall_x_r > 0:
					heap.collide(wall, dt)
				surface = wall.display()
				screen.blit(surface, (wall_x_l - self.view_point.x, wall.get_cords().y - round(wall.height/2) - self.view_point.y))
				if wall_x_r-self.view_point.x < 0:
					delta = round(self.width/(WALLS_COUNT-1))
					self.remove(wall)
					wall = Wall(Vector(self.walls_num//2*delta, wall.get_cords().y), Vector((self.walls_num//2 + 1)*delta, wall.get_cords().y), 3, 3, AMPLITUDE)
					self.append(wall)
					wall.step(random())
					self.walls_num += 1
			else:
				object.step(dt)
				surface = object.display()
				pos = object.get_cords() - self.view_point - Vector(surface.get_width(),surface.get_height())/2
				screen.blit(surface, (pos.x, pos.y))
			#pygame.draw.circle(screen, (0, 255, 0), (round(object.get_cords()[0]),round(object.get_cords()[1])), 10)
		return screen

	def start(self):
		delta = round(self.width/(WALLS_COUNT-1))
		up_walls = [Wall(Vector(i*delta, UPPER_WALL_Y), Vector((i+1)*delta, UPPER_WALL_Y+100), 3, 3, AMPLITUDE) for i in range(WALLS_COUNT)]
		down_walls = [Wall(Vector(i*delta, LOWER_WALL_Y), Vector((i+1)*delta, LOWER_WALL_Y+100), 3, 3, AMPLITUDE) for i in range(WALLS_COUNT)]
		self.walls_num = WALLS_COUNT*2

		self.heap = Heap(Dot(Vector(400, 500), 30), Vector(0, 0), 0)

		for wall in up_walls:
			wall.step(random()*10)
			self.append(wall)
		for wall in down_walls:
			wall.step(random()*10)
			self.append(wall)

		dots = [self.gen_rnd_dot() for i in range(5)]
		for dot in dots:
			self.append(dot)

		self.append(self.heap)

	def gen_rnd_dot(self):
		cords = Vector(randint(round(self.view_point.x+self.width/2), round(self.view_point.x+self.width)),
				randint(round(self.view_point.y), round(self.view_point.y+self.height)))
		dot = Dot(cords, randint(20, 60))
		for obj in self.objects:
			if isinstance(obj, Wall):
				wall = obj
				dot_x_l = dot.get_cords().x - dot.get_r()
				dot_x_r = dot.get_cords().x + dot.get_r()
				wall_x_l = wall.get_cords().x
				wall_x_r = wall.get_cords().x + wall.width
				if 	(dot_x_l - wall_x_l) * (dot_x_l - wall_x_r) < 0 or (dot_x_r - wall_x_l) * (dot_x_r - wall_x_r) < 0 or dot_x_l - wall_x_l < 0 and dot_x_r - wall_x_r > 0:
					if dot.collide(wall):
						return self.gen_rnd_dot()

		return dot
		

	def get_cords(self):
		return self.cords

	def heap_jump(self):
		self.heap.jump()
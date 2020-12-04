import pygame 
from random import randint
from model.gameobject import GameObject
from model.dot import Dot
from model.wall import Wall
from model.heap import Heap
from utility.vector import Vector

from typing import List

WHITE = (255, 255, 255)


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

		for object in self.objects:
			object.step(dt)

			if isinstance(object, Dot):
				dot = object
				if self.heap.intersect(dot):
					self.renew(dot)
				if dot.get_cords().x<self.view_point.x-dot.get_r():
					print("Foo")
					self.renew(dot)

			if isinstance(object, Wall) and self.heap.collide(object):
				pass

			surface = object.display()
			pos = object.get_cords() - self.view_point - Vector(surface.get_width(),surface.get_height())/2
			screen.blit(surface, (pos.x, pos.y))
			#pygame.draw.circle(screen, (0, 255, 0), (round(object.get_cords()[0]),round(object.get_cords()[1])), 10)

		return screen

	def start(self):
		dots = [Dot(Vector(700, 600), 15),
				Dot(Vector(750, 450), 20),
				Dot(Vector(850, 450), 30),
				Dot(Vector(850, 650), 25),
				Dot(Vector(800, 600), 15)]
		wall = Wall(0, 0, (500, 500), (1500, 900), 1, 2)
		wall.step(0.001)

		self.heap = Heap(Dot(Vector(400, 500), 20), Vector(0, 0), 0)

		for dot in dots:
			self.append(dot)

		self.append(self.heap)
		self.append(wall)

	def renew(self, dot):
		self.remove(dot)
		cords = Vector(randint(round(self.view_point.x+self.width/2), round(self.view_point.x+self.width)),
				randint(round(self.view_point.y), round(self.view_point.y+self.height)))
		dot = Dot(cords, dot.get_r())
		print(cords)
		self.append(dot)

	def get_cords(self):
		return self.cords

	def heap_jump(self):
		self.heap.jump()


		
import pygame 
from random import randint
from model.gameobject import GameObject
from model.dot import Dot
from model.wall import Wall
from model.heap import Heap

WHITE = (255, 255, 255)
class Scene(GameObject):
	def __init__(self, cords, start_point, v_x, width, height):
		self.cords = cords
		self.view_point = view_point
		self.v_x = v_x
		self.width = width
		self.height = height
		self.objects = []
		

	def __init__(self, view_point, v_x, width, height):
		self.cords = (0, 0)
		self.view_point = view_point
		self.v_x = v_x
		self.width = width
		self.height = height
		self.objects = []

	def append(self, object):
		self.objects.append(object)

	def remove(self, object):
		self.objects.remove(object)

	def step(self, DT):
		self.view_point = (self.view_point[0] + self.v_x * DT, self.view_point[1])
		screen = pygame.Surface((self.width, self.height))
		pygame.draw.rect(screen, WHITE, (0, 0, 1500, 1000))

		for object in self.objects:
			object.step(DT)

			if isinstance(object, Dot):
				dot = object
				if self.heap.intersect(dot):
					self.renew(dot)
				if dot.get_cords()[0]<self.view_point[0]-dot.get_r():
					self.renew(dot)

			if isinstance(object, Wall) and self.heap.collide(object):
				pass

			surface = object.display()
			x = object.get_cords()[0] - self.view_point[0] - surface.get_width()/2
			y = object.get_cords()[1] - self.view_point[1] - surface.get_height()/2
			screen.blit(surface, (x, y))
			#pygame.draw.circle(screen, (0, 255, 0), (round(object.get_cords()[0]),round(object.get_cords()[1])), 10)

		return screen

	def start(self):
		dots = [Dot((700, 600), 15), Dot((750, 450), 20), Dot((850, 450), 30), Dot((850, 650), 25), Dot((800, 600), 15)]
		wall = Wall(0, 0, (0, 900), (2700, 900), 4, 3)
		wall.step(0.001)

		self.heap = Heap(Dot((400, 500), 20), (0, 0), 0)

		for dot in dots:
			self.append(dot)

		self.append(self.heap)
		self.append(wall)

	def renew(self, dot):
		self.remove(dot)
		cords = (randint(round(self.view_point[0]), round(self.view_point[0]+self.width)), 
				randint(round(self.view_point[1]), round(self.view_point[1]+self.height)))
		dot = Dot(cords, dot.get_r())
		self.append(dot)

	def get_cords(self):
		return self.cords

	def heap_jump(self):
		self.heap.jump()


		
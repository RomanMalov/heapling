#Base game object
from utility.vector import Vector


class GameObject:

	def display(self):
		pass

	def step(self, dt):
		pass

	def get_cords(self) -> Vector:
		pass

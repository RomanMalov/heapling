from model.physicalobject import PhysicalObject

BLACK = (0, 0, 0)

class Wall(PhysicalObject):
	def __init__(self, dots):
		self.dots = dots

	def display(self, view):
		for i in range(len(self.dots)-1):
			view.draw_line(self.dots[i].x, self.dots[i].y,\
				self.dots[i+1].x, self.dots[i+1].y, BLACK)


import numpy

OPERATIONS = {
	"add": numpy.add,
	"sub": numpy.subtract,
	"mul": numpy.multiply,
	"dot": numpy.dot,
	"abs": numpy.linalg.norm
}


class Vector:
	DIMENSIONS = 2

	def __init__(self, *args):
		self._vector = numpy.zeros(Vector.DIMENSIONS, dtype=float)

		if len(args) == Vector.DIMENSIONS:
			# Assume it's three numbers
			for i in range(0, Vector.DIMENSIONS):
				self._vector[i] = args[i]

		else:
			# Assume the first arg is iterable
			try:
				it = iter(args[0])
				for i in range(0, Vector.DIMENSIONS):
					self._vector[i] = next(it)
			except TypeError:
				pass

	@property
	def x(self):
		return self._vector[0]

	@property
	def y(self):
		return self._vector[1]

	@x.setter
	def x(self, x):
		self._vector[0] = x

	@y.setter
	def y(self, y):
		self._vector[1] = y

	def __str__(self):
		return "Vector"+self._vector.__str__()

	def __getitem__(self, item):
		return self._vector[item]

	# noinspection PyTypeChecker
	def _apply_operation(self, operation, value=None):
		if isinstance(value, type(self)):
			result = OPERATIONS[operation](self._vector, value._vector)
		elif value is not None:
			result = OPERATIONS[operation](self._vector, value)
		else:
			result = OPERATIONS[operation](self._vector)
		return result

	# vector methods

	def __add__(self, other):
		return Vector(self._apply_operation("add", other))

	def __sub__(self, other):
		return Vector(self._apply_operation("sub", other))

	def __mul__(self, other):
		return Vector(self._apply_operation("mul", other))

	def __rmul__(self, other):
		return Vector(self._apply_operation("mul", other))

	def __truediv__(self, other):
		# works for scalars
		return Vector(self._vector / other)

	def __abs__(self):
		return self._apply_operation("abs")

	def dot(self, other) -> float:
		return self._apply_operation("dot", other)

	def cross(self, other) -> float:
		v1 = [*self._vector, 0]
		v2 = [*other._vector, 0]

		result = numpy.cross(v1, v2)
		return result[2]


if __name__ == "__main__":
	v1 = Vector(300, 100)
	print(v1)

	v2 = Vector((1, 2))
	print(v2)

	print(*v1)

	print(v2 * 2)
	print(v2 / 2)

	print("Magnitude of v1 : " + str(abs(v1)))
	print(abs(v2))

	print(v1 + v2)

	print(v1)
	print(v2)

	print(v1 - v2)

	print(v1 * v2)

	print("Cross product : " + str(v1.cross(v2)))

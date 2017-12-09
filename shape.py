#
# This is an example of inheritance and factory class
#

class Shape(object):

	def draw(self):
		raise Exception('Cannot draw an abstract shape')


class Rectangle(Shape):

	def draw(self):
		print('drawing a rectangle')


class Circle(Shape):

	def draw(self):
		print('drawing a circle')


class ShapeFactory(object):

	def __init__(self):
		self.shapes = {}

	def register(self, name, shape_class):
		self.shapes[name] = shape_class

	def create(self, name):
		if name in self.shapes:
			return self.shapes[name]()
		else:
			raise Exception('Cannot create shape: {}'.format(name))


if __name__ == '__main__':
	factory = ShapeFactory()
	factory.register('Rectangle', Rectangle)
	factory.register('Circle', Circle)

	factory.create('Rectangle').draw()
	factory.create('Circle').draw()
	factory.create('Triangle').draw()
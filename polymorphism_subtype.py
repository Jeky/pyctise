#
# Subtyping, or inheritance, is the most famous thing in OO. However, it is not suggested to use it widely since it is too heavy in designing.
#


class Shape(object):
    
    def draw(self):
        print('Cannot draw an abstract shape')


class Rectangle(Shape):

    def draw(self):
        print('Drawing a Rectangle')


class Circle(Shape):

    def draw(self):
        print('Drawing a Circle')


if __name__ == '__main__':
    shapes = [Rectangle(), Circle()]
    for s in shapes:
        s.draw()
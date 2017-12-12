#
# A full example of dynamic class
#
from types import MethodType


class DynamicClass(object):

    def __init__(self, property_dict):
        for k, v in property_dict.items():
            if callable(v):
                setattr(self, k, MethodType(v, self))
            else:
                setattr(self, k, v)


if __name__ == '__main__':
    def point_norm(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def point_print(self):
        print('({}, {})'.format(self.x, self.y))

    def point_move(self, x, y):
        self.x += x
        self.y += y


    p = DynamicClass({'x':1, 'y':2, 'print': point_print,
                      'norm': point_norm, 'move': point_move})

    p.print()
    print(p.norm())

    p.move(1, 1)
    p.print()
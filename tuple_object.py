#
# In Python you can define a class (a named tuple) without using class keyword
#
from collections import namedtuple


def create_class(name, *property_list):
    return namedtuple(name, property_list)


if __name__ == '__main__':
    Point = create_class('Point', 'x', 'y')
    # create an instance of Point
    p = Point(1, 2)
    print('p = ({}, {})'.format(p.x, p.y))
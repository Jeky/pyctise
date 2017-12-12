#
# You can add methods to a class dynamically.
#
from types import MethodType

class Person(object):

    def __init__(self, name):
        self.name = name


def fly(self):
    print('{} is flying'.format(self.name))


if __name__ == '__main__':
    bird_man = Person('bird man')
    bird_man.fly = MethodType(fly, bird_man)
    bird_man.fly()

    p = Person('normal man')
    try:
        p.fly()
    except Exception as e:
        print('p cannot fly')
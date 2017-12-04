#
# Although Python is trying to support Generic (https://en.wikipedia.org/wiki/Generic_programming), my suggestion is to use generic as type checking instead of templating.
# In Python (or similar languages), it is better to use duck typing (https://en.wikipedia.org/wiki/Duck_typing).
#

class Sparrow:

    def fly(self):
        print("Sparrow flying")

class Airplane:

    def fly(self):
        print("Airplane flying")


def lift_off(item):
    # Type doesn't matter here. All we need is this item having a fly() method.
    item.fly()


if __name__ == '__main__':
    fly_items = [Sparrow(), Airplane()]
    for item in fly_items:
        lift_off(item)
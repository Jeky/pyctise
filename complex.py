#
# OO example with magic methods. (see http://www.diveintopython3.net/special-method-names.html)
# For definition of Complex number, see: https://en.wikipedia.org/wiki/Complex_number
# This is an immutable example as well.
#

# dummy class to first register Complex as a type
class Complex(object):
    pass


class Complex(object): # always use new style instead of old style
    
    def __init__(self, real: float = 0.0, image: float = 0.0):
        self.real = real
        self.image = image

    def __add__(self, other: Complex) -> Complex:
        """ will be invoked for '+'
        """
        return Complex(self.real + other.real, self.image + other.image)

    def __sub__(self, other: Complex) -> Complex:
        """ will be invoked for '-'
        """
        return Complex(self.real - other.real, self.image - other.image)

    def __mul__(self, other: Complex) -> Complex:
        """ will be invoked for '*'
        """
        real = self.real * other.real - self.image * other.image
        image = self.real * other.image + self.image * other.real
        return Complex(real, image)

    def __truediv__(self, other: Complex) -> Complex:
        """ will be invoked for '/'
        """
        real = (self.real * other.real + self.image * other.image) / (other.real ** 2 + other.image ** 2)
        image = (self.image * other.real - self.real * other.image) / (other.real ** 2 + other.image ** 2)
        return Complex(real, image)

    def __floordiv__(self, other: Complex) -> Complex:
        """ will be invoked for '//'
        """
        return self.__truediv__(other)

    def __str__(self):
        """ will be invoked when printing
        """
        return '({} + {}i)'.format(self.real, self.image)


if __name__ == '__main__':
    a = Complex(1, 2)
    b = Complex(3, 4)

    print(a, '+', b, '=', a + b)
    print(a, '-', b, '=', a - b)
    print(a, '*', b, '=', a * b)
    print(a, '/', b, '=', a / b)
    print(a, '//', b, '=', a // b)
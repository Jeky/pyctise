#
# 3 classic functional programming operations: reduce
# It takes a list and a function, then tries to apply function to all the element pairs
#

from typing import Callable


def list_reduce(lst: list, func: Callable, initializer: object = None) -> object:
    if len(lst) == 0:
        return None

    if initializer == None:
        return list_reduce(lst[1:], func, lst[0])

    result = initializer
    for item in lst:
        result = func(result, item)

    return result


def add(num1: int, num2: int) -> int:
    return num1 + num2


def mul(num1: int, num2: int) -> int:
    return num1 * num2


if __name__ == '__main__':
    print(list_reduce([1, 2, 3], add))
    print(list_reduce([1, 2, 3], mul, 0))
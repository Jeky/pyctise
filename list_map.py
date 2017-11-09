#
# 3 classic functional programming operations: map
# It takes a list and a function, then applies this function to all the elements to the list
#

from typing import Callable


def list_map(lst: list, func: Callable) -> list:
    return [func(item) for item in lst]
    # Equals To
    # mapped_list = []
    # for item in lst:
    #     mapped_list.append(func(item))
    #
    # return mapped_list


def square(num: float) -> float:
    return num ** 2


if __name__ == '__main__':
    print(list_map([1, 2, 3], square))
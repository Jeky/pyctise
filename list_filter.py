#
# 3 classic functional programming operations: filter
# It takes a list and a function. 
# For each element in the list, it will be excluded if filter function return false
#

from typing import Callable


def list_filter(lst: list, func: Callable) -> list:
    return [item for item in lst if func(item)]
    # Equals To:
    #
    # filtered_list = []
    # for item in lst:
    #     if func(item):
    #         filtered_list.append(item)
    # return item


def is_even(num: int) -> bool:
    return num % 2 == 0


if __name__ == '__main__':
    print(list_filter([1, 2, 3, 4, 5], is_even))
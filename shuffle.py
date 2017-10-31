#
# Fisher–Yates shuffle algorithm
#
import random


def shuffle(lst: list) -> None:
    """Shuffle the target list
    """
    # From size - 1 to 0
    for i in range(len(lst) - 1, 0, -1):
        # randint(a, b) will return n such that a <= n <= b
        j = random.randint(0, i)
        # swap
        lst[i], lst[j] = lst[j], lst[i]


def gen_list(size: int) -> list:
    """Generate a list containing 0 to size - 1
    """
    return list(range(size))


if __name__ == '__main__':
    lst = gen_list(10)
    print(lst)
    shuffle(lst)
    print(lst)

#
# Reverse version of keyword in
#

from get_len import cdr
from reverse import car


def has_member(lst: list, target: object) -> bool:
    """Check if target is one member of the list
    """
    if not lst:
        return False
    elif car(lst) == target:
        return True
    else:
        return has_member(cdr(lst), target)


if __name__ == '__main__':
    print(has_member([], 1))
    print(has_member([1, 2, 3], 1))
    print(has_member([1, 2, 3], 4))
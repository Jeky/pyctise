#
# Recursive version of reverse()
#

from get_len import cdr


def car(lst: list) -> object:
    """ Another old name from LISP. 
        This function will return the first element of a list.
    """
    return lst[0]


def reverse(lst: list) -> list:
    """ Reverse a list
    """
    if lst:
        return reverse(cdr(lst)) + [car(lst)]
    else:
        return lst


if __name__ == '__main__':
    print(reverse([]))
    print(reverse([1, 2, 3]))
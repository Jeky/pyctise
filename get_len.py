#
# len() can be used to get the length of a list. Now we are trying to write a recurrsive len() function to get length
#

def cdr(lst: list) -> list:
    """ This old name comes from LISP (see: https://en.wikipedia.org/wiki/CAR_and_CDR)
        cdr will return the rest of a list without first element.
    """
    return lst[1:]


def list_len(lst: list) -> int:
    """ Get the length of list using recurrsion.
    """
    if lst:
        return 1 + list_len(cdr(lst))
    else:
        return 0


if __name__ == '__main__':
    print(list_len([]))
    print(list_len([1, 2, 3]))
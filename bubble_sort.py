#
# Simply sorting function that compares each pair of adjacent items and swaps them if they are in the wrong order
#
from shuffle import shuffle, gen_list


def bubble_sort(lst: list) -> None:
    """Sort list with bubble sorting algorithm
    """
    for i in range(len(lst)):
        for j in range(len(lst) - 1):
            if lst[j] > lst[j + 1]:
                # swap
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


if __name__ == '__main__':
    lst = gen_list(20)
    print('Generate List:', lst)
    shuffle(lst)
    print('Shuffled List:', lst)
    bubble_sort(lst)
    print('Sorted List:  ', lst)
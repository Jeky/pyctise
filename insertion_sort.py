#
# Insertion sorting algorithm
#

from shuffle import gen_list, shuffle


def insertion_sort(lst: list):
    """Insertion sorting algorithm
    """
    for i in range(1, len(lst)):
        current = lst[i]
        current_index = i - 1

        while (current_index >= 0) and (lst[current_index] > current):
            lst[current_index+1] = lst[current_index]
            current_index = current_index - 1

        lst[current_index+1] = current


if __name__ == '__main__':
    lst = gen_list(20)
    print('Generate List:', lst)
    shuffle(lst)
    print('Shuffled List:', lst)
    insertion_sort(lst)
    print('Sorted List:  ', lst)

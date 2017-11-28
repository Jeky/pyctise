#
# Generate all possible strings based on characters
# INPUT: ['a', 'b'], 2
# OUTPUT: ['aa', 'ab', 'ba', 'bb']
#
from typing import List
from pprint import pprint


def to_index(num, base, length):
    index = [0] * length
    i = -1
    while num != 0:
        index[i] = num % base
        num = num // base
        i -= 1

    return index


def generate_all_possible_strings(chars: List[str], length: int) -> List[str]:
    """ Generate all possible strings based on characters
    """
    count = len(chars) ** length
    generated = []
    for num in range(count):
        index_list = to_index(num, len(chars), length)
        generated.append(''.join([chars[i] for i in index_list]))

    return generated


if __name__ == '__main__':
    pprint(generate_all_possible_strings(['A', 'B', 'C'], 3))
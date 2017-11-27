#
# Generate all the permutations of a list
# There are several better algorithms: https://en.wikipedia.org/wiki/Heap%27s_algorithm or https://en.wikipedia.org/wiki/Steinhaus%E2%80%93Johnson%E2%80%93Trotter_algorithm
#
from typing import List
from pprint import pprint


def gen_permutation(lst: List[str]) -> List[List[str]]:
    """ Generate all the permutations
    """
    if len(lst) == 1:
        return [lst]

    perms = []
    for i in lst:
        # generate a list without element i
        copied = [item for item in lst if item != i]
        for sub_perm in gen_permutation(copied):
            # merge i and generated sub permutation list together
            perms.append([i] + sub_perm)

    return perms


if __name__ == '__main__':
    pprint(gen_permutation(['a', 'b', 'c', 'd']))    

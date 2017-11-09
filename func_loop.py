#
# Functions can also be stored in a list
#
import random


def decorate_str(seed: str) -> str:
    """Decorate string with '-' surrounded
    """
    return '-' + seed + '-'


def trim_str(seed: str) -> str:
    """Trim string
    """
    return seed.strip()


def gen_random_prefix(seed: str) -> str:
    """Generate a random prefix
    """
    return random.choice(['a', 'b', 'c']) + seed


def construct_complicated_str(seed: str) -> str:
    """Construct a compliated string based on seed
    """
    # try to add some other functions to this list
    funcs = [trim_str, decorate_str, gen_random_prefix, decorate_str, gen_random_prefix, decorate_str]
    generated = seed

    for func in funcs:
        generated = func(generated)

    return generated


if __name__ == '__main__':
    print(construct_complicated_str('hello!'))
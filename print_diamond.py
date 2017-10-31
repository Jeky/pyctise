#
# Print out a diamond.
#
import math

SPACE = ' '


def print_diamond(size: int, fill: bool, char_to_use: str):
    """Print out a diamond.
    Parameters: 
        size: the size of this diamond (size should always be odd number)
        fill: whether or not filling this diamond
        char_to_use: the character to be used to draw this diamond
    """
    if size % 2 == 0:
        print('Size should be an odd number')
        return

    r = int((size - 1) / 2)
    origin_x = r
    origin_y = r

    for i in range(size):
        for j in range(size):
            x = j - origin_x
            y = i - origin_y
            if math.fabs(x) + math.fabs(y) == r:            # print border
                print(char_to_use, end='')
            elif math.fabs(x) + math.fabs(y) < r and fill:  # fill in diamond
                print(char_to_use, end='')
            else:                                           # empty space
                print(SPACE, end='')
        # print a new line
        print()


if __name__ == '__main__':
    print_diamond(21, True, '*')
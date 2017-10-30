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

    origin_point = ((size - 1) / 2, (size - 1) / 2)

    for i in range(size):
        for j in range(size):
            x = j - origin_point[1]
            y = i - origin_point[0]
            
            if math.ceil((i + j) ** 0.5) == (size - 1) / 2:
                print(char_to_use, end='')
            else:
                print(SPACE, end='')
        print('')


if __name__ == '__main__':
    print_diamond(5, True, '*')
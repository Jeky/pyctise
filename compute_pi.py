#
# A Monte Carlo method to compute PI.
# You can tell how slow a python program is....
#
import random
import math

def compute_pi(iteration_count: int) -> float:
    """compute the real value of PI
    In this algorithm, we first define two shapes:
        * circle = { center = (0, 0), radius = 1 } 
        * square = { vertex = {(1,1), (-1,1), (1,-1), (-1,-1)} }
    These two shapes will be mentioned in the following code.
    """
    hit = 0
    for i in range(iteration_count):
        # generate random float numbers from [-1, 1] using uniform distribution (every float number will appear by the same chance)
        # all the generated (x, y) will hit the square
        x = random.uniform(-1, 1)  
        y = random.uniform(-1, 1)
        # compute the distance from (x, y) to (0, 0)
        # if distance < radius, it hits the circle
        if math.sqrt(x ** 2 + y ** 2) <= 1:
            hit += 1

    # The probability of (x, y) hitting the circle is:
    #       (Area of circle) / (Area of square) = (PI * 1^2) / (2 * 2) = PI / 4
    # and   hit / iteration_count = PI / 4
    # so    PI = hit / iteration_count * 4

    return hit / iteration_count * 4


if __name__ == '__main__':
    print('This will take several minutes...')
    for i in range(5):
        iteration_count = 10 ** i * 10000
        computed_pi = compute_pi(iteration_count)
        print('Computing PI with iteration =', iteration_count)
        print('PI =', computed_pi)
        print('Accuracy =', math.fabs(computed_pi - math.pi) / math.pi)

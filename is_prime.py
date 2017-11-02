#
# Check if the given number is prime
#
import random

def is_prime(num: int) -> bool:
    """Check if the given number is prime
    """
    if num % 2 == 0:
        return False

    for i in range(3, int(num ** 0.5), 2):
        if num % i == 0:
            return False
    return True

if __name__ == '__main__':
    for i in range(100):
        num = random.randint(2, 10000000)
        print('{} : {}'.format(num, is_prime(num)))
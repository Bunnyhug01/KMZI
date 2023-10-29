from math import ceil
from math import sqrt


def isPrime(mod: int) -> bool: 
    if 2 == mod:
        return True

    for p in range(2, int(ceil(sqrt(mod + 0.1)) + 1)):
        if mod % p == 0:
            return False
    return True
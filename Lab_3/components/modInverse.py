from .euclidean_gcdex import euclidean_gcdex
from .euclidean_gcd import euclidean_gcd
from .phi import phi


def modInverse(a, m):
    g, x, _ = euclidean_gcdex(a, m)

    if g != 1:
        return None
    else:
        x = (x % m + m) % m
    return x


def inverse(a, m):
    return modInverse(a ** (phi(m) - 1), m)


def ring(m):
    return list(filter(lambda x: euclidean_gcd(x, m) == 1, range(1, m)))
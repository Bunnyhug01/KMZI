from .powMod import powMod
from .inverse import inverse


def findX(g, p, y):
    for x in range(2, p - 1):
        yp = powMod(g, x, p)
        if yp == y:
            return x


def decryptElgamal(w, Ock, y, p, g):
    x = findX(g, p, y)
    return (w * inverse(powMod(Ock, x, p), p)) % p
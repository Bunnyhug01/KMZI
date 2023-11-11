from .powMod import powMod
from .phi import phi


def inverse(a, m):
    return powMod(a, phi(m) - 1, m)
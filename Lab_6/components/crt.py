from .powMod import powMod


def crt(w, e, p, q):
    return powMod(w, e, p * q)
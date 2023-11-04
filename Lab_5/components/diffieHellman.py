from .powMod import powMod


def diffieHellman(a, b, alpha, p):
    A = powMod(alpha, a, p) # Alice's open key
    B = powMod(alpha, b, p) # Bob's open key
    
    keyA = powMod(B, a, p) # Alice's secret key
    keyB = powMod(A, b, p) # Bob's secret key
    
    return A, B, keyA, keyB
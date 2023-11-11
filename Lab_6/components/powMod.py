def powMod(a, b, p):
    res = 1
    while b:
        if b & 1:
            res = int(res * a % p)
            b -= 1
        else:
            a = int(a * a % p)
            b >>= 1
    return res
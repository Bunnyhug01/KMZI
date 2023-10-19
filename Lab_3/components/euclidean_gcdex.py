def euclidean_gcdex(a, b):
    if b == 0:
        return (a, 1, 0)
    g, x, y = euclidean_gcdex(b, a % b)
    return (g, y - (a // b) * x, x)
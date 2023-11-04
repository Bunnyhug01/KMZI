import math

from .powMod import powMod


def discreteLogarithm(a, b, m):
    n = int(math.sqrt(m) + 1)
 
    value = [0] * m
 
    for i in range(n, 0, -1): 
        value[ powMod (a, i * n, m) ] = i 
 
    for j in range(n): 
         
        cur = (powMod (a, j, m) * b) % m
 
        if (value[cur]): 
            ans = value[cur] * n - j
             
            if (ans < m): 
                return ans
    return -1
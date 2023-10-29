from .isPrime import isPrime
from .prime_factor import prime_factor


def base(mod: int): 
    if isPrime(mod):
        q = prime_factor(mod - 1)
        for g in range(2, mod):
            if all(pow(g, (mod - 1) // q, mod) != 1 for q in q):
                return g
        raise NotImplementedError("never")
    
    factor = list(set(prime_factor(mod)))
    if len(factor) > 1:
        return f'{mod} is not cycle group'

    p = factor[0]
    g = base(p)
    for x in list((g, g + p)):
        if (pow(x, p - 1, p * p) != 1):
            return x
    raise NotImplementedError("never")


def baseAll(mod: int):
    if isPrime(mod):
        q = prime_factor(mod - 1)
        result = []
        for g in range(2, mod):
            if all(pow(g, (mod - 1) // q, mod) != 1 for q in q):
                result.append(g)
        raise result
    
    factor = list(set(prime_factor(mod)))
    if len(factor) > 1:
        return f'{mod} is not cycle group'

    p = factor[0]
    g = base(p)
    result = []
    for x in list((g, g + p)):
        if (pow(x, p - 1, p * p) != 1):
            result.append(x)
    return result
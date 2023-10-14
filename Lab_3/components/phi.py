from .prime_factor import prime_factor

def phi(number):
    result = number
    factor = set(prime_factor(number))
    
    for el in factor:
        result *= 1 - 1 / el

    return int(result)
from components.phi import phi
from components.prime_factor import prime_factor, gcd
from components.euclidean_gcd import euclidean_gcd
from components.euclidean_gcdex import euclidean_gcdex
from components.modInverse import inverse, ring

def menu():
    m = 7672333
    n = 48685811

    print(f'Prime factor:\n 1. m {prime_factor(m)} \n 2. n {prime_factor(n)}')
    print(f'GCD: {euclidean_gcd(m, n)}\nGCD Prime factor {gcd(m, n)}\nGCD Extended {euclidean_gcdex(m, n)}')
    
    k = 13
    n = 18
    m = 2001
    
    print(f'Phi:\n 1. m {phi(m)} \n 2. n {phi(n)} \n 3. k {phi(k)}')
    print(f'Z/kZ: {ring(k)}\nZ/nZ: {ring(n)}')
    
    for i in [5, 6, 7]:
        inv = inverse(i, m)
        if inv == None:
            print(f'{i}: No solution')
        else:
            print(f'{i} * {inv} === 1 (mod {m})')


if __name__ == "__main__":
    menu()
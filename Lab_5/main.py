import random

from components.diffieHellman import diffieHellman
from components.discreteLogarithm import discreteLogarithm


def menu():
    
    alpha = 7
    p = 134041249
    
    a = random.randint(0, 134041248)
    b = random.randint(0, 134041248)

    
    print(f"Alice's private key: {a}\nBob's private key: {b}\n")
    
    A, B, keyA, keyB = diffieHellman(a, b, alpha, p)
    
    print(f"Alice's open key: {A}\nBob's open key: {B}\n")
    print(f"Alice's secret key: {keyA}\nBob's secret key: {keyB}\n")
    
    print(f"Discrete Logarithm keys:\n Alice's key {discreteLogarithm(alpha, A, p)}\n Bob's key {discreteLogarithm(alpha, B, p)}")

        
if __name__ == "__main__":
    menu()
from components.decryptElgamal import decryptElgamal
from components.crt import crt


def menu():
    w = 160936054
    Ock = 144946434
    y = 57348448
    p = 206181067
    g = 7
    
    print(f'Decrypted Elgamal: {decryptElgamal(w, Ock, y, p, g)}')
    
    w = 2428010006080722311
    p = 2038074743
    q = 2038074751
    e = 1299709
    
    print(f'CRT X: {crt(w, e, p, q)}')

        
if __name__ == "__main__":
    menu()
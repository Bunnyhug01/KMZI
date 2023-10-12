import random

from components.clear import clear
from components.saveToFile import save
from components.crypto import encrypt
from components.generator import Random
from components.ceaser_cipher import ceaser_cipher, ceaser_decrypt


def main_menu():
    random_value = None
    generator = Random()

    while(True):
        try:
            clear()
            choice:int = int(input('Choose a variant:\n1.Random from 0.0 to 1.0\n2.Random with user diapason\n3.Encrypt\n4.Generator\n5.Encrypt(Ceaser)\n6.Decrypt(Ceaser)\n7.Exit\n'))
            clear()
            
            if choice == 1:
                random_value = random.random()
            elif choice == 2:
                print('Enter the start and the end of the diapason:\n')

                start, end = input().split()
                random_value = random.randrange(int(start), int(end))
            elif choice == 3:
                string = input('Enter a string:\n')
                random_value = encrypt(string)
            elif choice == 4:
                random_value = generator.next()
            elif choice == 5:
                string:str = input('Enter text:\n')
                literal_key:str = input('Enter a key (number or letter):\n')
                print(ceaser_cipher(string, literal_key))
                input()
            elif choice == 6:
                string:str = input('Enter text:\n')
                clear()
                print(ceaser_decrypt(string))
                input()
            elif choice == 7:
                break
            else:
                continue
            
            clear()
            if (random_value != None):
                print(random_value)

                save(str(random_value), 'output.txt', 'w')
                input('')
                random_value = None

        except TypeError:
            print('Wrong value!')


if __name__ == "__main__":
    main_menu()
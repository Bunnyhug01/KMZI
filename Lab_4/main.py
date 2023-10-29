from components.random_substitution import random_substitution
from components.base import base, baseAll
from components.group import group
from components.cycles import cycles


def menu():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    rand_shuffled = random_substitution(array)
    
    print(f'Random Substitution:\n{rand_shuffled[0]}\n{rand_shuffled[1]}')

    f = [4, 7, 3, 6, 2, 5, 1]
    print(f'Cycles: {cycles(f)}')
    
    m = 32460
    print('Group:')
    print(group(m))
    
    m = 29791
    print(group(m))
    
    m = 27
    print(f'All bases: {baseAll(m)}')
    
    m = 2543
    print(f'Base: {base(m)}')


if __name__ == "__main__":
    menu()
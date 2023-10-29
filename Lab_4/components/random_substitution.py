import random


def random_substitution(array: list[int]):
    result: list[int] = []
    array_shuffled: list[int] = random.sample(array, len(array))
    
    result.append(array)
    result.append(array_shuffled)

    return result
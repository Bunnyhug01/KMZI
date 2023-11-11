def prime_factor(number):
    result = []
    d = 2
    while d * d <= number:
        if number % d == 0:
            result.append(d)
            number //= d
        else:
            d += 1
    if number > 1:
        result.append(number)
    return result
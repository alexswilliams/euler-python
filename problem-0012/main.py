from math import sqrt, floor


def factors_of(n):
    result = set()
    for factor in range(1, floor(sqrt(n + 1))):
        if n % factor == 0:
            result.add(factor)
            result.add(n // factor)
    return result


index = 1
triangular_number = 1
length = 1

while length <= 500:
    index += 1
    triangular_number += index
    length = len(factors_of(triangular_number))

print(triangular_number)

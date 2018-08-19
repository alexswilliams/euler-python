from math import sqrt, floor


def is_prime(n):
    for i in range(2, floor(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def nth_prime(n):
    count = 0
    x = 2
    while count < n:
        if is_prime(x):
            count += 1
        x += 1
    return x - 1


print(nth_prime(10_001))

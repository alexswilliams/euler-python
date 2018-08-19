from math import sqrt, floor


def is_prime(n):
    for i in range(2, floor(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def all_primes_below(n):
    yield 2
    if n > 2:
        x = 3
        while x <= n:
            if is_prime(x):
                yield x
            x += 2


print(sum(all_primes_below(2_000_000)))

from math import sqrt, floor


def build_sieve(n):
    sieve = [x for x in range(3, n + 1, 2)]

    for index in range(0, floor(sqrt(len(sieve)))):
        if sieve[index] == 0:  # any composite numbers are set to 0 later
            continue

        for x in range(sieve[index] ** 2, n + 1, sieve[index] * 2):
            sieve[x // 2 - 1] = 0

    return sieve


sieve_2m = build_sieve(2_000_000)
print(sum(sieve_2m) + 2)

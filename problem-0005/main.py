from math import sqrt, floor


def is_prime(n):
    for i in range(2, floor(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def next_prime_at_or_after(start):
    x = start
    while not is_prime(x):
        x += 1
    return x


def prime_factors_of(n):
    factors = []
    (a, b) = (2, n)
    while a <= b:
        prime = next_prime_at_or_after(a)
        if b % prime == 0:
            factors.append(prime)
            (a, b) = (2, b // prime)
        else:
            a = prime + 1
    return factors


# e.g. given the list [2, 2, 2, 2, 2, 3, 4], it will return a dictionary of {2:5, 3:1, 4:1}
def count_members_of(lst):
    members = {}
    for i in lst:
        if i in members.keys():
            members[i] += 1
        else:
            members[i] = 1
    return members


# e.g. given {a:1, b:2} and {a:3, c:1}, it will return {a:3, b:2, c:1}
def merge_counts_taking_max(a, b):
    members = a
    for key in b.keys():
        if key in members:
            members[key] = max(members[key], b[key])
        else:
            members[key] = b[key]
    return members


covering_factor_set = {}
for number in range(1, 21):
    covering_factor_set = merge_counts_taking_max(
        covering_factor_set,
        count_members_of(
            prime_factors_of(number)
        )
    )

print("Covering set of prime factors:", covering_factor_set)

accumulator = 1
for (factor, count) in covering_factor_set.items():
    accumulator *= factor ** count

print(accumulator)

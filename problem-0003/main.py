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


input_number = 600_851_475_143
highest_prime_factor_seen_so_far = 1

big_num = input_number
small_num = 2

while big_num >= small_num:
    next_prime = next_prime_at_or_after(small_num)

    if big_num % next_prime == 0:
        # print("Prime Factor:", next_prime)
        if highest_prime_factor_seen_so_far < next_prime:
            highest_prime_factor_seen_so_far = next_prime
        big_num = big_num // next_prime
        small_num = 2
    else:
        small_num = next_prime + 1

# print("Highest prime factor:", highest_prime_factor_seen_so_far)
print(highest_prime_factor_seen_so_far)

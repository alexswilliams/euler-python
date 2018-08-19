from math import sqrt, floor


# Given a + b + c == s, and a**2 + b**2 == c**2
#  The problem is to find integer solutions for a * b == s(a + b) - 0.5 * s**2


def is_valid_solution(a, b, s):
    #    c = floor(sqrt((a ** 2 + b ** 2)))
    #    return (a ** 2 + b ** 2 == c ** 2) and (a + b + c == s)
    return a * b == s * (a + b) - 0.5 * (s ** 2)


def find_triplets_that_sum_to(s):
    results = []
    for a in range(1, s):
        for b in range(1, a):
            if is_valid_solution(a, b, s):
                results.append((b, a, floor(sqrt((a ** 2 + b ** 2)))))
    return results


triplets = find_triplets_that_sum_to(1000)

if len(triplets) == 1:
    (a, b, c) = triplets[0]
    print(a * b * c)
else:
    print("Error - expected exactly one triplet")

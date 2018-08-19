only_multiples_of_3_and_5 = [
    x for x in range(1, 1000)
    if x % 3 == 0 or x % 5 == 0
]

accumulator = 0
for x in only_multiples_of_3_and_5:
    accumulator += x

print(accumulator)

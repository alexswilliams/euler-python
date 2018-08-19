def fib_numbers_below(n):
    a = 0
    b = 1
    while b < n:
        yield b
        (a, b) = (b, a + b)


accumulator = 0
for num in fib_numbers_below(4_000_000):
    if num % 2 == 0:
        accumulator += num

print(accumulator)

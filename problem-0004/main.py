def is_palindrome(n):
    as_string = str(n)
    reversed_string = as_string[::-1]
    return as_string == reversed_string


input_ranges = (range(100, 1000), range(100, 1000))

largest_so_far = 0

for i in range(100, 1000):
    for j in range(100, i + 1):
        if is_palindrome(i * j):
            # print("%d x %d = %d" % (i, j, i * j))
            if largest_so_far < i * j:
                largest_so_far = i * j

# print("Largest palindrome:", largest_so_far)
print(largest_so_far)

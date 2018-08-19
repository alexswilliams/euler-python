def chain_length(start):
    length = 1
    x = start
    while x != 1:
        length += 1
        if x % 2 == 0:
            x //= 2
        else:
            x = 3 * x + 1
    return length


def find_longest_chain_start_number_under(n):
    longest = (0, 0)  # length, start number
    for start_number in range(1, n):
        length = chain_length(start_number)
        if length > longest[0]:
            longest = (length, start_number)
            # print(longest)
    return longest


chain = find_longest_chain_start_number_under(1_000_000)

print(chain[1])

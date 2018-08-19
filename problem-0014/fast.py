def chain_length(start, cache):
    cache_length = 0
    n = start

    seq = []
    while True:
        if n in cache.keys():
            cache_length = cache[n]
            break
        else:
            seq.append(n)
            if n == 1:
                break
            elif n % 2 == 0:
                n //= 2
            else:
                n = 3 * n + 1

    for i in range(len(seq)):
        cache[seq[i]] = cache_length + len(seq) - i
    # print(cache)

    return len(seq) + cache_length


def find_longest_chain_start_number_under(n, cache):
    longest = (0, 0)  # length, start number
    for start_number in range(1, n):
        length = chain_length(start_number, cache)
        if length > longest[0]:
            longest = (length, start_number)
            # print(longest)
    return longest


chain_cache = {1: 1}  # Dictionary of start_num : length
chain = find_longest_chain_start_number_under(1_000_000, chain_cache)

print(chain[1])

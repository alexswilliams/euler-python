def ways_to_reach_bottom_right_from_top_left(rows, cols, cache):
    if rows == 0 or cols == 0:
        return 1

    if (rows, cols) in cache.keys():
        return cache[(rows, cols)]

    going_right = ways_to_reach_bottom_right_from_top_left(rows, cols - 1, cache)
    going_down = ways_to_reach_bottom_right_from_top_left(rows - 1, cols, cache)

    cache[(rows, cols)] = going_down + going_right
    return going_down + going_right


print(ways_to_reach_bottom_right_from_top_left(20, 20, {}))

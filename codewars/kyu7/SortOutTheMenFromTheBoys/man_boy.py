def men_from_boys(arr):
    even = sorted(set(filter(lambda x: not x % 2, arr)))
    odd  = sorted(set(filter(lambda x: x % 2, arr)), reverse=True)
    return even + odd

def min_value(digits):
    num = str()
    for d in sorted(set(digits)):
        num += str(d)
    return int(num)
def beggars(values, n):
    if n == 0:
        return []
    else:
        which = 0
        beggs = n * [0]
        for v in range(len(values)):
            beggs[which] += values[v]
            which += 1
            if which == n:
                which = 0
        return beggs
def largestPower(N):
    k = -1
    while 3**(k+1) < N:
        k += 1
    return k
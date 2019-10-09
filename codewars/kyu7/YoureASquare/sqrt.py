import math
def is_square(n):
    if n >= 0:
        a = int(math.sqrt(n))
        return a*a == n
    return False
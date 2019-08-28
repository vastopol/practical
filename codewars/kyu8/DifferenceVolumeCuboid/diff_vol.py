def find_difference(a, b):
    lam = lambda x,y: x*y
    aa = reduce(lam,a)
    bb = reduce(lam,b)
    return abs(aa - bb)
import itertools

def matrix_addition(a, b):
    dim = len(a)
    aa = itertools.chain.from_iterable(a)
    bb = itertools.chain.from_iterable(b)
    cc = [ x+y for x,y in zip(aa,bb) ]
    mat = []
    row = []
    cnt = 1
    for c in cc:
        row.append(c)
        if cnt % dim == 0:
            mat.append(row)
            row = []
        cnt += 1
    return mat
    
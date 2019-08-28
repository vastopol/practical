import itertools
def flatten_and_sort(array):
    return sorted(itertools.chain.from_iterable(array))
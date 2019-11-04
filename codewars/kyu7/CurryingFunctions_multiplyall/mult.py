# curried list multiply
def multiply_all(arg1):
    def inner(arg2):
        return [arg2 * a for a in arg1]
    return inner
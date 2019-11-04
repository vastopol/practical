def calc(expr):

    if not expr:
        return 0

    stk = list()
    parts = expr.split(' ')

    for e in parts:
        if e.isdigit():
            stk.append(int(e))
        elif '.' in e:
            stk.append(float(e))
        else:
            b = stk.pop()
            a = stk.pop()
            if e == '+':
                stk.append(a+b)
            elif e == '-':
                stk.append(a-b)
            elif e == '*':
                stk.append(a*b)
            elif e == '/':
                stk.append(a/b)

    return stk.pop()


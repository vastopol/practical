def valid_parentheses(string):
    stk = []
    for s in string:
        if s == '(':
           stk.append('(')
        elif s == ')':
            if stk:
                stk.pop()
            else:
                return False
    if stk:
        return False
    return True
              
class Solution:
    def removeOuterParentheses(self, S: str) -> str:

        depth = 0;
        sub = str()
        fin = str()
        pars = list()

        for c in S:
            if c is '(':
                depth += 1
                sub += '('
            if c is ')':
                depth -= 1
                sub += ')'
            if depth is 0:
                pars.append(sub)
                sub = str()

        for par in pars:
            fin += par[1:-1]

        return fin
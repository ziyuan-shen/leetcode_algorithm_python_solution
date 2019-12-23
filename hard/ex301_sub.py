class Traverse:
    def __init__(self):
        self.exprs = []
    
    def remaining(self, s, idx, expr):
        if idx == len(s):
            self.exprs.append("".join(expr))
        else:
            self.remaining(s, idx+1, expr)
            expr.append(s[idx])
            self.remaining(s, idx+1, expr)
            expr.pop()

    def get_result(self, s):
        self.remaining(s, 0, [])
        return self.exprs


T = Traverse()
exprs = T.get_result("AD5")
print(exprs)
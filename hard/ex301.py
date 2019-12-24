class Solution:
    def __init__(self):
        self.valid_exprs = set()
        self.least_rem = float("inf")
                
    def remaining(self, s, idx, left, right, rem, expr):
        if idx == len(s):
            if left == right:
                if rem < self.least_rem:
                    self.valid_exprs = set()
                    self.least_rem = rem
                if rem <= self.least_rem:
                    self.valid_exprs.add("".join(expr))
        else:
            if s[idx] != '(' and s[idx] != ')':
                expr.append(s[idx])
                self.remaining(s, idx+1, left, right, rem, expr)
                expr.pop()
            else:
                if s[idx] == '(':
                    self.remaining(s, idx+1, left, right, rem+1, expr)
                    expr.append(s[idx])
                    self.remaining(s, idx+1, left+1, right, rem, expr)
                    expr.pop()
                else:
                    self.remaining(s, idx+1, left, right, rem+1, expr)
                    if right < left:
                        expr.append(s[idx])
                        self.remaining(s, idx+1, left, right+1, rem, expr)
                        expr.pop()

        
    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.remaining(s, 0, 0, 0, 0, [])
        return list(self.valid_exprs)
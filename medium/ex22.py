class Solution:
    def __init__(self):
        self.combs = []
        
    def remaining(self, idx, left, right, n, comb):
        if idx == 2 * n:
            self.combs.append(comb)
        else:
            if left < n:
                self.remaining(idx + 1, left + 1, right, n, comb + "(")
                if right < left:
                    self.remaining(idx + 1, left, right + 1, n, comb + ')')
            else:
                self.remaining(2 * n, n, n, n, comb + ")" * (n - right))
        
    def generateParenthesis(self, n: int) -> List[str]:
        self.remaining(1, 1, 0, n, '(')
        return self.combs
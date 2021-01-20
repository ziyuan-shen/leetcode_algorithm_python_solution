class Solution:
    def calculate(self, left, right, op):
        if op == '-':
            return left - right
        if op == '*':
            return left * right
        if op == '+':
            return left + right
        
    def diffWaysToCompute(self, input: str) -> List[int]:
        ans = []
        for i in range(len(input)):
            if not input[i].isdigit():
                leftnum = self.diffWaysToCompute(input[:i])
                rightnum = self.diffWaysToCompute(input[i+1:])
                for left in leftnum:
                    for right in rightnum:
                        ans.append(self.calculate(left, right, input[i]))
        if len(ans) == 0:
            ans.append(int(input))
        return ans
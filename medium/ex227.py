class Solution:
    def getnum(self, s):
        num = ""
        ops = ["+", "-", "*", "/"]
        idx = 0
        while idx < len(s) and s[idx] not in ops:
            if s[idx] != " ":
                num += s[idx]
            idx += 1
        return int(num), s[idx:]
    
    def calculate(self, s: str) -> int:
        stack = []
        num, s = self.getnum(s)
        stack.append(num)
        while s:
            if s[0] == "-" or s[0] == "+":
                stack.append(s[0])
                num, s = self.getnum(s[1:])
                stack.append(num)
            else:
                op = s[0]
                right, s = self.getnum(s[1:])
                left = stack.pop()
                if op == '*':
                    stack.append(left * right)
                else:
                    stack.append(left // right)
        if len(stack) == 1:
            return stack[0]
        else:
            ans = stack.pop(0)
            for i in range(0, len(stack), 2):
                if stack[i] == '+':
                    ans += stack[i+1]
                else:
                    ans -= stack[i+1]
            return ans
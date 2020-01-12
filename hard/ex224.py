class Solution:
    def calculate(self, s: str) -> int:
        idx = 0
        stack = []
        while idx < len(s):
            if s[idx] == "(" or s[idx] == "+" or s[idx] == "-":
                stack.append(s[idx])
                idx += 1
            elif s[idx] ==" ":
                idx += 1
            elif s[idx] ==")":
                num = stack.pop()
                stack.pop()
                while stack and (stack[-1] == "+" or stack[-1] == "-"):
                    op = stack.pop()
                    left = stack.pop()
                    if op == "+":
                        num = left + num
                    else:
                        num = left - num
                stack.append(num)
                idx += 1
            else:
                num = s[idx]
                idx += 1
                while idx < len(s) and s[idx] not in ["(", ")", "+", "-"]:
                    if s[idx] != " ":
                        num += s[idx]
                    idx += 1
                num = int(num)
                if stack and (stack[-1] == "-" or stack[-1] == "+"):
                    op = stack.pop()
                    left  = stack.pop()
                    if op == "+":
                        num = left + num
                    else:
                        num = left - num
                stack.append(num)
        return stack[0]
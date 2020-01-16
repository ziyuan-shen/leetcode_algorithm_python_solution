class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        infix_expression = []
        idx = 0
        ops = {"(", ")", "+", "-", "*", "/"}
        while idx < len(s):
            if s[idx] in ops:
                infix_expression.append(s[idx])
                idx += 1
            else:
                num = s[idx]
                idx += 1
                while idx < len(s) and s[idx] not in ops:
                    num += s[idx]
                    idx += 1
                infix_expression.append(int(num))
        infix_expression.append("#")
        isp = {"#": 0, "(": 1, "+": 3, "-": 3, "*": 5, "/": 5, ")": 6}
        icp = {"#": 0, "(": 6, "+": 2, "-": 2, "*": 4, "/": 4, ")": 1}
        postfix_expression = []
        stack = ["#"]
        ch = infix_expression.pop(0)
        while not (ch == "#" and not stack):
            if isinstance(ch, int):
                postfix_expression.append(ch)
                ch = infix_expression.pop(0)
            elif icp[ch] > isp[stack[-1]]:
                stack.append(ch)
                ch = infix_expression.pop(0)
            elif icp[ch] < isp[stack[-1]]:
                postfix_expression.append(stack.pop())
            else:
                top = stack.pop()
                if top == "(":
                    ch = infix_expression.pop(0)
        ans = []
        for elem in postfix_expression:
            if isinstance(elem, int):
                ans.append(elem)
            else:
                right = ans.pop()
                left = ans.pop()
                if elem == "+":
                    new = left + right
                elif elem == "-":
                    new = left - right
                elif elem == "*":
                    new = left * right
                else:
                    new = left // right
                ans.append(new)
        return ans[0]
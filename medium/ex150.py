class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for elem in tokens:
            if elem in ["+", "-", "*", "/"]:
                x = stack.pop()
                y = stack.pop()
                if elem == "+":
                    stack.append(x + y)
                elif elem == "-":
                    stack.append(y - x)
                elif elem == "*":
                    stack.append(x * y)
                else:
                    if x * y >= 0:
                        stack.append(y // x)
                    else:
                        stack.append(-(abs(y) // abs(x)))
            else:
                stack.append(int(elem))
        return stack[0]
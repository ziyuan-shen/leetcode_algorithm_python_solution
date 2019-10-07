class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)==0:
            return True
        stack = []
        dic = {')':'(', '}':'{', ']':'['}
        for i in s:
            if i not in dic:
                stack.append(i)
            else:
                if len(stack)==0:
                    return False
                top = stack.pop()
                if top!=dic[i]:
                    return False
        return not stack
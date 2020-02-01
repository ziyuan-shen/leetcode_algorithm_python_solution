class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        deletes = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append((i))
            if s[i] == ")":
                if stack:
                    stack.pop()
                else:
                    deletes.append(i)
        deletes += stack
        deletes = set(deletes)
        ans = ""
        for i in range(len(s)):
            if i not in deletes:
                ans += s[i]
        return ans
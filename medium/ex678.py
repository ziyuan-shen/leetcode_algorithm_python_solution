class Solution:
    def isValid(self, q, s):
        for idx, ch in enumerate(s):
            if ch == ")":
                if q:
                    q.pop()
                else:
                    return False
            elif ch == "(":
                q.append("(")
            else:
                if q:
                    if self.isValid(q[1:], s[idx+1:]):
                        return True
                if self.isValid(q + ["("], s[idx+1:]):
                    return True
                if self.isValid(q.copy(), s[idx+1:]):
                    return True
        return not q
            
    def checkValidString(self, s: str) -> bool:
        return self.isValid([], s)
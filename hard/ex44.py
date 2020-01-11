class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not bool(s)
        if p[0] == "?":
            return s != "" and self.isMatch(s[1:], p[1:])
        elif p[0] == "*":
            if not s:
                return self.isMatch(s, p[1:])
            else:
                return self.isMatch(s, p[1:]) or self.isMatch(s[1:], p)
        else:
            return s != "" and s[0] == p[0] and self.isMatch(s[1:], p[1:])
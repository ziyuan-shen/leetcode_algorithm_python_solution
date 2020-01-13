class Solution:
    def lastSubstring(self, s: str) -> str:
        if not s:
            return ""
        letter = s[0]
        ans = s
        for i in range(1, len(s)):
            if s[i] == letter:
                ans = max(ans, s[i:])
            elif s[i] > letter:
                letter = s[i]
                ans = s[i:]
        return ans
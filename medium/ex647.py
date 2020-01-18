class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
        for i in range(len(s)-1):
            dp[i][i+1] = s[i] == s[i+1]
        for length in range(3, len(s) + 1):
            for i in range(len(s) - length + 1):
                dp[i][i+length-1] = s[i] == s[i+length-1] and dp[i+1][i+length-2]
        flat = []
        for row in dp:
            flat += row
        return sum(flat)
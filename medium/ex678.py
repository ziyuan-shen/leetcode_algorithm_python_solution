class Solution:     
    def checkValidString(self, s: str) -> bool:
        if not s:
            return True
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            if s[i] == "*":
                dp[i][i] = True
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                if s[i] == "*":
                    if dp[i+1][i+length-1]:
                        dp[i][i+length-1] = True
                        continue
                if s[i] != ")":
                    for j in range(i+1, i+length):
                        if s[j] != "(":
                            if (j-1<i+1 or dp[i+1][j-1]) and (i+length-1<j+1 or dp[j+1][i+length-1]):
                                dp[i][i+length-1] = True
                                break
        return dp[0][n-1]
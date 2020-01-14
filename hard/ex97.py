class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)
        if n1 + n2 != n3:
            return False
        dp = [[[False for _ in range(n3+1)] for _ in range(n2+1)] for _ in range(n1+1)]
        dp[-1][-1][-1] = True
        for i in range(n1):
            for j in range(n3):
                dp[i][-1][j] = s1[i:] == s3[j:]
        for i in range(n2):
            for j in range(n3):
                dp[-1][i][j] = s2[i:] == s3[j:]
        for i in range(n1-1, -1, -1):
            for j in range(n2-1, -1, -1):
                for k in range(n3-1, -1, -1):
                    if s1[i] == s2[j]:
                        dp[i][j][k] = s3[k] == s1[i] and (dp[i+1][j][k+1] or dp[i][j+1][k+1])
                    elif s1[i] == s3[k]:
                        dp[i][j][k] = dp[i+1][j][k+1]
                    elif s2[j] == s3[k]:
                        dp[i][j][k] = dp[i][j+1][k+1]
        return dp[0][0][0]
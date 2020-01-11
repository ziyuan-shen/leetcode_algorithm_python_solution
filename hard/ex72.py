class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1) + 1
        n2 = len(word2) + 1
        dp = [[0 for _ in range(n2)] for _ in range(n1)]
        dp[0] = [i for i in range(n2)]
        for i in range(n1):
            dp[i][0] = i
        for r in range(1, n1):
            for c in range(1, n2):
                if word1[r-1] == word2[c-1]:
                    dp[r][c] = 1 + min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1] - 1)
                else:
                    dp[r][c] = 1 + min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1])
        return dp[-1][-1]
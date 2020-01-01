class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix == []:
            return 0
        nrow = len(matrix)
        ncol = len(matrix[0])
        dp = [[0 for _ in range(ncol)] for _ in range(nrow)]
        ans = 0
        for i in range(nrow):
            for j in range(ncol):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j] if i>=1 else 0, dp[i][j-1] if j >= 1 else 0, dp[i-1][j-1] if i >= 1 and j >= 1 else 0) + 1
                    if dp[i][j] > ans:
                        ans = dp[i][j]
        return ans ** 2
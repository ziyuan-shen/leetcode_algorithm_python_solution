class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        nrow = len(grid)
        ncol = len(grid[0])
        dp = [[0 for _ in range(ncol)] for _ in range(nrow)]
        for i in range(ncol):
            dp[-1][i] = sum(grid[-1][i:])
        for i in range(nrow):
            dp[i][-1] = sum([grid[k][-1] for k in range(i, nrow)])
        for i in range(nrow - 2, -1, -1):
            for j in range(ncol - 2, -1, -1):
                dp[i][j] = grid[i][j] + min(dp[i+1][j], dp[i][j+1])
        return dp[0][0]
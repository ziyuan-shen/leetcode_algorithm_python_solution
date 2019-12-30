class Solution: 
    def cherryPickup(self, grid: List[List[int]]) -> int:
        N = len(grid)
        dp = [[[float('-inf') for i in range(N)] for i in range(N)] for i in range(N)]
        dp[N-1][N-1][N-1] = grid[-1][-1]
        for t in range(2 * N - 3, -1 , -1):
            for r1 in range(min(t, N - 1), max(0, t - N + 1) - 1, -1):
                for r2 in range(min(t, N - 1), max(0, t - N + 1) - 1, -1):
                    c1 = t - r1
                    c2 = t - r2
                    if grid[r1][c1] == -1 or grid[r2][c2] == -1:
                        continue
                    else:
                        values = []
                        if r1 + 1 < N:
                            values.append(dp[r1+1][c1][r2])
                            if r2 + 1 < N:
                                values.append(dp[r1+1][c1][r2+1])
                        if c1 + 1 < N:
                            values.append(dp[r1][c1+1][r2])
                            if r2 + 1 < N:
                                values.append(dp[r1][c1+1][r2+1])
                        dp[r1][c1][r2] = grid[r1][c1] + grid[r2][c2] + max(values)
                        if r1 == r2 and c1 == c2 and grid[r1][c1] == 1:
                            dp[r1][c1][r2] -= 1
        return max(0, dp[0][0][0])
                
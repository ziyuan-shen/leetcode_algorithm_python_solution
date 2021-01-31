class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        x, y = [], []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    x.append(i)
                    y.append(j)
        x.sort()
        y.sort()
        ans = 0
        meetx = x[len(x)//2]
        meety = y[len(x)//2]
        for i in range(len(x)):
            ans += (abs(meetx - x[i]) + abs(meety - y[i]))
        return ans
class Solution:
    def dfs(self, i, j, visited, grid, closed):
        for neii, neij in [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]:
            if neii >= 0 and neii < len(grid) and neij >= 0 and neij < len(grid[0]):
                if (neii, neij) not in visited and grid[neii][neij] == 0:
                    visited.add((neii, neij))
                    if closed:
                        if neii == 0 or neii == len(grid) - 1 or neij == 0 or neij == len(grid[0]) - 1:
                            closed = False
                    closed = self.dfs(neii, neij, visited, grid, closed)
        return closed
    
    def closedIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == 0:
                    visited.add((i, j))
                    if self.dfs(i, j, visited, grid, i > 0 and i < len(grid) - 1 and j > 0 and j < len(grid[0]) - 1):
                        ans += 1
        return ans
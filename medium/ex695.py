from collections import defaultdict
class Solution:
    def dfs(self, start, neighbordic, visited):
        for neighbor in neighbordic[start]:
            if not visited[neighbor]:
                visited[neighbor] = True
                self.dfs(neighbor, neighbordic, visited)
                
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        nrow = len(grid)
        ncol = len(grid[0])
        neighbordic = defaultdict(set)
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == 1:
                    if i*ncol+j not in neighbordic:
                        neighbordic[i*ncol+j] = set()
                    for neighbor in [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]:
                        r = neighbor[0]
                        c = neighbor[1]
                        if r >= 0 and r < nrow and c >= 0 and c < ncol and grid[r][c] == 1:
                            neighbordic[i*ncol+j].add(r*ncol+c)
                            neighbordic[r*ncol+c].add(i*ncol+j)
        visited = {node: False for node in neighbordic}
        n = len(neighbordic)
        visited_num = 0
        ans = 0
        while visited_num < n:
            for node in neighbordic:
                if not visited[node]:
                    visited[node] = True
                    self.dfs(node, neighbordic, visited)
                    break
            ans = max(sum(visited.values()) - visited_num, ans)
            visited_num = sum(visited.values())
        return ans
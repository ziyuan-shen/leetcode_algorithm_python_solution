class Solution:
    def move(self, node, visited, grid):
        for nei in [(node[0]-1, node[1]), (node[0], node[1]+1), (node[0]+1, node[1]), (node[0], node[1]-1)]:
            if nei[0] >= 0 and nei[0] < self.length and nei[1] >= 0 and nei[1] < self.width:
                if grid[nei[0]][nei[1]] == 2:
                    if len(visited) == self.emptynum:
                        self.ans += 1
                elif nei not in visited and grid[nei[0]][nei[1]] == 0:
                    visited.add(nei)
                    self.move(nei, visited, grid)
                    visited.remove(nei)
        
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.length = len(grid)
        self.width = len(grid[0])
        self.emptynum = 0
        for r in range(self.length):
            for c in range(self.width):
                if grid[r][c] == 1:
                    start = (r, c)
                if grid[r][c] == 0:
                    self.emptynum += 1
        self.ans = 0
        visited = set()
        self.move(start, visited, grid)
        return self.ans
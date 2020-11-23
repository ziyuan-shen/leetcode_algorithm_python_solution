class Solution:
    def walk(self, node, movenum, visited_keys, visited, grid):
        if len(visited_keys) == self.keynum:
            return movenum
        minmove = float("inf")
        for nei in [(node[0]-1, node[1]), (node[0]+1, node[1]), (node[0], node[1]-1), (node[0], node[1]+1)]:
            if nei not in visited and nei[0] >= 0 and nei[0] < self.length and nei[1] >= 0 and nei[1] < self.width:
                content = grid[nei[0]][nei[1]]
                if content.islower():
                    visited_keys.add(content)
                    grid[nei[0]][nei[1]] = "."
                    minmove = min(minmove, self.walk(nei, movenum + 1, visited_keys, {nei}, grid))
                    visited_keys.remove(content)
                    grid[nei[0]][nei[1]] = content
                elif content == "@" or content == "." or (content.isupper() and content.lower() in visited_keys):
                    visited.add(nei)
                    minmove = min(minmove, self.walk(nei, movenum + 1, visited_keys, visited, grid))
                    visited.remove(nei)
        return minmove
                    
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        self.keynum = 0
        self.length = len(grid)
        self.width = len(grid[0])
        for i in range(self.length):
            grid[i] = list(grid[i])
        for i in range(self.length):
            for j in range(self.width):
                if grid[i][j] == '@':
                    start = (i, j)
                elif grid[i][j].islower():
                    self.keynum += 1
        visited_keys = set()
        visited = {start}
        ans = self.walk(start, 0, visited_keys, visited, grid)
        return ans if ans != float("inf") else -1
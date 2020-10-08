class Solution:
    def dfs(self, r, c, visited, affected_area, affected_cells, protected, grid):
        for nei in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if nei[0] >= 0 and nei[0] < self.length and nei[1] >= 0 and nei[1] < self.width:
                if nei not in visited and nei not in protected:
                    visited.add(nei)
                    if grid[nei[0]][nei[1]] == 1:
                        affected_area.add(nei)
                        affected_cells.add(nei)
                        self.dfs(nei[0], nei[1], visited, affected_area, affected_cells, protected, grid)
                        
    def get_affected_areas(self, affected_cells, protected, grid):
        visited = set()
        affected_areas = []
        for i in range(self.length):
            for j in range(self.width):
                if (i, j) not in visited and (i, j) not in protected:
                    visited.add((i, j))
                    if grid[i][j] == 1:
                        affected_area = {(i, j)}
                        affected_cells.add((i, j))
                        self.dfs(i, j, visited, affected_area, affected_cells, protected, grid)
                        affected_areas.append(affected_area)
        return affected_areas
        
    def containVirus(self, grid: List[List[int]]) -> int:
        self.length = len(grid)
        self.width = len(grid[0])
        affected_cells = set()
        protected = set()
        affected_areas = self.get_affected_areas(affected_cells, protected, grid)
        if len(affected_cells) == self.length * self.width:
            return 0
        ans = 0
        while affected_areas and len(affected_cells) < self.length * self.width:
            threatens = [set() for _ in range(len(affected_areas))]
            walls = [0 for _ in range(len(affected_areas))]
            for i in range(len(affected_areas)):
                for cell in affected_areas[i]:
                    for nei in [(cell[0]-1, cell[1]), (cell[0]+1, cell[1]), (cell[0], cell[1]-1), (cell[0], cell[1]+1)]:
                        if nei[0] >= 0 and nei[0] < self.length and nei[1] >= 0 and nei[1] < self.width:
                            if grid[nei[0]][nei[1]] == 0:
                                threatens[i].add(nei)
                                walls[i] += 1
            threatens_nums = [len(s) for s in threatens]
            build = threatens_nums.index(max(threatens_nums))
            ans += walls[build]
            for cell in affected_areas[build]:
                protected.add(cell)
            del threatens[build]
            for i in range(len(threatens)):
                for cell in threatens[i]:
                    grid[cell[0]][cell[1]] = 1
                    affected_cells.add(cell)
            affected_areas = self.get_affected_areas(affected_cells, protected, grid)
        return ans
                                
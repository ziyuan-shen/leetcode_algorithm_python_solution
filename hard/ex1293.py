class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        length = len(grid)
        width = len(grid[0])
        q = [(0, 0, 0, k)]
        visited = {(0, 0, k): 0}
        while q:
            level, x, y, r = q.pop(0)
            for neighbor in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                if neighbor[0] >= 0 and neighbor[0] < length and neighbor[1] >= 0 and neighbor[1] < width:
                    if grid[neighbor[0]][neighbor[1]] == 1:
                        new_r = r - 1
                    else:
                        new_r = r
                    if new_r >= 0 and (neighbor[0], neighbor[1], new_r) not in visited:
                        visited[(neighbor[0], neighbor[1], new_r)] = level + 1
                        q.append((level + 1, neighbor[0], neighbor[1], new_r))
        ans = float("inf")
        for x, y, r in visited:
            if x == length - 1 and y == width - 1 and r >= 0:
                ans = min(ans, visited[(x, y, r)])
        if ans != float("inf"):
            return ans
        else:
            return -1
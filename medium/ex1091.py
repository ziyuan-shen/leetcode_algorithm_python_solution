from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        if grid[0][0] == 1 or grid[N-1][N-1] == 1:
            return -1
        if N == 1:
            return 1
        q = deque([(0, 0, 1)])
        visited = {(0, 0)}
        while q:
            row, col, level = q.popleft()
            for nei in [(row-1, col-1), (row-1, col), (row-1, col+1), (row, col-1), (row, col+1), (row+1, col-1), (row+1, col), (row+1, col+1)]:
                if nei[0] == N-1 and nei[1] == N-1:
                    return level + 1
                if nei[0] >= 0 and nei[0] < N and nei[1] >= 0 and nei[1] < N and grid[nei[0]][nei[1]] == 0 and nei not in visited:
                    visited.add(nei)
                    q.append(nei + (level+1,))
        return -1
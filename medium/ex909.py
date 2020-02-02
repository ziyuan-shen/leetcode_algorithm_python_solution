from collections import defaultdict
from collections import deque
class Solution:
    def getCoord(self, i, N):
        row, col = 2 * ((i - 1) // (2 * N)), (i - 1) % (2 * N)
        if col >= N:
            row += 1
            col = N - 1 - (col - N)
        row = N - 1 - row
        return row, col
        
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        N = len(board)
        neighbordic = defaultdict(set)
        for i in range(1, N * N + 1):
            row, col = self.getCoord(i, N)
            for step in range(1, 7):
                if i + step <= N * N:
                    m, n = self.getCoord(i + step, N)
                    if board[m][n] == -1:
                        neighbordic[i].add(i + step)
                    else:
                        neighbordic[i].add(board[m][n])
        q = deque([(0, 1)])
        visited = {1}
        while q:
            level, node = q.popleft()
            for neighbor in neighbordic[node]:
                if neighbor == N * N:
                    return level + 1
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append((level + 1, neighbor))
        return -1
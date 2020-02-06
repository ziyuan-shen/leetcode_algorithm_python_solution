from collections import deque
class Solution:        
    def minKnightMoves(self, x: int, y: int) -> int:
        if x == 0 and y == 0:
            return 0
        xt = x
        yt = y
        q = deque([(0, 0, 0)])
        visited = {(0, 0)}
        while q:
            level, x, y = q.popleft()
            for neighbor in [(x+2,y+1), (x+1,y+2), (x-1,y+2), (x-2,y+1), (x-2,y-1), (x-1,y-2), (x+1,y-2), (x+2,y-1)]:
                if neighbor not in visited:
                    if neighbor[0] == xt and neighbor[1] == yt:
                        return level + 1
                    visited.add(neighbor)
                    q.append((level + 1, neighbor[0], neighbor[1]))      
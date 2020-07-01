class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        length = len(A)
        width = len(A[0])
        islands = set()
        for i in range(length):
            if islands:
                break
            for j in range(width):
                if A[i][j] == 1:
                    visited = {(i, j)}
                    islands.add((i, j))
                    q = [(i, j)]
                    while q:
                        x, y = q.pop(0)
                        for neighbor in [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]:
                            if neighbor[0] >= 0 and neighbor[0] < length and neighbor[1] >= 0 and neighbor[1] < width:
                                if neighbor not in visited and A[neighbor[0]][neighbor[1]] == 1:
                                    visited.add(neighbor)
                                    islands.add(neighbor)
                                    q.append(neighbor)
                    break
        ans = float("inf")
        for start in islands:
            visited = set()
            q = [(start[0], start[1], 0)]
            flag = False
            while q:
                x, y, level = q.pop(0)
                for neighbor in [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]:
                    if neighbor[0] >= 0 and neighbor[0] < length and neighbor[1] >= 0 and neighbor[1] < width:
                        if neighbor not in visited and neighbor not in islands:
                            if A[neighbor[0]][neighbor[1]] == 1:
                                ans = min(ans, level)
                                flag = True
                                break
                            visited.add(neighbor)
                            q.append((neighbor[0], neighbor[1], level + 1))
                if flag:
                    break
        return ans
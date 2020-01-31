from collections import defaultdict
from collections import deque
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        buildings = set()
        lands = set()
        nrow = len(grid)
        ncol = len(grid[0])
        neighbordic = defaultdict(set)
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == 2:
                    continue
                else:
                    num = i * ncol + j
                    if grid[i][j] == 1:
                        buildings.add(num)
                    else:
                        lands.add(num)
                        for n in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                            r = n[0]
                            c = n[1]
                            if r >= 0 and r < nrow and c >= 0 and c < ncol and grid[r][c] != 2:
                                neighbordic[num].add(r * ncol + c)
        nodes = buildings.union(lands)
        mindistance = float("inf")
        for land in lands:
            visited = {node: False for node in nodes}
            q = deque([(0, land)])
            visited[land] = True
            distance = 0
            visited_buildings_num = 0
            while q:
                level, node = q.popleft()
                for neighbor in neighbordic[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        q.append((level + 1, neighbor))
                        if neighbor in buildings:
                            distance += level + 1
                            visited_buildings_num += 1
                if visited_buildings_num == len(buildings) or distance > mindistance:
                    break
            if visited_buildings_num == len(buildings):
                mindistance = min(mindistance, distance)
        return -1 if mindistance == float("inf") else mindistance
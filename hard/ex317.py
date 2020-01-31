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
                        if r >= 0 and r < nrow and c >= 0 and c < ncol and grid[r][c] == 0:
                            neighbordic[num].add(r * ncol + c)
        reached = defaultdict(lambda: defaultdict(int))
        for building in buildings:
            visited = {land: False for land in lands}
            q = deque([(0, building)])
            while q:
                level, node = q.popleft()
                for neighbor in neighbordic[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        q.append((level + 1, neighbor))
                        reached[building][neighbor] = level + 1
        if len(reached) == len(buildings):
            commonlands = set(list(reached.values())[0].keys())
            for dic in reached.values():
                commonlands = commonlands.intersection(set(dic.keys()))
        else:
            commonlands = set()
        if len(commonlands) == 0:
            return -1
        else:
            return min([sum([reached[b][land] for b in buildings]) for land in commonlands])
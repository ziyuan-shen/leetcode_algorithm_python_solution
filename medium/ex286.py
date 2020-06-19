from collections import defaultdict
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return
        length = len(rooms)
        width = len(rooms[0])
        gates = set()
        graph = defaultdict(set)
        for i in range(length):
            for j in range(width):
                if rooms[i][j] == 0:
                    gates.add((i, j))
                if rooms[i][j] != -1:
                    for neighbor in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                        if neighbor[0] >= 0 and neighbor[0] < length and neighbor[1] >= 0 and neighbor[1] < width:
                            if rooms[neighbor[0]][neighbor[1]] != -1:
                                graph[(i, j)].add(neighbor)
        for gate in gates:
            visited = {gate}
            q = [(1, gate)]
            while q:
                level, node = q.pop(0)
                for neighbor in graph[node]:
                    if neighbor not in visited and rooms[neighbor[0]][neighbor[1]] != 0:
                        visited.add(neighbor)
                        rooms[neighbor[0]][neighbor[1]] = min(level, rooms[neighbor[0]][neighbor[1]])
                        q.append((level+1, neighbor))
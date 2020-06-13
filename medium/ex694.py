class Solution:
    def dfs(self, graph, visited, node, island):
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                island.append(neighbor)
                self.dfs(graph, visited, neighbor, island)
        
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        length = len(grid)
        width = len(grid[0])
        graph = {}
        for i in range(length):
            for j in range(width):
                if grid[i][j] == 1:
                    graph[(i, j)] = set()
                    for neighbor in [(i-1, j), (i+1, j), (i, j+1), (i, j-1)]:
                        if neighbor[0] >= 0 and neighbor[0] < length and neighbor[1] >= 0 and neighbor[1] < width:
                            if grid[neighbor[0]][neighbor[1]] == 1:
                                graph[(i, j)].add(neighbor)
        visited = set()
        islands = []
        for node in graph:
            if node not in visited:
                visited.add(node)
                islands.append([node])
                self.dfs(graph, visited, node, islands[-1])
        for island in islands:
            top = min([node[0] for node in island])
            left = min([node[1] for node in island])
            for idx, node in enumerate(island):
                island[idx] = (node[0] - top, node[1] - left)
            island.sort()
        return len(set([tuple(island) for island in islands]))
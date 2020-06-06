from collections import defaultdict
class Solution:
    def dfs(self, start, graph, visited, node):
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                if neighbor in self.pacific:
                    self.pa[start][0] = True
                if neighbor in self.atlantic:
                    self.pa[start][1] = True
                if self.pa[start][0] and self.pa[start][1]:
                    return True
                if self.dfs(start, graph, visited, neighbor):
                    return True
        return False
    
    def pacificAtlantic(self, matrix):
        if not matrix:
            return []
        length = len(matrix)
        width = len(matrix[0])
        graph = defaultdict(set)
        self.pacific = set()
        self.atlantic = set()
        for i in range(width):
            self.pacific.add((0, i))
            self.atlantic.add((length - 1, i))
        for j in range(length):
            self.pacific.add((j, 0))
            self.atlantic.add((j, width - 1))
        self.pa = {}
        for i in range(length):
            for j in range(width):
                self.pa[(i, j)] = [False, False]
                for neighbor in [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]:
                    if neighbor[0] >= 0 and neighbor[0] < length and neighbor[1] >= 0 and neighbor[1] < width:
                        if matrix[neighbor[0]][neighbor[1]] <= matrix[i][j]:
                            graph[(i, j)].add(neighbor)
        ans = []
        for i in range(length):
            for j in range(width):
                visited = {(i, j)}
                if (i, j) in self.pacific:
                    self.pa[(i, j)][0] = True
                if (i, j) in self.atlantic:
                    self.pa[(i, j)][1] = True
                if self.pa[(i, j)][0] and self.pa[(i, j)][1]:
                    ans.append([i, j])
                elif self.dfs((i, j), graph, visited, (i, j)):
                    ans.append([i, j])
        return ans
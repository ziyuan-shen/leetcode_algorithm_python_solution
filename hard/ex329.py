from collections import defaultdict
class Solution:
    def dfs(self, graph, node):
        ans = 0
        if node in graph:
            for neighbor in graph[node]:
                if neighbor in self.pathdic:
                    ans = max(ans, self.pathdic[neighbor])
                else:
                    ans = max(ans, self.dfs(graph, neighbor))
        self.pathdic[node] = ans + 1
        return ans + 1
    
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        nrow = len(matrix)
        ncol = len(matrix[0])
        graph = defaultdict(set)
        self.pathdic = dict()
        for r in range(nrow):
            for c in range(ncol):
                for n in [[r-1, c], [r+1, c], [r, c-1], [r, c+1]]:
                    if n[0] >= 0 and n[0] < nrow and n[1] >= 0 and n[1] < ncol:
                        if matrix[n[0]][n[1]] > matrix[r][c]:
                            graph[r * ncol + c].add(n[0] * ncol + n[1])
        for node in graph:
            self.dfs(graph, node)
        return max(self.pathdic.values()) if self.pathdic else 1
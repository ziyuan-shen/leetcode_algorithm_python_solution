class Solution:
    def dfs(self, edges, visited, start):
        for edge in edges:
            if edge[0] == start:
                if not visited[edge[1]]:
                    visited[edge[1]] = True
                    self.dfs(edges, visited, edge[1])
            elif edge[1] == start:
                if not visited[edge[0]]:
                    visited[edge[0]] = True
                    self.dfs(edges, visited, edge[0])
        
    def findCircleNum(self, M: List[List[int]]) -> int:
        N = len(M)
        edges = []
        visited = {i: False for i in range(N)}
        for i in range(1, N):
            for j in range(i):
                if M[i][j] == 1:
                    edges.append([i, j])
        visited[0] = True
        self.dfs(edges, visited, 0)
        ans = 1
        while sum(visited.values()) != N:
            for i in visited:
                if not visited[i]:
                    visited[i] = True
                    self.dfs(edges, visited, i)
                    ans += 1
        return ans
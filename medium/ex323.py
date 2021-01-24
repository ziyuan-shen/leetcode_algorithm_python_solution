class Solution:
    def dfs(self, node, graph, visited):
        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                self.dfs(nei, graph, visited)
                
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: set() for i in range(n)}
        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])
        ans = 0
        visited = set()
        for node in range(n):
            if node not in visited:
                ans += 1
                visited.add(node)
                self.dfs(node, graph, visited)
        return ans
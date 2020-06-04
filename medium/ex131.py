class Solution:
    def findPaths(self, graph, s, d):
        paths = []
        path = [s]
        visited = {node: False for node in graph}
        visited[s] = True
        def dfs(visited, path):
            for neighbor in graph[path[-1]]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    path.append(neighbor)
                    if neighbor == d:
                        paths.append(path.copy())
                    else:
                        dfs(visited, path)
                    path.pop()
                    visited[neighbor] = False
        dfs(visited, path)
        return paths

    def partition(self, s: str) -> List[List[str]]:
        length = len(s)
        dp = [[False for _ in range(length)] for _ in range(length)]
        for i in range(length):
            dp[i][i] = True
        for i in range(length - 1):
            dp[i][i+1] = (s[i] == s[i+1])
        for l in range(3, length+1):
            for i in range(length - l + 1):
                dp[i][i+l-1] = dp[i+1][i+l-2] and (s[i] == s[i+l-1])
        graph = {node: [] for node in range(length+1)}
        for l in range(1, length + 1):
            for i in range(length - l + 1):
                if dp[i][i+l-1]:
                    graph[i].append(i+l)
        paths = self.findPaths(graph, 0, length)
        ans = []
        for path in paths:
            partition = []
            for i in range(len(path)-1):
                partition.append(s[path[i]:path[i+1]])
            ans.append(partition)
        return ans
        
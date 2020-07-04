from collections import defaultdict
class Solution:
    def getNum(self, graph):
        visited = set()
        ans = 0
        def dfs(visited, node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(visited, neighbor)
        for node in graph:
            if node not in visited:
                dfs(visited, node)
                ans += 1
        return ans
        
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        ans = [0 for _ in range(len(positions))]
        lands = set()
        for idx, position in enumerate(positions):
            pos = (position[0], position[1])
            lands.add(pos)
            if pos not in graph:
                graph[pos] = set()
            for neighbor in [(pos[0] + 1, pos[1]), (pos[0] - 1, pos[1]), (pos[0], pos[1] + 1), (pos[0], pos[1] - 1)]:
                if neighbor[0] >= 0 and neighbor[0] < m and neighbor[1] >= 0 and neighbor[1] < n and neighbor in lands:
                    graph[pos].add(neighbor)
                    graph[neighbor].add(pos)
            ans[idx] = self.getNum(graph)
        return ans
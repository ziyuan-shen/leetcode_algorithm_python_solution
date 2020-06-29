from collections import defaultdict
class Solution:
    def dfs(self, visited, graph, node, cum, target):
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                cum *= weight
                if neighbor == target:
                    return cum
                ans = self.dfs(visited, graph, neighbor, cum, target)
                if ans != -1:
                    return ans
                else:
                    cum /= weight
        return -1
                
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(set)
        zeros = set()
        for i in range(len(equations)):
            if values[i] == 0:
                zeros.add(equations[i][0])
            else:
                graph[equations[i][0]].add((equations[i][1], values[i]))
                graph[equations[i][1]].add((equations[i][0], 1 / values[i]))
        ans = [-1 for _ in range(len(queries))]
        for idx, q in enumerate(queries):
            if q[0] in zeros:
                ans[idx] = 0
            elif q[1] in zeros:
                continue
            elif q[0] not in graph or q[1] not in graph:
                continue
            elif q[0] == q[1]:
                ans[idx] = 1
            else:
                ans[idx] = self.dfs({q[0]}, graph, q[0], 1, q[1])
        return ans
class Solution:
    def go(self, start, path, graph):
        for nei in graph[start]:
            if nei == len(graph) - 1:
                self.ans.append(path + [nei])
            else:
                path.append(nei)
                self.go(nei, path, graph)
                path.pop()
        
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.ans = []
        self.go(0, [0], graph)
        return self.ans
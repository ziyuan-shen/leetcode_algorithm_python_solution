from collections import defaultdict
from collections import deque
class Solution:
    def visit(self, graph, length, start):
        if start in self.mem:
            return length + self.mem[start]
        newlength = 0
        for nei in graph[start]:
            newlength = max(newlength, self.visit(graph, 1, nei))
        self.mem[start] = newlength
        return length + newlength
        
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        nonstart = set()
        graph = defaultdict(set)
        for i in range(len(envelopes)-1):
            for j in range(i+1, len(envelopes)):
                if envelopes[i][0] < envelopes[j][0] and envelopes[i][1] < envelopes[j][1]:
                    graph[i].add(j)
                    nonstart.add(j)
                if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                    graph[j].add(i)
                    nonstart.add(i)
        ans = 1
        self.mem = dict()
        for start in range(len(envelopes)):
            if start not in nonstart:
                ans = max(ans, self.visit(graph, 1, start))
        return ans
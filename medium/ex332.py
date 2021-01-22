from collections import defaultdict, OrderedDict
class Solution:
    def useTicket(self, path, graph):
        if len(path) == self.flights + 1:
            self.ans.append(path.copy())
            return True
        for dest in list(graph[path[-1]].keys()):
            if graph[path[-1]][dest] > 0:
                graph[path[-1]][dest] -= 1
                path.append(dest)
                res = self.useTicket(path, graph)
                if res:
                    return True
                path.pop()
                graph[path[-1]][dest] += 1
        return False
            
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(OrderedDict)
        tickets.sort()
        for ticket in tickets:
            if ticket[1] in graph[ticket[0]]:
                graph[ticket[0]][ticket[1]] += 1
            else:
                graph[ticket[0]][ticket[1]] = 1
        self.flights = len(tickets)
        self.ans = []
        self.useTicket(["JFK"], graph)
        self.ans.sort()
        return self.ans[0]
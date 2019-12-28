class Solution:
    def DFS(self, node_num, edges, visited):
        if len(visited) == node_num:
            return [visited]
        visiteds = []
        for edge in edges:
            if edge[0] == visited[-1]:
                if edge[1] not in visited:
                    visiteds.extend(self.DFS(node_num, edges, visited + [edge[1]]))
        return visiteds
        
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        node_num = len(tickets)
        edges = []
        for i in range(node_num - 1):
            for j in range(i + 1, node_num):
                if tickets[i][1] == tickets[j][0]:
                    edges.append([i, j])
                if tickets[i][0] == tickets[j][1]:
                    edges.append([j, i])
        itineraries = []
        for i in range(node_num):
            if tickets[i][0] == 'JFK':
                itineraries.extend(self.DFS(node_num, edges, [i]))
        paths = []
        for itinerary in itineraries:
            path = []
            for i in range(node_num):
                if i == node_num - 1:
                    path.extend(tickets[itinerary[i]])
                else:
                    path.append(tickets[itinerary[i]][0])
            paths.append(path)
        paths = ["".join(x) for x in paths]
        ans = min(paths)
        return [ans[i:i+3] for i in range(0, len(ans), 3)]
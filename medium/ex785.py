class Solution:
    def addEdges(self, subset1, subset2, edges):
        if not edges:
            return True
        edge = edges.pop()
        edges_copy = edges.copy()
        if (edge[0] in subset1 and edge[1] in subset1) or (edge[0] in subset2 and edge[1] in subset2):
            return False
        elif edge[0] in subset1 and edge[1] not in subset2:
            subset2.add(edge[1])
            return self.addEdges(subset1, subset2, edges)
        elif edge[0] in subset2 and edge[1] not in subset1:
            subset1.add(edge[1])
            return self.addEdges(subset1, subset2, edges)
        elif edge[1] in subset1 and edge[0] not in subset2:
            subset2.add(edge[0])
            return self.addEdges(subset1, subset2, edges)
        elif edge[1] in subset2 and edge[0] not in subset1:
            subset1.add(edge[0])
            return self.addEdges(subset1, subset2, edges)
        elif edge[1] not in subset1 and edge[1] not in subset2 and edge[0] not in subset1 and edge[0] not in subset2:
            subset1.add(edge[0])
            subset2.add(edge[1])
            if self.addEdges(subset1, subset2, edges):
                return True
            else:
                subset1.remove(edge[0])
                subset2.remove(edge[1])
                subset1.add(edge[1])
                subset2.add(edge[0])
                return self.addEdges(subset1, subset2, edges_copy)
        else:
            return self.addEdges(subset1, subset2, edges)
        
    def isBipartite(self, graph: List[List[int]]) -> bool:
        if graph == [[]]:
            return True
        edges = set()
        for node, neighbors in enumerate(graph):
            for nei in neighbors:
                if (node, nei) not in edges and (nei, node) not in edges:
                    edges.add((node, nei))
        edges = list(edges)
        edge = edges.pop()
        subset1 = {edge[0]}
        subset2 = {edge[1]}
        return self.addEdges(subset1, subset2, edges)
        
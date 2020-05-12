class Solution:
    def getEdgeSquare(self, p1, p2):
        return (p1[0]-p2[0]) ** 2 + (p1[1]-p2[1]) ** 2
    
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        edges = []
        for pair in [[p1, p2], [p1, p3], [p1, p4], [p2, p3], [p2, p4], [p3, p4]]:
            edges.append(self.getEdgeSquare(pair[0], pair[1]))
        edges.sort()
        return edges[0] > 0 and edges[0] == edges[1] and edges[0] == edges[2] and edges[0] == edges[3] and edges[4] > 0 and edges[4] == edges[5]
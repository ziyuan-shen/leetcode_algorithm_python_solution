from collections import defaultdict
class Solution:
    def bfs(self, start, node, neighbordic, visited):
        for neighbor in neighbordic[node]:
            if neighbor == start:
                return True
            if neighbor not in visited:
                visited.add(neighbor)
                if self.bfs(start, neighbor, neighbordic, visited):
                    return True
        return False
        
    def containCircle(self, neighbordic):
        for node in list(neighbordic.keys()):
            visited = {node}
            if self.bfs(node, node, neighbordic, visited):
                return True
        return False
            
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        neighbordic = defaultdict(set)
        for pre in prerequisites:
            neighbordic[pre[1]].add(pre[0])
        return not self.containCircle(neighbordic)
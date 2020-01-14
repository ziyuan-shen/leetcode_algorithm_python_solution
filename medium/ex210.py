from collections import defaultdict
class Solution:
    def containCircle(self, neighbourdic):
        def dfs(node, neighbours, visited):
            for neighbour in neighbours:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    dfs(neighbour, neighbourdic[neighbour], visited)
            return visited[node]
        
        for node in neighbourdic:
            visited = {n: False for n in neighbourdic}
            if dfs(node, neighbourdic[node], visited):
                return True
        return False
            
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        neighbourdic = defaultdict(set)
        nodes = [edge[0] for edge in prerequisites] + [edge[1] for edge in prerequisites]
        for node in nodes:
            neighbourdic[node] = set()
        for edge in prerequisites:
            neighbourdic[edge[1]].add(edge[0])
        if self.containCircle(neighbourdic):
            return []
        stack = []
        visited = {n: False for n in neighbourdic}
        
        def dfs(node):
            visited[node] = True
            for neighbour in neighbourdic[node]:
                if not visited[neighbour]:
                    dfs(neighbour)
            stack.append(node)
            
        for node in neighbourdic:
            if not visited[node]:
                dfs(node)
        stack = stack[::-1]
        if len(stack) < numCourses:
            for course in range(numCourses):
                if course not in stack:
                    stack.append(course)
        return stack
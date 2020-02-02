"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        q = deque([node])
        visited = {1}
        DFS = dict()
        while q:
            node = q.popleft()
            DFS[node.val] = node
            for neighbor in node.neighbors:
                if neighbor.val not in visited:
                    visited.add(neighbor.val)
                    q.append(neighbor)
        copy = {val: Node(val) for val in DFS}
        for val in DFS:
            node = DFS[val]
            new_node = copy[val]
            for neighbor in node.neighbors:
                new_node.neighbors.append(copy[neighbor.val])
        return copy[1]
        
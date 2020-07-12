"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        q = deque([])
        if root.left:
            q.append((root.left, 1))
        if root.right:
            q.append((root.right, 1))
        while q:
            node, level = q.popleft()
            if q and q[0][1] == level:
                node.next = q[0][0]
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))
        return root
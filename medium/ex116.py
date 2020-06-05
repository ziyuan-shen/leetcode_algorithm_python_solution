"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connectTwo(self, root1, root2):
        if not root1:
            return
        root1.next = root2
        if root1.left:
            self.connectTwo(root1.left, root1.right)
            self.connectTwo(root1.right, root2.left)
            self.connectTwo(root2.left, root2.right)
        
    def connect(self, root: 'Node') -> 'Node':
        if not root or not root.left:
            return root
        self.connectTwo(root.left, root.right)
        return root
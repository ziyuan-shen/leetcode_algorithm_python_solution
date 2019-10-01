"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root == None:
            return []
        else:
            l = []
            for node in root.children:
                l.extend(self.postorder(node))
            l.append(root.val)
            return l
        
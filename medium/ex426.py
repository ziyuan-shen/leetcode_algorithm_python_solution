"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        stack = []
        node = root
        while node:
            stack.append(node)
            node = node.left
        LVR = []
        while stack:
            node = stack.pop()
            new_node = node.right
            while new_node:
                stack.append(new_node)
                new_node = new_node.left
            if not LVR:
                LVR.append(node)
            else:
                LVR[-1].right = node
                node.left = LVR[-1]
                LVR.append(node)
        LVR[-1].right = LVR[0]
        LVR[0].left = LVR[-1]
        return LVR[0]
            
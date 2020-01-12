# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:    
    def findnode(self, root):
        if not root:
            return False
        left = self.findnode(root.left)
        right = self.findnode(root.right)
        current = root == self.p or root == self.q
        if current:
            if left or right:
                self.ans = root
        elif left and right:
            self.ans = root
        return left or right or current

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p = p
        self.q = q
        self.findnode(root)
        return self.ans
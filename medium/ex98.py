# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMin(self, root):
        p = root
        while p.left:
            p = p.left
        return p.val
    
    def getMax(self, root):
        p = root
        while p.right:
            p = p.right
        return p.val
        
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        if not root.left and not root.right:
            return True
        if not root.right:
            return self.getMax(root.left) < root.val and self.isValidBST(root.left)
        if not root.left:
            return self.getMin(root.right) > root.val and self.isValidBST(root.right)
        return self.getMax(root.left) < root.val and self.getMin(root.right) > root.val and self.isValidBST(root.left) and self.isValidBST(root.right)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxNodePath(self, root):
        if root == None:
            return None
        if root.left == None and root.right == None:
            return root.val
        if root.right == None:
            return max(self.maxNodePath(root.left) + root.val, root.val)
        if root.left == None:
            return max(self.maxNodePath(root.right) + root.val, root.val)
        return max(self.maxNodePath(root.left) + root.val, self.maxNodePath(root.right) + root.val, root.val)
        
    def maxPathSum(self, root: TreeNode) -> int:
        if root.left == None and root.right == None:
            return root.val
        if root.right == None:
            return max(self.maxPathSum(root.left), self.maxNodePath(root))
        if root.left == None:
            return max(self.maxPathSum(root.right), self.maxNodePath(root))
        left = self.maxNodePath(root.left)
        right = self.maxNodePath(root.right)
        return max(left + right + root.val, left + root.val, right + root.val, root.val, self.maxPathSum(root.left), self.maxPathSum(root.right))
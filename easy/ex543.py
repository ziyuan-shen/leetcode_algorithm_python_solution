# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def max_length(root):
            if root==None:
                return 0
            return max(max_length(root.left), max_length(root.right)) + 1
        if root == None:
            return 0
        return max(max_length(root.left)+max_length(root.right), self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        
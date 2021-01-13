# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root: return 0
        if root.val < L or root.val > R:
            return self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)
        else:
            return self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R) + root.val

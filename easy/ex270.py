# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        mindif = float("inf")
        while root:
            if abs(root.val - target) < mindif:
                mindif = abs(root.val - target)
                ans = root.val
            if root.val > target:
                root = root.left
            else:
                root = root.right
        return ans